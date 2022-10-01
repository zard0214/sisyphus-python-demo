#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 打印list:
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# break continue pass

# 打印数字 0 - 9 / iterate over a sequence of numbers
for x in range(10):
    print(x)


# Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
#
# # Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status