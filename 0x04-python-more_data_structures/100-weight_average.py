#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        new_list = list(map(lambda t: t[0]*t[1], my_list))
        sum1 = 0
        for num in new_list:
            sum1 += num
        second = list(map(lambda s: s[1], my_list))
        sum2 = 0
        for num2 in second:
            sum2 += num2
        return sum1 / sum2
