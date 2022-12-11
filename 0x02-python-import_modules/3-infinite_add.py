#!/usr/bin/python3
import sys
 
if __name__ == "__main__":
    n = len(sys.argv)
    sun = int(0)
    for i in range(1, n):
        sun = sun + int(sys.argv[i])
    print('{}'.format(sun))
