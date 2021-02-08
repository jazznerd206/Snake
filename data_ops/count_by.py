

# COUNT BY
# This function takes two arguments:
    # A list with items to be counted
    # The function the list will be mapped to
# This function uses the properties inherent in objects
# to create a new property for each unique value, then
# increase the count of that property each time that 
# element appears in the list.

def count_by(arr, fn=lambda x: x):
    key = {} 
    for el in map(fn, arr):
        key[el] = 0 if el not in key else key[el]
        key[el] += 1
    return key

print(count_by(['one','two','three'], len))
# returns {3: 2, 5: 1}
