#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_res = []
    for i in range(list_length):
        try:
            div_res.append(my_list_1[i] / my_list_2[i])
        except (ValueError, TypeError):
            print("wrong type")
            div_res.append(0)
        except ZeroDivisionError:
            print("division by 0")
            div_res.append(0)
        except IndexError:
            print("out of range")
            div_res.append(0)
        finally:
            print(end="")
    return div_res
