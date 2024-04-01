import random
from random import choice
import numpy as np
from .utils import capitalize_word, find_genus_object, find_number_object, choosing_declension_form, generate_context

def task_837():
    '''Генерация аналогичных задач № 837 с портала https://kuzovkin.info/one_exercise_1/837
    Пиджак дороже брюк на 25%. На сколько процентов брюки дешевле пиджака?'''
    cloth_1, cloth_2 = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 2)
    while True:
        percent = random.randint(10, 70)
        result = 100 - 10000 / (100 + percent)
        if result * 1000 % 1000 == 0:
          answer = int(result)
          break
        elif result * 1000 % 100 == 0:
          answer = result
          break
    task = f'{capitalize_word(cloth_1)} дороже {choosing_declension_form(cloth_2)} на {percent}%. На сколько процентов {cloth_2} дешевле {choosing_declension_form(cloth_1)}?'
    return {
      "condition": task,
      "answer": answer
    }

def task_838():
    '''Генерация аналогичных задач № 838 с портала https://kuzovkin.info/one_exercise_1/838
    Куртка дороже пиджака на 60%. На сколько процентов пиджак дешевле куртки?'''
    cloth_1, cloth_2 = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 2)
    while True:
        percent = random.randint(10, 70)
        result = 100 - 10000 / (100 + percent)
        if result * 1000 % 1000 == 0:
          answer = int(result)
          break
        elif result * 1000 % 100 == 0:
          answer = result
          break
    task = f'{capitalize_word(cloth_1)} дороже {choosing_declension_form(cloth_2)} на {percent}%. На сколько процентов {cloth_2} дешевле {choosing_declension_form(cloth_1)}?'
    return {
      "condition": task,
      "answer": answer
    }

def task_850():
    '''Генерация аналогичных задач № 850 с портала https://kuzovkin.info/one_exercise_1/850
    Цена на акцию сначала увеличилась на 20% процентов, а потом уменьшилась на 20%.
    На сколько процентов и в какую сторону изменилась цена акции по сравнению с первоначальной?'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        percent1, percent2 = np.random.randint(5, 30, size=2)
        result = 100 - (100 + percent1) * (100 - percent2) / 100
        if result != 0 and result * 1000 % 1000 == 0:
          answer = f'{"увеличилась" if result < 0 else "уменьшилась"} на {abs(int(result))}%'
          break
        elif result != 0 and result * 1000 % 100 == 0:
          answer = f'{"увеличилась" if result < 0 else "уменьшилась"} на {abs(result)}%'
          break
    task = f'Цена на {choosing_declension_form(cloth, "accs")} сначала увеличилась на {percent1}% процентов, а потом уменьшилась на {percent2}%. На сколько процентов и в какую сторону изменилась цена {choosing_declension_form(cloth)} по сравнению с первоначальной?'
    return {
      "condition": task,
      "answer": answer
    }

def task_863():
    '''Генерация аналогичных задач № 863 с портала https://kuzovkin.info/one_exercise_1/863
    В двух магазинах были одинаковые цены. В одном магазине их сначала понизили на 15%, а потом повысили на 10%,
    а в другом − сначала повысили на 10%, а потом понизили на 15%. В каком из магазинов выгоднее покупать товар?'''
    while True:
        percent11, percent22 = np.random.randint(5, 30, size=2)
        percent12, percent21 = np.random.randint(5, 30, size=2)
        result = (((100+percent12) / 100) * ((100 - percent11) / 100)) / (((100 - percent22) / 100) * ((100 + percent21) / 100))
        if result > 1:
            answer = f'выгоднее во втором'
            break
        elif result < 1:
            answer = f'выгоднее в первом'
            break
        elif result == 1:
            answer = f'одинаково'
            break
    task = f'В двух магазинах были одинаковые цены. В одном магазине их сначала понизили на {percent11}%, а потом повысили на {percent12}%, а в другом − сначала повысили на {percent21}%, а потом понизили на {percent22}%. В каком из магазинов выгоднее покупать товар?'
    return {
      "condition": task,
      "answer": answer
    }

def task_873():
    '''Генерация аналогичных задач № 873 с портала https://kuzovkin.info/one_exercise_1/873
    Цена на акции сначала два раза увеличилась на 5%, а потом уменьшилась на 10%.
    Как и на сколько процентов изменилась цена акции по сравнению с первоначальной?'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        percent1, percent2 = np.random.randint(2, 30, size=2)
        result = (100 + percent1) * (100 + percent1) * (100 - percent2) / 10000 - 100
        if result < 0 and abs(str(result).find('.') - len(str(result))) - 1 < 4:
            answer = f'цена уменьшилась на {abs(int(result) if result * 10000 % 10000 == 0 else abs(result))}%'
            break
        elif result > 0 and abs(str(result).find('.') - len(str(result))) - 1 < 3:
            answer = f'цена увеличилась на {int(result) if result * 10000 % 10000 == 0 else result}%'
            break
        elif result == 0:
            answer = f'цена не изменилась'
            break
    task = f'Цена на {choosing_declension_form(cloth, "accs")} сначала два раза увеличилась на {percent1}%, а потом уменьшилась на {percent2}%. Как и на сколько процентов изменилась цена {choosing_declension_form(cloth)} по сравнению с первоначальной?'
    return {
      "condition": task,
      "answer": answer
    }

