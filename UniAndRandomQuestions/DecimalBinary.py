"""

https://runestone.academy/ns/books/published/pythonds/BasicDS/ConvertingDecimalNumberstoBinaryNumbers.html

"""
from pythonds.basic import Stack


def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString


print(divideBy2(42))


def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString


print(baseConverter(25, 2))
print(baseConverter(25, 16))
print(baseConverter(25, 8))
print(baseConverter(256, 16))
print(baseConverter(16, 16))
