import random
import numpy as np
import pymorphy2

def parameters(i=0):
  values = {
      'item1': ['золото', 'хром', 'медь', 'алюминий', 'олово'],
      'item2': ['серебро', 'никель', 'цинк', 'железо', 'титан'],
      'task': [[('морская вода', 'соль', 'пресная вода'),
                ('яблочный сок', 'яблочное пюре', 'вода'),
                ('абрикосовый сок', 'абрикосовое пюре', 'вода'),
                ('гранатовый сок', 'гранат', 'вода'),
                ('уксусная кислота', 'уксус', 'чистая вода'),
                ('целлюлозная масса', 'целлюлоза', 'вода'),
                ('керамическая масса', 'глина', 'вода'),
                ('строительный раствор', 'цемент', 'вода'),
                ('сироп', 'подсластитель', 'вода')],
               [('свежие грибы', 'сухие грибы', 'вода'),
                ('свежий виноград', 'изюм', 'вода'),
                ('свежие абрикосы', 'сушеные абрикосы', 'вода'),
                ('свежие яблоки', 'сушеные яблоки', 'вода'),
                ('свежие бананы', 'сушеные бананы', 'вода'),
                ('свежие фрукты', 'сушеные фрукты', 'вода')],
               [('серная кислота', 'чистая вода' ),
                ('уксусная кислота', 'чистая вода'),
                ('соляная кислота', 'чистая вода'),
                ('касторовое масло', 'спирт'),
                ('глицерин', 'чистая вода'),
                ('хлорид натрия', 'вода')]]
  }
  return values['item1'][random.randint(0, len(values['item1'])-1)], values['item2'][random.randint(0, len(values['item1'])-1)], values['task'][i][random.randint(0, len(values['task'][i])-1)]


#выбираем правильное склонение слов https://opencorpora.org/dict.php?act=gram
def case_item(offer, case='gent'):
  morph = pymorphy2.MorphAnalyzer()
  if len(offer.split()) < 2:
    return morph.parse(offer)[0].inflect({case}).word
  else:
    list_offer = offer.split()
    list_morphy = []
    for i in list_offer:
      list_morphy.append(morph.parse(i)[0].inflect({case}).word)
    return ' '.join(list_morphy)

#пишем слово с заглавной буквы
def case_title(offer):
  if len(offer.split()) < 2:
    return offer.title()
  else:
    offer_list = offer.split(' ', 1)
    return offer_list[0].title() +' '+ offer_list[1]

#находим какого рода ключевое слово: 1 - мужского рода, 2 - женского рода, 3 - среднего рода
def case_gender(offer):
  morph = pymorphy2.MorphAnalyzer()
  if len(offer.split()) < 2:
    if morph.parse(offer)[0].tag.gender == 'masc':
      return 1
    elif morph.parse(offer)[0].tag.gender == 'femn':
      return 2
    else: return 3
  else:
    word = offer.split()[1]
    if morph.parse(word)[0].tag.gender == 'masc':
      return 1
    elif morph.parse(word)[0].tag.gender == 'femn':
      return 2
    else: return 3

#находим число нашего ключевого слова: 1 - единственное, 2 - множественное
def case_number(offer):
  morph = pymorphy2.MorphAnalyzer()
  if morph.parse(offer)[0].tag.number == 'sing':
    return 1
  elif morph.parse(offer)[0].tag.number == 'plur':
    return 2

#пишем числительные словами
def numeral(num):
  collection_numeral = {
      2: 'вдвое',
      3: 'втрое',
      4: 'вчетверо',
      5: 'впятеро'}
  return collection_numeral[num]



def task_2614():
    '''Генерация аналогичных задач № 2614 с портала https://kuzovkin.info/one_exercise_1/2614
    В сплав золота с серебром, содержащий 80 г золота, добавили 100 г золота.
    В результате содержание золота в сплаве увеличилось на 20 %. Сколько граммов серебра в сплаве?'''
    item1, item2, _ = parameters()
    while True:
        au, au1 = np.random.randint(10, 999, size=2)
        per = random.randint(1, 99)
        x = -1 * (2 * au + au1 - au1 * 100 / per) / 2
        if (2 * au + au1 - au1 * 100 / per) ** 2 - 4 * au * (au + au1) == 0 and 0 < x < 1000 and x * 1000 % 1000 == 0:
            answer = int(x)
            break
    task = f'В сплав {case_item(item1)} с {case_item(item2, "ablt")}, содержащий {au} г {case_item(item1)}, добавили {au1} г {case_item(item1)}. В результате содержание {case_item(item1)} в сплаве увеличилось на {per} %. Сколько граммов {case_item(item2)} в сплаве?'
    return task, answer