def task_876():
    '''Генерация аналогичных задач № 873 с портала https://kuzovkin.info/one_exercise_1/876
    Цена на акции выросла на 12%, потом упала на 16%, потом опять упала на 21%.
    Как и на сколько процентов изменилась цена акции по сравнению с первоначальной?'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        percent1, percent2, percent3 = np.random.randint(2, 30, size=3)
        result = (100 + percent1) * (100 - percent2) * (100 - percent3) / 10000 - 100
        if result < 0 and abs(str(result).find('.') - len(str(result))) - 1 < 4:
            answer = f'цена уменьшилась на {abs(int(result) if result * 10000 % 10000 == 0 else abs(result))}%'
            break
        elif result > 0 and abs(str(result).find('.') - len(str(result))) - 1 < 3:
            answer = f'цена увеличилась на {int(result) if result * 10000 % 10000 == 0 else result}%'
            break
        elif result == 0:
            answer = f'цена не изменилась'
            break
    task = f'Цена на {choosing_declension_form(cloth, "accs")} выросла на {percent1}%, потом упала на {percent2}%, потом опять упала на {percent3}%. Как и на сколько процентов изменилась цена {choosing_declension_form(cloth)} по сравнению с первоначальной?'
    return {
      "condition": task,
      "answer": answer
    }

def task_4483():
    '''Генерация аналогичных задач № 4483 с портала https://kuzovkin.info/one_exercise_1/4483
    Цена товара увеличилась на 5%. Сколько процентов составляет новая цена от старой?'''
    while True:
        percent = random.randint(2, 30)
        result = 100 + percent
        answer = result
        break
    task = f'Цена товара увеличилась на {percent}%. Сколько процентов составляет новая цена от старой?'
    return {
      "condition": task,
      "answer": answer
    }

def task_4503():
    '''Генерация аналогичных задач № 4503 с портала https://kuzovkin.info/one_exercise_1/4503
    Дисконтная карточка в магазине «Marks&Spencer» даёт мне скидку 3%.
    Цена шляпы с учётом скидки составила 1552 рубля. Сколько стоит шляпа без скидки?'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        percent = random.randint(2, 30)
        price = random.randint(1000, 5000)
        result = 100 * price / (100 - percent)
        if result * 1000 % 1000 == 0 and price % 10 != 1:
            answer = int(result)
            break
    task = f'Дисконтная карточка в магазине «Marks&Spencer» даёт мне скидку {percent}%. Цена {choosing_declension_form(cloth)} с учётом скидки составила {price} рубл{"я" if price % 10 in [2, 3, 4] else "ей"}. Сколько сто{"ит" if find_number_object(cloth) == 1 else "ят"} {cloth} без скидки?'
    return {
      "condition": task,
      "answer": answer
    }

def task_4689():
    '''Генерация аналогичных задач № 4689 с портала https://kuzovkin.info/one_exercise_1/4689
    Вкладчик положил в банк 15000 долларов. Проценты по вкладу составили 525 долларов. Какова доходность вклада?'''
    money = random.sample(generate_context('./text_tasks/context.json', 'currency'), 1)[0]
    while True:
        contr = np.random.randint(10000, 100000)
        profit = np.random.randint(300, 3000)
        if contr % 100 == 0 and profit % 10 in [0, 5, 6, 7, 8, 9]:
          result = 100 * profit / contr
          if result * 10000 % 10000 == 0:
              answer = int(result)
              break
          elif result * 10000 % 100 == 0:
              answer = result
              break
    task = f'Вкладчик положил в банк {contr} {choosing_declension_form(money)}. Проценты по вкладу составили {profit} {choosing_declension_form(money)}. Какова доходность вклада?'
    return {
      "condition": task,
      "answer": answer
    }

def task_4713():
    '''Генерация аналогичных задач № 4713 с портала https://kuzovkin.info/one_exercise_1/4713
    Шуба дороже пальто на 100%. На сколько процентов пальто дешевле шубы?'''
    cloth_1, cloth_2 = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 2)
    while True:
        percent = random.randint(5, 100)
        result = 100 - 10000 / (100 + percent)
        if result * 100000 % 100000 == 0:
            answer = int(result)
            break
        elif result * 100000 % 100 == 0:
            answer = result
            break
    task = f'{capitalize_word(cloth_1)} дороже {choosing_declension_form(cloth_2)} на {percent}%. На сколько процентов {cloth_2} дешевле {choosing_declension_form(cloth_1)}?'
    return {
      "condition": task,
      "answer": answer
    }

