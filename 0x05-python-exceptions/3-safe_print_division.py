#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        out_put = a / b
    except ZeroDivisionError:
        out_put = None
    finally:
        print("Inside result: {}".format(out_put))
        return out_put
