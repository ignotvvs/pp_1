# -*- coding: utf-8 -*-

import re
with open("sample.txt") as file:
    for i in file:
        x = re.findall(r"\w{6,}", i)
        if x: [print(j) for j in x]
