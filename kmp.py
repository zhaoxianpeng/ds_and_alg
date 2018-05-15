# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     kmp
   Description :
   Author :       xpzhao
   date：          18-5-15
-------------------------------------------------
   Change Activity:
                   18-5-15:
-------------------------------------------------
"""
__author__ = 'xpzhao'

"""
https://www.cnblogs.com/zhangtianq/p/5839909.html
"""


def cal_next(s):
    slen = len(s)
    next = [0] * slen
    next[0] = -1

    k = -1
    j = 0

    while j < slen -1:
        if k == -1 or s[j] == s[k]:
            k += 1
            j += 1
            next[j] = k
            print('next[%d] = %d       sub string is ' %(j, k), s[:j])
        else:
            k = next[k]

    return next


def kmp(s, p):
    next = cal_next(p)

    slen = len(s)
    plen = len(p)

    i = 0;
    j = 0;
    while i < slen and j < plen:
        if s[i] == p[j] or j == -1:
            i += 1
            j += 1
        else:
            j = next[j]

    if j == plen:
        return i - j
    else:
        return -1


def test_main():
    i = kmp('BBC ABCDAB  ABCDABCDABDE', 'ABCDABD')
    print(i)
    # print(cal_next("ABCDABDAD"))
