import random
from random import choice
import numpy as np
import pymorphy2
import math

# https://pymorphy2.readthedocs.io/en/0.2/user/index.html

def parameters():
  values = {
      'item1': choice(['пиджак', 'свитер', 'куртка', 'пальто', 'кофта', 'пуховик']),
      'item2': choice(['брюки', 'сорочка', 'туфли', 'футболка', 'шорты', 'жилет']),
      'item3': choice(['доллары', 'рубли', 'евро']),
      'item4': choice(['помидоры', 'огурцы', 'редис', 'баклажаны', 'перец', 'яблоки', 'груши'])
  }
  return values['item1'], values['item2'], values['item3'],values['item4']


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



def task_837():
    '''Генерация аналогичных задач № 837 с портала https://kuzovkin.info/one_exercise_1/837
    Пиджак дороже брюк на 25%. На сколько процентов брюки дешевле пиджака?'''
    item1, item2, _, _ = parameters()
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
    item1, item2, _, _ = parameters()
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
    prod, _, _, _ = parameters()
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
    prod, _, _, _ = parameters()
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
    prod, _, _, _ = parameters()
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
    _, prod, _, _ = parameters()
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
    _, _, value, _ = parameters()
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
    prod1, prod2, _, _ = parameters()
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
    _, prod, _, _ = parameters()
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
    prod, _, _, _ = parameters()
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

def task_4490():
    '''Генерация аналогичных задач № 4490 с портала https://kuzovkin.info/one_exercise_1/4490
    Вкладчик положил 300000 рублей в банк под 11% годовых. Какая сумма будет у него на счету через год?'''
    while True:
        period = choice([1, 2, 3])
        per = random.randint(3, 18)
        contrib = random.randint(50000, 500000)
        if contrib % 1000 == 0:
          x = contrib * ((100 + per) / 100) ** period
          if x * 1000 % 1000 == 0:
              answer = int(x)
              break
          elif x * 10000 % 100 == 0:
              answer = x
              break
    task = f'Вкладчик положил {contrib} рублей в банк под {per}% годовых. Какая сумма будет у него на счету через {period if period !=1 else ""}{"год" if period == 1 else " года"}?'
    return task, answer

def task_4673():
    '''Генерация аналогичных задач № 4673 с портала https://kuzovkin.info/one_exercise_1/4673
    Цена на акцию понизилась на 2,5% и составила 8677,5 рубля. Найдите первоначальную цену акции?'''
    prod, _, _, _ = parameters()
    while True:
        per = round(random.random(), 1) + random.randint(0, 8)
        cost = round(random.random(), 1) + random.randint(1000, 10000)
        x = cost * 100 / (100- per)
        if x * 1000 % 100000 == 0:
            answer = int(x)
            break
    task = f'Цена на {case_item(prod, "accs")} понизилась на {int(per) if per*10%10==0 else per}% и составила {int(cost) if cost*10%10==0 else cost} рубля. Найдите первоначальную цену {case_item(prod)}?'
    return task, answer

def task_8559():
    '''Генерация аналогичных задач № 8559 с портала https://kuzovkin.info/one_exercise_1/8559
    Цена товара повысилась с 450 рублей до 522 рублей. На сколько процентов была повышена цена товара?'''
    _, prod, _, _ = parameters()
    while True:
        price1, price2 = np.random.randint(400, 600, size=2)
        if price1 < price2 and price1 * 10 % 10 == 0 and price2 * 10 % 10 != 1:
          x = price2 * 100 / price1 - 100
          if x * 1000 % 1000 == 0:
              answer = int(x)
              break
    task = f'Цена {case_item(prod)} повысилась с {price1} рублей до {price2} рублей. На сколько процентов была повышена цена {case_item(prod)}?'
    return task, answer

