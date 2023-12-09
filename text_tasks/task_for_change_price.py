import random
from random import choice
import numpy as np
import pymorphy2
import math

# https://pymorphy2.readthedocs.io/en/0.2/user/index.html
#ЗАДАЧИ https://kuzovkin.info/zadachi/?class_parametr=None&exam_parametr=%5B%5D&topic_parametr=%5B%2734%27%5D&author_from_filter=&level_parametr=None

def parameters():
  values = {
      'item1': choice(['пиджак', 'свитер', 'куртка', 'пальто', 'кофта', 'пуховик']),
      'item2': choice(['брюки', 'сорочка', 'туфли', 'футболка', 'шорты', 'жилет']),
      'item3': choice(['доллары', 'рубли', 'евро'])
  }

  return values['item1'], values['item2'], values['item3']

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

#находим число нашего ключевого слова: 1 - единственное, 2 - множественное
def case_number(offer):
  morph = pymorphy2.MorphAnalyzer()
  if morph.parse(offer)[0].tag.number == 'sing':
    return 1
  elif morph.parse(offer)[0].tag.number == 'plur':
    return 2

def task_837():
    '''Генерация аналогичных задач № 837 с портала https://kuzovkin.info/one_exercise_1/837
    Пиджак дороже брюк на 25%. На сколько процентов брюки дешевле пиджака?'''
    item1, item2, _ = parameters()
    while True:
        per = random.randint(10, 70)
        x = 100 - 10000 / (100 + per)
        if x * 1000 % 1000 == 0:
          answer = int(x)
          break
        elif x * 1000 % 100 == 0:
          answer = x
          break
    task = f'{case_title(item1)} дороже {case_item(item2)} на {per}%. На сколько процентов {item2} дешевле {case_item(item1)}?'
    return task, answer

def task_838():
    '''Генерация аналогичных задач № 838 с портала https://kuzovkin.info/one_exercise_1/838
    Куртка дороже пиджака на 60%. На сколько процентов пиджак дешевле куртки?'''
    item1, item2, _ = parameters()
    while True:
        per = random.randint(10, 70)
        x = 100 - 10000 / (100 + per)
        if x * 1000 % 1000 == 0:
          answer = int(x)
          break
        elif x * 1000 % 100 == 0:
          answer = x
          break
    task = f'{case_title(item1)} дороже {case_item(item2)} на {per}%. На сколько процентов {item2} дешевле {case_item(item1)}?'
    return task, answer

def task_850():
    '''Генерация аналогичных задач № 850 с портала https://kuzovkin.info/one_exercise_1/850
    Цена на акцию сначала увеличилась на 20% процентов, а потом уменьшилась на 20%.
    На сколько процентов и в какую сторону изменилась цена акции по сравнению с первоначальной?'''
    prod, _, _ = parameters()
    while True:
        per1, per2 = np.random.randint(5, 30, size=2)
        x = 100 - (100 + per1) * (100 - per2) / 100
        if x != 0 and x * 1000 % 1000 == 0:
          answer = f'{"увеличилась" if x < 0 else "уменьшилась"} на {abs(int(x))}%'
          break
        elif x != 0 and x * 1000 % 100 == 0:
          answer = f'{"увеличилась" if x < 0 else "уменьшилась"} на {abs(x)}%'
          break
    task = f'Цена на {case_item(prod, "accs")} сначала увеличилась на {per1}% процентов, а потом уменьшилась на {per2}%. На сколько процентов и в какую сторону изменилась цена {case_item(prod)} по сравнению с первоначальной?'
    return task, answer

def task_863():
    '''Генерация аналогичных задач № 863 с портала https://kuzovkin.info/one_exercise_1/863
    В двух магазинах были одинаковые цены. В одном магазине их сначала понизили на 15%, а потом повысили на 10%,
    а в другом − сначала повысили на 10%, а потом понизили на 15%. В каком из магазинов выгоднее покупать товар?'''
    while True:
        per11, per22 = np.random.randint(5, 30, size=2)
        per12, per21 = np.random.randint(5, 30, size=2)
        x = (((100+per12) / 100) * ((100 - per11) / 100)) / (((100 - per22) / 100) * ((100 + per21) / 100))
        if x > 1:
            answer = f'выгоднее во втором'
            break
        elif x < 1:
            answer = f'выгоднее в первом'
            break
        elif x == 1:
            answer = f'одинаково'
            break
    task = f'В двух магазинах были одинаковые цены. В одном магазине их сначала понизили на {per11}%, а потом повысили на {per12}%, а в другом − сначала повысили на {per21}%, а потом понизили на {per22}%. В каком из магазинов выгоднее покупать товар?'
    return task, answer

def task_873():
    '''Генерация аналогичных задач № 873 с портала https://kuzovkin.info/one_exercise_1/873
    Цена на акции сначала два раза увеличилась на 5%, а потом уменьшилась на 10%.
    Как и на сколько процентов изменилась цена акции по сравнению с первоначальной?'''
    prod, _, _ = parameters()
    while True:
        per1, per2 = np.random.randint(2, 30, size=2)
        x = (100 + per1) * (100 + per1) * (100 - per2) / 10000 - 100
        if x < 0 and abs(str(x).find('.') - len(str(x))) - 1 < 4:
            answer = f'цена уменьшилась на {abs(int(x) if x * 10000 % 10000 == 0 else abs(x))}%'
            break
        elif x > 0 and abs(str(x).find('.') - len(str(x))) - 1 < 3:
            answer = f'цена увеличилась на {int(x) if x * 10000 % 10000 == 0 else x}%'
            break
        elif x == 0:
            answer = f'цена не изменилась'
            break
    task = f'Цена на {case_item(prod, "accs")} сначала два раза увеличилась на {per1}%, а потом уменьшилась на {per2}%. Как и на сколько процентов изменилась цена {case_item(prod)} по сравнению с первоначальной?'
    return task, answer

