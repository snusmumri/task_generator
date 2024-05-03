import random
import numpy as np
from .utils import choosing_declension_form, capitalize_word, find_number_object, find_genus_object, generate_context, write_numeral_word

def task_2614():
    '''Генерация аналогичных задач № 2614 с портала https://kuzovkin.info/one_exercise_1/2614
    В сплав золота с серебром, содержащий 80 г золота, добавили 100 г золота.
    В результате содержание золота в сплаве увеличилось на 20 %. Сколько граммов серебра в сплаве?'''
    metal_1, metal_2 = random.sample(generate_context('./text_tasks/context.json', 'metals'), 2)
    while True:
        weight, weight1 = np.random.randint(10, 999, size=2)
        percent = random.randint(1, 99)
        result = -1 * (2 * weight + weight1 - weight1 * 100 / percent) / 2
        if (2 * weight + weight1 - weight1 * 100 / percent) ** 2 - 4 * weight * (weight + weight1) == 0 and 0 < result < 1000 and result * 1000 % 1000 == 0:
            answer = int(result)
            break
    task = f'В сплав {choosing_declension_form(metal_1)} с {choosing_declension_form(metal_2, "ablt")}, содержащий {weight} г {choosing_declension_form(metal_1)}, добавили {weight1} г {choosing_declension_form(metal_1)}. В результате содержание {choosing_declension_form(metal_1)} в сплаве увеличилось на {percent} %. Сколько граммов {choosing_declension_form(metal_2)} в сплаве?'
    return {
      "condition": task,
      "answer": answer
    }
def task_4767():
    '''Генерация аналогичных задач № 4767 с портала https://kuzovkin.info/one_exercise_1/4767
    Морская вода содержит 8% (по весу) соли. Сколько килограммов пресной воды нужно добавить к 30 кг морской воды, чтобы содержание соли в последней составило 5%?'''
    options = random.sample(generate_context('./text_tasks/context.json', 'liquids'), 1)[0]
    while True:
        percent1, percent2 = np.random.randint(2, 15, size=2)
        weight = random.randint(5, 15)
        result = weight * (percent1 - percent2) / percent2
        if result * 1000 % 1000 == 0 and percent1 > percent2:
            answer = int(result)
            break
    task = f'{capitalize_word(choosing_declension_form(options[0], "nomn"))} содержит {percent1}% (по весу) {choosing_declension_form(options[1])}. Сколько килограммов {choosing_declension_form(options[2])} нужно добавить к {weight} кг {choosing_declension_form(options[0])}, чтобы содержание {choosing_declension_form(options[1])} в {choosing_declension_form(options[0], "loct")} составило {percent2}%?'
    return {
      "condition": task,
      "answer": answer
    }

def task_4770():
    '''Генерация аналогичных задач № 4770 с портала https://kuzovkin.info/one_exercise_1/4770
    Сколько килограммов воды нужно выпарить из 0,5 т целлюлозной массы, содержащей 85% воды, чтобы получить массу с содержанием 75% воды?'''
    options = random.sample(generate_context('./text_tasks/context.json', 'liquids'), 1)[0]
    while True:
        weight = random.randint(100, 2000)
        percent1, percent2 = np.random.randint(30, 90, size=2)
        result = (percent1 - percent2) * weight / (100 - percent2)
        if percent2 < percent1 and result * 1000 % 1000 == 0:
            answer = int(result)
            break
    task = f'Сколько килограммов {choosing_declension_form(options[2])} нужно выпарить из {weight/1000} т {choosing_declension_form(options[0])}, содержащей {percent1}% {choosing_declension_form(options[2])}, чтобы получить {choosing_declension_form((options[0] if len(options[0].split())<2 else options[0].split(" ", 1)[1]), "accs")} с содержанием {percent2}% {choosing_declension_form(options[2])}?'
    return {
      "condition": task,
      "answer": answer
    }

def task_4772():
    '''Генерация аналогичных задач № 4772 с портала https://kuzovkin.info/one_exercise_1/4772
    Свежие грибы содержат по весу 90% воды, а сухие − 12% воды. Сколько получится сухих грибов из 22 кг свежих?'''
    options = random.sample(generate_context('./text_tasks/context.json', 'vegetables'), 1)[0]
    while True:
        weight1 = random.randint(10, 100)
        percent1, percent2 = np.random.randint(10, 95, size=2)
        result = (100 - percent1) * weight1 / (100 - percent2)
        if percent2 < (percent1 - 40) and result * 1000 % 1000 == 0:
            answer = int(result)
            break
        elif percent2 < (percent1 - 40) and result * 1000 % 100 == 0:
            answer = result
            break
    task = f'{capitalize_word(options[0])} содержат по весу {percent1}% {choosing_declension_form(options[2])}, а {options[1]} − {percent2}% {choosing_declension_form(options[2])}. Сколько получится {choosing_declension_form(options[1])} из {weight1} кг {choosing_declension_form(options[0].split()[0])}?'
    return {
      "condition": task,
      "answer": answer
    }

