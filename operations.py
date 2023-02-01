import logging
import emp
logging.basicConfig(filename='logsample.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def add(x, y):
    z = x+y
    return z


def sub(x, y):
    z = x-y
    return z


def mul(x, y):
    z = x*y
    return z


def div(x, y):
    z = x/y
    return z


first_number = 40
second_number = 2
res = add(first_number, second_number)
logging.debug(res)
# print("sum is", res)
res = sub(first_number, second_number)
logging.debug(res)
# print("sub is", res)
res = mul(first_number, second_number)
logging.debug(res)
# print("mul is", res)
res = div(first_number, second_number)
logging.debug(res)
# print("div is", res)