def task_4767():
    '''Генерация аналогичных задач № 4767 с портала https://kuzovkin.info/one_exercise_1/4767
    Морская вода содержит 8% (по весу) соли. Сколько килограммов пресной воды нужно добавить к 30 кг морской воды, чтобы содержание соли в последней составило 5%?'''
    _, _, param = parameters()
    while True:
        s1, s2 = np.random.randint(2, 15, size=2)
        volume = random.randint(5, 15)

        x = volume * (s1 - s2) / s2
        if x * 1000 % 1000 == 0 and s1 > s2:
            answer = int(x)
            break
    task = f'{case_title(case_item(param[0], "nomn"))} содержит {s1}% (по весу) {case_item(param[1])}. Сколько килограммов {case_item(param[2])} нужно добавить к {volume} кг {case_item(param[0])}, чтобы содержание {case_item(param[1])} в {case_item(param[0], "loct")} составило {s2}%?'
    return task, answer

def task_4770():
    '''Генерация аналогичных задач № 4770 с портала https://kuzovkin.info/one_exercise_1/4770
    Сколько килограммов воды нужно выпарить из 0,5 т целлюлозной массы, содержащей 85% воды, чтобы получить массу с содержанием 75% воды?'''
    _, _, param = parameters()
    while True:
        m = random.randint(100, 2000)
        m1, m2 = np.random.randint(30, 90, size=2)
        x = (m1 - m2) * m / (100 - m2)
        if m2 < m1 and x * 1000 % 1000 == 0:
            answer = int(x)
            break
    task = f'Сколько килограммов {case_item(param[2])} нужно выпарить из {m/1000} т {case_item(param[0])}, содержащей {m1}% {case_item(param[2])}, чтобы получить {case_item((param[0] if len(param[0].split())<2 else param[0].split(" ", 1)[1]), "accs")} с содержанием {m2}% {case_item(param[2])}?'
    return task, answer

def task_4772():
    '''Генерация аналогичных задач № 4772 с портала https://kuzovkin.info/one_exercise_1/4772
    Свежие грибы содержат по весу 90% воды, а сухие − 12% воды. Сколько получится сухих грибов из 22 кг свежих?'''
    _, _, param = parameters(1)
    while True:
        m1 = random.randint(10, 100)
        p1, p2 = np.random.randint(10, 95, size=2)
        x = (100 - p1) * m1 / (100 - p2)
        if p2 < (p1 - 40) and x * 1000 % 1000 == 0:
            answer = int(x)
            break
        elif p2 < (p1 - 40) and x * 1000 % 100 == 0:
            answer = x
            break
    task = f'{case_title(param[0])} содержат по весу {p1}% {case_item(param[2])}, а {param[1]} − {p2}% {case_item(param[2])}. Сколько получится {case_item(param[1])} из {m1} кг {case_item(param[0].split()[0])}?'
    return task, answer

def task_4773():
    '''Генерация аналогичных задач № 4773 с портала https://kuzovkin.info/one_exercise_1/4773
    Кусок сплава меди и цинка массой 36 кг содержит 45% меди.
    Какую массу меди следует добавить к этому куску, чтобы получить сплав, содержащий 60% меди?'''
    item1, item2, _ = parameters()
    while True:
        m = random.randint(10, 100)
        cu1, cu2 = np.random.randint(10, 95, size=2)
        x = m * (cu2 - cu1) / (100 - cu2)
        if cu1 < (cu2 - 10) and x * 1000 % 1000 == 0:
            answer = int(x)
            break
        elif cu1 < (cu2 - 10) and x * 1000 % 100 == 0:
            answer = x
            break
    task = f'Кусок сплава {case_item(item1)} и {case_item(item2)} массой {m} кг содержит {cu1}% {case_item(item1)}. Какую массу {case_item(item1)} следует добавить к этому куску, чтобы получить сплав, содержащий {cu2}% {case_item(item1)}?'
    return task, answer

def task_4774():
    '''Генерация аналогичных задач № 4774 с портала https://kuzovkin.info/one_exercise_1/4774
    В 2 литра 10-процентного раствора уксусной кислоты добавили 8 л чистой воды. Определите процентное содержание уксусной кислоты в полученном растворе.'''
    _, _, param = parameters(2)
    while True:
        per = random.randint(5, 40)
        m1, m2 = np.random.randint(2, 20, size=2)
        x = m1 * per / (m1 + m2)
        if m1 < m2 and x * 1000 % 1000 == 0:
            answer = int(x)
            break
        elif m1 < m2 and x * 1000 % 100 == 0:
            answer = x
            break
    task = f'В {m1} литра {per}-процентного раствора {case_item(param[0])} добавили {m2} л {case_item(param[1])}. Определите процентное содержание {case_item(param[0])} в полученном растворе.'
    return task, answer