def task_4773():
    '''Генерация аналогичных задач № 4773 с портала https://kuzovkin.info/one_exercise_1/4773
    Кусок сплава меди и цинка массой 36 кг содержит 45% меди.
    Какую массу меди следует добавить к этому куску, чтобы получить сплав, содержащий 60% меди?'''
    metal_1, metal_2 = random.sample(generate_context('./text_tasks/context.json', 'metals'), 2)
    while True:
        weight = random.randint(10, 100)
        percent1, percent2 = np.random.randint(10, 95, size=2)
        result = weight * (percent2 - percent1) / (100 - percent2)
        if percent1 < (percent2 - 10) and result * 1000 % 1000 == 0:
            answer = int(result)
            break
        elif percent1 < (percent2 - 10) and result * 1000 % 100 == 0:
            answer = result
            break
    task = f'Кусок сплава {choosing_declension_form(metal_1)} и {choosing_declension_form(metal_2)} массой {weight} кг содержит {percent1}% {choosing_declension_form(metal_1)}. Какую массу {choosing_declension_form(metal_1)} следует добавить к этому куску, чтобы получить сплав, содержащий {percent2}% {choosing_declension_form(metal_1)}?'
    return {
      "condition": task,
      "answer": answer
    }

def task_4774():
    '''Генерация аналогичных задач № 4774 с портала https://kuzovkin.info/one_exercise_1/4774
    В 2 литра 10-процентного раствора уксусной кислоты добавили 8 л чистой воды. Определите процентное содержание уксусной кислоты в полученном растворе.'''
    options = random.sample(generate_context('./text_tasks/context.json', 'chemical_solution'), 1)[0]
    while True:
        percent = random.randint(5, 40)
        weight1, weight2 = np.random.randint(2, 20, size=2)
        result = weight1 * percent / (weight1 + weight2)
        if weight1 < weight2 and result * 1000 % 1000 == 0:
            answer = int(result)
            break
        elif weight1 < weight2 and result * 1000 % 100 == 0:
            answer = result
            break
    task = f'В {weight1} литра {percent}-процентного раствора {choosing_declension_form(options[0])} добавили {weight2} л {choosing_declension_form(options[1])}. Определите процентное содержание {choosing_declension_form(options[0])} в полученном растворе.'
    return {
      "condition": task,
      "answer": answer
    }

def task_4778():
    '''Генерация аналогичных задач № 4778 с портала https://kuzovkin.info/one_exercise_1/4778
    В 5 кг сплава олова и цинка содержится 80% цинка. Сколько кг олова надо добавить к сплаву, чтобы процентное содержание цинка стало вдвое меньше?'''
    metal_1, metal_2 = random.sample(generate_context('./text_tasks/context.json', 'metals'), 2)
    while True:
        weight = random.randint(2, 20)
        percent = random.randint(60, 90)
        num = random.randint(2,5)
        result = weight * num - weight
        if percent / num * 10000 % 100 == 0:
          answer = result
          break
    task = f'В {weight} кг сплава {choosing_declension_form(metal_1)} и {choosing_declension_form(metal_2)} содержится {percent}% {choosing_declension_form(metal_2)}. Сколько кг {choosing_declension_form(metal_1)} надо добавить к сплаву, чтобы процентное содержание {choosing_declension_form(metal_2)} стало {write_numeral_word(num)} меньше?'
    return {
      "condition": task,
      "answer": answer
    }

