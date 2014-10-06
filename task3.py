# coding=utf-8
__author__ = 'admin'
import math
#декоратор, форматирующий значение функции с точностью до N знаков после запятой
def decorateWithN(n):
    def decorateInput(func):
        def innerFunc(t):
            res = func(t)
            if n>0:
                return str("{:."+str(n)+"f}").format(res)
            else:
                return None
        return innerFunc
    return decorateInput

#задекорированная функция(в качестве примера функция делит корень из числа на 2)
@decorateWithN(11)
def funcSqrtDivTwo(t):
    return math.sqrt(t)/2

print funcSqrtDivTwo(2)