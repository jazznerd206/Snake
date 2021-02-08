
# KEYS ONLY

# This function accepts a dictionary of key value pairs 
# and returns a list of only the values.

# Best used for single level dictionary pairs, not 
# nested pairs.

def keys_to_the(kingdom):
    franz_liszt = []
    # loop through both key and value
    for k, v in kingdom.items():
        franz_liszt.append(k)
    return franz_liszt

composers = {
     "Johann": 10,
     "Hildegard": 11,
     "Igor": 9,
}
print(keys_to_the(composers)) # ['Johann', 'Hildegard', 'Igor']