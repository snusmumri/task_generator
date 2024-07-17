from functools import wraps
from string import Template
import random
import re as r
import math
import numpy as np
from decimal import Decimal

from sympy import *

from random import sample

def task(target, known):
    x_100 = random.randint(1,99)
    answer = x_100/100
    numb_1, numb_2 = '', 2
    segment_q = lambda x: latex(UnevaluatedExpr(S.One*pi*(math.floor(x*2/pi))/2)) + " < \\alpha < " + latex(UnevaluatedExpr(S.One*pi*(math.floor(x*2/pi)+1)/2))
    radian = random.randint(-10,10)
    if radian == 0:
        radian = 0.01
    segment = segment_q(radian)
    if x_100 != 10 or x_100 != (-10):

        if known == 'sin':
            sign_x = (sin(radian) / abs(sin(radian)))
            if target == 'sin':
                d = latex(sign_x * (sqrt(100 + x_100) - sqrt(100 - x_100)) / 20)
            if target == 'cos':
                d = latex(sign_x * sqrt(100 - x_100) / sqrt(200))
            if target == 'tg':
                d = latex(sign_x * (x_100) / (sqrt(2 * (10000 + x_100 ** 2 + sqrt(10000 + (x_100 ** 2)) * 100))))
            if target == 'ctg':
                d = latex(sign_x * 100 / (sqrt(2 * (10000 + x_100 ** 2 + (sqrt(10000 + x_100 ** 2)) * x_100))))

        if known == 'cos':
            sign_x = cos(2*radian)/abs(cos(2*radian))
            if target == 'sin':
                d = latex(sign_x * (sqrt(100+x_100)+sqrt(100-x_100))/20)
            if target == 'cos':
                d = latex(sign_x * (sqrt(100+x_100)/sqrt(2))/10)
            if target == 'tg':
                d = latex(sign_x * (sqrt(10000 + x_100**2 + 100*sqrt(10000 + x_100**2)))/(sqrt(20000 + 2* (x_100**2))))
            if target == 'ctg':
                d = latex(sign_x * (sqrt(10000 + x_100**2 + x_100 * sqrt(10000 + x_100**2)))/(sqrt(20000 + 2*(x_100**2))))

        if known == 'tg':
            sign_x = tan(2*radian)/abs(tan(2*radian))
            if target == 'sin':
                d = latex(sign_x * (sqrt(100+x_100)-sqrt(100-x_100))/((sqrt(100+x_100)+sqrt(100-x_100))))
            if target == 'cos':
                d = latex(sign_x * sqrt(100-x_100)/sqrt(100+x_100))
            if target == 'tg':
                d = latex(sign_x * x_100/(100 + sqrt(10000 + x_100**2)))
            if target == 'ctg':
                d = latex(sign_x * 100/(x_100 + sqrt(10000 + x_100**2)))

        if known == 'ctg':
            sign_x = tan(2*radian)/abs(tan(2*radian))
            if target == 'sin':
                d = latex(sign_x * (sqrt(100+x_100)+sqrt(100-x_100))/((sqrt(100+x_100)-sqrt(100-x_100))))
            if target == 'cos':
                d = latex(sign_x * sqrt(100+x_100)/sqrt(100-x_100))
            if target == 'tg':
                d = latex(sign_x * (100 + sqrt(10000 + x_100**2))/x_100)
            if target == 'ctg':
                d = latex(sign_x * (x_100 + sqrt(10000 + x_100**2))/100)

        if known == 'sin_2':
            sign_x = sin(radian)/abs(sin(radian))
            numb_1, numb_2 = 2, ''
            known = known[:-2]
            if target == 'sin' or target == 'cos':
                d = latex(sign_x * (x_100 * (sqrt(10000 - x_100**2)) /5000))
            if target == 'tg' or target == 'ctg':
                d = "\\frac{"+str(int((sign_x * 200 * x_100)/(math.gcd((200 * x_100), (10000 + x_100**2)))))+"}{"+str(int((10000 + x_100**2)/(math.gcd((200 * x_100), (10000 + x_100**2)))))+"}"

        if known == 'cos_2':
            sign_x = cos(radian)/abs(cos(radian))
            numb_1, numb_2 = 2, ''
            known = known[:-2]
            if target == 'sin':
                d = "\\frac{"+str(int(sign_x * (5000 - x_100**2)/(math.gcd((5000 - x_100**2),5000))))+"}{"+str(int((5000)/(math.gcd((5000 - x_100**2),5000))))+"}"
            if target == 'cos':
                d = "\\frac{"+str(int(sign_x * (x_100**2 - 5000)/(math.gcd((x_100**2 - 5000),5000))))+"}{"+str(int((5000)/(math.gcd((x_100**2 - 5000),5000))))+"}}"
            if target == 'tg':
                d = "\\frac{"+str(int(sign_x * (10000 - x_100**2)/(math.gcd((10000 - x_100**2), (10000 + x_100**2)))))+"}{"+str(int((10000 + x_100**2)/(math.gcd((10000 - x_100**2), (10000 + x_100**2)))))+"}"
            if target == 'ctg':
                d = "\\frac{"+str(int(sign_x * (x_100**2 - 10000)/(math.gcd((x_100**2 - 10000), (10000 + x_100**2)))))+"}{"+str(int((10000 + x_100**2)/(math.gcd((x_100**2 - 10000), (10000 + x_100**2)))))+"}"

        if known == 'tg_2':
            sign_x = tan(radian)/abs(tan(radian))
            numb_1, numb_2 = 2, ''
            known = known[:-2]
            if target == 'sin':
                d = latex(sign_x * (x_100 * (sqrt(10000 - x_100**2))) /(5000 - x_100**2))
            if target == 'cos':
                d = latex(sign_x * (x_100 * (sqrt(10000 - x_100**2))) /(x_100**2 - 5000))
            if target == 'tg':
                d = "\\frac{"+str(int(sign_x * (200 * x_100)/(math.gcd((200 * x_100), (10000 - x_100**2)))))+"}{"+str(int((10000 - x_100**2)/(math.gcd((200 * x_100), (10000 - x_100**2)))))+"}"
            if target == 'ctg':
                d = "\\frac{"+str(int(sign_x * (200 * x_100)/(math.gcd((200 * x_100), (x_100**2 - 10000)))))+"}{"+str(int((x_100**2 - 10000)/(math.gcd((200 * x_100), (x_100**2 - 10000)))))+"}"

        if known == 'ctg_2':
            sign_x = tan(radian)/abs(tan(radian))
            numb_1, numb_2 = 2, ''
            known = known[:-2]
            if target == 'sin':
                d = latex(sign_x * (5000 - x_100**2)/(x_100 * (sqrt(10000 - x_100**2))))
            if target == 'cos':
                d = latex(sign_x * (x_100**2 - 5000)/(x_100 * (sqrt(10000 - x_100**2))))
            if target == 'tg':
                d = "\\frac{"+str(int(sign_x * (10000 - x_100**2)/(math.gcd((10000 - x_100**2), (200 * x_100)))))+"}{"+str(int((200 * x_100)/(math.gcd((10000 - x_100**2), (200 * x_100)))))+"}"
            if target == 'ctg':
                d = "\\frac{"+str(int(sign_x * (x_100**2 - 10000)/(math.gcd((x_100**2 - 10000), (200 * x_100)))))+"}{"+str(int((200 * x_100)/(math.gcd((x_100**2 - 10000), (200 * x_100)))))+"}"

        if sign_x == 1:
            answer = answer
        else:
            answer = -answer

    task = "Зная, что $\\"+str(known)+"("+str(numb_1)+"\\alpha)="+""+str(d)+"$ и $"+str(segment)+"$, найдите: $ \\"+str(target)+"("+str(numb_2)+"\\alpha)$"

    return task, answer
def trig_identity_1(target_known='sin-sin'):
    target, known = target_known.split("-")
    t, a = task(target, known)
    return {
        'condition': t,
        'answer': a
        }