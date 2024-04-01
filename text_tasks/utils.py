import pymorphy2
import json
from sympy import Eq, symbols, solve
import re
from fractions import Fraction
from sympy import frac

def generate_context(file_json, category):
  '''Функция из файла-json возвращает список возможных вариантов сюжета для задачи,
  необходимо передать файл-json и требуемую категорию. Возвращает список'''
  with open(file_json, 'r', encoding='utf8') as my_file:
    templates = my_file.read()
    context = json.loads(templates)
  return context[category]

def choosing_declension_form(word, case='gent'):
  '''Функция подбирает правильную форму склонения переданного слова, см. https://opencorpora.org/dict.php?act=gram,
  по умолчанию слово пропишется в родительном падеже'''
  morph = pymorphy2.MorphAnalyzer()
  if len(word.split()) < 2:
    return morph.parse(word)[0].inflect({case}).word
  else:
    list_words = word.split()
    list_morphy = []
    for i in list_words:
      list_morphy.append(morph.parse(i)[0].inflect({case}).word)
    return ' '.join(list_morphy)

def capitalize_word(word):
  '''Функция напишет слово с заглавной буквы, если передается фраза,
  функция пропишет только первое слово с заглавной буквы'''
  if len(word.split()) < 2:
    return word.title()
  else:
    words_list = word.split(' ', 1)
    return words_list[0].title() +' '+ words_list[1]

def find_genus_object(item):
  '''Функция находит какого рода переданный объект,
  возвращает значение в виде цифры, где 1 - мужского рода, 2 - женского рода, 3 - среднего рода'''
  morph = pymorphy2.MorphAnalyzer()
  if len(item.split()) < 2:
    if morph.parse(item)[0].tag.gender == 'masc':
      return 1
    elif morph.parse(item)[0].tag.gender == 'femn':
      return 2
    else: return 3
  else:
    word = item.split()[1]
    if morph.parse(word)[0].tag.gender == 'masc':
      return 1
    elif morph.parse(word)[0].tag.gender == 'femn':
      return 2
    else: return 3

def find_number_object(item):
  '''Функция находит какого числа переданный предмет, множественного или единственного,
  в результате возвращает значение в виде цифры, где 1 - единственное число, 2 - множественное число'''
  morph = pymorphy2.MorphAnalyzer()
  if morph.parse(item)[0].tag.number == 'sing':
    return 1
  elif morph.parse(item)[0].tag.number == 'plur':
    return 2

def write_numeral_word(num):
  '''Функция напишет переданное числительное 2, 3, 4 или 5 словом в соответсвующей форме'''
  collection_numeral = {
      2: 'вдвое',
      3: 'втрое',
      4: 'вчетверо',
      5: 'впятеро'}
  return collection_numeral[num]

def create_regex_pattern(expression):
  '''Функция формирует шаблон регулярного выражения'''
  regex_pattern = re.escape(expression)
  return regex_pattern

def solves_equation(equation):
  '''Функция решает уравнение с неизвестной переменной х!'''
  x = symbols('x', real=True)
  equation_list = equation.split('=')
  eq = Eq(eval(equation_list[0]), eval(equation_list[1]))
  result = solve(eq, x)
  return result

def fraction_latex_format(result):
    '''Функция выводит число в дробь в стиле LaTeX и расчитывает все его целые значения, если таковы имеются'''
    fraction = Fraction(result).limit_denominator()
    if fraction.denominator == 1:
        return f'${fraction.numerator}$'
    else:
        whole_part, remainder = divmod(fraction.numerator, fraction.denominator)
        return f'${whole_part}\\frac{{{remainder}}}{{{fraction.denominator}}}$'
