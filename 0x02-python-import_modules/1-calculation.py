#!/usr/bin/python3
import calculator_1 as calc
if __name__ == "__main__":
    a = 10
    b = 5
    if (a != int(a) or b != int(b)):
        sys.stderr.write('Error\n')
    c = calc.add(a, b)
    d = calc.sub(a, b)
    e = calc.mul(a, b)
    f = calc.div(a, b)
    print('{} + {} = {}'.format(a, b, c))
    print('{} - {} = {}'.format(a, b, d))
    print('{} * {} = {}'.format(a, b, e))
    print('{} / {} = {}'.format(a, b, f))
