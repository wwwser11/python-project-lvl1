#!/usr/bin/env python3

def gcd(first_num, second_num):
    while first_num != 0 and second_num != 0:
        if first_num > second_num:
            first_num %= second_num
        else:
            second_num %= first_num
    result = (first_num + second_num)
    return result