def task_4751():
    '''Генерация аналогичных задач № 4751 с портала https://kuzovkin.info/one_exercise_1/4751
    Цена на товар была снижена на 80%. На сколько процентов надо теперь её повысить,
    чтобы получить первоначальную цену?'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        percent = random.randint(2, 99)
        result = 10000 / (100 - percent) - 100
        if result * 100000 % 10000 == 0:
            answer = int(result)
            break
    task = f'Цена на {choosing_declension_form(cloth, "accs")} была снижена на {percent}%. На сколько процентов надо теперь её повысить, чтобы получить первоначальную цену?'
    return {
      "condition": task,
      "answer": answer
    }

def task_8362():
    '''Генерация аналогичных задач № 8362 с портала https://kuzovkin.info/one_exercise_1/8362
    Пиджак стоит 5000 рублей. В связи с поступлением новой коллекции пиджак продают со скидкой 70%.
    Сколько стоит пиджак с учётом скидки?'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        price = random.randint(2000, 8000)
        if price % 10 == 0:
          percent = random.randint(10, 90)
          result = price * (100 - percent) / 100
          if result * 10000 % 10000 == 0:
              answer = int(result)
              break
    task = f'{capitalize_word(cloth)} сто{"ит" if find_number_object(cloth) == 1 else "ят"} {price} рублей. В связи с поступлением новой коллекции {cloth} продают со скидкой {percent}%. Сколько сто{"ит" if find_number_object(cloth) == 1 else "ят"} {cloth} с учётом скидки?'
    return {
      "condition": task,
      "answer": answer
    }

def task_4490():
    '''Генерация аналогичных задач № 4490 с портала https://kuzovkin.info/one_exercise_1/4490
    Вкладчик положил 300000 рублей в банк под 11% годовых. Какая сумма будет у него на счету через год?'''
    while True:
        period = choice([1, 2, 3])
        percent = random.randint(3, 18)
        contrib = random.randint(50000, 500000)
        if contrib % 1000 == 0:
          result = contrib * ((100 + percent) / 100) ** period
          if result * 1000 % 1000 == 0:
              answer = int(result)
              break
          elif result * 10000 % 100 == 0:
              answer = result
              break
    task = f'Вкладчик положил {contrib} рублей в банк под {percent}% годовых. Какая сумма будет у него на счету через {period if period !=1 else ""}{"год" if period == 1 else " года"}?'
    return {
      "condition": task,
      "answer": answer
    }

def task_4673():
    '''Генерация аналогичных задач № 4673 с портала https://kuzovkin.info/one_exercise_1/4673
    Цена на акцию понизилась на 2,5% и составила 8677,5 рубля. Найдите первоначальную цену акции?'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        percent = round(random.random(), 1) + random.randint(0, 8)
        cost = round(random.random(), 1) + random.randint(1000, 10000)
        result = cost * 100 / (100- percent)
        if result * 1000 % 100000 == 0:
            answer = int(result)
            break
    task = f'Цена на {choosing_declension_form(cloth, "accs")} понизилась на {int(percent) if percent*10%10==0 else percent}% и составила {int(cost) if cost*10%10==0 else cost} рубля. Найдите первоначальную цену {choosing_declension_form(cloth)}?'
    return {
      "condition": task,
      "answer": answer
    }

def task_8559():
    '''Генерация аналогичных задач № 8559 с портала https://kuzovkin.info/one_exercise_1/8559
    Цена товара повысилась с 450 рублей до 522 рублей. На сколько процентов была повышена цена товара?'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        price1, price2 = np.random.randint(400, 600, size=2)
        if price1 < price2 and price1 * 10 % 10 == 0 and price2 * 10 % 10 != 1:
          result = price2 * 100 / price1 - 100
          if result * 1000 % 1000 == 0:
              answer = int(result)
              break
    task = f'Цена {choosing_declension_form(cloth)} повысилась с {price1} рублей до {price2} рублей. На сколько процентов была повышена цена {choosing_declension_form(cloth)}?'
    return {
      "condition": task,
      "answer": answer
    }

def task_8548():
    '''Генерация аналогичных задач № 8548 с портала https://kuzovkin.info/one_exercise_1/8548
    Цена на товар была повышена на 11% и составила 1443 рубля. Сколько рублей стоил товар до повышения цены?'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        percent = np.random.randint(2, 20)
        price = np.random.randint(1000, 5000)
        result = price * 100 / (100 + percent)
        if result * 100 % 10000 == 0:
            answer = int(result)
            break
    task = f'Цена на {choosing_declension_form(cloth, "accs")} была повышена на {percent}% и составила {price} рубля. Сколько рублей стоил{"и" if find_number_object(cloth) == 2 else "o" if find_genus_object(cloth)== 3 else "a" if find_genus_object(cloth)== 2 else ""} {cloth} до повышения цены?'
    return {
      "condition": task,
      "answer": answer
    }

def task_4727():
    '''Генерация аналогичных задач № 4727 с портала https://kuzovkin.info/one_exercise_1/4727
    Цена на товар два раза увеличилась на 10%. На сколько процентов увеличилась цена по сравнению с первоначальной?'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        percent = np.random.randint(2, 30)
        result = (100 + percent) ** 2 / 100 - 100
        if result * 1000 % 1000 == 0:
          answer = int(result)
          break
        elif abs(str(result).find('.') - len(str(result))) - 1 < 3:
          answer = result
          break
    task = f'Цена на {choosing_declension_form(cloth, "accs")} два раза увеличилась на {percent}%. На сколько процентов увеличилась цена по сравнению с первоначальной?'
    return {
      "condition": task,
      "answer": answer
    }

