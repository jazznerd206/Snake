# count_vowels
# Retuns number of vowels in provided string.
# Use a regular expression to count the number of vowels (A, E, I, O, U) in a string.

import re

def count_vowels(str):
    return len(re.findall(r'[aeiou]', str, re.IGNORECASE))

print(count_vowels('foobar')) # 3
print(count_vowels('gym')) # 0

# count_vowels
# Retuns number of vowels in provided string.
# Use a regular expression to count the number of vowels (A, E, I, O, U) in a string.

import re

def count_consonants(str):
    return len(re.findall(r'[b-df-hj-np-tv-z]', str, re.IGNORECASE))

print(count_consonants('foobar')) # 3
print(count_consonants('gym')) # 3