def task_8548():
    '''Генерация аналогичных задач № 8548 с портала https://kuzovkin.info/one_exercise_1/8548
    Цена на товар была повышена на 11% и составила 1443 рубля. Сколько рублей стоил товар до повышения цены?'''
    prod, _, _, _ = parameters()
    while True:
        per = np.random.randint(2, 20)
        price = np.random.randint(1000, 5000)
        x = price * 100 / (100 + per)
        if x * 100 % 10000 == 0:
            answer = int(x)
            break
    task = f'Цена на {case_item(prod, "accs")} была повышена на {per}% и составила {price} рубля. Сколько рублей стоил{"o" if case_gender(prod)== 3 else "a" if case_gender(prod)== 2 else ""} {prod} до повышения цены?'
    return task, answer

def task_4727():
    '''Генерация аналогичных задач № 4727 с портала https://kuzovkin.info/one_exercise_1/4727
    Цена на товар два раза увеличилась на 10%. На сколько процентов увеличилась цена по сравнению с первоначальной?'''
    prod, _, _, _ = parameters()
    while True:
        per = np.random.randint(2, 30)
        x = (100 + per) ** 2 / 100 - 100
        if x * 1000 % 1000 == 0:
          answer = int(x)
          break
        elif abs(str(x).find('.') - len(str(x))) - 1 < 3:
          answer = x
          break
    task = f'Цена на {case_item(prod, "accs")} два раза увеличилась на {per}%. На сколько процентов увеличилась цена по сравнению с первоначальной?'
    return task, answer

def task_4717():
    '''Генерация аналогичных задач № 4717 с портала https://kuzovkin.info/one_exercise_1/4717
    Цена на акцию сначала снизилась на 10%, потом снизилась ещё на 10%, а потом увеличилась на 20%.
    На сколько процентов изменилась цена акции по сравнению с первоначальной?'''
    prod, _, _, _ = parameters()
    while True:
        per1, per2, per3 = np.random.randint(2, 30, size=3)
        x = (100 - per1) * (100 - per2) * (100 + per3) / 10000 - 100
        if x * 10000 % 10000 == 0:
            answer = abs(int(x))
            break
        elif abs(str(x).find('.') - len(str(x))) - 1 < 3:
            answer = abs(x)
            break
    task = f'Цена на {case_item(prod, "accs")} сначала снизилась на {per1}%, потом снизилась ещё на {per2}%, а потом увеличилась на {per3}%. На сколько процентов изменилась цена {case_item(prod)} по сравнению с первоначальной?'
    return task, answer

def task_9213():
    '''Генерация аналогичных задач № 9213 с портала https://kuzovkin.info/one_exercise_1/9213
    Цена на товар повысилась на 21% и составила 7865 рублей. Найдите первоначальную цену товара.'''
    prod, _, _, _ = parameters()
    while True:
        per = np.random.randint(2, 40)
        price = np.random.randint(1000, 10000)
        x = price * 100 / (100 + per)
        if x * 100 % 10000 == 0:
            answer = int(x)
            break
    task = f'Цена на {case_item(prod, "accs")} повысилась на {per}% и составила {price} рублей. Найдите первоначальную цену {case_item(prod)}.'
    return task, answer

def task_9198():
    '''Генерация аналогичных задач № 9198 с портала https://kuzovkin.info/one_exercise_1/9198
    Цена на чайник повысилась на 11% и стала равна 1332 рубля. Сколько стоил чайник до повышения цены?'''
    _, prod, _, _ = parameters()
    while True:
        per = random.randint(2, 30)
        price = random.randint(1000, 3000)
        x = price * 100 / (100 + per)
        if x * 100 % 1000 == 0:
            answer = int(x)
            break
    task = f'Цена на {case_item(prod, "accs")} повысилась на {per}% и стала равна {price} рубля. Сколько стоил{"и" if case_number(prod)==2 else "" if case_gender(prod)==1 else "a" if case_gender(prod)==2 else "о"} {prod} до повышения цены?'
    return task, answer

