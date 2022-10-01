#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])
classmates.pop()
print('classmates =', classmates)

classmates.append('a')
# Add an item to the end of the list. Equivalent to a[len(a):] = [x].

# classmates.extend(iterable)
# Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

classmates.insert(0, 'a')
# Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

classmates.remove('a')
# Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

classmates.pop([0])
# Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

classmates.clear()
# Remove all items from the list. Equivalent to del a[:].

# classmates.index(x[, start[, end]])
# Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

# The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

classmates.count(0)
# Return the number of times x appears in the list.

# classmates.sort(*, key=None, reverse=False)
# Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

classmates.reverse()
# Reverse the elements of the list in place.

classmates.copy()
# Return a shallow copy of the list. Equivalent to a[:].


knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# gallahad the pure
# robin the brave

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
...
# 0 tic
# 1 tac
# 2 toe

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
...
# What is your name?  It is lancelot.
# What is your quest?  It is the holy grail.
# What is your favorite color?  It is blue.