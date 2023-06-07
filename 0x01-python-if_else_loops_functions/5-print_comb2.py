#!/usr/bin/python3
for i in range(100):
    if i < 10:
        print("0{}, ".format(i), end="")
    elif i > 9 and i < 20:
        print("1{}, ".format(i), end="")
    elif i > 19 and i < 30:
         print("{}, ".format(i), end="")
    elif i > 29 and i < 40:
         print("{}, ".format(i), end="")
    elif i > 39 and i < 50:
        print("{}, ".format(i), end="")
    elif i > 49 and i < 60:
        print("{}, ".format(i), end="")
    elif i > 59 and i < 70:
        print("{}, ".format(i), end="")
    elif i > 69 and i < 80:
        print("{}, ".format(i), end="")
    elif i > 79 and i < 90:
         print("{}, ".format(i), end="")
    elif i > 89 and i < 99:
        print("{}, ".format(i), end="")
print("99")
