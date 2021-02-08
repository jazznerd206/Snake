# capitalize
# Capitalizes the first letter of a string.

# Capitalizes the fist letter of the sring and then adds it with rest of the string. Omit the lower_rest parameter to keep the rest of the string intact, or set it to true to convert to lowercase.

def capitalize(string, lower_rest=False):
    return string[:1].upper() + (string[1:].lower() if lower_rest else string[1:])

print(capitalize('fooBar')) # 'FooBar'
print(capitalize('fooBar', True)) # 'Foobar'



# decapitalize
# Decapitalizes the first letter of a string.

# Decapitalizes the first letter of the string and then adds it with rest of the string. Omit the upper_rest parameter to keep the rest of the string intact, or set it to True to convert to uppercase.

def decapitalize(string, upper_rest=False):
    return string[:1].lower() + (string[1:].upper() if upper_rest else string[1:])

print(decapitalize('FooBar')) # 'fooBar'
print(decapitalize('FooBar', True)) # 'fOOBAR'