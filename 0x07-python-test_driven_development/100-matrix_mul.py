#!/usr/bin/python3
""" This modules multiplies
two matrices"""


def matrix_mul(m_a, m_b):
    """ This function takes two
    matrices as args and returns
    their product"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    elif type(m_b) is not list:
        raise TypeError("m_b must be a list")
    elif type(m_a[0]) is not list:
        raise TypeError("m_a must be a list of lists")
    elif type(m_b[0]) is not list:
        raise TypeError("m_b must be a list of lists")
    elif len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    elif len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    elif:
        for i in range(0, len(m_a)):
            for j in range(0, len(m_a[i])):
                if type(m_a[i][j]) not in [int, float]:
                    raise TypeError("m_a should contain only integers or floats")
        for k in range(0, len(m_b)):
            for l in range(0, len(m_b[k])):
                if type(m_b[k][l] not in [int, float]:
                    raise TypeError("m_b should contain only integers or floats")
    elif:
        for i in range(1, len(m_a)):
            n = len(m_a[0])
            if len(m_a[i]) > n or len(m_a[i]) < n:
                raise TypeError("each row of m_a must be of the same size")
        for k in range(1, len(m_b)):
            m = len(m_b[0])
            if len(m_b[i]) > m or len(m_b[i]) < m:
                raise TypeError("each row of m_b must be of the same size")
    elif len(m_a) != len(m_b[0]):
        raise ValueError("m_a and m_b can't be multiplied")
    else:
        m_r