def task_4717():
    '''Генерация аналогичных задач № 4717 с портала https://kuzovkin.info/one_exercise_1/4717
    Цена на акцию сначала снизилась на 10%, потом снизилась ещё на 10%, а потом увеличилась на 20%.
    На сколько процентов изменилась цена акции по сравнению с первоначальной?'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        percent1, percent2, percent3 = np.random.randint(2, 30, size=3)
        result = (100 - percent1) * (100 - percent2) * (100 + percent3) / 10000 - 100
        if result * 10000 % 10000 == 0:
            answer = abs(int(result))
            break
        elif abs(str(result).find('.') - len(str(result))) - 1 < 3:
            answer = abs(result)
            break
    task = f'Цена на {choosing_declension_form(cloth, "accs")} сначала снизилась на {percent1}%, потом снизилась ещё на {percent2}%, а потом увеличилась на {percent3}%. На сколько процентов изменилась цена {choosing_declension_form(cloth)} по сравнению с первоначальной?'
    return {
      "condition": task,
      "answer": answer
    }

def task_9213():
    '''Генерация аналогичных задач № 9213 с портала https://kuzovkin.info/one_exercise_1/9213
    Цена на товар повысилась на 21% и составила 7865 рублей. Найдите первоначальную цену товара.'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        percent = np.random.randint(2, 40)
        price = np.random.randint(1000, 10000)
        result = price * 100 / (100 + percent)
        if result * 100 % 10000 == 0:
            answer = int(result)
            break
    task = f'Цена на {choosing_declension_form(cloth, "accs")} повысилась на {percent}% и составила {price} рублей. Найдите первоначальную цену {choosing_declension_form(cloth)}.'
    return {
      "condition": task,
      "answer": answer
    }

def task_9198():
    '''Генерация аналогичных задач № 9198 с портала https://kuzovkin.info/one_exercise_1/9198
    Цена на чайник повысилась на 11% и стала равна 1332 рубля. Сколько стоил чайник до повышения цены?'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        percent = random.randint(2, 30)
        price = random.randint(1000, 3000)
        result = price * 100 / (100 + percent)
        if result * 100 % 1000 == 0:
            answer = int(result)
            break
    task = f'Цена на {choosing_declension_form(cloth, "accs")} повысилась на {percent}% и стала равна {price} рубля. Сколько стоил{"и" if find_number_object(cloth)==2 else "" if find_genus_object(cloth)==1 else "a" if find_genus_object(cloth)==2 else "о"} {cloth} до повышения цены?'
    return {
      "condition": task,
      "answer": answer
    }

def task_9445():
    '''Генерация аналогичных задач № 9445 с портала https://kuzovkin.info/one_exercise_1/9445
    В двух магазинах были одинаковые цены. В одном магазине их сначала понизили на 15%, а потом повысили на 10%,
    а в другом − сначала повысили на 10%, а потом понизили на 15%. Как изменились цены в этих магазинах по сравнению с первоначальной?'''
    while True:
      percent11, percent12 = np.random.randint(5, 30, size=2)
      percent21, percent22 = np.random.randint(5, 30, size=2)
      result1 = (100 - percent11) * (100 + percent12) / 100 - 100
      result2 = (100 + percent21) * (100 - percent22) / 100 - 100
      if abs(str(result1).find('.') - len(str(result1))) - 1 < 3 and abs(str(result2).find('.') - len(str(result2))) - 1 < 3:
        if result1 == 0 and result2 == 0:
          answer = f'не изменилась'
          break
        elif result1 == result2 :
          answer = f'{"увеличилась" if result1 > 0 else "уменьшилась"} на {abs(int(result1)) if result1*1000%1000==0 else abs(result1)}%'
          break
        else:
          answer = f'в первом {"увеличилась" if result1 > 0 else "уменьшилась"} на {abs(int(result1)) if result1*1000%1000==0 else abs(result1)}%, во втором {"увеличилась" if result2 > 0 else "уменьшилась"} на {abs(int(result2)) if result2*1000%1000==0 else abs(result2)}%'
          break
    task = f'В двух магазинах были одинаковые цены. В одном магазине их сначала понизили на {percent11}%, а потом повысили на {percent12}%, а в другом − сначала повысили на {percent21}%, а потом понизили на {percent22}%. Как изменились цены в этих магазинах по сравнению с первоначальной?'
    return {
      "condition": task,
      "answer": answer
    }

def task_9460():
    '''Генерация аналогичных задач № 9460 с портала https://kuzovkin.info/one_exercise_1/9460
    Цена на акции два раза упала на 20%, а потом два раза выросла на 30%. Как и на сколько процентов изменилась цена акции по сравнению с первоначальной?'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        percent1, percent2 = np.random.randint(2, 40, size=2)
        result = (100 - percent1) ** 2 *(100 + percent2) ** 2 / 100 ** 3 - 100
        if result < 0 and abs(str(result).find('.') - len(str(result))) - 1 < 3:
            answer = f'цена уменьшилась на {abs(int(result) if result * 10000 % 10000 == 0 else abs(result))}%'
            break
        elif result > 0 and abs(str(result).find('.') - len(str(result))) - 1 < 3:
            answer = f'цена увеличилась на {int(result) if result * 10000 % 10000 == 0 else result}%'
            break
        elif result == 0:
            answer = f'цена не изменилась'
            break
    task = f'Цена на {choosing_declension_form(cloth, "accs")} два раза упала на {percent1}%, а потом два раза выросла на {percent2}%. Как и на сколько процентов изменилась цена {choosing_declension_form(cloth)} по сравнению с первоначальной?'
    return {
      "condition": task,
      "answer": answer
    }

