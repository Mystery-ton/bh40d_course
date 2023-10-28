class Category:
    categories = ["rt", None, "1", "pok"]

    @classmethod
    def add(cls, cat_name: str):
        if cat_name in cls.categories:
            raise ValueError
        else:
            cls.categories.append(cat_name)
            return cls.categories.index(cat_name)

    @classmethod
    def get(cls, index: int):
        if cls.categories[index] is None or cls.categories[index] == "":
            raise IndexError
        else:
            return cls.categories[index]

    @classmethod
    def delete(cls, index: int):
        if not (cls.categories[index] is None or cls.categories[index] == ""):
            cls.categories.pop(index)

    @classmethod
    def update(cls, index: int, cat_name: str):
        if cat_name in cls.categories:
            raise ValueError
        else:
            if cls.categories[index] is None or cls.categories[index] == "":
                cls.categories[index] = cat_name


# print(Category.update(1, "ttl"))
print(Category.categories)
Category.delete(1)
print(Category.categories)
