#!/usr/bin/python3
if __name__ == "__main__":
    import sys
count = len(sys.argv) - 1
summ = 0
# print("-------test------")
for i in range(count):
    argg = int(sys.argv[i+1])
    summ = summ + argg
print(summ)
