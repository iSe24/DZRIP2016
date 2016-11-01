#!/usr/bin/env python3
from librip.gen import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 7, 10)
d2 = ['f','F','fa','d']
print(list(Unique(data1)))

print(list(Unique(list(data2))))

print(list(Unique(d2, ignore_case=True)))

# Реализация задания 2