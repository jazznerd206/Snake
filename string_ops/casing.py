# is_upper_case
# Checks if a string is upper case.

# Convert the given string to upper case, using str.upper() method and compare it to the original.

def is_upper_case(string):
    return string == string.upper()

print(is_upper_case('ABC')) # True
print(is_upper_case('a3@$')) # False
print(is_upper_case('aB4')) # False


# is_lower_case
# Checks if a string is lower case.

# Convert the given string to lower case, using str.lower() method and compare it to the original.

def is_lower_case(string):
    return string == string.lower()

print(is_lower_case('abc')) # True
print(is_lower_case('a3@$')) # True
print(is_lower_case('A3@$')) # False
print(is_lower_case('aB4')) # False