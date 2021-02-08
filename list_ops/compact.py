# compact
# Removes falsey values from a list.

# Use filter() to filter out falsey values (False, None, 0, and "").

import random

def compact(lst):
    return list(filter(bool, lst))

def boolWizard():
    a = 5
    randNum = random.randint(1,10)
    return False if randNum > a else True

trash = [0, 1, False, 2, '', 0j, 3, None, 's', 34, boolWizard()]
print(compact(trash)) # [ 1, 2, 3, 'a', 's', 34 ]