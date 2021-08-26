def factorial(num):
    fact = 1
    if num < 0:
        print("Enter a positive number")
        exit()
    if num == 0 or num == 1:
        return 1;
    while num > 0:
        fact = fact * num
        num = num - 1

    return fact


print(factorial(3))


def factorial_recursive(num):

    if num == 0:
        return 1
    if num > 0:
        return num * factorial_recursive(num - 1)
    else:
        return "Enter a positive number"


print(factorial_recursive(5))