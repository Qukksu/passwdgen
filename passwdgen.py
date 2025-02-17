'''Copyright (C) <2025> <Evrotskii Artem>
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or (at your option)
any later version.
'''

from random import randint
import string

def keygen(lenght:int):
    password = ""
    all_chars = string.ascii_letters + string.digits + string.punctuation
    for i in range(lenght):
        password += all_chars[randint(0,len(all_chars)-1)]
    return password

while True:
    psswdlen = int(input("Введите длину пароля:"))
    print("Ваш пароль: ", keygen(psswdlen))