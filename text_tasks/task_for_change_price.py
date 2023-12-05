import random
import numpy as np
import pymorphy2

# https://pymorphy2.readthedocs.io/en/0.2/user/index.html
#ЗАДАЧИ https://kuzovkin.info/zadachi/?class_parametr=None&exam_parametr=%5B%5D&topic_parametr=%5B%2734%27%5D&author_from_filter=&level_parametr=None

def parameters():
  values = {
      'item1': ['пиджак', 'свитер', 'куртка', 'пальто', 'кофта', 'пуховик'],
      'item2': ['брюки', 'сорочка', 'туфли', 'футболка', 'шорты', 'жилет'],
  }

  return values['item1'][random.randint(0, len(values['item1'])-1)], values['item2'][random.randint(0, len(values['item1'])-1)]


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


def task_837():
    '''Генерация аналогичных задач № 837 с портала https://kuzovkin.info/one_exercise_1/837
    Пиджак дороже брюк на 25%. На сколько процентов брюки дешевле пиджака?'''
    item1, item2 = parameters()
    while True:
        per = random.randint(10, 70)
        x = 100 - 10000 / (100 + per)
        if x * 1000 % 1000 == 0:
          answer = int(x)
          break
        elif x * 100000 % 100 == 0:
          answer = x
          break
    task = f'{case_title(item1)} дороже {case_item(item2)} на {per}%. На сколько процентов {item2} дешевле {case_item(item1)}?'
    return task, answer

def task_838():
    '''Генерация аналогичных задач № 838 с портала https://kuzovkin.info/one_exercise_1/838
    Куртка дороже пиджака на 60%. На сколько процентов пиджак дешевле куртки?'''
    item1, item2 = parameters()
    while True:
        per = random.randint(10, 70)
        x = 100 - 10000 / (100 + per)
        if x * 1000 % 1000 == 0:
          answer = int(x)
          break
        elif x * 100000 % 100 == 0:
          answer = x
          break
    task = f'{case_title(item1)} дороже {case_item(item2)} на {per}%. На сколько процентов {item2} дешевле {case_item(item1)}?'
    return task, answer

def task_850():
    '''Генерация аналогичных задач № 850 с портала https://kuzovkin.info/one_exercise_1/850
    Цена на акцию сначала увеличилась на 20% процентов, а потом уменьшилась на 20%.
    На сколько процентов и в какую сторону изменилась цена акции по сравнению с первоначальной?'''
    prod, _ = parameters()
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
    prod, _ = parameters()
    while True:
        per1, per2 = np.random.randint(2, 30, size=2)
        x = (100 + per1) * (100 + per1) * (100 - per2) / 10000 - 100
        if x < 0 and abs(str(x).find('.') - len(str(x))) - 1 < 4:
            answer = f'цена уменьшилась на {abs(int(x) if x * 10000 % 10000 == 0 else abs(x))} %'
            break
        elif x > 0 and abs(str(x).find('.') - len(str(x))) - 1 < 3:
            answer = f'цена увеличилась на {int(x) if x * 10000 % 10000 == 0 else x} %'
            break
        elif x == 0:
            answer = f'цена не изменилась'
            break
    task = f'Цена на {case_item(prod, "accs")} сначала два раза увеличилась на {per1}%, а потом уменьшилась на {per2}%. Как и на сколько процентов изменилась цена {case_item(prod)} по сравнению с первоначальной?'
    return task, answer