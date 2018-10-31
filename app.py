import math
import random


def is_prime(num):
    if num > 1:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                # print("not prime")
                return False
        else:
            # print("prime")
            return True
    else:
        return False


def prime_numbers_between():
    lower = int(input("enter lower bound:"))
    upper = int(input("enter upper bound"))
    for i in range(lower, upper + 1):
        if is_prime(i) is True:
            print(i)


def factorial(num):
    if num is 0:
        return 1
    return num * factorial(num - 1)


def fibonacci(count):
    x = 0
    y = 1
    while count > 0:
        print(x)
        temp = y
        y = x + y
        x = temp
        count = count - 1


def is_armstrong(num):
    temp = num
    sum1 = 0
    order = len(str(num))
    while temp > 0:
        digit = temp % 10
        temp //= 10
        sum1 += digit ** order
    if sum1 == num:
        return True
    else:
        return False


def armstrong_numbers_in_range():
    low = int(input("enter lower bound:"))
    up = int(input("enter upper bound"))
    for i in range(low, up + 1):
        if is_armstrong(i) is True:
            print(i)


def infinite_loop():
    while True:
        num = int(input("Enter an integer: "))
        print("The double of", num, "is", 2 * num)


def roll_a_dice():
    while True:
        print(random.randint(1, 6))
        choice = input("again Y/n:")
        if choice is 'n':
            break


def calculate_hcf(x, y):
    while y != 0:
        temp = y
        y = x % y
        x = temp
    return x


def hcf():
    first = int(input("enter the first num:"))
    second = int(input("enter the second number"))
    if first > second:
        print("HCF of ",first,"and ",second,"is ",calculate_hcf(first,second))
    else:
        print("HCF of ",first,"and ",second,"is ",calculate_hcf(second,first))

hcf()

#roll_a_dice()
