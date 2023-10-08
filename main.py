print("hi anton")

print("hello world")
print("he world")
print("helloworld")
print("bye pycharm")


def hello():
    pass


print("hello")

text = "Hello"
print(text.istitle())

text = input("Enter sentence: ")

text2 = text.split()
text3 = text2[2] + " " + text2[1] + " " + text2[0]
print(text3)

first_space_index = text.find(" ")
first_word = text[:first_space_index]
last_space_index = text.rfind(" ")
last_word = text[last_space_index + 1 :]
center = text[first_space_index : last_space_index + 1]
result = last_word + center + first_word
print(result)