def task_9461():
    '''Генерация аналогичных задач № 9461 с портала https://kuzovkin.info/one_exercise_1/9461
    Цена на акции сначала выросла на 10%, потом упала на 15%, потом выросла на 20%, а потом упала на 12%.
    Как и на сколько процентов изменилась цена акции по сравнению с первоначальной?'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        percent1, percent2, percent3, percent4 = np.random.randint(2, 30, size=4)
        result = (100 + percent1) * (100 - percent2) * (100 + percent3) * (100 - percent4) / 100 ** 3 - 100
        if result < 0 and abs(str(result).find('.') - len(str(result))) - 1 < 3:
            answer = f'цена уменьшилась на {abs(int(result) if result * 10000 % 10000 == 0 else abs(result))}%'
            break
        elif result > 0 and abs(str(result).find('.') - len(str(result))) - 1 < 3:
            answer = f'цена увеличилась на {int(result) if result * 10000 % 10000 == 0 else result}%'
            break
        elif result == 0:
            answer = f'цена не изменилась'
            break
    task = f'Цена на {choosing_declension_form(cloth, "accs")} сначала выросла на {percent1}%, потом упала на {percent2}%, потом выросла на {percent3}%, а потом упала на {percent4}%. Как и на сколько процентов изменилась цена {choosing_declension_form(cloth)} по сравнению с первоначальной?'
    return {
      "condition": task,
      "answer": answer
    }

def task_9463():
    '''Генерация аналогичных задач № 9463 с портала https://kuzovkin.info/one_exercise_1/9463
    Цена на товар была повышена на 25%. На сколько процентов надо теперь её снизить, чтобы получить первоначальную цену?'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        percent = np.random.randint(1, 91)
        result = 100 - 10000 / (100 + percent)
        if result * 1000 % 1000 == 0:
          answer = int(result)
          break
        elif abs(str(result).find('.') - len(str(result))) - 1 < 4:
          answer = result
          break
    task = f'Цена на {choosing_declension_form(cloth, "accs")} была повышена на {percent}%. На сколько процентов надо теперь её снизить, чтобы получить первоначальную цену?'
    return {
      "condition": task,
      "answer": answer
    }

def task_11011():
    '''Генерация аналогичных задач № 11011 с портала https://kuzovkin.info/one_exercise_1/11011
    Цена на акцию увеличилась на 10%, потом уменьшилась на 20%, потом увеличилась на 30%, далее уменьшилась на 40%,
    и наконец увеличилась на 60%. На сколько процентов и в какую сторону изменилась цена по сравнению с первоначальной?'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        percent1, percent2, percent3, percent4, percent5 = np.random.randint(1, 60, size=5)
        result = ((100 + percent1) * (100 - percent2) / 100 ** 2) * ((100 + percent3) * (100 - percent4) / 100 ** 2) * (100 + percent5) - 100
        if result < 0 and abs(str(result).find('.') - len(str(result))) - 1 < 3:
            answer = f'цена уменьшилась на {abs(int(result) if result * 10000 % 10000 == 0 else abs(result))}%'
            break
        elif result > 0 and abs(str(result).find('.') - len(str(result))) - 1 < 3:
            answer = f'цена увеличилась на {int(result) if result * 10000 % 10000 == 0 else result}%'
            break
        elif result == 0:
            answer = f'цена не изменилась'
            break
    task = f'Цена на {choosing_declension_form(cloth, "accs")} увеличилась на {percent1}%, потом уменьшилась на {percent2}%, потом увеличилась на {percent3}%, далее уменьшилась на {percent4}%, и наконец увеличилась на {percent5}%. На сколько процентов и в какую сторону изменилась цена по сравнению с первоначальной?'
    return {
      "condition": task,
      "answer": answer
    }

def task_11010():
    '''Генерация аналогичных задач № 11010 с портала https://kuzovkin.info/one_exercise_1/11010
    Цена на акцию увеличилась на 10%, потом ещё на 5%, а потом упала на 20%. Сколько стоит теперь акция, если первоначально она стоила 4000 рублей?'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        percent1, percent2, percent3 = np.random.randint(2, 30, size=3)
        price = random.randint(1000, 5000)
        if price % 10 == 0:
          result = (100 + percent1) * (100 + percent2) * (100 - percent3) / 100 ** 3 * price
          if result * 1000 % 1000 == 0:
              answer = int(result)
              break
          elif abs(str(result).find('.') - len(str(result))) - 1 < 3:
              answer = result
              break
    task = f'Цена на {choosing_declension_form(cloth, "accs")} увеличилась на {percent1}%, потом ещё на {percent2}%, а потом упала на {percent3}%. Сколько сто{"ит" if find_number_object(cloth) == 1 else "ят"} теперь {cloth}, если первоначально {"они" if find_number_object(cloth) == 2 else "он" if find_genus_object(cloth)==1 else "она" if find_genus_object(cloth)==2 else "оно"} стоил{"и" if find_number_object(cloth) == 2 else "" if find_genus_object(cloth)==1 else "а" if find_genus_object(cloth)==2 else "о"} {price} рублей?'
    return {
      "condition": task,
      "answer": answer
    }

