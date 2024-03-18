from sympy import *
import numpy as np
import fractions
from fractions import Fraction
import random
import math
import decimal
from pytexit import py2tex
import re

def transformation_task(string):
  while True:
    elements = []
    start_index = string.find('C_')

    while start_index != -1:
      end_index = string.find(']', start_index)
      element = string[start_index: end_index + 1]
      elements.append(element)
      start_index = string.find('C_', end_index)

      values = []

    for element in elements:
      start_index = element.find('[') + 1
      end_index = element.find(']')
      range_string = element[start_index: end_index]
      range_values = list(map(int, range_string.split(', ')))
      random_value = random.randint(range_values[0], range_values[1])
      values.append(random_value)

    elements_g = []
    start_index = string.find('G_')

    while start_index != -1:
      end_index = string.find(']', start_index)
      element = string[start_index : end_index + 1]
      elements_g.append(element)
      start_index = string.find('G_', end_index)

    values_g = []

    for element in elements_g:
      start_index = element.find('[') + 1
      end_index = element.find(']')
      range_string = element[start_index : end_index]
      range_values = list(map(float, range_string.split(', ')))
      random_value = round(random.uniform(range_values[0], range_values[1]), 2)
      values_g.append(random_value)

    updated_string = string

    for i, el in enumerate(elements):
      updated_string = updated_string.replace(el, str(values[i]))

    for i, el in enumerate(elements_g):
      updated_string = updated_string.replace(el, str(values_g[i]))

    answer = eval(updated_string)
    task_ower = 'Вычислите: '+py2tex(updated_string,
                                print_formula = False,
                                print_latex = False,
                                tex_enclosure='$',
                                simplify_multipliers=False,
                                tex_multiplier='\cdot',
                                simplify_fractions =True)

    pattern_1 = r'{(\\)?frac{(\d+)}{(\d+)}}\^(\d+)'
    replacement = r'(\1frac{\2}{\3})^\4'
    task_show = re.sub(pattern_1, replacement, task_ower)

    pattern_2 = r'\\frac{(\d+)}{(\d+)}'
    matches = re.findall(pattern_2, task_show)

    list_results = []
    for match in matches:
      a = int(match[0])
      b = int(match[1])
      result = f'\\frac{{{a}}}{{{b}}}'
      list_results.append(result)
    
    numerators = []
    for fraction in list_results:
      match = re.match(r'\\frac{(\d+)}{(\d+)}', fraction)
      a = int(match.group(1))
      b = int(match.group(2))
      if a >= b:
        d = b
        a, b = a // b, a % b
        numerators.append(b)
        frac_to_add = r'('+str(a) + r'\frac{' + str(b) + '}{' + str(d) + '})'
      else:
        frac_to_add =  r'\frac{' + str(a) + '}{' + str(b) + '}'
      task_show = task_show.replace(fraction, frac_to_add)

    if abs(answer)>=0.000001 and 0 not in numerators:
      if abs(int(answer * 1000) - answer * 1000) < 0.0001:
        if answer<=10000 and answer>=-1000:
          break

  return {
      "condition": task_show,
      "answer": round(answer, 5)
    }