def task_4780():
    '''Генерация аналогичных задач № 4780 с портала https://kuzovkin.info/one_exercise_1/4780
    Морская вода содержит 5% соли по массе. Сколько килограммов пресной воды нужно добавить к 30 кг морской воды, чтобы она содержала 1,5% по массе?'''
    options = random.sample(generate_context('./text_tasks/context.json', 'liquids'), 1)[0]
    while True:
        percent1 = round (random.random(), 1) + random.randint(1, 30)
        percent2 = round (random.random(), 1) + random.randint(1, 30)
        weight = random.randint(5, 30)
        result = weight * (percent1 - percent2) / percent2
        if percent1 > percent2 and result * 1000 % 1000 == 0:
            answer = int(result)
            break
    task = f'{capitalize_word(options[0])} содержит {int(percent1) if percent1 * 10 % 10 == 0 else percent1}% {choosing_declension_form(options[1])} по массе. Сколько килограммов {choosing_declension_form(options[2])} нужно добавить к {weight} кг {choosing_declension_form(options[0])}, чтобы {"она" if find_genus_object(options[0]) == 2 else "он"} {"содержала" if find_genus_object(options[0]) == 2 else "содержал"} {int(percent1) if percent2 * 10 % 10 == 0 else percent2}% {choosing_declension_form(options[1])} по массе?'
    return {
      "condition": task,
      "answer": answer
    }

def task_4782():
    '''Генерация аналогичных задач № 4782 с портала https://kuzovkin.info/one_exercise_1/4782
    Из 10 кг свежих фруктов получают 3,5 кг сушёных фруктов, содержащих 20% воды. Каково процентное содержание воды в свежих фруктах?'''
    options = random.sample(generate_context('./text_tasks/context.json', 'vegetables'), 1)[0]
    while True:
        percent = random.randint(5, 30)
        weight1 = round (random.random(), 1) + random.randint(5,30)
        weight2 = round (random.random(), 1) + random.randint(1, 20)
        result = (weight1 * 100 - weight2 * 100 + weight2 * percent) / weight1
        if weight2 < weight1 and result * 1000 % 1000 == 0:
            answer = int(result)
            break
    task = f'Из {int(weight1) if weight1 * 10 % 10 == 0 else weight1} кг {choosing_declension_form(options[0])} получают {int(weight2) if weight2 * 10 % 10 == 0 else weight2} кг {choosing_declension_form(options[1])}, {"содержащих" if find_number_object(options[0]) == 2 else "сoдержащего"} {percent}% {choosing_declension_form(options[2])}. Каково процентное содержание {choosing_declension_form(options[2])} в {choosing_declension_form(options[0], "loct")}?'
    return {
      "condition": task,
      "answer": answer
    }

def task_4784():
    '''Генерация аналогичных задач № 4784 с портала https://kuzovkin.info/one_exercise_1/4784
    В результате очистки сырья количество примесей в нём уменьшается с 20% в исходном сырье до 4% в очищенном.
    Сколько надо взять исходного сырья для получения 100 кг очищенного сырья?'''
    while True:
        percent1, percent2 = np.random.randint(2, 70, size=2)
        weight = random.randint(20, 100)
        result = (weight * 100 - percent2 * weight) / (100 - percent1)
        if percent1 > percent2 and result * 1000 % 1000 == 0:
            answer = int(result)
            break
    task = f'В результате очистки сырья количество примесей в нём уменьшается с {percent1}% в исходном сырье до {percent2}% в очищенном. Сколько надо взять исходного сырья для получения {weight} кг очищенного сырья?'
    return {
      "condition": task,
      "answer": answer
    }

def task_4787():
    '''Генерация аналогичных задач № 4787 с портала https://kuzovkin.info/one_exercise_1/4787
    Какое количество 8%-го раствора соли надо взять, чтобы его можно было развести чистой водой до получения 100 г 3%-го раствора соли?'''
    options = random.sample(generate_context('./text_tasks/context.json', 'chemical_solution'), 1)[0]
    while True:
        percent1, percent2 = np.random.randint(1, 20, size=2)
        weight = random.randint(50, 999)
        result = percent2 * weight / percent1
        if percent1 > percent2 and result * 1000 % 1000 == 0:
            answer = int(result)
            break
        elif percent1 > percent2 and result * 1000 % 100 == 0:
            answer = result
            break
    task = f'Какое количество {percent1}%-го раствора {choosing_declension_form(options[0])} надо взять, чтобы его можно было развести {choosing_declension_form(options[1], "ablt")} до получения {weight} г {percent2}%-го раствора {choosing_declension_form(options[0])}?'
    return {
      "condition": task,
      "answer": answer
    }

