from sympy import Eq, symbols, solve, expand, factor
from pytexit import py2tex
import random
import re

from task_generator.text_tasks.utils import create_regex_pattern, solves_equation


def generation_and_solution_new_equation(sample_equation):
  '''Функция генерирует уравнение с неивестной х! исходя из образца путем подстановки новых коэффициентов и решает это уравнение.
  Если в образце есть квадратный трехчлен, который раскладывается на линейные множители, и эти множители присутствуют в образце,
  тогда сгенерированное уравнение также будет содержать это условие. Важное замечание! Если в образце несколько квадратных трехчленов,
  то раскладуемый должен идти первым, второй будет игнорироваться.'''
  x = symbols('x', real=True)
  sample_equation = sample_equation.replace(' ','')
  pattern_search_coefficients = re.compile(r'(?<!\*\*)(\d+)')                                         # шаблон поиска всех коэффициентов
  coefficients_findall = pattern_search_coefficients.findall(sample_equation)
  pattern_search_quadr_equation   = re.compile(r'(\d*\**x\*{2}2[-+]\d*\**x[-+]\d+)')                  # шаблон поиска квадратных уравнений
  quadr_equation = pattern_search_quadr_equation.search(sample_equation)
  if quadr_equation != None and quadr_equation[0] != (str(factor(quadr_equation[0]))).replace(' ', ''):
    sample_equation_brackets = re.sub(create_regex_pattern(quadr_equation[0]), '['+quadr_equation[0]+']', sample_equation)
    pattern_linear_multipls = re.compile(r'(\(\d*\**x[-+]\d{1,}\))')                                  # шаблон поиска линейных множителей
    linear_multipls_list = pattern_linear_multipls.findall((str(factor(quadr_equation[0]))).replace(' ', ''))
    index_linear_multipls = []
    for i in linear_multipls_list:
      linear_factors = re.finditer(create_regex_pattern(i), sample_equation)
      sample_equation_brackets = re.sub(create_regex_pattern(i), '{'+i+'}', sample_equation_brackets)
      [index_linear_multipls.append(k.span()) for k in linear_factors]
    while True:
        random_coefficient = [random.randint(2, 9) for _ in range(len(coefficients_findall))]
        new_equation = re.sub(pattern_search_coefficients, lambda match: str(random_coefficient.pop(0)), sample_equation_brackets)
        if len(linear_multipls_list) == len(index_linear_multipls) == 2:
          pattern_multipls_in_brackets = re.compile(r'{(\(\d*\**x[-+]\d*\))}')                         # шаблон поиска множителей в фигурных скобках
          linear_multipls_new = pattern_multipls_in_brackets.findall(new_equation)[0]+'*'+pattern_multipls_in_brackets.findall(new_equation)[1]
          new_equation_right = re.sub(re.compile(r'\[.*\]'), str(expand(linear_multipls_new)).replace(' ', ''), new_equation).replace('{', '')
          new_equation_right = new_equation_right.replace('}', '')
        elif len(linear_multipls_list) == len(index_linear_multipls) == 1:
          pattern_multipls_in_brackets = re.compile(r'{(\(\d*\**x[-+]\d*\))}')                         # шаблон поиска множителей в фигурных скобках
          linear_multipls_new = pattern_multipls_in_brackets.findall(new_equation)[0]+'**2'
          new_equation_right = re.sub(re.compile(r'\[.*\]'), str(expand(linear_multipls_new)).replace(' ', ''), new_equation).replace('{', '')
          new_equation_right = new_equation_right.replace('}', '')
        else:
          new_equation_right = re.sub(re.compile(r'[\[\]{}]'), '', new_equation).replace(' ', '')
        result = solves_equation(new_equation_right)
        if 0 < len(result) < 3 and abs(int(result[0]*1000)-result[0]*1000)<0.0001:
          break
  else:
    while True:
      random_coefficient = [random.randint(2, 12) for _ in range(len(coefficients_findall))]
      new_equation_right = re.sub(pattern_search_coefficients, lambda match: str(random_coefficient.pop(0)), sample_equation)
      result = solves_equation(new_equation_right)
      if 0 < len(result) < 3 and abs(int(result[0]*1000)-result[0]*1000)<0.0001:
        break
  string_for_latex = new_equation_right.split('=')[0] + '==' + new_equation_right.split('=')[1]
  latex_string = py2tex(string_for_latex,
                    print_formula = False,
                    print_latex = False,
                    tex_enclosure='$',
                    simplify_multipliers=False,
                    tex_multiplier='',
                    simplify_fractions =True)
  task = f'Решите уравнение: {latex_string}'
  answer = ""
  for position, value in enumerate(result):
      numerator = value.p
      denominator = value.q
      if denominator == 1:
          answer += ((r"\(" + f"{numerator}") + "\)")
      else:
          answer += ((((r"\(\frac{" + f"{numerator}") + "}{") + f"{denominator}") + r"}\)")
      if position < len(result) - 1:
          answer += ", "
  return {
      "condition": task,
      "answer": answer
    }


