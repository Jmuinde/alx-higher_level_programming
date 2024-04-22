#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    enum = 0
    k = 0
    list1 = []
    for k in range(list_length):
        try:
            of = my_list_1[k] / my_list_2[k]
        except TypeError:
            print("wrong type")
            of = 0
        except ZeroDivisionError:
            print("division by 0")
            of = 0
        except IndexError:
            print("out of range")
            of = 0
        finally:
            list1.append(of)
    return list1
