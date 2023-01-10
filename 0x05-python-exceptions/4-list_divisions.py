#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        return_list = []
        return_list_2 = []
        for i in range(0, len(my_list_1)):
            if (my_list_1[i] == 0) or (my_list_2[i] == 0):
                print('division by 0')
                return_list.append(0)
            elif isinstance(my_list_1[i], int) != isinstance(my_list_2[i], int):
                print('wrong type')
                return_list.append(0)
            elif (my_list_1[i] is None) or (my_list_2[i] is None):
                print('out of range')
                return_list.append(0)
            else:
                return_list.append(my_list_1[i] / my_list_2[i])
        for l in range(0, list_length):
            return_list_2.append(return_list[l])
    except ZeroDivisionError:
        print('division by 0')
    except TypeError:
        print('wrong type')
    except IndexError:
        print('out of range')
    finally:
        return (return_list_2)
