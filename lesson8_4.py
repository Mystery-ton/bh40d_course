class Category:
    categories = [
        {"name": "rt", "is_published": True},
        {"name": "efvbl,", "is_published": True},
        {"name": "1", "is_published": False},
    ]

    @classmethod
    def add(cls, cat_name: str):
        if cat_name in [x["name"] for x in cls.categories]:
            raise ValueError
        else:
            cls.categories.append({"name": cat_name, "is_published": None})
            return cls.categories.index({"name": cat_name, "is_published": None})

    @classmethod
    def get(cls, index: int):
        if cls.categories[index] is None or cls.categories[index] == "":
            raise IndexError
        else:
            return cls.categories[index]

    @classmethod
    def delete(cls, index: int):
        if not (
            cls.categories[index]["name"] is None or cls.categories[index]["name"] == ""
        ):
            cls.categories.pop(index)

    @classmethod
    def update(cls, index: int, cat_name: str):
        if cat_name in [x["name"] for x in cls.categories]:
            raise ValueError
        else:
            if (
                cls.categories[index]["name"] is None
                or cls.categories[index]["name"] == ""
            ):
                cls.categories[index]["name"] = cat_name

    @classmethod
    def make_published(cls, index):
        if index < len(cls.categories):
            cls.categories[index]["is_published"] = True
        else:
            raise IndexError

    @classmethod
    def make_unpublished(cls, index):
        if index < len(cls.categories):
            cls.categories[index]["is_published"] = False
        else:
            raise IndexError


# print(Category.update(1, "ttl"))
print(Category.categories)
print(Category.add("qwerty"))
print(Category.categories)
Category.make_published(3)
print(Category.categories)
