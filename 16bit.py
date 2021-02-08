# Encodes a given utf-8 string into base-16.


import base64

def encode_to_b16(inp):
    encoded = inp.encode("utf-8")
    b16encoded = base64.b16encode(encoded)
    return b16encoded

print(encode_to_b16('this is a string'))
print(encode_to_b16('this is different string'))