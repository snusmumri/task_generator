import fractions
import random
from sympy import *
import re


# Функция для вывода ответа
def find_answer(splitted_eq):
  x = symbols('x')
  eq = Eq(sympify(splitted_eq[0]), sympify(splitted_eq[1]))
  answer = solve(eq, x)
  if len(answer) > 0 and im(solve(eq, x)[0])==0:
    if (answer[0] == 0 or abs(int(answer[0]) - answer[0]) < 0.000001) and abs(answer[0]) < 100: #добавила, чтобы очень большие целочисленные ответы не получались
      return round(answer[0])
    elif abs(int(answer[0]*100) - answer[0]*100) < 0.0001 and abs(answer[0]) < 100: #добавила, чтобы очень большие целочисленные ответы не получались
      return round(answer[0], 2)
  return False


# Функция создания обыкновенной дроби
def create_fraction():
  n = random.randrange(-30, 30)
  m = random.randrange(2, 15)
  while n == 0 or abs(n) == m or abs(n) % m == 0:
    n = random.randrange(-30, 30)
  return fractions.Fraction(n, m)


# Новый генератор значений (немного увеличила его за счет добавления блока генерации дробей)
def generate_values_and_recieve_answer(equation_to_solve):
  variables = re.findall('\{c\d+\}', equation_to_solve) # Найдите все вхождения c1, c2, c3, c4 в выражении
  fractions_ = re.findall('\{fr\d+\}', equation_to_solve) # Найдите все вхождения обыкновенных дробей, если они есть
  deci = re.findall('\{deci\d+\}', equation_to_solve) # Найдите все вхождения десятичных дробей, если они есть
  while True:
    equation_to_solve_after_parse = equation_to_solve
    for var in variables:
      rand_num = random.randint(-20, 20)
      while rand_num == 0 or (var in ['{c20}', '{c21}', '{c22}', '{c23}', '{c24}', '{c25}', '{c26}', '{c27}', '{c28}', '{c29}']
                              and (rand_num == -1 or rand_num == 1)):
        rand_num = random.randint(-20, 20)
      equation_to_solve_after_parse = re.sub(var, str(rand_num), equation_to_solve_after_parse)
    if len(fractions_) != 0:
      for fract in fractions_:
        gen_fr = create_fraction()
        equation_to_solve_after_parse = re.sub(fract, str(gen_fr), equation_to_solve_after_parse)
    if len(deci) != 0:
      for de in deci:
        de_gen = random.randrange(-1000, 1000, 5) / 100
        while de_gen == 0 or de_gen % 1 == 0:
          de_gen = random.randrange(-1000, 1000, 5) / 100
        equation_to_solve_after_parse = re.sub(de, str(de_gen), equation_to_solve_after_parse)
    splitted_eq = equation_to_solve_after_parse.split('=')
    answer = find_answer(splitted_eq)
    if answer or str(answer) == '0':
        break
  return equation_to_solve_after_parse, answer