def task_10790():
    '''Генерация аналогичных задач № 10790 с портала https://kuzovkin.info/one_exercise_1/10790
    Цена на товар понизилась на 15% и составила 2176 рублей. Найдите первоначальную цену товара.'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        percent = random.randint(2, 30)
        price = random.randint(1000, 4000)
        if price % 10 != 1:
          result = 100 * price / (100 - percent)
          if result % 10 == 0:
              answer = int(result)
              break
    task = f'Цена на {choosing_declension_form(cloth, "accs")} понизилась на {percent}% и составила {price} рубл{"я" if price%10 in [2, 3, 4] else "ей"}. Найдите первоначальную цену {choosing_declension_form(cloth)}.'
    return {
      "condition": task,
      "answer": answer
    }

def task_10776():
    '''Генерация аналогичных задач № 10776 с портала https://kuzovkin.info/one_exercise_1/10776
    Пиджак стоит 5250 рублей. В магазине проводят распродажу со скидкой 15%. Сколько стоит пиджак на распродаже?'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        percent = random.randint(2, 30)
        price = random.randint(2000, 8000)
        if price % 10 == 0:
          result = (100 - percent) / 100 * price
          if result * 1000 % 1000 == 0:
              answer = int(result)
              break
          elif abs(str(result).find('.') - len(str(result))) - 1 < 3:
              answer = result
              break
    task = f'{capitalize_word(cloth)} сто{"ит" if find_number_object(cloth)==1 else "ят"} {price} рублей. В магазине проводят распродажу со скидкой {percent}%. Сколько сто{"ит" if find_number_object(cloth)==1 else "ят"} {cloth} на распродаже?'
    return {
      "condition": task,
      "answer": answer
    }

def task_9477():
    '''Генерация аналогичных задач № 9477 с портала https://kuzovkin.info/one_exercise_1/9477
    Цена на товар в течение месяца упала сначала на 18%, а затем на 20% и составила 328 рублей. Найдите исходную цену товара.'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        percent1, percent2 = np.random.randint(2, 30, size=2)
        price = random.randint(300, 3000)
        if price % 10 != 1:
          result = price * 100 ** 2 / ((100 - percent1) * (100 - percent2))
          if result * 1000 % 1000 == 0:
              answer = int(result)
              break
          elif abs(str(result).find('.') - len(str(result))) - 1 < 3:
              answer = result
              break
    task = f'Цена на {choosing_declension_form(cloth, "accs")} в течение месяца упала сначала на {percent1}%, а затем на {percent2}% и составила {price} рубл{"я" if price%10 in [2, 3, 4] else "ей"}. Найдите исходную цену {choosing_declension_form(cloth)}.'
    return {
      "condition": task,
      "answer": answer
    }

def task_9476():
    '''Генерация аналогичных задач № 9476 с портала https://kuzovkin.info/one_exercise_1/9476
    Цена товара сначала поднялась на 10%, потом уменьшилась на 20%, далее увеличилась на 5% и стала равна 6468 рублей. Найдите первоначальную цену товара.'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        percent1, percent2, percent3 = np.random.randint(2, 30, size=3)
        price = random.randint(3000, 9000)
        if price % 10 != 1:
          result = price * 100 ** 3 / ((100 + percent1) * (100 - percent2) * (100 + percent3))
          if result * 1000 % 1000 == 0:
              answer = int(result)
              break
          elif abs(str(result).find('.') - len(str(result))) - 1 < 3:
              answer = result
              break
    task = f'Цена {choosing_declension_form(cloth)} сначала поднялась на {percent1}%, потом уменьшилась на {percent2}%, далее увеличилась на {percent3}% и стала равна {price} рубл{"я" if price%10 in [2, 3, 4] else "ей"}. Найдите первоначальную цену {choosing_declension_form(cloth)}.'
    return {
      "condition": task,
      "answer": answer
    }

