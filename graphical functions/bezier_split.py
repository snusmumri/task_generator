# -*- coding: utf-8 -*-
"""bezier_split_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zgxuAnHtmG1B0rgw9cetoH8ETSoIabWL
"""

import random
import bezier
import numpy as np
import math
import fractions
from sympy import *
import matplotlib.pyplot as plt
import re
import time
from utilities.converting import save_to_base64


def graph_derivative_function_task_33_task_34():
    n_1 = random.randint(20, 30)
    x_start = random.randint(-9, -6)
    x_end = random.randint(2, 17)
    latex_interval = "[{}; {})".format(x_start, x_end + 1)
    x_arr = sorted(np.random.uniform(x_start, x_end, n_1))
    y_arr = np.random.uniform(-15, 15, n_1)
    nodes1 = np.asfortranarray([[x_start, *x_arr, x_end + 1], [1.0, *y_arr, 1.0]])
    curve1 = bezier.Curve(nodes1, degree=n_1 + 1)
    t_values = np.linspace(0.0, 1, 1000)
    points = curve1.evaluate_multi(t_values)
    points[1, 500:] += 5
    if random.randint(0, 1) == 1:
        text = r" Найдите промежутки убывания функции f(x)."
        numbers = []
        for i in range(1, len(points[0])):
            if points[1][i] <= 0:
                numbers.append(points[0][i])
        numbers.sort()
        segments = []
        segment = [numbers[0]]
        for i in range(1, len(numbers)):
            if numbers[i] - segment[-1] <= 0.2:
                segment.append(numbers[i])
            else:
                segments.append(segment)
                segment = [numbers[i]]
        segments.append(segment)
        cleaned_segments = []
        for segment in segments:
            cleaned_segments.append([segment[0], segment[-1]])
        tuples = [tuple(segment) for segment in cleaned_segments]
        integer_values = []
        for segment in tuples:
            start = segment[0]
            end = segment[1]
            if start - int(start) <= 0 and int(start) != 0 and int(end) > 0:
                integer_values.extend(range(int(start), int(end) + 1))
            elif start - int(start) <= 0 and int(start) != 0 and int(end) < 0:
                integer_values.extend(range(int(start), int(end)))
            elif start - int(start) <= 0 and int(start) == 0 and int(end) != 0:
                integer_values.extend(range(int(start), int(end) + 1))
            elif start - int(start) > 0 and int(end) != 0:
                integer_values.extend(range(int(start) + 1, int(end) + 1))
            elif start - int(start) <= 0 and int(start) != 0 and int(end) == 0 and end > 0:
                integer_values.extend(range(int(start), int(end) + 1))
            elif start - int(start) <= 0 and int(start) != 0 and int(end) == 0 and end < 0:
                integer_values.extend(range(int(start), int(end)))
            elif start - int(start) <= 0 and int(start) == 0 and end == 0:
                integer_values.extend(range(int(start) + 1, end))
            elif start - int(start) > 0 and end == 0:
                integer_values.extend(range(int(start) + 1, end))
            elif start - int(start) <= 0 and int(start) != 0 and int(start) == end:
                continue
        number = sum(integer_values)
    else:
        text = r" Найдите промежутки возрастания функции."
        numbers = []
        for i in range(1, len(points[0])):
            if points[1][i] > 0:
                numbers.append(points[0][i])
        numbers.sort()
        segments = []
        segment = [numbers[0]]
        for i in range(1, len(numbers)):
            if numbers[i] - segment[-1] <= 0.2:
                segment.append(numbers[i])
            else:
                segments.append(segment)
                segment = [numbers[i]]
        segments.append(segment)
        cleaned_segments = []
        for segment in segments:
            cleaned_segments.append([segment[0], segment[-1]])
        tuples = [tuple(segment) for segment in cleaned_segments]
        integer_values = []
        for segment in tuples:
            start = segment[0]
            end = segment[1]
            if start - int(start) <= 0 and int(start) != 0 and int(end) > 0:
                integer_values.extend(range(int(start), int(end) + 1))
            elif start - int(start) <= 0 and int(start) != 0 and int(end) < 0:
                integer_values.extend(range(int(start), int(end)))
            elif start - int(start) <= 0 and int(start) == 0 and int(end) != 0:
                integer_values.extend(range(int(start), int(end) + 1))
            elif start - int(start) > 0 and int(end) != 0:
                integer_values.extend(range(int(start) + 1, int(end) + 1))
            elif start - int(start) <= 0 and int(start) != 0 and int(end) == 0 and end > 0:
                integer_values.extend(range(int(start), int(end) + 1))
            elif start - int(start) <= 0 and int(start) != 0 and int(end) == 0 and end < 0:
                integer_values.extend(range(int(start), int(end)))
            elif start - int(start) <= 0 and int(start) == 0 and end == 0:
                integer_values.extend(range(int(start) + 1, end))
            elif start - int(start) > 0 and end == 0:
                integer_values.extend(range(int(start) + 1, end))
            elif start - int(start) <= 0 and int(start) != 0 and int(start) == end:
                continue
        integer_values_without_last = integer_values[:-1]
        number = sum(integer_values_without_last)
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    plt.plot(points[0, :500], points[1, :500], color='purple')
    plt.plot(points[0, 500:], points[1, 500:], color='purple')
    plt.plot(points[0][500], points[1][500],
             color='purple', marker='o', markerfacecolor='white', markeredgewidth=2, markersize=8)
    plt.plot(points[0][999], points[1][999],
             color='purple', marker='o', markerfacecolor='white', markeredgewidth=2, markersize=8)
    plt.plot(points[0][1], points[1][1],
             color='purple', marker='o', markerfacecolor='white', markeredgewidth=2, markersize=8)
    plt.plot(points[0][499], points[1][499],
             color='purple', marker='o', markerfacecolor='white', markeredgewidth=2, markersize=8)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    arrow_length = 10
    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(0, arrow_length), textcoords='offset points',
                ha='center', va='bottom')
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(arrow_length, 0), textcoords='offset points',
                ha='center', va='bottom')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.grid(True, linewidth=0.5, linestyle='dotted')
    plt.axis('equal')
    ax.set_xticks(range(x_start - 9, x_end + 9))
    ax.set_yticks(range(-17, 17))
    ax.set_xticklabels([i if i % 2 == 0 else '' for i in range(x_start - 9, x_end + 9)])
    ax.set_yticklabels([i if i % 2 == 0 else '' for i in range(-17, 17)])
    ax.set_xlim(x_start - 1, x_end + 2)
    ax.set_ylim(min(points[1]) - 1, max(points[1]) + 1)
    plt.legend(labels=["y = f'(x)"])
    plt_base64 = save_to_base64(plt)
    plt.close()
    task = r'Функция определена и непрерывна на полуинтервале' + ' ' + '\(' + str(latex(latex_interval)) + '\).' + r' На рисунке изображен график её производной.' + text + r' В ответе укажите сумму целых точек, входящих в эти промежутки.'
    answer = number
    return {
        "condition": task,
        "answer": answer,
        "image": plt_base64,
        }
