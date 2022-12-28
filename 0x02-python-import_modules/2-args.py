#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n = len(sys.argv)
    if n < 2:
        print('0 arguments.')
    if n == 2:
        print('1 argument:')
        print('1: {}'.format(sys.argv[1]))
    if n > 2:
        print('{} arguments:'.format(n-1))
        for i in range(1, n):
            print('{}: {}'.format(i, sys.argv[i]))