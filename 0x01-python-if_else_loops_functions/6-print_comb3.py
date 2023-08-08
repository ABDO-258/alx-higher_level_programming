#!/usr/bin/python3
for c in range(10):
    for d in range((c+1), 10):
        if (c == 8 and d == 9):
            print("89")
        else:
            print("{}".format(c), end="")
            print("{},".format(d), end=" ")