def task_11051():
    '''Генерация аналогичных задач № 11051 с портала https://kuzovkin.info/one_exercise_1/11051
    Цена на некоторый товар была снижена дважды − сначала на 15%, а потом ещё на 20%. Каков общий процент снижения цены?'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        percent1, percent2 = np.random.randint(2, 30, size=2)
        result = 100 - (100 - percent1) * (100 - percent2) / 100
        if result * 1000 % 1000 == 0:
            answer = int(result)
            break
        elif abs(str(result).find('.') - len(str(result))) - 1 < 3:
            answer = result
            break
    task = f'Цена на {choosing_declension_form(cloth, "accs")} была снижена дважды − сначала на {percent1}%, а потом ещё на {percent2}%. Каков общий процент снижения цены?'
    return {
      "condition": task,
      "answer": answer
    }

def task_11056():
    '''Генерация аналогичных задач № 11056 с портала https://kuzovkin.info/one_exercise_1/11056
    Цена товара поднялась сначала на 20%, потом ещё на 15% и стала равна 8280 рублей. Найдите первоначальную цену товара.'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        percent1, percent2 = np.random.randint(2, 30, size=2)
        price = random.randint(300, 6000)
        if price % 10 != 1:
          result = price * 100 ** 2 / ((100 + percent1) * (100 + percent2))
          if result * 1000 % 1000 == 0:
              answer = int(result)
              break
          elif abs(str(result).find('.') - len(str(result))) - 1 < 3:
              answer = result
              break
    task = f'Цена {choosing_declension_form(cloth)} поднялась сначала на {percent1}%, потом ещё на {percent2}% и стала равна {price} рубл{"я" if price%10 in [2, 3, 4] else "ей"}. Найдите первоначальную цену {choosing_declension_form(cloth)}.'
    return {
      "condition": task,
      "answer": answer
    }

def task_11059():
    '''Генерация аналогичных задач № 11059 с портала https://kuzovkin.info/one_exercise_1/11059
    Цена на товар в течение месяца упала сначала на 40%, а потом увеличилась на 50% и составила 5130 рублей. Найдите первоначальную цену товара.'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        percent1, percent2 = np.random.randint(2, 30, size=2)
        price = random.randint(2000, 8000)
        if price % 10 != 1:
          result = price * 100 ** 2 / ((100 - percent1) * (100 + percent2))
          if result * 1000 % 1000 == 0:
              answer = int(result)
              break
          elif abs(str(result).find('.') - len(str(result))) - 1 < 3:
              answer = result
              break
    task = f'Цена на {choosing_declension_form(cloth, "accs")} в течение месяца упала сначала на {percent1}%, а потом увеличилась на {percent2}% и составила {price} рубл{"я" if price%10 in [2, 3, 4] else "ей"}. Найдите первоначальную цену {choosing_declension_form(cloth)}.'
    return {
      "condition": task,
      "answer": answer
    }

def task_12793():
    '''Генерация аналогичных задач № 12793 с портала https://kuzovkin.info/one_exercise_1/12793
    Первоначально цена на некоторый товар была повышена на 44%, затем 2 раза понижалась на одинаковое число процентов.
    В результате конечная цена оказалась на 19% меньше первоначальной. На сколько процентов производилось двукратное снижение цены?'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        percent1, percent2 = np.random.randint(2, 90, size=2)
        decline = 200 ** 2 - 4 * (100 ** 2 - ((100 - percent2) * 100 ** 2 / (100 + percent1)))
        if decline ** 0.5 * 1000 % 1000 == 0:
          result = (200 - decline ** 0.5) / 2
          if result * 1000 % 1000 == 0:
            answer = int(result)
            break
          else:
            answer = result
            break
    task = f'Первоначально цена на {choosing_declension_form(cloth, "accs")} была повышена на {percent1}%, затем 2 раза понижалась на одинаковое число процентов. В результате конечная цена оказалась на {percent2}% меньше первоначальной. На сколько процентов производилось двукратное снижение цены?'
    return {
      "condition": task,
      "answer": answer
    }

def task_12794():
    '''Генерация аналогичных задач № 12794 с портала https://kuzovkin.info/one_exercise_1/12794
    Первый банк дает 5% годовых, а второй - 10%. Вкладчик часть своих денег положил в первый банк, а остальные - во второй.
    Через 2 года суммарное число вложенных денег увеличилось на 18,85%. Какую долю своих денег положил вкладчик в первый банк?'''
    while True:
        percent1, percent2, percent3 = np.random.randint(2, 30, size=3)
        if (100 + percent2) ** 2 - 100 * (100 + percent3) != 0 and (1 + (100 * (100 + percent3) - (100 + percent1) ** 2) / ((100 + percent2) ** 2 - 100 * (100 + percent3))) != 0:
          result = 100 / (1 + (100 * (100 + percent3) - (100 + percent1) ** 2) / ((100 + percent2) ** 2 - 100 * (100 + percent3)))
          if 0 < result < 100 and result * 10000 % 100 == 0:
              answer = f'{int(result) if result*1000%1000==0 else result}%'
              break
    task = f'Первый банк дает {percent1}% годовых, а второй - {percent2}%. Вкладчик часть своих денег положил в первый банк, а остальные - во второй. Через 2 года суммарное число вложенных денег увеличилось на {percent3}%. Какую долю своих денег положил вкладчик в первый банк?'
    return {
      "condition": task,
      "answer": answer
    }

