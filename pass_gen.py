#!/usr/bin/env python3
# Basic password generator

import string, random
def passgenerator():
    chars = string.digits + string.ascii_letters + '!@#$%^&*()'
    pass_length = 13
    password = ""

    for char in range(pass_length):
        next_index = random.randrange(len(chars))
        password = password + chars[next_index]
    return password

print(passgenerator())
