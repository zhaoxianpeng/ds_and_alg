# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     quick_sort
   Description :
   Author :       xpzhao
   date：          18-5-15
-------------------------------------------------
   Change Activity:
                   18-5-15:
-------------------------------------------------
"""
__author__ = 'xpzhao'

import random
import turtle
import turtledemo



# 可视化过程
def print_list(nums, left=None, right=None, action=None):
    pass


# 分割nums[i ~ j]
def partition_recursion(nums, left, right):
    if left >= right: return

    pos = random.randint(left, right)
    pivot = nums[pos]

    # 把povit交换到最左边
    nums[pos] = nums[left]
    nums[left] = pivot

    # print("pivot:%d" % pivot, nums)

    begin = left
    end = right

    while left < right:
        while left < right and nums[right] > pivot: right -= 1
        if left < right:
            nums[left] = nums[right]
            left += 1
        while left < right and nums[left] < pivot: left += 1
        if left < right:
            nums[right] = nums[left]
            right -= 1

    nums [left] = pivot

    partition_recursion(nums,  begin, left -1)
    partition_recursion(nums, right + 1, end)


def quick_sort(nums):
    partition_recursion(nums, 0, len(nums) - 1)


def test_main():
    nums = [10, 17, 9, 1, 2, 11, 5, 6, 7, 9, 1]
    quick_sort(nums)
    print(nums)


if __name__ == '__main__':
    test_main()