def task_9445():
    '''Генерация аналогичных задач № 9445 с портала https://kuzovkin.info/one_exercise_1/9445
    В двух магазинах были одинаковые цены. В одном магазине их сначала понизили на 15%, а потом повысили на 10%,
    а в другом − сначала повысили на 10%, а потом понизили на 15%. Как изменились цены в этих магазинах по сравнению с первоначальной?'''
    while True:
      per11, per12 = np.random.randint(5, 30, size=2)
      per21, per22 = np.random.randint(5, 30, size=2)
      x1 = (100 - per11) * (100 + per12) / 100 - 100
      x2 = (100 + per21) * (100 - per22) / 100 - 100
      if abs(str(x1).find('.') - len(str(x1))) - 1 < 3 and abs(str(x2).find('.') - len(str(x2))) - 1 < 3:
        if x1 == 0 and x2 == 0:
          answer = f'не изменилась'
          break
        elif x1 == x2 :
          answer = f'{"увеличилась" if x1 > 0 else "уменьшилась"} на {abs(int(x1)) if x1*1000%1000==0 else abs(x1)}%'
          break
        else:
          answer = f'в первом {"увеличилась" if x1 > 0 else "уменьшилась"} на {abs(int(x1)) if x1*1000%1000==0 else abs(x1)}%, во втором {"увеличилась" if x2 > 0 else "уменьшилась"} на {abs(int(x2)) if x2*1000%1000==0 else abs(x2)}%'
          break
    task = f'В двух магазинах были одинаковые цены. В одном магазине их сначала понизили на {per11}%, а потом повысили на {per12}%, а в другом − сначала повысили на {per21}%, а потом понизили на {per22}%. Как изменились цены в этих магазинах по сравнению с первоначальной?'
    return task, answer

def task_9460():
    '''Генерация аналогичных задач № 9460 с портала https://kuzovkin.info/one_exercise_1/9460
    Цена на акции два раза упала на 20%, а потом два раза выросла на 30%. Как и на сколько процентов изменилась цена акции по сравнению с первоначальной?'''
    prod, _, _, _ = parameters()
    while True:
        per1, per2 = np.random.randint(2, 40, size=2)
        x = (100 - per1) ** 2 *(100 + per2) ** 2 / 100 ** 3 - 100
        if x < 0 and abs(str(x).find('.') - len(str(x))) - 1 < 3:
            answer = f'цена уменьшилась на {abs(int(x) if x * 10000 % 10000 == 0 else abs(x))}%'
            break
        elif x > 0 and abs(str(x).find('.') - len(str(x))) - 1 < 3:
            answer = f'цена увеличилась на {int(x) if x * 10000 % 10000 == 0 else x}%'
            break
        elif x == 0:
            answer = f'цена не изменилась'
            break
    task = f'Цена на {case_item(prod, "accs")} два раза упала на {per1}%, а потом два раза выросла на {per2}%. Как и на сколько процентов изменилась цена {case_item(prod)} по сравнению с первоначальной?'
    return task, answer

def task_9461():
    '''Генерация аналогичных задач № 9461 с портала https://kuzovkin.info/one_exercise_1/9461
    Цена на акции сначала выросла на 10%, потом упала на 15%, потом выросла на 20%, а потом упала на 12%.
    Как и на сколько процентов изменилась цена акции по сравнению с первоначальной?'''
    _, prod, _, _ = parameters()
    while True:
        per1, per2, per3, per4 = np.random.randint(2, 30, size=4)
        x = (100 + per1) * (100 - per2) * (100 + per3) * (100 - per4) / 100 ** 3 - 100
        if x < 0 and abs(str(x).find('.') - len(str(x))) - 1 < 3:
            answer = f'цена уменьшилась на {abs(int(x) if x * 10000 % 10000 == 0 else abs(x))}%'
            break
        elif x > 0 and abs(str(x).find('.') - len(str(x))) - 1 < 3:
            answer = f'цена увеличилась на {int(x) if x * 10000 % 10000 == 0 else x}%'
            break
        elif x == 0:
            answer = f'цена не изменилась'
            break
    task = f'Цена на {case_item(prod, "accs")} сначала выросла на {per1}%, потом упала на {per2}%, потом выросла на {per3}%, а потом упала на {per4}%. Как и на сколько процентов изменилась цена {case_item(prod)} по сравнению с первоначальной?'
    return task, answer

