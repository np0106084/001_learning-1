# import sys
# print(sys.path)
print("In calculator.py")


def add(x, y):
    pass


def subtract(x, y):
    pass


def multiplication(x, y):
    pass


def divide(x, y):
    pass


def greet(greeting, name="World"):
    msg = f"{greeting} {name}"
    print(msg)
    return msg


def student_info(arg1, *args, **kwargs):
    print(arg1)
    print(args)
    print(kwargs)
    # for arg in args:
    #     print(arg)
    # for key, value in kwargs.items():
    #     print(key, value)


# greet("Hello")
# student_info('English', 'Bangla', 'Physics', 'Math', name='Andy', age=25)

# courses = ["Bangla", "Physics", "Math"]
# info = {"name": "Andy", "age": 25}
# print(info)
# student_info("First Argument", courses, info)
# print()
# student_info("First Argument", *courses, **info)
