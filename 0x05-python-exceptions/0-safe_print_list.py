#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        h = 0
        j = 0
        for k in my_list:
            h += 1
        if x > h:
            for i in range(0, h):
                print(my_list[i], end='')
                j += 1
            print()
        else:
            for i in range(0, x):
                print(my_list[i], end='')
                j += 1
            print()
    except TypeError:
        print("Pls check your code an error has occured")
    else:
        return (j)