def task_4778():
    '''Генерация аналогичных задач № 4778 с портала https://kuzovkin.info/one_exercise_1/4778
    В 5 кг сплава олова и цинка содержится 80% цинка. Сколько кг олова надо добавить к сплаву, чтобы процентное содержание цинка стало вдвое меньше?'''
    item1, item2, _ = parameters()
    while True:
        m = random.randint(2, 20)
        per = random.randint(60, 90)
        num = random.randint(2,5)
        x = m * num - m
        if per / num * 10000 % 100 == 0:
          answer = x
          break
    task = f'В {m} кг сплава {case_item(item1)} и {case_item(item2)} содержится {per}% {case_item(item2)}. Сколько кг {case_item(item1)} надо добавить к сплаву, чтобы процентное содержание {case_item(item2)} стало {numeral(num)} меньше?'
    return task, answer

def task_4780():
    '''Генерация аналогичных задач № 4780 с портала https://kuzovkin.info/one_exercise_1/4780
    Морская вода содержит 5% соли по массе. Сколько килограммов пресной воды нужно добавить к 30 кг морской воды, чтобы она содержала 1,5% по массе?'''
    _, _, param = parameters()
    while True:
        per1 = round (random.random(), 1) + random.randint(1, 30)
        per2 = round (random.random(), 1) + random.randint(1, 30)
        m = random.randint(5, 30)
        x = m * (per1 - per2) / per2
        if per1 > per2 and x * 1000 % 1000 == 0:
            answer = int(x)
            break
    task = f'{case_title(param[0])} содержит {int(per1) if per1 * 10 % 10 == 0 else per1}% {case_item(param[1])} по массе. Сколько килограммов {case_item(param[2])} нужно добавить к {m} кг {case_item(param[0])}, чтобы {"она" if case_gender(param[0]) == 2 else "он"} {"содержала" if case_gender(param[0]) == 2 else "содержал"} {int(per1) if per2 * 10 % 10 == 0 else per2}% по массе?'
    return task, answer

def task_4782():
    '''Генерация аналогичных задач № 4782 с портала https://kuzovkin.info/one_exercise_1/4782
    Из 10 кг свежих фруктов получают 3,5 кг сушёных фруктов, содержащих 20% воды. Каково процентное содержание воды в свежих фруктах?'''
    _, _, param = parameters(1)
    while True:
        per = random.randint(5, 30)
        m1 = round (random.random(), 1) + random.randint(5,30)
        m2 = round (random.random(), 1) + random.randint(1, 20)
        x = (m1 * 100 - m2 * 100 + m2 * per) / m1
        if m2 < m1 and x * 1000 % 1000 == 0:
            answer = int(x)
            break
    task = f'Из {int(m1) if m1 * 10 % 10 == 0 else m1} кг {case_item(param[0])} получают {int(m2) if m2 * 10 % 10 == 0 else m2} кг {case_item(param[1])}, {"содержащих" if case_number(param[0]) == 2 else "сoдержащего"} {per}% {case_item(param[2])}. Каково процентное содержание {case_item(param[2])} в {case_item(param[0], "loct")}?'
    return task, answer

def task_4784():
    '''Генерация аналогичных задач № 4784 с портала https://kuzovkin.info/one_exercise_1/4784
    В результате очистки сырья количество примесей в нём уменьшается с 20% в исходном сырье до 4% в очищенном.
    Сколько надо взять исходного сырья для получения 100 кг очищенного сырья?'''
    item1, item2, _ = parameters()
    while True:
        per1, per2 = np.random.randint(2, 70, size=2)
        m = random.randint(20, 100)
        x = (m * 100 - per2 * m) / (100 - per1)
        if per1 > per2 and x * 1000 % 1000 == 0:
            answer = int(x)
            break
    task = f'В результате очистки сырья количество примесей в нём уменьшается с {per1}% в исходном сырье до {per2}% в очищенном. Сколько надо взять исходного сырья для получения {m} кг очищенного сырья?'
    return task, answer

def task_4787():
    '''Генерация аналогичных задач № 4787 с портала https://kuzovkin.info/one_exercise_1/4787
    Какое количество 8%-го раствора соли надо взять, чтобы его можно было развести чистой водой до получения 100 г 3%-го раствора соли?'''
    _, _, param = parameters(2)
    while True:
        per1, per2 = np.random.randint(1, 20, size=2)
        m = random.randint(50, 999)
        x = per2 * m / per1
        if per1 > per2 and x * 1000 % 1000 == 0:
            answer = int(x)
            break
        elif per1 > per2 and x * 1000 % 100 == 0:
            answer = x
            break
    task = f'Какое количество {per1}%-го раствора {case_item(param[0])} надо взять, чтобы его можно было развести {case_item(param[1], "ablt")} до получения {m} г {per2}%-го раствора {case_item(param[0])}?'
    return task, answer