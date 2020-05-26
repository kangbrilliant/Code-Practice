#!/usr/bin/env python
# -*- coding:utf-8 -*-
import argparse
import time
import os
import sys

class Solution:
	# time cost: o(n)
	# space cost: o(m) char size
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        n = len(s)
        temp = set()
        rk = -1
        for i, _ in enumerate(s):
            if i != 0:
                temp.remove(s[i-1])
            while rk + 1 < n and s[rk+1] not in temp:
                temp.add(s[rk+1])
                rk += 1
            max_count = max(max_count, rk - i + 1)
        return max_count


# class Solution:
# 	# time cost: o(n^2)
# 	# space cost: o(1)
#     def lengthOfLongestSubstring(self, s: str) -> int:
#     	max_count = 0
#     	for i, _ in eunmerate(s):
#     		max_str = ''
#     		count = 0
#     		for j in s[i:]:
#     			if j not in max_str:
#     				max_str += j
#     				count += 1
#     				if count > max_count:
#     					max_count = count
#     			else:
#     				break
#   		return max_count