def task_4788():
    '''Генерация аналогичных задач № 4788 с портала https://kuzovkin.info/one_exercise_1/4788
    Морская вода содержит 5% соли. Сколько килограммов воды надо выпарить из 80 кг морской воды,
    чтобы концентрация соли в ней увеличилась до 20%?'''
    options = random.sample(generate_context('./text_tasks/context.json', 'liquids'), 1)[0]
    while True:
        percent1, percent2 = np.random.randint(2, 60, size=2)
        weight = random.randint(20, 100)
        result = weight * (percent2 - percent1) / percent2
        if percent1 < percent2 and result * 1000 % 1000 == 0:
            answer = int(result)
            break
    task = f'{capitalize_word(options[0])} содержит {percent1}% {choosing_declension_form(options[1])}. Сколько килограммов {choosing_declension_form(options[2].split()[-1])} надо выпарить из {weight} кг {choosing_declension_form(options[0])}, чтобы концентрация {choosing_declension_form(options[1])} в {"ней" if find_genus_object(options[0]) == 2 else "нём"} увеличилась до {percent2}%?'
    return {
      "condition": task,
      "answer": answer
    }

def task_4789():
    '''Генерация аналогичных задач № 4789 с портала https://kuzovkin.info/one_exercise_1/4789
    Сколько воды надо выпарить из 350 г 42%-го раствора соли, чтобы получить 60%-ый раствор?'''
    options = random.sample(generate_context('./text_tasks/context.json', 'chemical_solution'), 1)[0]
    while True:
        percent1, percent2 = np.random.randint(10, 80, size=2)
        weight = random.randint(100, 999)
        result = weight * (percent2 - percent1) / percent2
        if percent1 < percent2 and result * 1000 % 1000 == 0:
            answer = int(result)
            break
    task = f'Сколько {choosing_declension_form(options[1])} надо выпарить из {weight} г {percent1}%-го раствора {choosing_declension_form(options[0])}, чтобы получить {percent2}%-ый раствор?'
    return {
      "condition": task,
      "answer": answer
    }

def task_6488():
    '''Генерация аналогичных задач № 6488 с портала https://kuzovkin.info/one_exercise_1/6488
    В сплав меди и цинка, содержащий 5 кг цинка, добавили 15 кг цинка, после чего содержание цинка в сплаве повысилось на 30 %.
    Какова первоначальная масса сплава, если известно, что в нем меди было больше, чем цинка?'''
    metal_1, metal_2 = random.sample(generate_context('./text_tasks/context.json', 'metals'), 2)
    while True:
        weight1, weight2 = np.random.randint(1, 100, size=2)
        percent = random.randint(1,98)
        d = (percent*weight2-weight2*100)**2-4*percent*weight2*weight1*100
        if d > 0 and (d**0.5)*1000%1000 == 0:
          x1 = (weight2*100-percent*weight2+d**0.5)/(2*percent)
          x2 = (weight2*100-percent*weight2-d**0.5)/(2*percent)
          if x1*1000%1000 == 0 and x2*1000%1000 == 0 and (x1-weight1) > weight1 and (x2-weight1) <=weight1:
            answer = int(x1)
            break
    task = f'В сплав {choosing_declension_form(metal_1)} и {choosing_declension_form(metal_2)}, содержащий {weight1} кг {choosing_declension_form(metal_2)}, добавили {weight2} кг {choosing_declension_form(metal_2)}, после чего содержание {choosing_declension_form(metal_2)} в сплаве повысилось на {percent} %. Какова первоначальная масса сплава, если известно, что в нем {choosing_declension_form(metal_1)} было больше, чем {choosing_declension_form(metal_2)}?'
    return {
      "condition": task,
      "answer": answer
    }

def task_6489():
    '''Генерация аналогичных задач № 6489 с портала https://kuzovkin.info/one_exercise_1/6489
    Cлиток сплава меди и цинка массой 36 кг содержит 45% меди. Какую массу меди надо добавить к этому куску, чтобы плученный сплав содержал 60% меди?'''
    metal_1, metal_2 = random.sample(generate_context('./text_tasks/context.json', 'metals'), 2)
    while True:
        percent1, percent2 = np.random.randint(10, 80, size=2)
        weight = random.randint(1,80)
        result = (weight*percent2 - weight*percent1) / (100 - percent2)
        if percent1 < percent2 and result*10000%10000 == 0:
          answer = int(result)
          break
        elif percent1 < percent2 and result*10000%1000 == 0:
          answer = result
          break
    task = f'Cлиток сплава {choosing_declension_form(metal_1)} и {choosing_declension_form(metal_2)} массой {weight} кг содержит {percent1}% {choosing_declension_form(metal_1)}. Какую массу {choosing_declension_form(metal_1)} надо добавить к этому куску, чтобы плученный сплав содержал {percent2}% {choosing_declension_form(metal_1)}?'
    return {
      "condition": task,
      "answer": answer
    }

