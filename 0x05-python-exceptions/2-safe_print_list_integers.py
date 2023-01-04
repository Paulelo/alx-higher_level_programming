#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        h = 0 
        j = 0
        a_list = []
        b_list = []
        for l in my_list:
            if isinstance(l, int):
                a_list.append(l)
            else:
                b_list.append(l)
        for k in my_list:
            h += 1
        if x == h:
            for i in a_list:
                print(i, end='')
                j += 1
            print('\n')
        else:
            for i in range(0, x):
                print(a_list[i], end='')
                j += 1
            print('\n')
    except TypeError:
        print("Pls check your code an error has occured")
    else:
        return (j)
