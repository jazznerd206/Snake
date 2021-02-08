# List too long? #CHUNKITOUT

# This function takes in two parmaeters:
    # list 'lst'
    # num 'size
# It returns a newly instantiated list made up of 
# of the smaller chunks of the original list.
# Use range() to create a list of size {size}
# Use map() on the newly created list to add
# splices of the original list to it.

from math import ceil

def chunk(lst, size):
    return list(
        map(lambda x: lst[x * size:x * size + size],
            list(range(0, ceil(len(lst) / size))))
    )
print(chunk([1,2,3,4,5], 2))