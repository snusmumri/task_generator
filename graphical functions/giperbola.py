"""
СДАМ ГИА: РЕШУ ЕГЭ. Каталог заданий. Гиперболы. https://math-ege.sdamgia.ru/test?theme=125
"""

import bezier
from sympy import *
import time
from utilities.converting import save_to_base64

import matplotlib.pyplot as plt
from random import randint
import numpy as np
import math as m

def plot():
  fig = plt.figure(figsize = (7, 7))
  ax = plt.axes()
  fig.add_axes(ax)
  ax.spines[["left", "bottom"]].set_position('zero')
  ax.spines[["top", "right"]].set_visible(False)
  ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
  ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
  plt.xticks(np.arange(-30, 30, 1), fontsize=8)
  plt.yticks(np.arange(-30, 30, 1), fontsize=8)
  plt.xlim(-10, 10)
  plt.ylim(-10, 10)
  ax.grid(True)
  arrow_length = 10
  ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
              xytext=(0, arrow_length), textcoords='offset points',
              ha='center', va='bottom')
  ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
              xytext=(arrow_length, 0), textcoords='offset points',
              ha='center', va='bottom')
  return fig, ax

""" Тип 11 508951, 508961"""
def giperbola_1():
    fig, ax = plot()
    b = randint(1, 7)
    a = randint(2, 10 - b)
    x_1 = np.linspace(-10, (-0.1))
    x_2 = np.linspace(0.1, 10)
    y_1 = a/x_1 + b
    y_2 = a/x_2 + b

    while True:
      x_known = randint(-9, 9)
      x_task = randint(11, 100)
      if x_known != 0 and x_task != 0:
        y_known = a/(x_known) + b
        y_task = a/(x_task) + b
        if (int(y_known)- y_known) == 0 and abs(int(y_task*10) - y_task*10) < 0.001:
          break

    random_task = randint(0, 1)
    if random_task == 0:
      task = "На рисунке изображён график функции $\\f(x)=\\frac{a}{x} + b$. Найдите, при каком значении x значение функции равно $\\"+str(y_task)+"$."
      answer = x_task
    if random_task == 1:
      task = "На рисунке изображён график функции $\\f(x)=\\frac{a}{x} + b$. Найдите, $\\f("+str(x_task)+")$."
      answer = y_task

    plt.ylim(-10 + b, 10 + b)
    plt.plot(x_1, y_1, 'g')
    plt.plot(x_2, y_2, 'g')
    plt.scatter(x_known, y_known, color = 'black', marker = 'p')
    plt.axhline(y=b, color="black", linestyle="--")
    plt.legend(labels=["y = f(x)"])
    plt_base64 = save_to_base64(plt)
    plt.close()
    return {
        "condition": task,
        "answer": answer,
        "image": plt_base64,
    }

""" Тип 11 508971, 508983"""
def giperbola_2():
    fig, ax = plot()
    b = randint(1, 7)
    a = randint(2, 10 - b)
    x_1 = np.linspace((-10 - b), (-0.1 - b))
    x_2 = np.linspace((0.1 - b), (10 - b))
    y_1 = a / (x_1 + b)
    y_2 = a / (x_2 + b)

    while True:
        x_known = randint((-9 - b), (9 - b))
        x_task = randint(11, 100)
        if (x_known + b) != 0 and (x_task + b) != 0:
            y_known = a / (x_known + b)
            y_task = a / (x_task + b)
            if (int(y_known) - y_known) == 0 and abs(int(y_task * 10) - y_task * 10) < 0.001:
                break

    random_task = randint(0, 1)
    if random_task == 0:
        task = "На рисунке изображён график функции $\\f(x)=\\frac{a}{x + b}$. Найдите, при каком значении x значение функции равно $\\" + str(
            y_task) + "$."
        answer = x_task
    if random_task == 1:
        task = "На рисунке изображён график функции $\\f(x)=\\frac{a}{x + b}$. Найдите, $\\f(" + str(x_task) + ")$."
        answer = y_task

    plt.xlim(-10 - b, 10 - b)
    plt.plot(x_1, y_1, 'g')
    plt.plot(x_2, y_2, 'g')
    plt.scatter(x_known, y_known, color='black', marker='p')
    plt.axvline(x=-b, color="black", linestyle="--")
    plt.legend(labels=["y = f(x)"])
    plt_base64 = save_to_base64(plt)
    plt.close()
    return {
        "condition": task,
        "answer": answer,
        "image": plt_base64,
    }

""" Тип 11 508993, 509001"""
def giperbola_3():
    fig, ax = plot()
    b = randint(1, 7)
    a = randint(2, 10 - b)
    k = randint(1, 2)
    x_1 = np.linspace((-10 - b), (-0.1 - b))
    x_2 = np.linspace((0.1 - b), (10 - b))
    y_1 = (k * x_1 + a)/(x_1 + b)
    y_2 = (k * x_2 + a)/(x_2 + b)

    while True:
      x_known_1 = randint((-9 - b), (9 - b))
      x_known_2 = randint((-9 - b), (9 - b))
      x_task = randint(-200, 200)
      if x_known_1 != x_known_2 and (x_known_1 + b) != 0 and (x_known_2 + b) != 0 and (x_task + b) != 0:
        y_known_1 = (k * x_known_1 + a)/(x_known_1 + b)
        y_known_2 = (k * x_known_2 + a)/(x_known_2 + b)
        y_task = (k * x_task + a)/(x_task + b)
        if (int(y_known_1)- y_known_1) == 0 and (int(y_known_2)- y_known_2) == 0 and abs(int(y_task*10) - y_task*10) < 0.001:
          break

    random_task = randint(0, 1)
    if random_task == 0:
      task = "На рисунке изображён график функции $\\f(x)=\\frac{kx + a}{x + b}$. Найдите a."
      answer = a
    if random_task == 1:
      task = "На рисунке изображён график функции $\\f(x)=\\frac{kx + a}{x + b}$. Найдите k."
      answer = k

    plt.xlim(-10 - b, 10 - b)
    plt.ylim(-9, 11)
    plt.plot(x_1, y_1, 'g')
    plt.plot(x_2, y_2, 'g')
    plt.scatter(x_known_1, y_known_1, color = 'black', marker = 'p')
    plt.scatter(x_known_2, y_known_2, color = 'black', marker = 'p')
    plt.axvline(x=-b, color="black", linestyle="--")
    plt.axhline(y=k, color="black", linestyle="--")
    plt.legend(labels=["y = f(x)"])
    plt_base64 = save_to_base64(plt)
    plt.close()
    return {
        "condition": task,
        "answer": answer,
        "image": plt_base64,
    }