def task_9463():
    '''Генерация аналогичных задач № 9463 с портала https://kuzovkin.info/one_exercise_1/9463
    Цена на товар была повышена на 25%. На сколько процентов надо теперь её снизить, чтобы получить первоначальную цену?'''
    _, prod, _, _ = parameters()
    while True:
        per = np.random.randint(1, 91)
        x = 100 - 10000 / (100 + per)
        if x * 1000 % 1000 == 0:
          answer = int(x)
          break
        elif abs(str(x).find('.') - len(str(x))) - 1 < 4:
          answer = x
          break
    task = f'Цена на {case_item(prod, "accs")} была повышена на {per}%. На сколько процентов надо теперь её снизить, чтобы получить первоначальную цену?'
    return task, answer

def task_11011():
    '''Генерация аналогичных задач № 11011 с портала https://kuzovkin.info/one_exercise_1/11011
    Цена на акцию увеличилась на 10%, потом уменьшилась на 20%, потом увеличилась на 30%, далее уменьшилась на 40%,
    и наконец увеличилась на 60%. На сколько процентов и в какую сторону изменилась цена по сравнению с первоначальной?'''
    _, prod, _, _ = parameters()
    while True:
        per1, per2, per3, per4, per5 = np.random.randint(1, 60, size=5)
        x = ((100 + per1) * (100 - per2) / 100 ** 2) * ((100 + per3) * (100 - per4) / 100 ** 2) * (100 + per5) - 100
        if x < 0 and abs(str(x).find('.') - len(str(x))) - 1 < 3:
            answer = f'цена уменьшилась на {abs(int(x) if x * 10000 % 10000 == 0 else abs(x))}%'
            break
        elif x > 0 and abs(str(x).find('.') - len(str(x))) - 1 < 3:
            answer = f'цена увеличилась на {int(x) if x * 10000 % 10000 == 0 else x}%'
            break
        elif x == 0:
            answer = f'цена не изменилась'
            break
    task = f'Цена на {case_item(prod, "accs")} увеличилась на {per1}%, потом уменьшилась на {per2}%, потом увеличилась на {per3}%, далее уменьшилась на {per4}%, и наконец увеличилась на {per5}%. На сколько процентов и в какую сторону изменилась цена по сравнению с первоначальной?'
    return task, answer

def task_11010():
    '''Генерация аналогичных задач № 11010 с портала https://kuzovkin.info/one_exercise_1/11010
    Цена на акцию увеличилась на 10%, потом ещё на 5%, а потом упала на 20%. Сколько стоит теперь акция, если первоначально она стоила 4000 рублей?'''
    prod, _, _, _ = parameters()
    while True:
        per1, per2, per3 = np.random.randint(2, 30, size=3)
        price = random.randint(1000, 5000)
        if price % 10 == 0:
          x = (100 + per1) * (100 + per2) * (100 - per3) / 100 ** 3 * price
          if x * 1000 % 1000 == 0:
              answer = int(x)
              break
          elif abs(str(x).find('.') - len(str(x))) - 1 < 3:
              answer = x
              break
    task = f'Цена на {case_item(prod, "accs")} увеличилась на {per1}%, потом ещё на {per2}%, а потом упала на {per3}%. Сколько стоит теперь {prod}, если первоначально {"он" if case_gender(prod)==1 else "она" if case_gender(prod)==2 else "оно"} стоил{"" if case_gender(prod)==1 else "а" if case_gender(prod)==2 else "о"} {price} рублей?'
    return task, answer

def task_10790():
    '''Генерация аналогичных задач № 10790 с портала https://kuzovkin.info/one_exercise_1/10790
    Цена на товар понизилась на 15% и составила 2176 рублей. Найдите первоначальную цену товара.'''
    _, prod, _, _ = parameters()
    while True:
        per = random.randint(2, 30)
        price = random.randint(1000, 4000)
        if price % 10 != 1:
          x = 100 * price / (100 - per)
          if x % 10 == 0:
              answer = int(x)
              break
    task = f'Цена на {case_item(prod, "accs")} понизилась на {per}% и составила {price} рубл{"я" if price%10 in [2, 3, 4] else "ей"}. Найдите первоначальную цену {case_item(prod)}.'
    return task, answer

