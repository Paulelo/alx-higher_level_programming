#!/usr/bin/python3

#This programme print the odd number in a list
def check_odd(num): #Funtion to check for odd numbers in list
    if (num % 2) == 0:
        return False
    else:
        return True

#Function that runs odd number checker
#over iterable and retiurns list containg 
#odd number
def print_odd(lists, func): 
    new_list = []
    for i in lists:
        if check_odd(i):
            new_list.append(i)
    return (new_list)

#list from which odd number are to be extracted
list_new = list(range(1, 20))
print(print_odd(list_new, check_odd))

print(list(map((lambda num : '' if (num % 2) == 0 else num), list_new)))
