# IS PALINDROME
# This function takes in one parameter, a string.
# Returns True if the input string is the same 
# forwards as it is backwards, False otherwise.
# STEPS:
    # 1. Convert string to lower case to prevent
    # returning false because the compared letters
    # are the different cases.
    # 2. Remove all non alphanumeric characters with 
    # Python re library
    # 3. Reverse string with Python slice magic,
    # compare and return the final verdict.

def palindrome(string):
    from re import sub
    s = sub('[\W_]', '', string.lower())
    return s == s[::-1]

print(palindrome('Never odd or even'))