def task_10776():
    '''Генерация аналогичных задач № 10776 с портала https://kuzovkin.info/one_exercise_1/10776
    Пиджак стоит 5250 рублей. В магазине проводят распродажу со скидкой 15%. Сколько стоит пиджак на распродаже?'''
    prod, _, _, _ = parameters()
    while True:
        per = random.randint(2, 30)
        price = random.randint(2000, 8000)
        if price % 10 == 0:
          x = (100 - per) / 100 * price
          if x * 1000 % 1000 == 0:
              answer = int(x)
              break
          elif abs(str(x).find('.') - len(str(x))) - 1 < 3:
              answer = x
              break
    task = f'{case_title(prod)} сто{"ит" if case_number(prod)==1 else "ят"} {price} рублей. В магазине проводят распродажу со скидкой {per}%. Сколько сто{"ит" if case_number(prod)==1 else "ят"} {prod} на распродаже?'
    return task, answer

def task_9477():
    '''Генерация аналогичных задач № 9477 с портала https://kuzovkin.info/one_exercise_1/9477
    Цена на товар в течение месяца упала сначала на 18%, а затем на 20% и составила 328 рублей. Найдите исходную цену товара.'''
    _, prod, _, _ = parameters()
    while True:
        per1, per2 = np.random.randint(2, 30, size=2)
        price = random.randint(300, 3000)
        if price % 10 != 1:
          x = price * 100 ** 2 / ((100 - per1) * (100 - per2))
          if x * 1000 % 1000 == 0:
              answer = int(x)
              break
          elif abs(str(x).find('.') - len(str(x))) - 1 < 3:
              answer = x
              break
    task = f'Цена на {case_item(prod, "accs")} в течение месяца упала сначала на {per1}%, а затем на {per2}% и составила {price} рубл{"я" if price%10 in [2, 3, 4] else "ей"}. Найдите исходную цену {case_item(prod)}.'
    return task, answer

def task_9476():
    '''Генерация аналогичных задач № 9476 с портала https://kuzovkin.info/one_exercise_1/9476
    Цена товара сначала поднялась на 10%, потом уменьшилась на 20%, далее увеличилась на 5% и стала равна 6468 рублей. Найдите первоначальную цену товара.'''
    prod, _, _, _ = parameters()
    while True:
        per1, per2, per3 = np.random.randint(2, 30, size=3)
        price = random.randint(3000, 9000)
        if price % 10 != 1:
          x = price * 100 ** 3 / ((100 + per1) * (100 - per2) * (100 + per3))
          if x * 1000 % 1000 == 0:
              answer = int(x)
              break
          elif abs(str(x).find('.') - len(str(x))) - 1 < 3:
              answer = x
              break
    task = f'Цена {case_item(prod)} сначала поднялась на {per1}%, потом уменьшилась на {per2}%, далее увеличилась на {per3}% и стала равна {price} рубл{"я" if price%10 in [2, 3, 4] else "ей"}. Найдите первоначальную цену {case_item(prod)}.'
    return task, answer

def task_11051():
    '''Генерация аналогичных задач № 11051 с портала https://kuzovkin.info/one_exercise_1/11051
    Цена на некоторый товар была снижена дважды − сначала на 15%, а потом ещё на 20%. Каков общий процент снижения цены?'''
    prod, _, _, _ = parameters()
    while True:
        per1, per2 = np.random.randint(2, 30, size=2)
        x = 100 - (100 - per1) * (100 - per2) / 100
        if x * 1000 % 1000 == 0:
            answer = int(x)
            break
        elif abs(str(x).find('.') - len(str(x))) - 1 < 3:
            answer = x
            break
    task = f'Цена на {case_item(prod, "accs")} была снижена дважды − сначала на {per1}%, а потом ещё на {per2}%. Каков общий процент снижения цены?'
    return task, answer

