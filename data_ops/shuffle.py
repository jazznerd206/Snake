# shuffle
# this is a behind the scenes look at the built in shuffle function for Python
# Uses the Fisher-Yates algorithm to reorder the elements of the list.

# Randomizes the order of the values of an list, returning a new list.

from copy import deepcopy
from random import randint


def shuffle(lst):
    temp_lst = deepcopy(lst)
    m = len(temp_lst)
    while (m):
        m -= 1
        i = randint(0, m)
        temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
    return temp_lst

foo = [1,2,3]
print(shuffle(foo)) # [2,3,1] , foo = [1,2,3]