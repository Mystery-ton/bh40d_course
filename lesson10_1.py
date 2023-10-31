from csv import DictReader, reader, writer, DictWriter
from schemas import SimpleSchema

with open(r"C:\pythonCourse\bh40d_course\input.csv", "r+") as file:
    data_list = SimpleSchema.from_csv(file)
    for item in data_list:
        print(item.name, item.surname, item.email)

    new_data = SimpleSchema(name="example", surname="rik", email="e")
    new_data.to_csv(file)
