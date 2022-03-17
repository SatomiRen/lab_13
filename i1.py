#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def positive_sum(*args):
    if args:
        i = 0
        for index, arg in enumerate(args):
            if arg > 0:
                i = index
        pos_s = sum(arg for index, arg in enumerate(args) if index < i)
        return pos_s
    else:
        return None


if __name__ == "__main__":
    arguments = [int(i) for i in input("Enter the arguments: ").split()]
    print("The sum of the arguments before the last positive element is: "
          f"{positive_sum(*arguments)}"
    )