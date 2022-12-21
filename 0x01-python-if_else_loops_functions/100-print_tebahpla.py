#!/usr/bin/python3

back = list(range(97, 123))
order = []
i = 25
while i >= 0:
    order.append(chr(back[i]))
    i = i - 1
while i >= 0:
    print(order[i])
    i = i + 1