def task_9479():
    '''Генерация аналогичных задач № 9479 с портала https://kuzovkin.info/one_exercise_1/9479
    Сплав олова с медью весом 12 кг содержит 45% меди. Сколько чистого олова надо добавить, чтобы получить сплав, содержащий 40% меди?'''
    metal_1, metal_2 = random.sample(generate_context('./text_tasks/context.json', 'metals'), 2)
    while True:
        percent1, percent2 = np.random.randint(10, 80, size=2)
        weight = random.randint(1,80)
        result = weight * (percent1 - percent2) / percent2
        if percent1 > percent2 and result*10000%10000 == 0:
          answer = int(result)
          break
        elif percent1 > percent2 and result*10000%1000 == 0:
          answer = result
          break
    task = f'Сплав {choosing_declension_form(metal_1)} с {choosing_declension_form(metal_2, "ablt")} весом {weight} кг содержит {percent1}% {choosing_declension_form(metal_2)}. Сколько {"чистой" if find_genus_object(metal_1) == 2 else "чистого"} {choosing_declension_form(metal_1)} надо добавить, чтобы получить сплав, содержащий {percent2}% {choosing_declension_form(metal_2)}?'
    return {
      "condition": task,
      "answer": answer
    }

def task_9481():
    '''Генерация аналогичных задач № 9481 с портала https://kuzovkin.info/one_exercise_1/9481
    Свежие грибы содержат по массе 90% воды, а сухие − 20%. Сколько надо собрать свежих грибов, чтобы из них получить 4,5 кг сухих грибов?'''
    options = random.sample(generate_context('./text_tasks/context.json', 'vegetables'), 1)[0]
    while True:
        percent1, percent2 = np.random.randint(10, 90, size=2)
        weight = random.randint(1,20)
        result = weight * (100 - percent2) / (100 - percent1)
        if percent1 > percent2+30 and result*10000%10000 == 0:
          answer = int(result)
          break
    task = f'{capitalize_word(options[0])} {"содержит" if find_number_object(options[0]) == 1 else "содержат"} по массе {percent1}% {choosing_declension_form(options[2])}, а {"сухой" if find_number_object(options[0]) == 1 else "сухие"} − {percent2}%. Сколько надо собрать {choosing_declension_form(options[0])}, чтобы из {"него" if find_number_object(options[0]) == 1 else "них"} получить {weight} кг {"сухого" if find_number_object(options[0]) == 1 else "сухих"} {choosing_declension_form(options[0].split()[1])}?'
    return {
      "condition": task,
      "answer": answer
    }

def task_9486():
    '''Генерация аналогичных задач № 9486 с портала https://kuzovkin.info/one_exercise_1/9486
    В 4 кг сплава меди и олова содержится 40% олова. Сколько кг олова надо добавить к этому сплаву, чтобы его процентное содержание в новом сплаве стало равно 70%?'''
    metal_1, metal_2 = random.sample(generate_context('./text_tasks/context.json', 'metals'), 2)
    while True:
        percent1, percent2 = np.random.randint(10, 90, size=2)
        weight = random.randint(1,20)
        result = weight * (percent2 - percent1) / (100 - percent2)
        if percent1 < percent2 and result*10000%10000 == 0:
          answer = int(result)
          break
    task = f'В {weight} кг сплава {choosing_declension_form(metal_1)} и {choosing_declension_form(metal_2)} содержится {percent1}% {choosing_declension_form(metal_2)}. Сколько кг {choosing_declension_form(metal_2)} надо добавить к этому сплаву, чтобы его процентное содержание в новом сплаве стало равно {percent2}%?'
    return {
      "condition": task,
      "answer": answer
    }

def task_9487():
    '''Генерация аналогичных задач № 9487 с портала https://kuzovkin.info/one_exercise_1/9487
    К 40% раствору серной кислоты добавили 50 г чистой серной кислоты, после чего концентрация раствора стала равна 60%. Найдите первоначальный вес раствора.'''
    options = random.sample(generate_context('./text_tasks/context.json', 'chemical_solution'), 1)[0]
    while True:
        percent1, percent2 = np.random.randint(10, 90, size=2)
        if (percent1+10) < percent2:
            weight = random.randint(10,100)
            result = weight * (100 - percent2) / (percent2 - percent1)
            if result*10000%10000 == 0:
              answer = int(result)
              break
    task = f'К {percent1}% раствору {choosing_declension_form(options[0])} добавили {weight} г {"чистой" if find_genus_object(options[0]) == 2 else "чистого"} {choosing_declension_form(options[0])}, после чего концентрация раствора стала равна {percent2}%. Найдите первоначальный вес раствора.'
    return {
      "condition": task,
      "answer": answer
    }

