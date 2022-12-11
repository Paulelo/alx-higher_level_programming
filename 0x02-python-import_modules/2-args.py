#!/usr/bin/python3
import sys
 
# total arguments
n = len(sys.argv)
print("Total arguments passed: {}".format(n))
 
# Arguments passed
print("\nName of Python script: {}".format(sys.argv[0])
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print('{}'.format(sys.argv[i]), end = " ")
     
# Addition of numbers
Sum = 0
# Using argparse module
for i in range(1, n):
    Sum += int(sys.argv[i])
     
print("\n\nResult:", Sum)
