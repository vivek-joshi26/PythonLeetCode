def fib(num):
    a = 0
    b = 1
    c = 0
    if num < 2 and num > 0:
        return 1
    while(num > 2):
        c = a + b
        a = b
        b = c
        num -= 1
    return c

# 0 1 1 2
#print(fib(-1))

def fib2(num):
    if num < 0:
        return "Provide a positive number"
    num1 = 0
    num2 = 1
    num3 = 0
    print(num1)
    while(num > 1):
        num3 = num1 + num2
        print(num2)
        num1 = num2
        num2 = num3
        num -= 1
    exit()

print(fib2(5))