'''Генерация аналогичных задач № 2295 с портала https://kuzovkin.info/zadachi/?read_text_from_string=2295
    Решите уравнение: (x**2−3)/2−6*x=5'''
prototype_2295 = '(x**2-3)/2-6*x=5'

'''Генерация аналогичных задач № 2317 с портала https://kuzovkin.info/zadachi/?read_text_from_string=2317
    Решите уравнение: 3*x+4/x=7'''
prototype_2317 = '3*x+4/x=7'

'''Генерация аналогичных задач № 2333 с портала https://kuzovkin.info/zadachi/?read_text_from_string=2333
    Решите уравнение: (4*x-5)**2-(2*x+3)**2=0'''
prototype_2333 = '(4*x-5)**2-(2*x+3)**2=0'

'''Генерация аналогичных задач № 6159 с портала https://kuzovkin.info/zadachi/?read_text_from_string=6159
    Решите уравнение: (2*x-1)*(2*x+1)+x*(x-1)=2*x*(x+1)'''
prototype_6159 = '(2*x-1)*(2*x+1)+x*(x-1)=2*x*(x+1)'

'''Генерация аналогичных задач № 6169 с портала https://kuzovkin.info/zadachi/?read_text_from_string=6169
    Решите уравнение: (2*x**2+x)/5=(4*x-2)/3'''
prototype_6169 = '(2*x**2+x)/5=(4*x-2)/3'

'''Генерация аналогичных задач № 6170 с портала https://kuzovkin.info/zadachi/?read_text_from_string=6170
    Решите уравнение: (4*x**2+x)/3-(5*x-1)/6=(x**2+17)/9'''
prototype_6170 = '(4*x**2+x)/3-(5*x-1)/6=(x**2+17)/9'

'''Генерация аналогичных задач № 6207 с портала https://kuzovkin.info/zadachi/?read_text_from_string=6207
    Решите уравнение: (x**2+4*x+11)**2=(7*x**2+2*x+3)**2'''
prototype_6207 =  '(x**2+4*x+11)**2=(7*x**2+2*x+3)**2'

'''Генерация аналогичных задач № 6208 с портала https://kuzovkin.info/zadachi/?read_text_from_string=6208
    Решите уравнение: (4*x-5)**2+(2*x+3)**2=0'''
prototype_6208 =  '(4*x-5)**2+(2*x-3)**2=0'

'''Генерация аналогичных задач № 12300 с портала https://kuzovkin.info/one_exercise_1/12300
    Решите уравнение: x**2+5*x=0'''
prototype_12300 =  'x**2+5*x=0'

'''Генерация аналогичных задач № 12301 с портала https://kuzovkin.info/one_exercise_1/12301
    Решите уравнение: 2*x**2-9*x=0'''
prototype_12301 =  '2*x**2-9*x=0'

'''Генерация аналогичных задач № 12329 с портала https://kuzovkin.info/one_exercise_1/12329
    Решите уравнение: (x**2-6*x)/3=x'''
prototype_12329 =  '(x**2-6*x)/3=x'

'''Генерация аналогичных задач № 12330 с портала https://kuzovkin.info/one_exercise_1/12330
    Решите уравнение: (x**2-x)/2+x/3=0'''
prototype_12330 =  '(x**2-x)/2+x/3=0'

