#!/usr/bin/python3
"""A module that inherits from list"""


class MyList(list):
    """A class that inherits from lists."""

    def print_sorted(self):
        """A function that prints sorted list.

        Args:
            None
        Returns:
            nothing
        """
        sorted_list = sorted(self)
        print(sorted_list)
