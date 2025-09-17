# -*- coding: utf-8 -*-
# @Time : 2024/10/13 18:39
# @Author : CSR
# @File : strcount.py.py
message = "sadfasdffgfhtujru etwefdsjhr fddsszzbnn erterter4 cbx"
char_count = {}
for i in range(len(message)):
    char_count.setdefault(message[i], 0)
    char_count[message[i]] += 1

# print(char_count)

import  pyperclip
pyperclip.copy(str(char_count))
print(pyperclip.paste())