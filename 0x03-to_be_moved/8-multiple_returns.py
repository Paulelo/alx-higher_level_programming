#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        tup1 = (0, None)
        return (tup1)
    tup = (len(sentence), sentence[0])
    return (tup)
