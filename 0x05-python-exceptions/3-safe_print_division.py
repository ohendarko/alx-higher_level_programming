#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("Inside result: {}".format(result))
        return result
    except ZeroDivisionError:
        reslt = None
        print("Inside result: {}".format(reslt))
        return reslt
    finally:
        print(end="")