def task_9491():
    '''Генерация аналогичных задач № 9491 с портала https://kuzovkin.info/one_exercise_1/9491
    Собрали 100 кг грибов. Оказалось, что их влажность 99%. Когда их подсушили, то влажность снизилась до 98%.
    Какой стала масса этих грибов после того, как их подсушили?'''
    options = random.sample(generate_context('./text_tasks/context.json', 'vegetables'), 1)[0]
    while True:
        percent1, percent2 = np.random.randint(80, 99, size=2)
        weight = random.randint(10,200)
        result = weight * (100 - percent1) / (100 - percent2)
        if percent1 > percent2 and result*10000%10000 == 0:
              answer = int(result)
              break
    task = f'Собрали {weight} кг {choosing_declension_form(options[0].split()[1])}. Оказалось, что {"их" if find_number_object(options[0]) == 2 else "его"} влажность {percent1}%. Когда {"их" if find_number_object(options[0]) == 2 else "его"} подсушили, то влажность снизилась до {percent2}%. Какой стала масса {"этих" if find_number_object(options[0]) == 2 else "этого"} {choosing_declension_form(options[0].split()[1])} после того, как {"их" if find_number_object(options[0]) == 2 else "его"} подсушили?'
    return {
      "condition": task,
      "answer": answer
    }

def task_9495():
    '''Генерация аналогичных задач № 9495 с портала https://kuzovkin.info/one_exercise_1/9495
    Только что добытый каменный уголь содержит 2% воды, а после двухнедельного пребывания на воздухе он содержит 20% воды.
    На сколько кг увеличилась масса добытой тонны угля после того, как он две недели полежал на воздухе?'''
    options = random.sample(generate_context('./text_tasks/context.json', 'mineral'), 1)[0]
    while True:
        percent1, percent2 = np.random.randint(2, 40, size=2)
        weight = random.randint(1000,4999)
        result = weight * (percent2 - percent1) / (100 - percent2)
        if percent1+10 < percent2 and result*10000%10000 == 0:
              answer = int(result)
              break
    task = f'Только что добыт{"ая" if find_genus_object(options[0]) == 2 else "ый"} {options[0]} содержит {percent1}% воды, а после двухнедельного пребывания на воздухе {"она" if find_genus_object(options[0]) == 2 else "он"} содержит {percent2}% {choosing_declension_form(options[1])}. На сколько кг увеличилась масса добытой {weight//1000 if weight > 1000 else ""}{" " if weight > 1000 else ""}тонн{"ы" if weight//1000 in [1,2,3,4] else ""} {weight%1000 if weight%1000 != 0 else ""}{" колограмма " if weight%1000 in [2, 3, 4] else " колограммов " if weight%1000 != 0 else ""}{choosing_declension_form(options[0].split()[1] if len(options[0].split()) > 1 else options[0])} после того, как {"она" if find_genus_object(options[0]) == 2 else "он"} две недели полежал{"а" if find_genus_object(options[0]) == 2 else ""} на воздухе?'
    return {
      "condition": task,
      "answer": answer
    }

def task_9496():
    '''Генерация аналогичных задач № 9496 с портала https://kuzovkin.info/one_exercise_1/9496
    Виноград содержит 91% влаги, а изюм − 7%. Сколько килограммов винограда требуется для получения 21 килограмма изюма?'''
    options = random.sample(generate_context('./text_tasks/context.json', 'vegetables'), 1)[0]
    while True:
        percent1, percent2 = np.random.randint(2, 99, size=2)
        weight = random.randint(1, 30)
        result = weight * (100 - percent2) / (100 - percent1)
        if percent1 > percent2+50 and result*10000%10000 == 0:
              answer = int(result)
              break
    task = f'{"Виноград" if options[0].split()[1] == "виноград" else capitalize_word(options[0])} содерж{"ит" if find_number_object(options[1]) == 1 else "ат"} {percent1}% влаги, а {"изюм" if options[1].split()[1] == "виноград" else options[1]} − {percent2}%. Сколько килограммов {"винограда" if options[0].split()[1] == "виноград" else choosing_declension_form(options[0])} требуется для получения {weight} килограмм{"а" if weight%10 == 1 else "ов"} {"изюма" if options[1].split()[1] == "виноград" else choosing_declension_form(options[1])}?'
    return {
      "condition": task,
      "answer": answer
    }

