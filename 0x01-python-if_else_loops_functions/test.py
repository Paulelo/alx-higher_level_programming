#!/usr/bin/python3

back = list(range(97, 123))
order = []
i = 25
while i >= 0:
    if (i % 2 == 0):
        up = chr(back[i])
	
        back.append(up.upper())
    else:
        order.append(chr(back[i]))
    i = i - 1
print(order)