'''Генерация аналогичных задач № 12332 с портала https://kuzovkin.info/one_exercise_1/12332
    Решите уравнение: (x**2-4)/5-(x**2-1)/3=-1'''
prototype_12332 =  '(x**2-4)/5-(x**2-1)/3=-1'

'''Генерация аналогичных задач № 12369 с портала https://kuzovkin.info/one_exercise_1/12369
    Решите уравнение: 2*x-(x+1)**2=3*x**2-5'''
prototype_12369 =  '2*x-(x+1)**2=3*x**2-5'

'''Генерация аналогичных задач № 12371 с портала https://kuzovkin.info/one_exercise_1/12371
    Решите уравнение: 6*x**2-(x+2)**2=4*(4-x)'''
prototype_12371 =  '6*x**2-(x+2)**2=4*(4-x)'

'''Генерация аналогичных задач № 12374 с портала https://kuzovkin.info/one_exercise_1/12374
    Решите уравнение: (x-3)/(x+3)-(x+3)/(x-3)=0'''
prototype_12374 =  '(x-3)/(x+3)-(x+3)/(x-3)=0'

'''Генерация аналогичных задач № 12398 с портала https://kuzovkin.info/one_exercise_1/12398
    Решите уравнение: 5*x**2-8*x+3=0'''
prototype_12398 =  '5*x**2-8*x+3=0'

'''Генерация аналогичных задач № 12400 с портала https://kuzovkin.info/one_exercise_1/12400
    Решите уравнение: 3*x**2+32*x+80=0'''
prototype_12400 =  '3*x**2+32*x+80=0'

'''Генерация аналогичных задач № 12401 с портала https://kuzovkin.info/one_exercise_1/12401
    Решите уравнение: 100*x**2-160*x+63=0'''
prototype_12401 =  '100*x**2-160*x+63=0'

'''Генерация аналогичных задач № 12408 с портала https://kuzovkin.info/one_exercise_1/12408
    Решите уравнение: x**2=2*x+48'''
prototype_12408 =  'x**2=2*x+48'

'''Генерация аналогичных задач № 12409 с портала https://kuzovkin.info/one_exercise_1/12409
    Решите уравнение: 6*x**2+7*x=5'''
prototype_12409 =  '6*x**2+7*x=5'

'''Генерация аналогичных задач № 12717 с портала https://kuzovkin.info/one_exercise_1/12717
    Решите уравнение: (x**2+1)/(x**2-4*x+3)+2/(x-1)=3/(x-3)'''
prototype_12717 =  '(x**2+1)/(x**2-4*x+3)+2/(x-1)=3/(x-3)'

'''Генерация аналогичных задач № 12719 с портала https://kuzovkin.info/one_exercise_1/12719
    Решите уравнение: (x**2+14)/(x**2-x-2)+10/(x+1)=3*x/(x-2)'''
prototype_12719 =  '(x**2+14)/(x**2-x-2)+10/(x+1)=3*x/(x-2)'

'''Генерация аналогичных задач № 12720 с портала https://kuzovkin.info/one_exercise_1/12720
    Решите уравнение: 6/(x-4)-3*x/(x+2)=(x**2+20)/(x**2+2*x-8)'''
prototype_12720 =  '6/(x-4)-3*x/(x+2)=(x**2+20)/(x**2-2*x-8)'

'''Генерация аналогичных задач № 12721 с портала https://kuzovkin.info/one_exercise_1/12721
    Решите уравнение: (x**2-5)/(x**2-3*x+2)-(x+3)/(x-1)=(2*x+2)/(x-2)'''
prototype_12721 =  '(x**2-5)/(x**2-3*x+2)-(x+3)/(x-1)=(2*x+2)/(x-2)'

'''Генерация аналогичных задач № 12722 с портала https://kuzovkin.info/one_exercise_1/12722
    Решите уравнение: (2*x**2+9*x)/(x**2-x-6)+(3*x+2)/(x+2)=(2*x+3)/(x-3)'''
prototype_12722 =  '(2*x**2+9*x)/(x**2-x-6)+(3*x+2)/(x+2)=(2*x+3)/(x-3)'
