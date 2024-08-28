import matplotlib.pyplot as plt
from random import randint
import numpy as np
import math as m
from matplotlib.ticker import FixedFormatter
from utilities.converting import save_to_base64

def plot():
  fig = plt.figure(figsize = (7, 7))
  ax = plt.axes()
  fig.add_axes(ax)
  ax.spines[["left", "bottom"]].set_position('zero')
  ax.spines[["top", "right"]].set_visible(False)
  ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
  ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
  plt.xticks(np.arange(-3*np.pi, 3*np.pi, np.pi/4), fontsize=8)
  ax.xaxis.set_major_formatter(FixedFormatter(['$-3\\pi$', '', '', '', '$-2\\pi$',
                                               '', '', '', '$-\\pi$', '', '', '',
                                               '', '', '', '', '$\\pi$', '', '',
                                               '', '$2\\pi$', '', '', '', '$3\\pi$']))
  plt.yticks(np.arange(-30, 30, 1), fontsize=8)
  ax.grid(True)
  arrow_length = 10
  ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
              xytext=(0, arrow_length), textcoords='offset points',
              ha='center', va='bottom')
  ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
              xytext=(arrow_length, 0), textcoords='offset points',
              ha='center', va='bottom')
  return fig, ax

#СДАМ ГИА: РЕШУ ЕГЭ. Каталог заданий. Тригонометрические функции https://ege.sdamgia.ru/test?theme=191

def trigonometria(name_func_target):
    fig = plt.figure()
    fig, ax = plot()
    a = randint(1, 9)
    b = randint(1, 5)
    x = np.linspace(-3*np.pi, 3*np.pi, 1000, endpoint=True)
    x_mark_1, x_mark_2 = 0, np.pi/2
    y_max, y_min = 0, 0

    name_func, target = name_func_target.split('-')

    if name_func == 'cos':
      y = a * np.cos(x) + b
      for i in x:
        y_i = a * np.cos(i) + b
        if y_i > y_max:
          y_max = y_i
        if y_i < y_min:
          y_min = y_i
      y_mark_1 = a * np.cos(0) + b
      y_mark_2 = a * np.cos(np.pi/2) + b

    if name_func == 'sin':
      y = a * np.sin(x) + b
      for i in x:
        y_i = a * np.sin(i) + b
        if y_i > y_max:
          y_max = y_i
        if y_i < y_min:
          y_min = y_i
      y_mark_1 = a * np.sin(0) + b
      y_mark_2 = a * np.sin(np.pi/2) + b

    if name_func == 'tg':
      y = a * np.tan(x) + b
      y[:-1][np.diff(y) < 0] = np.nan
      y_mark_1 = a * np.tan(0) + b
      x_mark_2 = np.pi/4
      y_mark_2 = a * np.tan(np.pi/4) + b
      plt.axvline(x= -2.5 * np.pi, color="black", linestyle="--")
      plt.axvline(x= -1.5 * np.pi, color="black", linestyle="--")
      plt.axvline(x= -np.pi/2, color="black", linestyle="--")
      plt.axvline(x= np.pi/2, color="black", linestyle="--")
      plt.axvline(x= 1.5 * np.pi, color="black", linestyle="--")
      plt.axvline(x= 2.5 * np.pi, color="black", linestyle="--")

    if target == 'f(0)':
      answer = y_mark_1
    if target == 'a':
      answer = a
    else:
      answer = b
    task = "На рисунке изображен график функции $\\f(x)$=$a$ $\\"+str(name_func)+"(x) + b$. Найдите $"+str(target)+"$."

    plt.xlim(-3*np.pi, 3*np.pi)
    if name_func == 'tg':
      if y_mark_2 > 9.9:
        plt.ylim(-10 + (y_mark_2 - 9), y_mark_2 + 1)
      else:
        plt.ylim(-10, 10)
    else:
      if y_max < 9.9 and y_min > (-9.9):
        plt.ylim(-10, 10)

    plt.scatter(x_mark_1, y_mark_1, color='blue', marker='p')
    plt.scatter(x_mark_2, y_mark_2, color='blue', marker='p')
    plt.plot(x, y)
    plt_base64 = save_to_base64(plt)
    plt.close()

    return {
        'answer': answer,
        'condition': task,
        "image": plt_base64,
    }