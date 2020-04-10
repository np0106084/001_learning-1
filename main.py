import math


def main():
    # learn_str_func(False)
    learn_number_func(True)


def learn_number_func(learn):
    #    num = 3
    #    print(type(num))
    #    num = 3.14
    #    print(type(num))
    num1 = 7
    num2 = 3
    # print("Addition: ", (num1 + num2))
    # print("Subtraction: ", (num1 - num2))
    # print("Multiplication: ", (num1 * num2))
    # print("Division: ", (num1 / num2))
    # print("Floor Division: ", (num1 // num2))
    # print("Exponent: ", (num1 ** num2))
    # print("Modulus: ", (num1 % num2))
    # print("Absolute: ", abs(-num1))
    # print("Round: ", round(num1 / num2))
    # print("Round: ", round(math.pi, 5))
    # print("++: ", num1++) # not available
    # num1 = num1 + 1
    # print("increment by 1: ", num1)
    # num1 += 9  # num1 = num1 + 1
    # print("increment by 9: ", num1)
    # num1 *= 2
    # print("multiplied by 2: ", num1)

    num1 = "z"
    num2 = "b"
    print(type(num1), type(num2))
    print(ord(num1), ord(num2))

    print("Equal: ", (num1 == num2))
    print("Not Equal: ", (num1 != num2))
    print("Greater than: ", (num1 > num2))
    print("Less than: ", (num1 < num2))
    print("Greater OR equal: ", (num1 >= num2))
    print("Less OR equal: ", (num1 <= num2))


def learn_str_func(learn):
    if learn == True:
        msg = "Hello World Hello hello hello World"
        # print(msg)
        # print(type(msg))
        # print(len(msg))

        # print(msg[1])
        # print(msg[0:5]) #0=included but 5=not included i.e. 0,1,2,3,4
        # print(msg[:5]) # before : => empty means start from beginning

        # print(msg[6:]) #6,7,...end

        # print(msg.lower())
        # print(msg.upper())
        # print(msg.count('Hello'),'\n')
        # print(msg.count('World'))
        # print(msg.lower().count('hello'))
        # 'Hello World Hello hello hello World'
        # print(msg.find('world')) # case sensitive - not found = -1
        # print(msg.find('World'))
        # print('World' in msg)
        # print(msg.find('World',7))

        # print(msg.replace("hello", "Hello"))
        a = 1
        first_str = "Hello"
        second_str = "World"
        msg = first_str + " " + second_str  # \t
        # msg = '{} {}. We\'re learning python...story....first, second'.format(first_str, second_str)
        # msg = '{1} {0}. We\'re learning python...story....first, second'.format(first_str, second_str)
        # msg = f'{first_str} {second_str}. We\'re learning python...story....first, second'
        print(msg)


main()
