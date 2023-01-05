#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        h = 0
        j = 0
        a_list = []
        b_list = []
        for i in my_list:
            if isinstance(i, int):
                a_list.append(i)
            else:
                b_list.append(i)
        for k in my_list:
            h += 1
        if x == h:
            for i in a_list:
                print('{:d}'.format(i), end='')
                j += 1
            print()
        else:
            for i in range(0, x):
                print('{:d}'.format(a_list[i]), end='')
                j += 1
            print()
    except TypeError:
        print("Pls check your code an error has occured")
    else:
        return (j)