def task_11036():
    '''Генерация аналогичных задач № 11036 с портала https://kuzovkin.info/one_exercise_1/11036
    Из 38 т сырья второго сорта, содержащего 25% примесей, после очистки получается 30 т сырья первого сорта.
    Каков процент примесей в сырье первого сорта?'''
    options = random.sample(generate_context('./text_tasks/context.json', 'grade'), 1)[0]
    while True:
        weight1, weight2 = np.random.randint(20, 80, size=2)
        if weight1 > weight2:
          percent = random.randint(5, 50)
          result = (weight2 * 100 - weight1 * 100 + weight1 * percent) / weight2
          if result > 0 and result*10000%10000 == 0 and (weight2 * result/100)*1000%100 == 0:
                answer = int(result)
                break
    task = f'Из {weight1} т сырья {options[1]} сорта, содержащего {percent}% примесей, после очистки получается {weight2} т сырья {options[0]} сорта. Каков процент примесей в сырье {options[0]} сорта?'
    return {
      "condition": task,
      "answer": answer
    }

def task_11037():
    '''Генерация аналогичных задач № 11037 с портала https://kuzovkin.info/one_exercise_1/11037
    Сколько килограммов сухарей с влажностью 15% можно получить из 255 кг хлеба с влажностью 45%?'''
    options = random.sample(generate_context('./text_tasks/context.json', 'dried_food'), 1)[0]
    while True:
         percent1, percent2 = np.random.randint(10, 60, size=2)
         if percent1+10 < percent2:
           weight = random.randint(100, 900)
           result = weight * (100 - percent2) / (100 - percent1)
           if result*10000%10000 == 0:
                 answer = int(result)
                 break
    task = f'Сколько килограммов {choosing_declension_form(options[1])} с влажностью {percent1}% можно получить из {weight} кг {choosing_declension_form(options[0])} с влажностью {percent2}%?'
    return {
      "condition": task,
      "answer": answer
    }

def task_11066():
    '''Генерация аналогичных задач № 11066 с портала https://kuzovkin.info/one_exercise_1/11066
    Имеется 200 г сплава, содержащего золото и серебро. Золото составляет 40% сплава.
    Сколько граммов серебра надо добавить к этому сплаву, чтобы новый сплав содержал 80% серебра?'''
    metal_1, metal_2 = random.sample(generate_context('./text_tasks/context.json', 'metals'), 2)
    while True:
         percent1, percent2 = np.random.randint(20, 70, size=2)
         if percent1 + percent2 > 100:
           weight = random.randint(10, 500)
           result = weight * (percent2 + percent1 - 100) / (100 - percent2)
           if result*10000%10000 == 0:
                 answer = int(result)
                 break
    task = f'Имеется {weight} г сплава, содержащего {metal_1} и {metal_2}. {capitalize_word(metal_1)} составляет {percent1}% сплава. Сколько граммов {choosing_declension_form(metal_2)} надо добавить к этому сплаву, чтобы новый сплав содержал {percent2}% {choosing_declension_form(metal_2)}?'
    return {
      "condition": task,
      "answer": answer
    }

def task_11070():
    '''Генерация аналогичных задач № 11070 с портала https://kuzovkin.info/one_exercise_1/11070
    К 5 кг сплава олова и цинка добавили 4 кг олова. Найдите процентное содержание цинка в первоначальном сплаве,
    если в новом сплаве цинка стало в 2 раза меньше, чем олова.'''
    metal_1, metal_2 = random.sample(generate_context('./text_tasks/context.json', 'metals'), 2)
    while True:
      weight1, weight2 = np.random.randint(1, 20, size=2)
      multipl = random.randint(2, 10)
      result = 100 * (weight1 + weight2) / (weight1 + multipl * weight1)
      if result*10000%10000 == 0:
        answer = int(result)
        break
    task = f'К {weight1} кг сплава {choosing_declension_form(metal_1)} и {choosing_declension_form(metal_2)} добавили {weight2} кг {choosing_declension_form(metal_1)}. Найдите процентное содержание {choosing_declension_form(metal_2)} в первоначальном сплаве, если в новом сплаве {choosing_declension_form(metal_2)} стало в {multipl} раза меньше, чем {choosing_declension_form(metal_1)}.'
    return {
      "condition": task,
      "answer": answer
    }

