# coding=utf-8
__author__ = 'admin'
import math
n = int(raw_input("Input N: "))
#декоратор, форматирующий значение функции с точностью до N знаков после запятой
def decorateInput(func):
    def innerFunc(t):
        res = func(t)
        return str("{:."+str(n)+"f}").format(res)
    return innerFunc

#задекорированная функция(в качестве примера функция делит корень из числа на 2)
@decorateInput
def funcSqrtDivTwo(t):
    return math.sqrt(t)/2

print funcSqrtDivTwo(2)