def task_11056():
    '''Генерация аналогичных задач № 11056 с портала https://kuzovkin.info/one_exercise_1/11056
    Цена товара поднялась сначала на 20%, потом ещё на 15% и стала равна 8280 рублей. Найдите первоначальную цену товара.'''
    _, prod, _, _ = parameters()
    while True:
        per1, per2 = np.random.randint(2, 30, size=2)
        price = random.randint(300, 6000)
        if price % 10 != 1:
          x = price * 100 ** 2 / ((100 + per1) * (100 + per2))
          if x * 1000 % 1000 == 0:
              answer = int(x)
              break
          elif abs(str(x).find('.') - len(str(x))) - 1 < 3:
              answer = x
              break
    task = f'Цена {case_item(prod)} поднялась сначала на {per1}%, потом ещё на {per2}% и стала равна {price} рубл{"я" if price%10 in [2, 3, 4] else "ей"}. Найдите первоначальную цену {case_item(prod)}.'
    return task, answer

def task_11059():
    '''Генерация аналогичных задач № 11059 с портала https://kuzovkin.info/one_exercise_1/11059
    Цена на товар в течение месяца упала сначала на 40%, а потом увеличилась на 50% и составила 5130 рублей. Найдите первоначальную цену товара.'''
    prod, _, _, _ = parameters()
    while True:
        per1, per2 = np.random.randint(2, 30, size=2)
        price = random.randint(2000, 8000)
        if price % 10 != 1:
          x = price * 100 ** 2 / ((100 - per1) * (100 + per2))
          if x * 1000 % 1000 == 0:
              answer = int(x)
              break
          elif abs(str(x).find('.') - len(str(x))) - 1 < 3:
              answer = x
              break
    task = f'Цена на {case_item(prod, "accs")} в течение месяца упала сначала на {per1}%, а потом увеличилась на {per2}% и составила {price} рубл{"я" if price%10 in [2, 3, 4] else "ей"}. Найдите первоначальную цену {case_item(prod)}.'
    return task, answer

def task_12793():
    '''Генерация аналогичных задач № 12793 с портала https://kuzovkin.info/one_exercise_1/12793
    Первоначально цена на некоторый товар была повышена на 44%, затем 2 раза понижалась на одинаковое число процентов.
    В результате конечная цена оказалась на 19% меньше первоначальной. На сколько процентов производилось двукратное снижение цены?'''
    prod, _, _, _ = parameters()
    while True:
        per1, per2 = np.random.randint(2, 90, size=2)
        d = 200 ** 2 - 4 * (100 ** 2 - ((100 - per2) * 100 ** 2 / (100 + per1)))
        if d ** 0.5 * 1000 % 1000 == 0:
          x = (200 - d ** 0.5) / 2
          if x * 1000 % 1000 == 0:
            answer = int(x)
            break
          else:
            answer = x
            break
    task = f'Первоначально цена на {case_item(prod, "accs")} была повышена на {per1}%, затем 2 раза понижалась на одинаковое число процентов. В результате конечная цена оказалась на {per2}% меньше первоначальной. На сколько процентов производилось двукратное снижение цены?'
    return task, answer

def task_12794():
    '''Генерация аналогичных задач № 12794 с портала https://kuzovkin.info/one_exercise_1/12794
    Первый банк дает 5% годовых, а второй - 10%. Вкладчик часть своих денег положил в первый банк, а остальные - во второй.
    Через 2 года суммарное число вложенных денег увеличилось на 18,85%. Какую долю своих денег положил вкладчик в первый банк?'''
    while True:
        per1, per2, per3 = np.random.randint(2, 30, size=3)
        if (100 + per2) ** 2 - 100 * (100 + per3) != 0 and (1 + (100 * (100 + per3) - (100 + per1) ** 2) / ((100 + per2) ** 2 - 100 * (100 + per3))) != 0:
          x = 100 / (1 + (100 * (100 + per3) - (100 + per1) ** 2) / ((100 + per2) ** 2 - 100 * (100 + per3)))
          if 0 < x < 100 and x * 10000 % 100 == 0:
              answer = f'{int(x) if x*1000%1000==0 else x}%'
              break
    task = f'Первый банк дает {per1}% годовых, а второй - {per2}%. Вкладчик часть своих денег положил в первый банк, а остальные - во второй. Через 2 года суммарное число вложенных денег увеличилось на {per3}%. Какую долю своих денег положил вкладчик в первый банк?'
    return task, answer