# Парсер уравнений
def parse_and_generate_task(equation_to_solve):
  equation_to_solve = equation_to_solve.replace('+-', '-').replace('--', '+')
  spl_eq = equation_to_solve.split(' = ')
  splitted_eq = []
  for eq_part in spl_eq:
    splitted_eq.append(eq_part.split(' '))
  k = 0
  all_parts_list = []
  for spl_part in splitted_eq:
    ind = 0 # считаем индексы
    for part in spl_part:
      if part == '/':
        all_parts_list.append(':')
        ind += 1
        continue
      elif len(re.findall(r'^\-\d+$', part)) != 0 and spl_part[spl_part.index(part)-1] == '/':
        all_parts_list.append('('+part+')')
        continue
      elif len(re.findall(r'^\([-x\d*]+$', part)) != 0 or part == ')':
        all_parts_list.append(part)
        continue
      elif len(re.findall(r'^[-]*\d+\*\([-\d*]+[+-]+[-()\d]+', part))!=0 or len(re.findall(r'^x\*\([-\d*]+\*x[+-]+[\d]+\)$', part))!=0: # Проверка и упрощение для выражений типа '16*(2*4*14-(4)**2*(1*2-5*-11)/(5*1))+(14)**2-((4)**2*2*-11)/(5*1)'
        part = str(sympify(part))
      elif (len(re.findall(r'^[-]*[()\/\d*x.]+', part))!=0 and len(re.findall(r'\([-]*[\d]+\/[\d]+\)[*]+', part))==0
            and len(re.findall(r'\([-]*[\d]+\/[\d]+\)\*\([-\d.]+\*x[+-]+[\d.]+\)', part))==0 and len(re.findall(r'\([-\d.*x+]*\)\/[-]*[\d.]+$', part))==0
            and len(re.findall(r'^\([-\d.]*\/\([-]*[\d.x*]+\)\)$', part))==0 and len(re.findall(r'^[-\d.x*]*\([-\d.*x+^{}()]*\)\/[-]*[\d.]+$', part))==0
            and len(re.findall(r'^[-\d.x*()]*[*]*\([-\d.*x+^{}()]*\)\/\([-\d.*x+^{}()]*\)$', part))==0 and len(re.findall(r'^(\-*[\d]+[+-][\d*]*\()+', part))==0
            and len(re.findall(r'^\([-\d()\/]+[+-][-\d*x]*\)$', part))==0 and len(re.findall(r'^\([-]*[\d]+\)\/\([-\d]*\+[-(\d\/x]+\)\)$', part))==0): # что угодно: (2)**2*3*x*(3*x+18), (12)**2/-2*(-2*x**2+3), -1*x, -1*2*x**2, (2)**2*3*x*(3*x+18)*(3*x+18)
        part_sym_spl = part.split('*(', 1)
        if len(re.findall(r'^[-]*\d+[.]\d+$', part_sym_spl[0]))!=0:
          if len(part_sym_spl)==2:  part = part_sym_spl[0]+'*('+part_sym_spl[1]
          else: part = str(part)
        elif len(part_sym_spl) == 2 and '(' in part_sym_spl[0] and ('+' or '-') in part_sym_spl[0]:
          part = '('+str(sympify(part_sym_spl[0]))+')'+'*('+part_sym_spl[1]
        elif len(part_sym_spl) == 2 and ')*(' in part_sym_spl[1]:
          part = str(sympify(part_sym_spl[0]))+'*('+part_sym_spl[1]
        elif len(part_sym_spl) == 2 and '(' not in part_sym_spl[0]:
          part = str(sympify(part_sym_spl[0]))+'*('+part_sym_spl[1]
        elif len(part_sym_spl) == 1 and '(' in part and len(re.findall(r'\*\*\d$', part))==0:
          part = '('+str(sympify(part))+')'
        else: part = str(sympify(part))
      part = part.replace(' ', '').replace('*x', ' x').replace('**2', '^{2}').replace('**3', '^{3}').replace('**5', '^{5}')

      if len(re.findall(r'\([-]*[\dx. ]+\/[-(]*[\dx. ]+[)]*\)', part)) != 0 and len(re.findall(r'^\([-]*[\d]+\)\/\([-\d]*\+[-(\d\/x]+\)\)$', part))==0: # для обыкновенных дробей (3/5), при генерации обязательно задаются скобки
        if len(re.findall(r'^\([-\d()\/]+[+-][-\d x]+\)$', part)) != 0:
          if len(re.findall(r'\-[\d]+[ x]+', part)) != 0:
            splitted_part = [part.strip('()').split(')-')[0], '-'+part.strip('()').split(')-')[1]]
          elif len(re.findall(r'\+[\d]+[ x]+', part)) != 0:
            splitted_part = [part.strip('()').split('+')[0], '+'+part.strip('()').split('+')[1]]
        elif len(re.findall(r'\(.*\)\*\([^(].*\)', part)) != 0:
          splitted_part = part.strip('()').split('*')
        elif len(re.findall(r'\/\(.*\)\)', part)) != 0:
          splitted_part = [part.strip('()')]
        elif len(re.findall(r'\*\(\(.* x[+-]', part))!=0:
          splitted_part = [part.split('*')[0], part.split('*')[1].split(' ')[0], *part.split('*')[1].split(' ')[1].split('+')]
        else: splitted_part = part.strip('()').split(' ')
        list_ = []
        for el in splitted_part:
          if '/' in el:
            sp_el = el.split('/')
            if (sp_el[0].strip('()') == '-x' or ('x' in sp_el[1] and len(re.findall(r'^[(]*\-', sp_el[1])) == 0 and float(sp_el[0].strip('()')) < 0)
                or ('x' in sp_el[1] and len(re.findall(r'^[(]*\-', sp_el[1])) != 0 and float(sp_el[0].strip('()')) > 0)):
              list_.append('-'+'\\frac{'+sp_el[0].strip('-()')+'}{'+sp_el[1].strip('-()')+'}')
            elif (sp_el[0].strip('()') == 'x' or 'x' in sp_el[1]
                  or ('x' in sp_el[1] and len(re.findall(r'^[(]*\-', sp_el[1])) != 0 and float(sp_el[0].strip('()')) < 0)):
              list_.append('\\frac{'+sp_el[0].strip('-()')+'}{'+sp_el[1].strip('-()')+'}')
            elif int(sp_el[0].strip('-()')) > int(sp_el[1].strip('()')) and int(sp_el[0].strip('()')) < 0:
              list_.append('-'+str(int(int(sp_el[0].strip('-()'))/int(sp_el[1].strip('()'))))+'\\frac{'+str(int(sp_el[0].strip('-()'))%int(sp_el[1].strip('()')))+'}{'+sp_el[1].strip('()')+'}')
            elif int(sp_el[0].strip('()')) > int(sp_el[1].strip('()')) and int(sp_el[0].strip('()')) > 0:
              list_.append(str(int(int(sp_el[0].strip('()'))/int(sp_el[1].strip('()'))))+'\\frac{'+str(int(sp_el[0].strip('()'))%int(sp_el[1].strip('()')))+'}{'+sp_el[1].strip('()')+'}')
            elif int(sp_el[0].strip('()')) < 0:
              list_.append('-'+'\\frac{'+sp_el[0].strip('-()')+'}{'+sp_el[1].strip('()')+'}')
            else: list_.append('\\frac{'+sp_el[0].strip('-()')+'}{'+sp_el[1].strip('()')+'}')
          else: list_.append(el)
        expr = ''
        for el in list_:
          if '(' in el:
            expr += '\\cdot('+el.strip('()')+')'
          elif '((' in splitted_part[list_.index(el)]:
            expr += '\\cdot('+el.strip('()')
          elif list_[list_.index(el)-1]=='x' and len(re.findall(r'^\-', el))!=0 and '))' in splitted_part[list_.index(el)]:
            expr += el+')'
          elif list_[list_.index(el)-1]=='x' and len(re.findall(r'^\-', el))==0 and '))' in splitted_part[list_.index(el)]:
            expr += '+'+el+')'
          elif len(list_) != 2 and list_[list_.index(el)-1]=='x' and len(re.findall(r'^\-', el))==0:
            expr += '+'+el
          else: expr += el
        if expr.count('(') < expr.count(')'):
          expr = expr.strip(')')
        if len(re.findall(r'^\(\(', part)) != 0:
          expr = '('+expr+')'
        all_parts_list.append(expr)

      elif len(re.findall(r'^\-*[\d.]*[x ]*[*]*\([-\d. x+^{}()]*\)\/[-]*[\d.]+$', part)) != 0: # ловим (-5 x-6)/8, -5 x*(-5 x-6)/8, -5*(-5 x-6)/8, -5*(-6-5 x)/8
        splitted_part = part.split('/')
        for el in splitted_part:
          splitted_part[splitted_part.index(el)] = el.split('*')
        spl_eq_part = []
        for el in splitted_part:
          if type(el) == list:
            for i in range(0, len(el)):
              spl_eq_part.append(el[i])
          else: spl_eq_part.append(el)
        if spl_eq_part[0] == '-1 x': spl_eq_part[0] = '-x'
        elif spl_eq_part[0] == '1 x': spl_eq_part[0] = 'x'
        if len(spl_eq_part) == 3:
          if '-' in spl_eq_part[0] and '-' in spl_eq_part[2]: # для такой структуры: ['-7', '(1*x+101)', '-14']
            spl_eq_part[0] = spl_eq_part[0].strip('-')
            spl_eq_part[2] = spl_eq_part[2].strip('-')
          elif '-' not in spl_eq_part[0] and '-' in spl_eq_part[2]: # для такой структуры: ['7', '(1*x+101)', '-14']
            spl_eq_part[0] = '-' + spl_eq_part[0]
            spl_eq_part[2] = spl_eq_part[2].strip('-')
        elif len(spl_eq_part) == 2:
          if '-' in spl_eq_part[1]:
            spl_eq_part[0] = '-' + spl_eq_part[0]
            spl_eq_part[1] = spl_eq_part[1].strip('-')

        for el in spl_eq_part:
          if el == '1':
            spl_eq_part.remove(el)
          elif el == '-1':
            spl_eq_part[spl_eq_part.index(el)+1] = '-'+spl_eq_part[spl_eq_part.index(el)+1]
            spl_eq_part.remove(el)
        if len(spl_eq_part) == 3 and len(re.findall(r'^\-', spl_eq_part[0])) != 0 and spl_part[ind-1] == '/':
          all_parts_list.append('\\frac{('+spl_eq_part[0]+')\\cdot'+spl_eq_part[1]+'}{'+spl_eq_part[2]+'}')
        elif len(spl_eq_part) == 3 and spl_part[ind-1] == '/':
          all_parts_list.append('\\frac{'+spl_eq_part[0]+'\\cdot'+spl_eq_part[1]+'}{'+spl_eq_part[2]+'}')
        elif len(spl_eq_part) == 3:
          all_parts_list.append(spl_eq_part[0]+'\\cdot'+'\\frac{'+spl_eq_part[1].strip('()')+'}{'+spl_eq_part[2]+'}')
        elif len(spl_eq_part) == 2 and '(' in spl_eq_part[1]:
          all_parts_list.append(spl_eq_part[0]+'\\cdot'+spl_eq_part[1])
        elif len(spl_eq_part) == 2 and len(re.findall(r'^\-', spl_eq_part[0])) != 0 and '))' in spl_eq_part[0]:
          all_parts_list.append('-\\frac{'+spl_eq_part[0].strip('-')+'}{'+spl_eq_part[1]+'}')
        elif len(spl_eq_part) == 2 and len(re.findall(r'^\-', spl_eq_part[0])) != 0:
          all_parts_list.append('-\\frac{'+spl_eq_part[0].strip('-').strip('()')+'}{'+spl_eq_part[1]+'}')
        elif len(spl_eq_part) == 2 and '(' in spl_eq_part[0] and '))' in spl_eq_part[0]:
          all_parts_list.append('\\frac{'+spl_eq_part[0]+'}{'+spl_eq_part[1]+'}')
        elif len(spl_eq_part) == 2 and '(' in spl_eq_part[0]:
          all_parts_list.append('\\frac{'+spl_eq_part[0].strip('()')+'}{'+spl_eq_part[1]+'}')
        else: all_parts_list.append(*spl_eq_part)

      # вывод различных вариантов структур (обозначены регулярными выражениями)
      elif len(re.findall(r'^[-]*\d*[ x]*\/\d*(\*\([-\d x+^{}]*\))+$', part)) != 0:  # для таких структур -x/11*(11 x-19), 110 x/11*(11 x-19), 110 x/11*(11 x^{2}-19), 110 x/11*(11 x-19)*(11 x-19), 7/2*(14 x-15)*(1 x-5)
        splitted_part = part.split('*')
        if len(splitted_part) == 3:
          if len(re.findall(r'^\-', splitted_part[0])) != 0:
            all_parts_list.append('-\\frac{'+splitted_part[0].split('/')[0].strip('-')+'}{'+splitted_part[0].split('/')[1]+'}\\cdot'+splitted_part[1]+'\\cdot'+splitted_part[2])
          else: all_parts_list.append('\\frac{'+splitted_part[0].split('/')[0]+'}{'+splitted_part[0].split('/')[1]+'}\\cdot'+splitted_part[1]+'\\cdot'+splitted_part[2])
        elif len(splitted_part) == 2:
          if len(re.findall(r'^\-', splitted_part[0])) != 0:
            all_parts_list.append('-\\frac{'+splitted_part[0].split('/')[0].strip('-')+'}{'+splitted_part[0].split('/')[1]+'}\\cdot'+splitted_part[1])
          else: all_parts_list.append('\\frac{'+splitted_part[0].split('/')[0]+'}{'+splitted_part[0].split('/')[1]+'}\\cdot'+splitted_part[1])
      elif len(re.findall(r'^[-\d. x^{}]*([*]*\([-\d. x+^{}()]*\))+[\d{}^]*$', part)) != 0: # для таких структур -5 x*(x-13), -2*(x-11), (2 x^{2}-9)*(2 x+3), (x^{2}+17), (2 x-2)*(x^{2}-2 x+17), -x*(2 x^{2}-9)*(2 x+3), -15 x*(-15+(9 x+8))
        splitted_part = part.split('*')
        if len(splitted_part) == 3:
          all_parts_list.append(splitted_part[0]+'\\cdot'+splitted_part[1]+'\\cdot'+splitted_part[2])
        elif len(splitted_part) == 2:
          all_parts_list.append(splitted_part[0]+'\\cdot'+splitted_part[1])
        else: all_parts_list.append(str(part))
      elif len(re.findall(r'^[-\d.x ()]*[*]*\([-\d. x+^{}()]*\)\/\([-\d. x+^{}()]*\)$', part)) != 0: # для таких структур (2 x+14)/(4 x+7), (2)*(2 x+14)/(4 x+7), (-2 x)*(2 x+14)/(4 x+7), (-2)*(2 x+14)/(4 x+7)
        splitted_part = part.split('/')
        if '*' in splitted_part[0]:
          splitted_part = [*splitted_part[0].split('*'), splitted_part[1]]
          if len(re.findall(r'^\(\-', splitted_part[0])) != 0:
            splitted_part = [splitted_part[0]+'\\cdot'+splitted_part[1], splitted_part[2]]
          else: splitted_part = [splitted_part[0].strip('()')+'\\cdot'+splitted_part[1], splitted_part[2]]
        elif len(re.findall(r'^\([-\d. x]*\)$', splitted_part[0])) != 0:
          splitted_part = [splitted_part[0].strip('()'), splitted_part[1].strip('()')]
        all_parts_list.append('\\frac{'+splitted_part[0]+'}{'+splitted_part[1]+'}')
      elif len(re.findall(r'^\([-]*[\d]+\)\/\([-\d]*\+[-(\d\/x]+\)\)$', part)) != 0:
        splitted_part = [part.strip('()').split(')/(')[0], *part.strip('()').split(')/(')[1].split('/')]
        if '+(-' in splitted_part[1]:
          splitted_part = [splitted_part[0], splitted_part[1].split('+(-')[0]+'-', splitted_part[1].split('+(-')[1], splitted_part[2]]
        else: splitted_part = [splitted_part[0], splitted_part[1].split('+(')[0]+'+', splitted_part[1].split('+(')[1], splitted_part[2]]
        all_parts_list.append('\\frac{'+splitted_part[0]+'}{('+splitted_part[1]+'\\frac{'+splitted_part[2]+'}{'+splitted_part[3]+'})}')
      elif len(re.findall(r'^(\-*[\d]+[+-][\d*]*\()+', part)) != 0:
        if '*' in part:
          all_parts_list.append(str(part.replace('*', '')))
      # # elif.. а тут пойдет ветка для других хитрых структур, которые надо парсить (если еще будет надо)

      else: all_parts_list.append(str(part))
      ind += 1 # считаем индексы
    if k == 0:
      all_parts_list.append('=')
      k += 1
  # Сборка выражения
  i = 0
  final_string = 'Решите уравнение: \('
  while i < len(all_parts_list):
    if i == 0:
      final_string += all_parts_list[i]
      i += 1
    elif all_parts_list[i] == '+' and len(re.findall(r'^\-', all_parts_list[i+1])) != 0 and i != len(all_parts_list)-2:
      final_string += ' - ' + all_parts_list[i+1].strip('-')
      i += 2
    elif all_parts_list[i] == '-' and len(re.findall(r'^\-', all_parts_list[i+1])) != 0 and i != len(all_parts_list)-2:
      final_string += ' + ' + all_parts_list[i+1].strip('-')
      i += 2
    elif all_parts_list[i] == '+' and len(re.findall(r'^\-', all_parts_list[i+1])) != 0 and i == len(all_parts_list)-2:
      final_string += ' - ' + all_parts_list[i+1].strip('-')+'\)'
      break
    elif all_parts_list[i] == '-' and len(re.findall(r'^\-', all_parts_list[i+1])) != 0 and i == len(all_parts_list)-2:
      final_string += ' + ' + all_parts_list[i+1].strip('-')+'\)'
      break
    elif i == len(all_parts_list)-1:
      final_string += ' '+all_parts_list[i]+'\)'
      i += 1
    else:
      final_string += ' '+all_parts_list[i]+' '
      i += 1

  return final_string


def x_equation_generator_with_parser(equation_to_solve):
  '''Функция для создания линейного уравнения, которая обращается внутри себя к парсеру для вывода уравнения'''
  while True:
    prep_equation, answer = generate_values_and_recieve_answer(equation_to_solve)
    task = parse_and_generate_task(prep_equation)
    answer = float(answer)
    if len(str(answer).split('.')[1]) <= 6:
      if answer % 1 == 0:
        answer = int(answer)
        break
  return {
      "condition": task,
      "answer": answer
    }
