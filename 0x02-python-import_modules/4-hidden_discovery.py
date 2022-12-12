#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    name = dir(hidden_4)
    for na in filter(lambda x: not x.startswith("_"), name):
        print(end=""'{}\n'.format(na))