def task_35687():
    '''Генерация аналогичных задач № 35687 с портала https://kuzovkin.info/one_exercise_1/35687
    Магазин увеличил цену товара в 8 раз. Однако по результатам проверки антимонопольная служба предписала вернуть прежнюю цену.
    На сколько процентов придётся снизить цену? Ответ подать в процентах, округлить до десятых'''
    prod, _, _, _ = parameters()
    while True:
        n = random.randint(2, 30)
        x = 100 - 100 / n
        if x * 10000 % 10000 == 0:
            answer = int(x)
            break
        else:
            answer = round(x, 1)
            break
    task = f'Магазин увеличил цену {case_item(prod)} в {n} раз. Однако по результатам проверки антимонопольная служба предписала вернуть прежнюю цену. На сколько процентов придётся снизить цену? Ответ подать в процентах, округлить до десятых'
    return task, answer

def task_35690():
    '''Генерация аналогичных задач № 35690 с портала https://kuzovkin.info/one_exercise_1/35690
    В начале мая цена на помидоры повысилась на 20, а в начале июня понизилась на 20. На сколько процентов цена помидоров в июне после понижения стала ниже,
    чем цена помидоров в мае до повышения? Ответ подать в процентах, округлить до целого'''
    _, _, _, prod = parameters()
    while True:
        per  = random.randint(2, 30)
        x = 100 - (100 + per) * (100 - per) / 100
        if x * 10000 % 10000 == 0:
            answer = int(x)
            break
        elif x > 1:
            answer = int(round(x, 0))
            break
    task = f'В начале мая цена на {case_item(prod, "accs")} повысилась на {per}%, а в начале июня понизилась на {per}%. На сколько процентов цена {case_item(prod)} в июне после понижения стала ниже, чем цена {case_item(prod)} в мае до повышения? Ответ подать в процентах, округлить до целого'
    return task, answer

def task_35702():
    '''Генерация аналогичных задач № 35702 с портала https://kuzovkin.info/one_exercise_1/35702
    Цена на телевизор была повышена на 16% и составила 34800 рублей. Сколько рублей стоил телевизор до повышения цены?'''
    prod, _, _, _ = parameters()
    while True:
        per = random.randint(2, 30)
        price =  random.randint(4000, 15000)
        x = price * 100 / (100 + per)
        if x * 1000 % 10000 == 0:
            answer = int(x)
            break
    task = f'Цена на {case_item(prod, "accs")} была повышена на {per}% и составила {price} рублей. Сколько рублей стоил{"" if case_gender(prod)==1 else "а" if case_gender(prod)==2 else "о"} {prod} до повышения цены?'
    return task, answer

def task_35703():
    '''Генерация аналогичных задач № 35703 с портала https://kuzovkin.info/one_exercise_1/35703
    Подставка для книг стоила 80 рублей. После снижения цены она стала стоить 68 рублей. На сколько процентов была снижена цена на подставку?'''
    _, prod, _, _ = parameters()
    while True:
        price1, price2 = np.random.randint(500, 5000, size=2)
        if price1 > price2 and price1 % 10 != 1 and price2 % 10 != 1:
          x = 100 - price2 * 100 / price1
          if x * 10000 % 10000 == 0:
              answer = int(x)
              break
          elif x * 10000 % 1000 == 0:
              answer = x
              break
    task = f'{case_title(prod)} стоил{"и" if case_number(prod) == 2 else "" if case_gender(prod)==1 else "а" if case_gender(prod)==2 else "о"} {price1} рубл{"я" if price1%10 in [2, 3, 4] else "ей"}. После снижения цены {"они" if case_number(prod)==2 else "он" if case_gender(prod)==1 else "она" if case_gender(prod)==2 else "оно"} стал{"и" if case_number(prod) == 2 else "" if case_gender(prod)==1 else "а" if case_gender(prod)==2 else "о"} стоить {price2} рубл{"я" if price2%10 in [2, 3, 4] else "ей"}. На сколько процентов была снижена цена на {case_item(prod, "accs")}?'
    return task, answer