def task_11074():
    '''Генерация аналогичных задач № 11074 с портала https://kuzovkin.info/one_exercise_1/11074
    Собрали 42 кг свежих грибов, содержащих по массе 95% воды. Когда их подсушили, они стали весить 3 кг.
    Каков процент содержания воды по массе в сухих грибах?'''
    options = random.sample(generate_context('./text_tasks/context.json', 'vegetables'), 1)[0]
    while True:
         weight1, weight2 = np.random.randint(1, 70, size=2)
         if weight1 > weight2+20:
           percent = random.randint(60, 97)
           result = (weight1 * (percent - 100) + weight2 * 100) / weight2
           if result > 0 and result*10000%10000 == 0:
                 answer = int(result)
                 break
    task = f'Собрали {weight1} кг {choosing_declension_form(options[0])}, содержащ{"их" if find_number_object(options[0]) == 2 else "его"} по массе {percent}% {choosing_declension_form(options[2])}. Когда {"их" if find_number_object(options[0]) == 2 else "его"} подсушили, {"они" if find_number_object(options[0]) == 2 else "он"} стал{"и" if find_number_object(options[0]) == 2 else ""} весить {weight2} кг. Каков процент содержания {choosing_declension_form(options[2])} по массе в {choosing_declension_form(options[1], "loct")}?'
    return {
      "condition": task,
      "answer": answer
    }

def task_12790():
    '''Генерация аналогичных задач № 12790 с портала https://kuzovkin.info/one_exercise_1/12790
    Морская вода содержит 5% соли. Сколько килограммов пресной воды нужно добавить к 40 кг морской воды,
    чтобы содержание соли в смеси составило 2 %?'''
    options = random.sample(generate_context('./text_tasks/context.json', 'liquids'), 1)[0]
    while True:
        percent1, percent2 = np.random.randint(1, 20, size=2)
        weight = random.randint(1, 50)
        if percent1 > percent2:
            result = weight * (percent1 - percent2) / percent2
            if result * 1000 % 1000 == 0:
              answer = int(result)
              break
    task = f'{capitalize_word(options[0])} содержит {percent1}% {choosing_declension_form(options[1])}. Сколько килограммов {choosing_declension_form(options[2])} нужно добавить к {weight} кг {choosing_declension_form(options[0])}, чтобы содержание {choosing_declension_form(options[1])} в смеси составило {percent2}%?'
    return {
      "condition": task,
      "answer": answer
    }

def task_17644():
    '''Генерация аналогичных задач № 17644 с портала https://kuzovkin.info/one_exercise_1/17644
    Кусок сплава меди и цинка массой 36кг содержит 45% меди. Какую массу меди следует добавить к этому куску,
    чтобы получить сплав, содержащий 60% меди?'''
    metal_1, metal_2 = random.sample(generate_context('./text_tasks/context.json', 'metals'), 2)
    while True:
        percent1, percent2 = np.random.randint(10, 90, size=2)
        weight = random.randint(1, 50)
        if percent1 < percent2:
            result = weight * (percent2 - percent1) / (100 - percent2)
            if result * 1000 % 1000 == 0:
              answer = int(result)
              break
            elif result * 1000 % 100 == 0:
              answer = result
              break
    task = f'Кусок сплава {choosing_declension_form(metal_1)} и {choosing_declension_form(metal_2)} массой {weight}кг содержит {percent1}% {choosing_declension_form(metal_1)}. Какую массу {choosing_declension_form(metal_1)} следует добавить к этому куску, чтобы получить сплав, содержащий {percent2}% {choosing_declension_form(metal_1)}?'
    return {
      "condition": task,
      "answer": answer
    }

def task_17645():
    '''Генерация аналогичных задач № 17645 с портала https://kuzovkin.info/one_exercise_1/17645
    В 2 литра 10-процентного раствора уксусной кислоты добавили 8л чистой воды.
    Определить процентное соотношение уксусной кислоты в полученном растворе.'''
    options = random.sample(generate_context('./text_tasks/context.json', 'chemical_solution'), 1)[0]
    while True:
        weight1, weight2 = np.random.randint(1, 20, size=2)
        percent = random.randint(5, 40)
        if weight1 < weight2:
            result = weight1 * percent / (weight1 + weight2)
            if result * 1000 % 1000 == 0:
              answer = int(result)
              break
    task = f'В {weight1} литр{("а" if weight1 in [2, 3, 4]  else "ов") if weight1 != 1 else "" } {percent}-процентного раствора {choosing_declension_form(options[0])} добавили {weight2}л {choosing_declension_form(options[1])}. Определить процентное соотношение {choosing_declension_form(options[0])} в полученном растворе.'
    return {
      "condition": task,
      "answer": answer
    }