def task_876():
    '''Генерация аналогичных задач № 873 с портала https://kuzovkin.info/one_exercise_1/876
    Цена на акции выросла на 12%, потом упала на 16%, потом опять упала на 21%.
    Как и на сколько процентов изменилась цена акции по сравнению с первоначальной?'''
    prod, _, _ = parameters()
    while True:
        per1, per2, per3 = np.random.randint(2, 30, size=3)
        x = (100 + per1) * (100 - per2) * (100 - per3) / 10000 - 100
        if x < 0 and abs(str(x).find('.') - len(str(x))) - 1 < 4:
            answer = f'цена уменьшилась на {abs(int(x) if x * 10000 % 10000 == 0 else abs(x))}%'
            break
        elif x > 0 and abs(str(x).find('.') - len(str(x))) - 1 < 3:
            answer = f'цена увеличилась на {int(x) if x * 10000 % 10000 == 0 else x}%'
            break
        elif x == 0:
            answer = f'цена не изменилась'
            break
    task = f'Цена на {case_item(prod, "accs")} выросла на {per1}%, потом упала на {per2}%, потом опять упала на {per3}%. Как и на сколько процентов изменилась цена {case_item(prod)} по сравнению с первоначальной?'
    return task, answer

def task_4483():
    '''Генерация аналогичных задач № 4483 с портала https://kuzovkin.info/one_exercise_1/4483
    Цена товара увеличилась на 5%. Сколько процентов составляет новая цена от старой?'''
    while True:
        per = random.randint(2, 30)
        x = 100 + per
        answer = x
        break
    task = f'Цена товара увеличилась на {per}%. Сколько процентов составляет новая цена от старой?'
    return task, answer

def task_4503():
    '''Генерация аналогичных задач № 4503 с портала https://kuzovkin.info/one_exercise_1/4503
    Дисконтная карточка в магазине «Marks&Spencer» даёт мне скидку 3%.
    Цена шляпы с учётом скидки составила 1552 рубля. Сколько стоит шляпа без скидки?'''
    _, prod, _ = parameters()
    while True:
        per = random.randint(2, 30)
        price = random.randint(1000, 5000)
        x = 100 * price / (100 - per)
        if x * 1000 % 1000 == 0 and price % 10 != 1:
            answer = int(x)
            break
    task = f'Дисконтная карточка в магазине «Marks&Spencer» даёт мне скидку {per}%. Цена {case_item(prod)} с учётом скидки составила {price} рубл{"я" if price % 10 in [2, 3, 4] else "ей"}. Сколько сто{"ит" if case_number(prod) == 1 else "ят"} {prod} без скидки?'
    return task, answer

def task_4689():
    '''Генерация аналогичных задач № 4689 с портала https://kuzovkin.info/one_exercise_1/4689
    Вкладчик положил в банк 15000 долларов. Проценты по вкладу составили 525 долларов. Какова доходность вклада?'''
    _, _, value = parameters()
    while True:
        contr = np.random.randint(10000, 100000)
        profit = np.random.randint(300, 3000)
        if contr % 100 == 0 and profit % 10 in [0, 5, 6, 7, 8, 9]:
          x = 100 * profit / contr
          if x * 10000 % 10000 == 0:
              answer = int(x)
              break
          elif x * 10000 % 100 == 0:
              answer = x
              break
    task = f'Вкладчик положил в банк {contr} {case_item(value)}. Проценты по вкладу составили {profit} {case_item(value)}. Какова доходность вклада?'
    return task, answer

def task_4713():
    '''Генерация аналогичных задач № 4713 с портала https://kuzovkin.info/one_exercise_1/4713
    Шуба дороже пальто на 100%. На сколько процентов пальто дешевле шубы?'''
    prod1, prod2, _ = parameters()
    while True:
        per = random.randint(5, 100)
        x = 100 - 10000 / (100 + per)
        if x * 100000 % 100000 == 0:
            answer = int(x)
            break
        elif x * 100000 % 100 == 0:
            answer = x
            break
    task = f'{case_title(prod1)} дороже {case_item(prod2)} на {per}%. На сколько процентов {prod2} дешевле {case_item(prod1)}?'
    return task, answer

def task_4751():
    '''Генерация аналогичных задач № 4751 с портала https://kuzovkin.info/one_exercise_1/4751
    Цена на товар была снижена на 80%. На сколько процентов надо теперь её повысить,
    чтобы получить первоначальную цену?'''
    _, prod, _ = parameters()
    while True:
        per = random.randint(2, 99)
        x = 10000 / (100 - per) - 100
        if x * 100000 % 10000 == 0:
            answer = int(x)
            break
    task = f'Цена на {case_item(prod, "accs")} была снижена на {per}%. На сколько процентов надо теперь её повысить, чтобы получить первоначальную цену?'
    return task, answer

def task_8362():
    '''Генерация аналогичных задач № 8362 с портала https://kuzovkin.info/one_exercise_1/8362
    Пиджак стоит 5000 рублей. В связи с поступлением новой коллекции пиджак продают со скидкой 70%.
    Сколько стоит пиджак с учётом скидки?'''
    prod, _, _ = parameters()
    while True:
        price = random.randint(2000, 8000)
        if price % 10 == 0:
          per = random.randint(10, 90)
          x = price * (100 - per) / 100
          if x * 10000 % 10000 == 0:
              answer = int(x)
              break
    task = f'{case_title(prod)} стоит {price} рублей. В связи с поступлением новой коллекции {prod} продают со скидкой {per}%. Сколько стоит {prod} с учётом скидки?'
    return task, answer