def task_35687():
    '''Генерация аналогичных задач № 35687 с портала https://kuzovkin.info/one_exercise_1/35687
    Магазин увеличил цену товара в 8 раз. Однако по результатам проверки антимонопольная служба предписала вернуть прежнюю цену.
    На сколько процентов придётся снизить цену? Ответ подать в процентах, округлить до десятых'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        multipl = random.randint(2, 30)
        result = 100 - 100 / multipl
        if result * 10000 % 10000 == 0:
            answer = int(result)
            break
        else:
            answer = round(result, 1)
            break
    task = f'Магазин увеличил цену {choosing_declension_form(cloth)} в {multipl} раз. Однако по результатам проверки антимонопольная служба предписала вернуть прежнюю цену. На сколько процентов придётся снизить цену? Ответ подать в процентах, округлить до десятых'
    return {
      "condition": task,
      "answer": answer
    }

def task_35690():
    '''Генерация аналогичных задач № 35690 с портала https://kuzovkin.info/one_exercise_1/35690
    В начале мая цена на помидоры повысилась на 20, а в начале июня понизилась на 20. На сколько процентов цена помидоров в июне после понижения стала ниже,
    чем цена помидоров в мае до повышения? Ответ подать в процентах, округлить до целого'''
    fruit = random.sample(generate_context('./text_tasks/context.json', 'fruits'), 1)[0]
    while True:
        percent  = random.randint(2, 30)
        result = 100 - (100 + percent) * (100 - percent) / 100
        if result * 10000 % 10000 == 0:
            answer = int(result)
            break
        elif result > 1:
            answer = int(round(result, 0))
            break
    task = f'В начале мая цена на {choosing_declension_form(fruit, "accs")} повысилась на {percent}%, а в начале июня понизилась на {percent}%. На сколько процентов цена {choosing_declension_form(fruit)} в июне после понижения стала ниже, чем цена {choosing_declension_form(fruit)} в мае до повышения? Ответ подать в процентах, округлить до целого'
    return {
      "condition": task,
      "answer": answer
    }

def task_35702():
    '''Генерация аналогичных задач № 35702 с портала https://kuzovkin.info/one_exercise_1/35702
    Цена на телевизор была повышена на 16% и составила 34800 рублей. Сколько рублей стоил телевизор до повышения цены?'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        percent = random.randint(2, 30)
        price =  random.randint(4000, 15000)
        result = price * 100 / (100 + percent)
        if result * 1000 % 10000 == 0:
            answer = int(result)
            break
    task = f'Цена на {choosing_declension_form(cloth, "accs")} была повышена на {percent}% и составила {price} рублей. Сколько рублей стоил{"и" if find_number_object(cloth) == 2 else "" if find_genus_object(cloth)==1 else "а" if find_genus_object(cloth)==2 else "о"} {cloth} до повышения цены?'
    return {
      "condition": task,
      "answer": answer
    }

def task_35703():
    '''Генерация аналогичных задач № 35703 с портала https://kuzovkin.info/one_exercise_1/35703
    Подставка для книг стоила 80 рублей. После снижения цены она стала стоить 68 рублей. На сколько процентов была снижена цена на подставку?'''
    cloth = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 1)[0]
    while True:
        price1, price2 = np.random.randint(500, 5000, size=2)
        if price1 > price2 and price1 % 10 != 1 and price2 % 10 != 1:
          result = 100 - price2 * 100 / price1
          if result * 10000 % 10000 == 0:
              answer = int(result)
              break
          elif result * 10000 % 1000 == 0:
              answer = result
              break
    task = f'{capitalize_word(cloth)} стоил{"и" if find_number_object(cloth) == 2 else "" if find_genus_object(cloth)==1 else "а" if find_genus_object(cloth)==2 else "о"} {price1} рубл{"я" if price1%10 in [2, 3, 4] else "ей"}. После снижения цены {"они" if find_number_object(cloth)==2 else "он" if find_genus_object(cloth)==1 else "она" if find_genus_object(cloth)==2 else "оно"} стал{"и" if find_number_object(cloth) == 2 else "" if find_genus_object(cloth)==1 else "а" if find_genus_object(cloth)==2 else "о"} стоить {price2} рубл{"я" if price2%10 in [2, 3, 4] else "ей"}. На сколько процентов была снижена цена на {choosing_declension_form(cloth, "accs")}?'
    return {
      "condition": task,
      "answer": answer
    }
