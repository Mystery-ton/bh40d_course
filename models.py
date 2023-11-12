from datetime import datetime
from decimal import Decimal
from typing import Annotated, TYPE_CHECKING

from annotated_types import Predicate
from pydantic import BaseModel, PositiveInt, Field
from sqlalchemy import (
    Column,
    INT,
    VARCHAR,
    ForeignKey,
    CheckConstraint,
    DECIMAL,
    BOOLEAN,
    create_engine,
    TEXT,
    select,
    update,
    delete,
    or_,
    and_,
    TIMESTAMP,
)
from sqlalchemy.orm import (
    declarative_base,
    DeclarativeBase,
    sessionmaker,
    relationship,
    selectinload,
)
from sqlalchemy.sql.functions import count
from sqlalchemy.exc import IntegrityError


OldBase = declarative_base()

engine = create_engine("sqlite:///db_alchemy2.sqlite3")
session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    id = Column(INT, primary_key=True, autoincrement=True)

    def model_validate(self, obj):
        for k, v in obj.__dict__.items():
            if hasattr(self, k) and not isinstance(getattr(self, k), list):
                setattr(self, k, v)

    def dump(self) -> dict:
        data = self.__dict__
        data.pop("_sa_instance_state", None)
        for k, v in data.items():
            if isinstance(v, list):
                sub_objs = v.copy()
                data[k] = []
                for i, obj in enumerate(sub_objs):
                    data[k].append(obj.dump())
        return data


class Category(Base):
    __tablename__ = "categories"
    __table_args__ = (CheckConstraint("length(name) >= 2 and name not like '% %'"),)
    if TYPE_CHECKING:
        id: int
        name: str
        products: list["Product"]
    else:
        name = Column(VARCHAR(32), nullable=False, unique=True)

        products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"
    __table_args__ = (
        CheckConstraint("length(name) >= 2 and name not like '% %'"),
        CheckConstraint("price > 0"),
    )

    if TYPE_CHECKING:
        id: int
        name: str
        price: Decimal
        is_published: bool
        descr: str
        category_id: int
        category: Category
        date_created: datetime
    else:
        name = Column(VARCHAR(128), nullable=False)
        price = Column(DECIMAL(8, 2), nullable=False, server_default="1")
        is_published = Column(BOOLEAN, nullable=False, server_default="false")
        descr = Column(TEXT, nullable=False, server_default="''")
        category_id = Column(
            INT,
            ForeignKey(column="categories.id", ondelete="RESTRICT", onupdate="CASCADE"),
            nullable=False,
            index=True,
        )
        date_created = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)
        order_items = relationship("OrderItem", back_populates="product")
        category = relationship("Category", back_populates="products")

    @property
    def isodate(self) -> str:
        return self.date_created.isoformat()

    def __str__(self) -> str:
        return self.name


class User(Base):
    __tablename__ = "users"
    __table_args__ = (CheckConstraint("length(name) >= 2 and name not like '% %'"),)
    if TYPE_CHECKING:
        id: int
        name: str
        email: str
    else:
        name = Column(VARCHAR(24), nullable=False)
        email = Column(VARCHAR(24), unique=True)
        orders = relationship("Order", back_populates="user")


class Order(Base):
    __tablename__ = "orders"

    if TYPE_CHECKING:
        id: int
        user_id: int
        status_id: int
    else:
        user_id = Column(
            INT,
            ForeignKey(column="users.id", ondelete="RESTRICT", onupdate="CASCADE"),
            nullable=False,
            index=True,
        )
        status_id = Column(
            INT,
            ForeignKey(column="statuses.id", ondelete="RESTRICT", onupdate="CASCADE"),
            nullable=False,
            index=True,
        )
        order_items = relationship("OrderItem", back_populates="order")
        status = relationship("Status", back_populates="orders")
        user = relationship("User", back_populates="orders")


class Status(Base):
    __tablename__ = "statuses"
    __table_args__ = (CheckConstraint("length(name) >= 2 and name not like '% %'"),)
    if TYPE_CHECKING:
        id: int
        name: str

    else:
        name = Column(VARCHAR(10), nullable=False, unique=True)
        orders = relationship("Order", back_populates="status")


class OrderItem(Base):
    __tablename__ = "order_items"

    if TYPE_CHECKING:
        id: int
        order_id: int
        product_id: int
    else:
        order_id = Column(
            INT,
            ForeignKey(column="orders.id", ondelete="RESTRICT", onupdate="CASCADE"),
            nullable=False,
            index=True,
        )
        product_id = Column(
            INT,
            ForeignKey(column="products.id", ondelete="RESTRICT", onupdate="CASCADE"),
            nullable=False,
            index=True,
        )
        order = relationship("Order", back_populates="order_items")
        product = relationship("Product", back_populates="order_items")


AlphaStr = Annotated[str, Predicate(str.isalpha)]


class ProductSchema(BaseModel):
    id: PositiveInt
    name: str = Field(min_length=2, max_length=32)
    price: Decimal = Field(default=1, gt=0, decimal_places=2, max_digits=8)
    is_published: bool = Field(default=False)
    descr: str = Field(default=None)


class CategorySchema(BaseModel):
    id: PositiveInt
    name: str = Field(min_length=2, max_length=32)
    products: list[ProductSchema] = Field(default=None)


# with session() as s:
# cat1 = Category(name="category-6")
# cat2 = Category(name="category-7")
# s.add_all((cat1, cat2))
# try:
#     s.commit()
# except IntegrityError:
#     pass
# else:
#     print(cat1.id)
#     print(cat2.id)
# cat = s.get(Category, ident=3)
# print(cat.name, cat.id)
# cat.name = "Coffee"
# s.commit()
# cat = s.get(Category, ident=3)
# s.delete(cat)
# s.commit()
# objs = s.scalars(
#     select(Category)
#     .filter(or_(Category.name.like("%cat%"), Category.id >= 3))
# )
# print(objs.all())
# s.execute(
#     update(Category).values(name="Product1").filter(Category.id == 1)
# )
# s.commit()
# s.execute(delete(Category).filter(Category.id == 1))
# s.commit()
# prod = Product(name="Product1", price=4.5, category_id=2)
# s.add(prod)
# s.commit()
# objs = s.execute(
#     select(count(Product.id), Category.name)
#     .join(Category, isouter=True)
# )
# print(objs.all())
# cat2 = s.get(Category, 2, options=[selectinload(Category.products)])
# print(cat2.products[0])
# cat = Category(
#     name="NewCategory",
#     products=[
#         Product(name="Prod1", price=5),
#         Product(name="Prod2", price=6),
#     ]
# )
# s.add(cat)
# s.commit()
# schema = CategorySchema(id=8, name="NewNewCategory")
# cat = s.get(Category, 8, options=[selectinload(Category.products)])
# print(cat.dump())
# cat.model_validate(obj=schema)
# s.commit()
# schema = CategorySchema.model_validate(cat, from_attributes=True)
# print(schema)
