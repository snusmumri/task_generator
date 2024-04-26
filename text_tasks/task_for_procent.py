from fractions import Fraction
import numpy as np
import random
from math import log
from .utils import choosing_declension_form, capitalize_word, find_number_object, find_genus_object, generate_context, write_numeral_word, fraction_latex_format


def task_642():
    '''Генерация аналогичных задач № 642 с портала https://kuzovkin.info/one_exercise_1/642
    Мельхиор − общее название группы сплавов на основе меди, содержащих никель, железо и марганец.
    В мельхиоре содержится 33% никеля, 1% железа и 1% марганца. Сколько процентов меди содержится в сплаве?'''
    metal, metal_1, metal_2, metal_3 = random.sample(generate_context('./text_tasks/context.json', 'metals'), 4)
    while True:
        number, number1, number2 = np.random.randint(1, 95, size=3)
        result = 100 - (number + number1 + number2)
        if  45 < result < 95 and result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'Группы сплавов на основе {choosing_declension_form(metal)}, содержащих {choosing_declension_form(metal_1)}, {choosing_declension_form(metal_2)} и {choosing_declension_form(metal_3)}. В сплаве содержится {number}% {choosing_declension_form(metal_1, "gent")}, {number1}% {choosing_declension_form(metal_2, "gent")} и {number2}% {choosing_declension_form(metal_3, "gent")}. Сколько процентов {choosing_declension_form(metal, "gent")} содержится в сплаве? '
    return {
      "condition": task,
      "answer": answer
    }



def task_645():
    '''Генерация аналогичных задач № 645 с портала https://kuzovkin.info/one_exercise_1/645
    Воздух состоит из азота (78,09% по объёму), кислорода (20,95%), углекислого газа (0,03%).
    Кроме этих газов, в воздухе содержатся ещё так называемые инертные газы: аргон, неон, гелий, криптон, радон.
    Каково процентное содержание инертных газов в воздухе?'''
    gas, gas_1, gas_2, gas_3, gas_4, gas_5, gas_6, gas_7 = random.sample(generate_context('./text_tasks/context.json', 'gases'), 8)
    while True:
        number, number1, number2 = round(np.random.uniform(1, 95), 2), round(np.random.uniform(1, 95), 2), round(np.random.uniform(1, 95), 2)
        if number * 10 % 10 == 0 or number1 * 10 % 10 == 0 or number2 * 10 % 10 == 0:
          continue
        result = 100 - (number + number1 + number2)
        if  0 < result < 95 and len(str(result)) <= 5 and result * 10 % 10 != 0:
            answer = result
            break
    task = f'Смесь газов состоит из {choosing_declension_form(gas)} ({number}% по объёму), {choosing_declension_form(gas_1)} ({number1}%), {choosing_declension_form(gas_2)} ({number2}%). Кроме этих газов, содержатся ещё: {gas_3}, {gas_4}, {gas_5}, {gas_6}, {gas_7}. Каково процентное содержание этих газов?'
    return {
      "condition": task,
      "answer": answer
    }



def task_930():
    '''Генерация аналогичных задач № 930 с портала https://kuzovkin.info/one_exercise_1/930
    При анализе куска угля весом в 7 г обнаружили, что он содержит 5,2 г углерода, 0,5 г водорода, 0,42 г кислорода,
    0,28 г азота, остальное составляет зола. Определить процентное содержание указанных веществ в угле.'''
    gas, gas_1, gas_2, gas_3 = random.sample(generate_context('./text_tasks/context.json', 'gases'), 4)
    while True:
        number, number1, number2, number3, number4 = round(np.random.uniform(0, 10), 1),  round(np.random.uniform(0, 10), 1), round(np.random.uniform(0, 10), 2), round(np.random.uniform(0, 10), 2), round(np.random.uniform(0, 10), 1)
        result = number + number1 + number2 + number3 + number4

        if  1 < result < 30 and len(str(result)) <= 3:
            ans, ans1, ans2, ans3 = round(number * 100 / result, 2), round(number1 * 100 / result, 2), round(number2 * 100 / result, 2), round(number3 * 100 / result, 2)
            answer = f'{ans}:{ans1}:{ans2}:{ans3}'
            break
    task = f'При анализе вещества весом в {result} г обнаружили, что он содержит {number} г {choosing_declension_form(gas)}, {number1} г {choosing_declension_form(gas_1)}, {number2} г {choosing_declension_form(gas_2)}, {number3} г {choosing_declension_form(gas_3)}, остальное составляет зола. Определить процентное содержание указанных веществ.'
    return {
      "condition": task,
      "answer": answer
    }



def task_1039():
    '''Генерация аналогичных задач № 1039 с портала https://kuzovkin.info/one_exercise_1/1039
    В растворе массой 280 г содержится 56 г соли. Какова концентрация этого раствора?'''
    product = np.random.choice(generate_context('./text_tasks/context.json', 'products'))
    while True:
        number, number1 = np.random.randint(1, 1000, size=2)
        if number <= number1:
          continue
        result = number1 * 100 / number
        if  0 < result < 95 and result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'В растворе массой {number} г содержится {number1} г {choosing_declension_form(product)}. Какова концентрация этого раствора?'
    return {
      "condition": task,
      "answer": answer
    }



def task_1047():
    '''Генерация аналогичных задач № 1047 с портала https://kuzovkin.info/one_exercise_1/1047
    В семенах подсолнечника нового сорта содержится 49,5% масла.
    Сколько килограммов таких семян надо взять, чтобы в них содержалось 29,7 кг масла?'''
    oil = np.random.choice(generate_context('./text_tasks/context.json', 'oils'))
    while True:
        number, number1 = np.random.randint(1, 100, size=2)
        if number <= number1:
          continue
        result = number1 * 100 / number
        if  0 < result < 95 and result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'В семенах {choosing_declension_form(oil)} нового сорта содержится {number}% масла. Сколько килограммов таких семян надо взять, чтобы в них содержалось {number1} кг масла?'
    return {
      "condition": task,
      "answer": answer
    }



def task_611():
    '''Генерация аналогичных задач № 611 с портала https://kuzovkin.info/one_exercise_1/611
    Оптовая цена товара на складе 5500 р. Торговая надбавка в магазине составляет 12%.
    Сколько стоит этот товар в магазине?'''
    while True:
        number, number1 = np.random.randint(100, 100000), np.random.randint(1, 100)
        result = (number / 100 * number1) + number
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'Оптовая цена товара на складе {number} р. Торговая надбавка в магазине составляет {number1}%. Сколько стоит этот товар в магазине?'
    return {
      "condition": task,
      "answer": answer
    }



def task_621():
    '''Генерация аналогичных задач № 621 с портала https://kuzovkin.info/one_exercise_1/621
    Проезд в маршрутке от станции метро Университет до ГЗ МГУ имени М. В. Ломоносова подорожал с 20 рублей до 25 рублей.
    На сколько процентов повысилась цена проезда?'''
    transport = np.random.choice(generate_context('./text_tasks/context.json', 'transports'))
    while True:
        number, number1 = np.random.randint(10, 100, size=2)
        if number >= number1:
          continue
        result = ((number1 - number) / number) * 100
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'Проезд на {choosing_declension_form(transport, "loct")} подорожал с {number} рублей до {number1} рублей. На сколько процентов повысилась цена проезда?'
    return {
      "condition": task,
      "answer": answer
    }


def task_626():
    '''Генерация аналогичных задач № 626 с портала https://kuzovkin.info/one_exercise_1/626
    Цена на товар повысилась на 15% и составила 2944 рубля. Найдите первоначальную цену товара'''
    while True:
        number, number1 = np.random.randint(10, 100), np.random.randint(10, 10000)
        if number >= number1:
          continue
        result = (number1 * 100) / (100 + number)
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'Цена на товар повысилась на {number}% и составила {number1} рубля. Найдите первоначальную цену товара'
    return {
      "condition": task,
      "answer": answer
    }


def task_638():
    '''Генерация аналогичных задач № 638 с портала https://kuzovkin.info/one_exercise_1/638
    В голосовании приняли участие 64,3% электората. Сколько процентов электората не пришли на выборы?'''
    value = np.random.choice(['элеторат', 'жители', 'население'])
    while True:
        number = np.random.randint(1, 100)
        result = 100 - number
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'В голосовании приняли участие {number}% {choosing_declension_form(value)}. Сколько процентов {choosing_declension_form(value)} не пришли на выборы?'
    return {
      "condition": task,
      "answer": answer
    }


def task_647():
    '''Генерация аналогичных задач № 647 с портала https://kuzovkin.info/one_exercise_1/647
    Найдите число, 17% которого на 27 больше 14% его.'''
    while True:
        number, number1, number2 = np.random.randint(1, 90, size=3)
        if number <= number2:
          continue
        result = (number1 / (number - number2)) * 100
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'Найдите число, {number}% которого на {number1} больше {number2}% его.'
    return {
      "condition": task,
      "answer": answer
    }


def task_659():
    '''Генерация аналогичных задач № 659 с портала https://kuzovkin.info/one_exercise_1/659
    Найдите: 140% от 365'''
    while True:
        number, number1 = np.random.randint(1, 1000, size=2)
        result = (number1 * number) / 100
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'Найдите: {number}% от {number1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_661():
    '''Генерация аналогичных задач № 661 с портала https://kuzovkin.info/one_exercise_1/661
    Найдите: 130,5% от 1500'''
    while True:
        number, number1 = round(np.random.uniform(10, 300), 2), np.random.randint(100, 5000)
        if number * 10 % 10 == 0:
          continue
        result = (number1 * number) / 100
        if len(str(result)) <= 5 and result * 10 % 10 != 0:
            answer = result
            break
    task = f'Найдите: {number}% от {number1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_673():
    '''Генерация аналогичных задач № 673 с портала https://kuzovkin.info/one_exercise_1/673
    Найдите: 3,75% от 18,4'''
    while True:
        number, number1 = round(np.random.uniform(10, 300), 2), round(np.random.uniform(10, 300), 2)
        if number * 10 % 10 == 0 or number1 * 10 % 10 == 0:
          continue
        result = (number1 * number) / 100
        if len(str(result)) <= 5 and result * 10 % 10 != 0:
            answer = result
            break
    task = f'Найдите: {number}% от {number1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_682():
    '''Генерация аналогичных задач № 682 с портала https://kuzovkin.info/one_exercise_1/682
    Найдите целое, если 4% равны 28'''
    while True:
        number, number1 = np.random.randint(1, 90, size=2)
        if number == number1:
          continue
        result = (number1 * 100) / number
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'Найдите целое, если {number}% равны {number1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_722():
    '''Генерация аналогичных задач № 722 с портала https://kuzovkin.info/one_exercise_1/722
    Переведите проценты в десятичную дробь: 5,7%'''
    while True:
        number = round(np.random.uniform(1, 100), 2)
        if number * 10 % 10 == 0:
          continue
        result = number / 100
        if len(str(result)) <= 6 and result * 10 % 10 != 0:
            answer = result
            break
    task = f'Переведите проценты в десятичную дробь: {number}%'
    return {
      "condition": task,
      "answer": answer
    }


def task_757():
    '''Генерация аналогичных задач № 757 с портала https://kuzovkin.info/one_exercise_1/757
    Переведите дроби в проценты: 0,004'''
    while True:
        number = round(np.random.uniform(0, 1), 3)
        if number * 10 % 10 == 0:
          continue
        result = number * 100
        if 0 <= result <= 99 and len(str(result)) <= 6 and result * 10 % 10 != 0:
            answer = result
            break
    task = f'Переведите дроби в проценты: {number}'
    return {
      "condition": task,
      "answer": answer
    }


def task_760():
    '''Генерация аналогичных задач № 760 с портала https://kuzovkin.info/one_exercise_1/760
    Переведите дроби в проценты: 0,063'''
    while True:
        number = round(np.random.uniform(0, 1), 3)
        if number * 10 % 10 == 0:
          continue
        result = number * 100
        if 0 <= result <= 99 and len(str(result)) <= 6 and result * 10 % 10 != 0:
            answer = result
            break
    task = f'Переведите дроби в проценты: {number}'
    return {
      "condition": task,
      "answer": answer
    }


def task_763():
    '''Генерация аналогичных задач № 763 с портала https://kuzovkin.info/one_exercise_1/763
    Переведите дроби в проценты: 1,01'''
    while True:
        number = round(np.random.uniform(1, 50), 3)
        if number * 10 % 10 == 0:
          continue
        result = number * 100
        if len(str(result)) <= 5 and result * 10 % 10 != 0:
            answer = result
            break
    task = f'Переведите дроби в проценты: {number}'
    return {
      "condition": task,
      "answer": answer
    }


def task_781():
    '''Генерация аналогичных задач № 781 с портала https://kuzovkin.info/one_exercise_1/781
    Переведите дроби в проценты: 1/3'''
    while True:
        number, number1 = np.random.randint(1, 50, size=2)
        result = (number / number1) * 100
        if len(str(result)) <= 5 and result * 10 % 10 != 0:
            answer = result
            break
    task = f'Переведите дроби в проценты: $\\frac{{{number}}}{{{number1}}}$'
    return {
      "condition": task,
      "answer": answer
    }


def task_794():
    '''Генерация аналогичных задач № 794 с портала https://kuzovkin.info/one_exercise_1/794
    В избирательном округе 25000 избирателей. На выборы пришли 57% избирателей.
    Сколько человек приняли участие в голосовании?'''
    value = np.random.choice(['избиратели', 'люди'])
    while True:
        number, number1 = np.random.randint(1000, 100000), np.random.randint(1, 100)
        result = (number * number1) / 100
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'В избирательном округе {number} {choosing_declension_form(value)}. На выборы пришли {number1}% {choosing_declension_form(value)}. Сколько человек приняли участие в голосовании?'
    return {
      "condition": task,
      "answer": answer
    }


def task_833():
    '''Генерация аналогичных задач № 833 с портала https://kuzovkin.info/one_exercise_1/833
    Мальчик Гриша прочитал в первый день 30% всей книги, во второй − 40% оставшейся части, а в третий − оставшиеся 105 страниц.
    Сколько всего страниц было в книге?'''
    book = np.random.choice(generate_context('./text_tasks/context.json', 'books'))
    name = np.random.choice(['Гриша', 'Коля', 'Ваня'])
    while True:
        number, number1, number2 = np.random.randint(1, 50), np.random.randint(1, 50), np.random.randint(100, 200)
        result = ((((number1 * number2) / (100 - number1) + number2) * number) / (100 - number)) + (number1 * number2) / (100 - number1) + number2
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'Мальчик {name} прочитал в первый день {number}% {choosing_declension_form(book)}, во второй − {number1}% оставшейся части, а в третий − оставшиеся {number2} страниц. Сколько всего страниц было в {choosing_declension_form(book, "loct")}?'
    return {
      "condition": task,
      "answer": answer
    }


def task_851():
    '''Генерация аналогичных задач № 851 с портала https://kuzovkin.info/one_exercise_1/851
    Цена на акцию сначала увеличилась на 1% процент, а потом уменьшилась на 1%.
    На сколько процентов и в какую сторону изменилась цена акции по сравнению с первоначальной?'''
    value = np.random.choice(['акция', 'товар'])
    while True:
        number, number1 = np.random.randint(1, 20, size=2)
        result = ((((100 + number) - ((100 + number) * (number1 / 100))) - 100) / 100) * 100
        if result * 10 % 10 != 0 and len(str(result)) <= 6:
            break
    task = f'Цена на {choosing_declension_form(value, "accs")} сначала увеличилась на {number}% процент, а потом уменьшилась на {number1}%. На сколько процентов и в какую сторону изменилась цена {choosing_declension_form(value)} по сравнению с первоначальной?'
    if result < 0:
        answer = f'уменьшилась на {abs(result)}'
        return {
            "condition": task,
            "answer": answer
        }
    else:
        answer = f'увеличилась на {result}'
        return {
            "condition": task,
            "answer": answer
        }


def task_855():
    '''Генерация аналогичных задач № 855 с портала https://kuzovkin.info/one_exercise_1/855
    Цена на проезд три раза увеличилась на 10%.
    На сколько процентов увеличилась цена по сравнению с первоначальной?'''
    value = np.random.choice(['два', 'четыре', 'три'])
    while True:
        number = np.random.randint(1, 100)

        if value == 'два':
            result = ((1 + (number / 100)) ** 2 - 1) * 100
        elif value == 'четыре':
            result = ((1 + (number / 100)) ** 4 - 1) * 100
        else:
            result = ((1 + (number / 100)) ** 3 - 1) * 100

        if len(str(result)) <= 8:
            break
    task = f'Цена на проезд {value} раза увеличилась на {number}%. На сколько процентов увеличилась цена по сравнению с первоначальной?'
    if result * 10 % 10 == 0:
        answer = int(result)
        return {
            "condition": task,
            "answer": answer
        }
    else:
        answer = result
        return {
            "condition": task,
            "answer": answer
        }


def task_870():
    '''Генерация аналогичных задач № 870 с портала https://kuzovkin.info/one_exercise_1/870
    Акционер компании “Математика Forever” решил уберечь деньги во время финансового кризиса и вложить их в какой-нибудь надёжный банк.
    Он выбрал ММБ − Московский Математический Банк (там работают только математики, так что банк очень надёжный).
    В ММБ есть много видов вкладов, но наш акционер остановил свой выбор на двух.
    А) Вклад на два года, 12% годовых, проценты выплачиваются в конце срока.
    Б) Вклад на два года, 11% годовых, проценты выплачиваются в конце каждого года и причисляются к сумме вклада (капитализация).
    Какую прибыль получит наш акционер, если положит 1000000000 рублей на первый вклад?'''
    value = np.random.choice(['два', 'три', 'четыре'])
    while True:
        number, number1 = np.random.randint(1, 20), np.random.randint(100000, 90000000)
        if number1 % 10000 != 0:
          continue

        if value == 'два':
            result = number1 * (number * 2 / 100)
        elif value == 'четыре':
            result = number1 * (number * 4 / 100)
        else:
            result = number1 * (number * 3 / 100)

        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'Акционер решил уберечь деньги и вложить их в банк. Где вклад на {value} года, {number}% годовых, проценты выплачиваются в конце срока. Какую прибыль получит акционер, если положит {number1} рублей?'
    return {
      "condition": task,
      "answer": answer
    }


def task_918():
    '''Генерация аналогичных задач № 918 с портала https://kuzovkin.info/one_exercise_1/918
    Колхоз засеял овсом 47 га, что составляет 37,6% всего участка, намеченного под овёс.
    Определить размеры этого участка.'''
    value = np.random.choice(['овёс', 'пшеница', 'рожь'])
    while True:
        number, number1 = np.random.randint(1, 100), round(np.random.uniform(1, 95), 2)
        if number1 * 10 % 10 == 0:
          continue
        result = number / (number1  / 100)
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'Колхоз засеял {choosing_declension_form(value, "ablt")} {number} га, что составляет {number1}% всего участка, намеченного под {choosing_declension_form(value, "accs")}. Определить размеры этого участка.'
    return {
      "condition": task,
      "answer": answer
    }


def task_925():
    '''Генерация аналогичных задач № 925 с портала https://kuzovkin.info/one_exercise_1/925
    Военные специалисты считали, что продвижение вперёд с боями на 15 км в сутки является пределом.
    Войска Советской Армии показали невиданно стремительный темп наступления, проходя летом 1944 г. с боями по 25 км в сутки.
    На сколько процентов были превзойдены Советской Армией нормы, считавшиеся предельными?'''
    while True:
        number, number1 = np.random.randint(10, 50, size=2)
        if number1 <= number:
          continue
        result = ((number1 - number) / number) * 100
        if result * 10 % 10 != 0 and len(str(result)) <= 6:
            answer = result
            break
    task = f'Военные специалисты считали, что продвижение вперёд с боями на {number} км в сутки является пределом. Войска показали невиданно стремительный темп наступления с боями по {number1} км в сутки. На сколько процентов были превзойдены войском нормы, считавшиеся предельными?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4465():
    '''Генерация аналогичных задач № 4465 с портала https://kuzovkin.info/one_exercise_1/4465
    120 г золота сплавили с 80 г серебра.
    Найдите концентрацию золота и серебра в полученном сплаве.'''
    metal, metal_1 = random.sample(generate_context('./text_tasks/context.json', 'metals'), 2)
    while True:
        number, number1 = np.random.randint(10, 300), np.random.randint(10, 100)
        result, result1 = (number / (number + number1)) * 100, (number1 / (number + number1)) * 100
        if result * 10 % 10 == 0 and result1 * 10 % 10 == 0 :
            answer = f'{int(result)}:{int(result1)}'
            break
    task = f'{number} г {choosing_declension_form(metal)} сплавили с {number1} г {choosing_declension_form(metal_1)}. Найдите концентрацию {choosing_declension_form(metal)} и {choosing_declension_form(metal_1)} в полученном сплаве.'
    return {
      "condition": task,
      "answer": answer
    }


def task_4468():
    '''Генерация аналогичных задач № 4468 с портала https://kuzovkin.info/one_exercise_1/4468
    Концентрация серной кислоты в растворе составляет 22%.
    Сколько чистой серной кислоты и сколько воды содержится в 150 г раствора?'''
    acid = np.random.choice(generate_context('./text_tasks/context.json', 'acids'))
    while True:
        number, number1 = np.random.randint(1, 95), np.random.randint(10, 500)
        result, result1 = (number / 100) * number1, ((100 - number) / 100) * number1
        if result * 10 % 10 == 0 and result1 * 10 % 10 == 0 :
            answer = f'{int(result)}:{int(result1)}'
            break
    task = f'Концентрация {choosing_declension_form(acid)} кислоты в растворе составляет {number}%. Сколько чистой {choosing_declension_form(acid)} кислоты и сколько воды содержится в {number1} г раствора?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4471():
    '''Генерация аналогичных задач № 4471 с портала https://kuzovkin.info/one_exercise_1/4471
    Сколько воды надо добавить к 30 г соли, чтобы получить пятипроцентный раствор соли?'''
    product = np.random.choice(generate_context('./text_tasks/context.json', 'products'))
    percent = np.random.choice(['пятипроцентный', 'четырехпроцентный', 'десятипроцентный'])
    while True:
        number = np.random.randint(1, 100)

        if percent == 'пятипроцентный':
            result = (number * 100 / 5) - number
        elif percent == 'четырехпроцентный':
            result = (number * 100 / 4) - number
        else:
            result = (number * 100 / 10) - number

        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'Сколько воды надо добавить к {number} г {choosing_declension_form(product)}, чтобы получить {percent} раствор {choosing_declension_form(product)}?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4474():
    '''Генерация аналогичных задач № 4474 с портала https://kuzovkin.info/one_exercise_1/4474
    Сколько соли надо добавить к 190 г воды, чтобы получить пятипроцентный раствор соли?'''
    product = np.random.choice(generate_context('./text_tasks/context.json', 'products'))
    percent = np.random.choice(['пятипроцентный', 'четырехпроцентный', 'десятипроцентный'])
    while True:
        number = np.random.randint(100, 500)

        if percent == 'пятипроцентный':
            result = (5 * number) / (95)
        elif percent == 'четырехпроцентный':
            result = (4 * number) / (96)
        else:
            result = (10 * number) / (90)

        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'Сколько {choosing_declension_form(product)} надо добавить к {number} г воды, чтобы получить {percent} раствор {choosing_declension_form(product)}?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4488():
    '''Генерация аналогичных задач № 4488 с портала https://kuzovkin.info/one_exercise_1/4488
    Стоимость покупки с учётом четырёхпроцентной скидки по дисконтной карте составила 1152 рубля.
    Сколько рублей пришлось бы заплатить за покупку при отсутствии дисконтной карты?'''
    percent = np.random.choice(['пятипроцентной', 'четырёхпроцентной', 'десятипроцентной'])
    value = np.random.choice(['товар', 'покупка', 'продукт'])
    while True:
        number = np.random.randint(1000, 100000)

        if percent == 'пятипроцентной':
            result = number / (95 / 100)
        elif percent == 'четырёхпроцентной':
            result = number / (96 / 100)
        else:
            result = number / (90 / 100)

        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'Стоимость {choosing_declension_form(value)} с учётом {percent} скидки по дисконтной карте составила {number} рубля. Сколько рублей пришлось бы заплатить за {choosing_declension_form(value, "accs")} при отсутствии дисконтной карты?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4497():
    '''Генерация аналогичных задач № 4497 с портала https://kuzovkin.info/one_exercise_1/4497
    В первом квартале доля рынка, занимаемая товарами отечественных производителей, увеличилась с 20% до 25% процентов, а во втором − с 25% до 30%.
    На сколько процентов увеличилась отечественная доля рынка во 2 квартале?'''
    product = np.random.choice(generate_context('./text_tasks/context.json', 'goods'))
    while True:
        number, number1, number2 = np.random.randint(1, 95, size=3)
        if number >= number1 or number1 >= number2:
          continue
        result = number2 - number1
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'В первом квартале доля рынка, занимаемая {choosing_declension_form(product, "ablt")} товарами, увеличилась с {number}% до {number1}% процентов, а во втором − с {number1}% до {number2}%. На сколько процентов увеличилась доля рынка во 2 квартале?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4498():
    '''Генерация аналогичных задач № 4498 с портала https://kuzovkin.info/one_exercise_1/4498
    В первом квартале доля рынка, занимаемая товарами отечественных производителей, увеличилась с 20% до 25% процентов, а во втором − с 25% до 30%.
    В каком квартале увеличение было более значительным(в ответ написать разность процентов между первым и вторым)?'''
    product = np.random.choice(generate_context('./text_tasks/context.json', 'goods'))
    while True:
        number, number1, number2 = np.random.randint(1, 95, size=3)
        if number >= number1 or number1 >= number2:
          continue
        result = (number1 - number) - (number2 - number1)
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'В первом квартале доля рынка, занимаемая {choosing_declension_form(product, "ablt")} товарами, увеличилась с {number}% до {number1}% процентов, а во втором − с {number1}% до {number2}%. В каком квартале увеличение было более значительным(в ответ написать разность процентов между первым и вторым)?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4501():
    '''Генерация аналогичных задач № 4501 с портала https://kuzovkin.info/one_exercise_1/4501
    Кофе при обжаривании теряет 12,5% своего веса.
    Сколько килограммов свежего кофе нужно взять, чтобы получить 42 кг жареного?'''
    product = np.random.choice(['банан', 'виноград', 'абрикос'])
    while True:
        percent = round(np.random.uniform(60, 85), 2)
        number = np.random.randint(1, 100)
        if percent * 10 % 10 == 0:
          continue
        result = number / ((100 - percent) / 100)
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'{product.capitalize()} при сушки теряет {percent}% своего веса. Сколько килограммов {choosing_declension_form(product)} нужно взять, чтобы получить {number} кг сушеного?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4510():
    '''Генерация аналогичных задач № 4510 с портала https://kuzovkin.info/one_exercise_1/4510
    Туристы проехали 50% пути на поезде и 40% пути на автобусе. Какую часть пути осталось пройти туристам?'''
    value = np.random.choice(['люди', 'туристы', 'пассажиры'])
    while True:
        number, number1 = np.random.randint(10, 100, size=2)
        if number + number1 >= 100:
          continue
        result = 100 - (number + number1)
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'{value.capitalize()} проехали {number}% пути на поезде и {number1}% пути на автобусе. Какую часть пути осталось пройти {choosing_declension_form(value, "datv")}?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4512():
    '''Генерация аналогичных задач № 4512 с портала https://kuzovkin.info/one_exercise_1/4512
    Сплав меди, цинка и олова содержит 20% меди и 45% цинка. Сколько в этом сплаве олова?'''
    metal, metal_1, metal_2 = random.sample(generate_context('./text_tasks/context.json', 'metals'), 3)
    while True:
        number, number1 = np.random.randint(10, 100, size=2)
        if number + number1 >= 100:
          continue
        result = 100 - (number + number1)
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'Сплав {choosing_declension_form(metal)}, {choosing_declension_form(metal_1)} и {choosing_declension_form(metal_2)} содержит {number}% {choosing_declension_form(metal)} и {number1}% {choosing_declension_form(metal_1)}. Сколько в этом сплаве {choosing_declension_form(metal_2)}?'
    return {
      "condition": task,
      "answer": answer
    }

def task_4517():
    '''Генерация аналогичных задач № 4517 с портала https://kuzovkin.info/one_exercise_1/4517
    Основным материалом при изготовлении самолётов является сплав дюралюминий (другие названия − дуралюмин, дюраль).
    Дюралюминий − самый прочный сплав среди сплавов на основе алюминия.
    Кроме алюминия, дюралюминий содержит медь (1,4%), магний (0,4%), марганец (1%), кремний (0,5%), цинк (7%), железо (1,8%) и титан (0,35%).
    Сколько в таком сплаве процентов алюминия?'''
    metal, metal_1, metal_2, metal_3, metal_4, metal_5, metal_6, metal_7 = random.sample(generate_context('./text_tasks/context.json', 'metals'), 8)
    while True:
        number, number1, number2, number3, number4, number5, number6 = np.round(np.random.uniform(0, 10, size=7), 2)
        numbers_list = [number, number1, number2, number3, number4, number5 ,number6]
        for i in numbers_list:
          if i * 10 % 10 == 0:
            continue
        result = 100 - (number + number1 + number2 + number3 + number4 + number5 + number6)
        if result * 10 % 10 != 0 and len(str(result)) <= 5:
            answer = result
            break
    task = f'Сплав, кроме {choosing_declension_form(metal)}, содержит {choosing_declension_form(metal_1, "accs")} ({number}%), {choosing_declension_form(metal_2, "accs")} ({number1}%), {choosing_declension_form(metal_3, "accs")} ({number2}%), {choosing_declension_form(metal_4, "accs")} ({number3}%), {choosing_declension_form(metal_5, "accs")} ({number4}%), {choosing_declension_form(metal_6, "accs")} ({number5}%) и {choosing_declension_form(metal_7, "accs")} ({number6}%). Сколько в таком сплаве процентов {choosing_declension_form(metal)}?'
    return {
      "condition": task,
      "answer": answer
    }

def task_4521():
    '''Генерация аналогичных задач № 4521 с портала https://kuzovkin.info/one_exercise_1/4521
    Который теперь час, если остающаяся часть суток равна 60% протекшей части?'''
    while True:
        number = np.random.randint(1, 100)
        total = 86400 / (1 + number / 100)
        if total * 10 % 10 != 0:
          continue
        hours = int(total / 3600)
        minutes = int(total / 60) - (hours * 60)
        seconds = int(total % 60)

        if hours <= 9:
            hours = f'0{hours}'
        if minutes <= 9:
            minutes = f'0{minutes}'
        if seconds <= 9:
            seconds = f'0{seconds}'

        answer = f'{hours}:{minutes}:{seconds}'
        break
    task = f'Который теперь час, если остающаяся часть суток равна {number}% протекшей части?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4526():
    '''Генерация аналогичных задач № 4526 с портала https://kuzovkin.info/one_exercise_1/4526
    Найдите: 34,1% от 1010'''
    while True:
        number, number1 = round(np.random.uniform(1, 99), 2), np.random.randint(1000, 10000)
        if number * 10 % 10 == 0:
          continue
        result = number1 * (number / 100)
        if len(str(result)) <= 5 and result * 10 % 10 != 0:
            answer = result
            break
    task = f'Найдите: {number}% от {number1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_4535():
    '''Генерация аналогичных задач № 4535 с портала https://kuzovkin.info/one_exercise_1/4535
    Найдите: 0,4% от 55'''
    while True:
        number, number1 = round(np.random.uniform(0, 1), 2), np.random.randint(10, 100)
        if number * 10 % 10 == 0:
          continue
        result = number1 * (number / 100)
        if len(str(result)) <= 5 and result * 10 % 10 != 0:
            answer = result
            break
    task = f'Найдите: {number}% от {number1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_4542():
    '''Генерация аналогичных задач № 4542 с портала https://kuzovkin.info/one_exercise_1/4542
    Найдите: 13,4% от 180'''
    while True:
        number, number1 = round(np.random.uniform(10, 99), 2), np.random.randint(100, 1000)
        if number * 10 % 10 == 0:
          continue
        result = number1 * (number / 100)
        if len(str(result)) <= 5 and result * 10 % 10 != 0:
            answer = result
            break
    task = f'Найдите: {number}% от {number1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_4543():
    '''Генерация аналогичных задач № 4543 с портала https://kuzovkin.info/one_exercise_1/4543
    Найдите: 0,5% от 12'''
    while True:
        number, number1 = round(np.random.uniform(0, 1), 2), np.random.randint(1, 100)
        if number * 10 % 10 == 0:
          continue
        result = number1 * (number / 100)
        if len(str(result)) <= 5 and result * 10 % 10 != 0:
            answer = result
            break
    task = f'Найдите: {number}% от {number1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_4547():
    '''Генерация аналогичных задач № 4547 с портала https://kuzovkin.info/one_exercise_1/4547
    Найдите: 9,75% от 540'''
    while True:
        number, number1 = round(np.random.uniform(10, 99), 2), np.random.randint(100, 1000)
        if number * 10 % 10 == 0:
          continue
        result = number1 * (number / 100)
        if len(str(result)) <= 5 and result * 10 % 10 != 0:
            answer = result
            break
    task = f'Найдите: {number}% от {number1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_4551():
    '''Генерация аналогичных задач № 4551 с портала https://kuzovkin.info/one_exercise_1/4551
    Найдите: 7,45% от 56,2'''
    while True:
        number, number1 = np.round(np.random.uniform(1, 99, size=2), 2)
        if number * 10 % 10 == 0 or number1 * 10 % 10 == 0:
          continue
        result = number1 * (number / 100)
        if len(str(result)) <= 5 and result * 10 % 10 != 0:
            answer = result
            break
    task = f'Найдите: {number}% от {number1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_4556():
    '''Генерация аналогичных задач № 4556 с портала https://kuzovkin.info/one_exercise_1/4556
    Найдите целое, если 15% равны 45'''
    while True:
        number, number1 = np.random.randint(10, 99, size=2)
        result = number1 / (number / 100)
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'Найдите целое, если {number}% равны {number1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_4557():
    '''Генерация аналогичных задач № 4557 с портала https://kuzovkin.info/one_exercise_1/4557
    Найдите целое, если 19% равны 57'''
    while True:
        number, number1 = np.random.randint(10, 99, size=2)
        result = number1 / (number / 100)
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'Найдите целое, если {number}% равны {number1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_4559():
    '''Генерация аналогичных задач № 4559 с портала https://kuzovkin.info/one_exercise_1/4559
    Найдите целое, если 35% равны 105'''
    while True:
        number, number1 = np.random.randint(10, 99), np.random.randint(100, 1000)
        result = number1 / (number / 100)
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'Найдите целое, если {number}% равны {number1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_4562():
    '''Генерация аналогичных задач № 4562 с портала https://kuzovkin.info/one_exercise_1/4562
    Найдите целое, если 120% равны 360'''
    while True:
        number, number1 = np.random.randint(100, 1000, size=2)
        result = number1 / (number / 100)
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'Найдите целое, если {number}% равны {number1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_4564():
    '''Генерация аналогичных задач № 4564 с портала https://kuzovkin.info/one_exercise_1/4564
    Найдите целое, если 5% равны 2,5'''
    while True:
        number, number1 = np.random.randint(1, 100), round(np.random.uniform(1, 10), 2)
        if number1 * 10 % 10 == 0:
          continue
        result = number1 / (number / 100)
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'Найдите целое, если {number}% равны {number1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_4565():
    '''Генерация аналогичных задач № 4565 с портала https://kuzovkin.info/one_exercise_1/4565
    Найдите целое, если 7% равны 0,77'''
    while True:
        number, number1 = np.random.randint(1, 100), round(np.random.uniform(0, 1), 2)
        if number1 * 10 % 10 == 0:
          continue
        result = number1 / (number / 100)
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'Найдите целое, если {number}% равны {number1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_4566():
    '''Генерация аналогичных задач № 4566 с портала https://kuzovkin.info/one_exercise_1/4566
    Найдите целое, если 15% равны 6'''
    while True:
        number, number1 = np.random.randint(1, 100, size=2)
        if number == number1:
          continue
        result = number1 / (number / 100)
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'Найдите целое, если {number}% равны {number1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_4568():
    '''Генерация аналогичных задач № 4568 с портала https://kuzovkin.info/one_exercise_1/4568
    Найдите целое, если 18% равны 27'''
    while True:
        number, number1 = np.random.randint(1, 100, size=2)
        if number == number1:
          continue
        result = number1 / (number / 100)
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'Найдите целое, если {number}% равны {number1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_4571():
    '''Генерация аналогичных задач № 4571 с портала https://kuzovkin.info/one_exercise_1/4571
    Найдите целое, если 5,05% равны 161,6'''
    while True:
        number, number1 = round(np.random.uniform(1, 10), 2), round(np.random.uniform(100, 1000), 2)
        if number * 10 % 10 == 0 or number1 * 10 % 10 == 0:
          continue
        result = number1 / (number / 100)
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'Найдите целое, если {number}% равны {number1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_4574():
    '''Генерация аналогичных задач № 4574 с портала https://kuzovkin.info/one_exercise_1/4574
    Найдите целое, если 99,9% равны 25174,8'''
    while True:
        number, number1 = round(np.random.uniform(10, 100), 2), round(np.random.uniform(1000, 100000), 2)
        if number * 10 % 10 == 0 or number1 * 10 % 10 == 0:
          continue
        result = number1 / (number / 100)
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'Найдите целое, если {number}% равны {number1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_4575():
    '''Генерация аналогичных задач № 4575 с портала https://kuzovkin.info/one_exercise_1/4575
    Найдите целое, если 5,7% равны 57'''
    while True:
        number, number1 = round(np.random.uniform(1, 100), 2), np.random.randint(1, 100)
        if number * 10 % 10 == 0:
          continue
        result = number1 / (number / 100)
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'Найдите целое, если {number}% равны {number1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_4576():
    '''Генерация аналогичных задач № 4576 с портала https://kuzovkin.info/one_exercise_1/4576
    Найдите целое, если 5% равны 3 1/3'''
    while True:
        number = np.random.randint(1, 100)
        number1, number2, number3 = np.random.randint(1, 20, size=3)
        if number2 >= number3:
          continue
        fract = number1 + (number2 / number3)
        result = fract / (number / 100)
        if result * 10 % 10 != 0 and len(str(result)) <= 4:
            answer = fraction_latex_format(result)
            break
    task = f'Найдите целое, если {number}% равны ${number1}\\frac{{{number2}}}{{{number3}}}$'
    return {
      "condition": task,
      "answer": answer
    }


def task_4579():
    '''Генерация аналогичных задач № 4579 с портала https://kuzovkin.info/one_exercise_1/4579
    Найдите целое, если 0,2% равны 2'''
    while True:
        number, number1 = round(np.random.uniform(0, 1), 2), np.random.randint(1, 100)
        if number * 10 % 10 == 0:
          continue
        result = number1 / (number / 100)
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'Найдите целое, если {number}% равны {number1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_4581():
    '''Генерация аналогичных задач № 4581 с портала https://kuzovkin.info/one_exercise_1/4581
    Найдите целое, если 0,001% равны 57'''
    while True:
        number, number1 = round(np.random.uniform(0, 1), 4), np.random.randint(1, 100)
        if number * 10 % 10 == 0:
          continue
        result = number1 / (number / 100)
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'Найдите целое, если {number}% равны {number1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_4583():
    '''Генерация аналогичных задач № 4583 с портала https://kuzovkin.info/one_exercise_1/4583
    В библиотеке 98000 книг. Книги на русском языке составляют 78% всех книг, из них 5% − учебники.
    Сколько учебников на русском языке в библиотеке?'''
    value = choosing_declension_form(np.random.choice(generate_context('./text_tasks/context.json', 'books')), "plur")
    if value == "книги":
        value = value = choosing_declension_form(np.random.choice(generate_context('./text_tasks/context.json', 'books')), "plur")
    while True:
        book, percent, percent_1 = np.random.randint(10000, 99999), np.random.randint(45, 80), np.random.randint(1, 20)
        if percent + percent_1 >= 100:
          continue
        result = (((book * percent) / 100) * percent_1) / 100
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'В библиотеке {book} книг. Книги на русском языке составляют {percent}% всех книг, из них {percent_1}% − {value}. Сколько {choosing_declension_form(value)} на русском языке в библиотеке?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4587():
    '''Генерация аналогичных задач № 4587 с портала https://kuzovkin.info/one_exercise_1/4587
    За год число книг в библиотеке увеличилось на 10% и стало равным 8800.
    Сколько книг было в библиотеке в прошлом году?'''
    value = choosing_declension_form(np.random.choice(generate_context('./text_tasks/context.json', 'books')), "plur")
    if value == "книги":
        value = "книг"
    while True:
        book, percent = np.random.randint(1000, 9999), np.random.randint(1, 50)
        result = (book * 100) / (100 + percent)
        if result * 10 % 10 == 0:
            answer = int(result)
            break
    task = f'За год число {choosing_declension_form(value)} в библиотеке увеличилось на {percent}% и стало равным {book}. Сколько {choosing_declension_form(value)} было в библиотеке в прошлом году?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4592():
    '''Генерация аналогичных задач № 4592 с портала https://kuzovkin.info/one_exercise_1/4592
    При перегонке нефти получается 30% керосина и 53% мазута, остальное – потери при переработке.
    Сколько керосина и мазута получится из 64 т нефти?'''
    product, product_1 = random.sample(generate_context('./text_tasks/context.json', 'hydrocarbon_products'), 2)
    while True:
        tone, percent, percent_1 = np.random.randint(10, 100, size=3)
        if percent + percent_1 >= 90:
          continue
        result = (tone * percent) / 100
        result_1 = (tone * percent_1) / 100
        if result * 10 % 10 != 0 and result_1 * 10 % 10 != 0:
            answer = f'{result}:{result_1}'
            break
    task = f'Из вещества получается {percent}% {choosing_declension_form(product)} и {percent_1}% {choosing_declension_form(product_1)}, остальное – потери. Сколько {choosing_declension_form(product)} и {choosing_declension_form(product_1)} получится из {tone} т вещества?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4603():
    '''Генерация аналогичных задач № 4603 с портала https://kuzovkin.info/one_exercise_1/4603
    Переведите проценты в десятичную дробь: 0,009%'''
    while True:
        number = round(np.random.uniform(0, 1), 4)
        if number * 10 % 10 == 0:
          continue
        result = number / 100
        if len(str(result)) <= 6:
            answer = result
            break
    task = f'Переведите проценты в десятичную дробь: {number}'
    return {
      "condition": task,
      "answer": answer
    }


def task_4604():
    '''Генерация аналогичных задач № 4604 с портала https://kuzovkin.info/one_exercise_1/4604
    Переведите проценты в десятичную дробь: 133%'''
    while True:
        number = np.random.randint(100, 1000)
        result = number / 100
        if result % 1 != 0:
            answer = result
            break
    task = f'Переведите проценты в десятичную дробь: {number}%'
    return {
      "condition": task,
      "answer": answer
    }


def task_4607():
    '''Генерация аналогичных задач № 4607 с портала https://kuzovkin.info/one_exercise_1/4607
    Переведите проценты в десятичную дробь: 200%'''
    while True:
        number = np.random.randint(100, 1000)
        result = number / 100
        if result % 1 == 0:
            answer = int(result)
            break
        if result % 1 != 0:
            answer = result
            break
    task = f'Переведите проценты в десятичную дробь: {number}%'
    return {
      "condition": task,
      "answer": answer
    }


def task_4608():
    '''Генерация аналогичных задач № 4608 с портала https://kuzovkin.info/one_exercise_1/4608
    Переведите проценты в десятичную дробь: 1000%'''
    while True:
        number = np.random.randint(1000, 10000)
        result = number / 100
        if result % 1 == 0:
            answer = int(result)
            break
        if result % 1 != 0:
            answer = result
            break
    task = f'Переведите проценты в десятичную дробь: {number}%'
    return {
      "condition": task,
      "answer": answer
    }


def task_4612():
    '''Генерация аналогичных задач № 4612 с портала https://kuzovkin.info/one_exercise_1/4612
    Переведите проценты в десятичную дробь: 33 1/3 %'''
    while True:
        number, number1, number2 = np.random.randint(1, 50, size=3)
        if number1 % number2 == 0 or number1 >= number2:
          continue
        result = (number + (number1 / number2)) / 100
        if result % 1 != 0 and len(str(result)) <= 6:
            answer = result
            break
    task = f'Переведите проценты в десятичную дробь: ${number}\\frac{{{number1}}}{{{number2}}}$%'
    return {
      "condition": task,
      "answer": answer
    }


def task_4615():
    '''Генерация аналогичных задач № 4615 с портала https://kuzovkin.info/one_exercise_1/4615
    Переведите проценты в десятичную дробь: 5/7 %'''
    while True:
        number, number1 = np.random.randint(1, 50, size=2)
        if number % number1 == 0 or number >= number1:
          continue
        result = (number / number1) / 100
        if result % 1 != 0 and len(str(result)) <= 6:
            answer = result
            break
    task = f'Переведите проценты в десятичную дробь: $\\frac{{{number}}}{{{number1}}}$%'
    return {
      "condition": task,
      "answer": answer
    }


def task_4620():
    '''Генерация аналогичных задач № 4620 с портала https://kuzovkin.info/one_exercise_1/4620
    Переведите проценты в десятичную дробь: 8,75%'''
    while True:
        number = round(np.random.uniform(1, 20), 4)
        if number % 1 == 0:
          continue
        result = number / 100
        if result % 1 != 0 and len(str(result)) <= 6:
            answer = result
            break
    task = f'Переведите проценты в десятичную дробь: {number}%'
    return {
      "condition": task,
      "answer": answer
    }


def task_4622():
    '''Генерация аналогичных задач № 4622 с портала https://kuzovkin.info/one_exercise_1/4622
    Переведите проценты в десятичную дробь: 875%'''
    while True:
        number = np.random.randint(100, 1000)
        result = number / 100
        if result % 1 != 0 and len(str(result)) <= 4:
            answer = result
            break
    task = f'Переведите проценты в десятичную дробь: {number}%'
    return {
      "condition": task,
      "answer": answer
    }


def task_4623():
    '''Генерация аналогичных задач № 4623 с портала https://kuzovkin.info/one_exercise_1/4623
    Переведите проценты в десятичную дробь: 0,875%'''
    while True:
        number = round(np.random.uniform(0, 1), 3)
        if number % 1 == 0:
          continue
        result = number / 100
        if result % 1 != 0 and len(str(result)) <= 8:
            answer = result
            break
    task = f'Переведите проценты в десятичную дробь: {number}%'
    return {
      "condition": task,
      "answer": answer
    }


def task_4624():
    '''Генерация аналогичных задач № 4624 с портала https://kuzovkin.info/one_exercise_1/4624
    Переведите дроби в проценты: 0,04'''
    while True:
        number = round(np.random.uniform(0, 1), 3)
        result = number * 100
        if result % 1 != 0 and len(str(result)) <= 5:
            answer = result
            break
        elif result % 1 == 0:
            answer = int(result)
            break
    task = f'Переведите дроби в проценты: {number}'
    return {
      "condition": task,
      "answer": answer
    }


def task_4625():
    '''Генерация аналогичных задач № 4625 с портала https://kuzovkin.info/one_exercise_1/4625
    Переведите дроби в проценты: 0,32'''
    while True:
        number = round(np.random.uniform(0, 1), 3)
        result = number * 100
        if result % 1 != 0 and len(str(result)) <= 5:
            answer = result
            break
        elif result % 1 == 0:
            answer = int(result)
            break
    task = f'Переведите дроби в проценты: {number}'
    return {
      "condition": task,
      "answer": answer
    }


def task_4635():
    '''Генерация аналогичных задач № 4635 с портала https://kuzovkin.info/one_exercise_1/4635
    Переведите дроби в проценты: 1,2234'''
    while True:
        number = round(np.random.uniform(1, 5), 5)
        result = number * 100
        if result % 1 != 0 and len(str(result)) <= 6:
            answer = result
            break
        elif result % 1 == 0:
            answer = int(result)
            break
    task = f'Переведите дроби в проценты: {number}'
    return {
      "condition": task,
      "answer": answer
    }


def task_4639():
    '''Генерация аналогичных задач № 4639 с портала https://kuzovkin.info/one_exercise_1/4639
    Переведите дроби в проценты: 3,57'''
    while True:
        number = round(np.random.uniform(1, 10), 3)
        result = number * 100
        if result % 1 != 0 and len(str(result)) <= 5:
            answer = result
            break
        elif result % 1 == 0:
            answer = int(result)
            break
    task = f'Переведите дроби в проценты: {number}'
    return {
      "condition": task,
      "answer": answer
    }


def task_4647():
    '''Генерация аналогичных задач № 4647 с портала https://kuzovkin.info/one_exercise_1/4647
    Переведите дроби в проценты: 0,0777'''
    while True:
        number = round(np.random.uniform(0, 1), 4)
        result = number * 100
        if result % 1 != 0 and len(str(result)) <= 6:
            answer = result
            break
        elif result % 1 == 0:
            answer = int(result)
            break
    task = f'Переведите дроби в проценты: {number}'
    return {
      "condition": task,
      "answer": answer
    }


def task_4651():
    '''Генерация аналогичных задач № 4651 с портала https://kuzovkin.info/one_exercise_1/4651
    Переведите дроби в проценты: 9/20'''
    while True:
        number, number_1 = np.random.randint(1, 50, size=2)
        if number >= number_1:
            continue
        result = (number / number_1) * 100
        if result % 1 != 0 and len(str(result)) <= 5:
            answer = result
            break
        elif result % 1 == 0:
            answer = int(result)
            break
    task = f'Переведите дроби в проценты: $\\frac{{{number}}}{{{number_1}}}$'
    return {
      "condition": task,
      "answer": answer
    }


def task_4659():
    '''Генерация аналогичных задач № 4659 с портала https://kuzovkin.info/one_exercise_1/4659
    Переведите дроби в проценты: 2/3'''
    while True:
        number, number_1 = np.random.randint(1, 50, size=2)
        if number >= number_1:
            continue
        result = (number / number_1) * 100
        if result % 1 != 0 and len(str(result)) <= 5:
            answer = result
            break
        elif result % 1 == 0:
            answer = int(result)
            break
    task = f'Переведите дроби в проценты: $\\frac{{{number}}}{{{number_1}}}$'
    return {
      "condition": task,
      "answer": answer
    }


def task_4660():
    '''Генерация аналогичных задач № 4660 с портала https://kuzovkin.info/one_exercise_1/4660
    Переведите дроби в проценты: 1/10'''
    while True:
        number, number_1 = np.random.randint(1, 50, size=2)
        if number >= number_1:
            continue
        result = (number / number_1) * 100
        if result % 1 != 0 and len(str(result)) <= 5:
            answer = result
            break
        elif result % 1 == 0:
            answer = int(result)
            break
    task = f'Переведите дроби в проценты: $\\frac{{{number}}}{{{number_1}}}$'
    return {
      "condition": task,
      "answer": answer
    }


def task_4666():
    '''Генерация аналогичных задач № 4666 с портала https://kuzovkin.info/one_exercise_1/4666
    Переведите дроби в проценты: 1/20'''
    while True:
        number, number_1 = np.random.randint(1, 50, size=2)
        if number >= number_1:
            continue
        result = (number / number_1) * 100
        if result % 1 != 0 and len(str(result)) <= 5:
            answer = result
            break
        elif result % 1 == 0:
            answer = int(result)
            break
    task = f'Переведите дроби в проценты: $\\frac{{{number}}}{{{number_1}}}$'
    return {
      "condition": task,
      "answer": answer
    }

def task_4671():
    '''Генерация аналогичных задач № 4671 с портала https://kuzovkin.info/one_exercise_1/4671
    По данным N-ского горкомстата по сравнению с предыдущим годом товарооборот организаций,
    осуществляющих торговую деятельность, увеличился на 53% и составил 902 млн. рублей.
    На какую сумму увеличился товарооборот?'''
    product = np.random.choice(generate_context('./text_tasks/context.json', 'goods'))
    while True:
        percent, money = np.random.randint(1, 100), np.random.randint(100, 1000)
        result = (money / (1 + percent / 100)) * (percent / 100)
        if result % 1 != 0 and len(str(result)) <= 6:
            answer = result
            break
        elif result % 1 == 0:
            answer = int(result)
            break
    task = f'По данным N-ского горкомстата по сравнению с предыдущим годом товарооборот организаций, осуществляющих продажу {choosing_declension_form(product)} товаров, увеличился на {percent}% и составил {money} млн. рублей. На какую сумму увеличился товарооборот?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4674():
    '''Генерация аналогичных задач № 4674 с портала https://kuzovkin.info/one_exercise_1/4674
    Мальчик Гриша прочитал 138 страниц, что составляет 23% числа всех страниц в книге. Сколько страниц в книге?'''
    book = np.random.choice(generate_context('./text_tasks/context.json', 'books'))
    while True:
        percent, pages = np.random.randint(20, 100), np.random.randint(100, 300)
        if pages % 100 // 10 == 1:
            continue
        result = (pages * 100) / percent
        if result % 1 == 0:
            answer = int(result)
            break
    task = f'Мальчик Гриша прочитал {pages} страниц{"у" if pages % 10 == 1 else "ы" if pages % 10 in [2, 3, 4] else ""}, что составляет {percent}% числа всех страниц в {choosing_declension_form(book, "loct")}. Сколько страниц в {choosing_declension_form(book, "loct")}?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4684():
    '''Генерация аналогичных задач № 4684 с портала https://kuzovkin.info/one_exercise_1/4684
    В избирательном округе 25000 избирателей. В голосовании приняли участие 13000 избирателей.
    Какой процент избирателей участвовал в голосовании?'''
    value = np.random.choice(['избирателей', 'человек'])
    while True:
        total, people = np.random.randint(10000, 100000, size=2)
        if people >= total:
            continue
        result = (people * 100) / total
        if result % 1 == 0:
            answer = int(result)
            break
    task = f'В избирательном округе {total} {value}. В голосовании приняли участие {people} {value}. Какой процент {value} участвовал в голосовании?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4685():
    '''Генерация аналогичных задач № 4685 с портала https://kuzovkin.info/one_exercise_1/4685
    Из 30000 жителей города 6900 − дети. Какой процент всего населения составляют дети?'''
    value = np.random.choice(generate_context('./text_tasks/context.json', 'people'))
    while True:
        total, person = np.random.randint(1000, 100000, size=2)
        if person >= total:
            continue
        result = (person * 100) / total
        if result % 1 == 0:
            answer = int(result)
            break
    task = f'Из {total} жителей города {person} − {value}. Какой процент всего населения составляют {value}?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4694():
    '''Генерация аналогичных задач № 4694 с портала https://kuzovkin.info/one_exercise_1/4694
    Имеются два раствора соли массой 80 г и 120 г. В первом растворе содержится 12 г соли, а во втором − 15 г.
    Найдите концентрацию каждого из этих растворов. Найдите концентрацию раствора, полученного при смешивании двух данных растворов.'''
    product = np.random.choice(generate_context('./text_tasks/context.json', 'products'))
    while True:
        weight, weight_1 = np.random.randint(50, 500, size=2)
        gram, gram_1 = np.random.randint(1, 50, size=2)
        result, result_1 = (gram * 100) / weight, (gram_1 * 100) / weight_1
        total_result = ((gram + gram_1) * 100) / (weight + weight_1)
        if len(str(result)) <= 6 and len(str(result_1)) <= 6 and len(str(total_result)) <= 6:
            if result % 1 == 0:
                result = int(result)
            if result_1 % 1 == 0:
                result_1 = int(result_1)
            if total_result % 1 == 0:
                total_result = int(total_result)
                answer = f'{result};{result_1};{total_result}'
                break
    task = f'Имеются два раствора {choosing_declension_form(product)} массой {weight} г и {weight_1} г. В первом растворе содержится {gram} г {choosing_declension_form(product)}, а во втором − {gram_1} г. Найдите концентрацию каждого из этих растворов. Найдите концентрацию раствора, полученного при смешивании двух данных растворов.'
    return {
      "condition": task,
      "answer": answer
    }


def task_4696():
    '''Генерация аналогичных задач № 4696 с портала https://kuzovkin.info/one_exercise_1/4696
    Смешали 200 г 10%-ного сахарного сиропа и 300 г 20%-ного сахарного сиропа. Найдите концентрацию полученной смеси.'''
    taste = np.random.choice(generate_context('./text_tasks/context.json', 'tastes'))
    while True:
        weight, weight_1 = np.random.randint(100, 1000, size=2)
        percent, percent_1 = np.random.randint(10, 50, size=2)
        if percent == percent_1:
            continue
        result = (((weight * (percent / 100) ) + (weight_1 * (percent_1 / 100))) / (weight + weight_1)) * 100
        if result % 1 != 0 and len(str(result)) <= 6:
            answer = result
            break
        elif result % 1 == 0:
            answer = int(result)
            break
    task = f'Смешали {weight} г {percent}%-ного {choosing_declension_form(taste, "ablt")} сиропа и {weight_1} г {percent_1}%-ного {choosing_declension_form(taste, "ablt")} сиропа. Найдите концентрацию полученной смеси'
    return {
      "condition": task,
      "answer": answer
    }


def task_4697():
    '''Генерация аналогичных задач № 4697 с портала https://kuzovkin.info/one_exercise_1/4697
    К 200 г 15%-го раствора вещества добавили 300 г 40%-го раствора того же вещества. Какова концентрация полученной смеси?'''
    while True:
        weight, weight_1 = np.random.randint(100, 1000, size=2)
        percent, percent_1 = np.random.randint(10, 50, size=2)
        if percent == percent_1:
            continue
        result = (((weight * (percent / 100) ) + (weight_1 * (percent_1 / 100))) / (weight + weight_1)) * 100
        if result % 1 != 0 and len(str(result)) <= 6:
            answer = result
            break
        elif result % 1 == 0:
            answer = int(result)
            break
    task = f'К {weight} г {percent}%-го раствора вещества добавили {weight_1} г {percent_1}%-го раствора того же вещества. Какова концентрация полученной смеси?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4698():
    '''Генерация аналогичных задач № 4698 с портала https://kuzovkin.info/one_exercise_1/4698
    К 500 г 12%-го раствора соли добавили 300 г 8%-ного раствора соли. Какова концентрация полученной смеси?'''
    product = np.random.choice(generate_context('./text_tasks/context.json', 'products'))
    while True:
        weight, weight_1 = np.random.randint(100, 1000, size=2)
        percent, percent_1 = np.random.randint(10, 50, size=2)
        if percent == percent_1:
            continue
        result = (((weight * (percent / 100) ) + (weight_1 * (percent_1 / 100))) / (weight + weight_1)) * 100
        if result % 1 != 0 and len(str(result)) <= 6:
            answer = result
            break
        elif result % 1 == 0:
            answer = int(result)
            break
    task = f'К {weight} г {percent}%-го раствора {choosing_declension_form(product)} добавили {weight_1} г {percent_1}%-ного раствора {choosing_declension_form(product)}. Какова концентрация полученной смеси?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4699():
    '''Генерация аналогичных задач № 4699 с портала https://kuzovkin.info/one_exercise_1/4699
    Смешали три раствора некоторого вещества: 500 г 12%-го раствора, 200 г 15%-го раствора и 300 г 6%-го раствора.
    Какова концентрация полученной смеси?'''
    while True:
        weight, weight_1, weight_2 = np.random.randint(100, 1000, size=3)
        percent, percent_1, percent_2 = np.random.randint(10, 50, size=3)
        if percent == percent_1 or percent_1 == percent_2 or percent == percent_2:
            continue
        result = (((weight * (percent / 100) ) + (weight_1 * (percent_1 / 100)) + (weight_2 * (percent_2 / 100))) / (weight + weight_1 + weight_2)) * 100
        if result % 1 != 0 and len(str(result)) <= 6:
            answer = result
            break
        elif result % 1 == 0:
            answer = int(result)
            break
    task = f'Смешали три раствора некоторого вещества: {weight} г {percent}%-го раствора, {weight_1} г {percent_1}%-го раствора и {weight_2} г {percent_2}%-го раствора. Какова концентрация полученной смеси?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4700():
    '''Генерация аналогичных задач № 4700 с портала https://kuzovkin.info/one_exercise_1/4700
    Смешали три раствора некоторого вещества: 200 г однопроцентного раствора, 300 г двухпроцентного раствора и 300 г трёхпроцентного раствора.
    Какова концентрация полученной смеси?'''
    percent, percent_1, percent_2 = random.sample(generate_context('./text_tasks/context.json', 'percents'), 3)
    percent_list = [percent, percent_1, percent_2]
    for i in range(len(percent_list)):
        if percent_list[i] == "однопроцентный":
            percent_list[i] = 1
        elif percent_list[i] == "двухпроцентный":
            percent_list[i] = 2
        elif percent_list[i] == "трехпроцентный":
            percent_list[i] = 3
        elif percent_list[i] == "четырехпроцентный":
            percent_list[i] = 4
        else:
            percent_list[i] = 5
    while True:
        weight, weight_1, weight_2 = np.random.randint(100, 1000, size=3)
        result = ((((weight * percent_list[0]) / 100) + ((weight_1 * percent_list[1]) / 100) + ((weight_2 * percent_list[2]) / 100)) / (weight + weight_1 + weight_2)) * 100
        if result % 1 != 0 and len(str(result)) <= 6:
            answer = result
            break
        elif result % 1 == 0:
            answer = int(result)
            break
    task = f'Смешали три раствора некоторого вещества: {weight} г {choosing_declension_form(percent, "accs")} раствора, {weight_1} г {choosing_declension_form(percent_1, "accs")} раствора и {weight_2} г {choosing_declension_form(percent_2, "accs")} раствора. Какова концентрация полученной смеси?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4702():
    '''Генерация аналогичных задач № 4702 с портала https://kuzovkin.info/one_exercise_1/4702
    На сколько процентов изменится площадь прямоугольника, если одну его сторону увеличить на 10%, а другую − уменьшить на 10%'''
    while True:
        percent, percent_1 = np.random.randint(10, 100, size=2)
        result = ((1 + percent/100) * (1 - percent_1/100) - 1) * 100
        if result % 1 != 0 and len(str(result)) <= 6:
            if result < 0:
                answer = f'уменьшится на {abs(result)}'
                break
            else:
                answer = f'увеличится на {result}'
                break
        elif result % 1 == 0:
            if result < 0:
                answer = f'уменьшится на {int(abs(result))}'
                break
            else:
                answer = f'увеличится на {int(result)}'
                break
    task = f'На сколько процентов изменится площадь прямоугольника, если одну его сторону увеличить на {percent}%, а другую − уменьшить на {percent_1}%'
    return {
      "condition": task,
      "answer": answer
    }


def task_4703():
    '''Генерация аналогичных задач № 4703 с портала https://kuzovkin.info/one_exercise_1/4703
    В первую поездку автомобиль израсходовал 10% бензина, имеющегося в баке, затем во вторую поездку − 25% остатка.
    После этого в баке осталось на 13 л меньше, чем было первоначально. Сколько литров бензина было в баке первоначально?'''
    while True:
        percent, percent_1 = np.random.randint(10, 70, size=2)
        weight = np.random.randint(1, 50)
        result = weight / (((percent_1 / 100) * (1 - percent / 100)) + (percent / 100))
        if result % 1 != 0 and len(str(result)) <= 6:
            answer = result
            break
        elif result % 1 == 0:
            answer = int(result)
            break
    task = f'В первую поездку автомобиль израсходовал {percent}% бензина, имеющегося в баке, затем во вторую поездку − {percent_1}% остатка. После этого в баке осталось на {weight} л меньше, чем было первоначально. Сколько литров бензина было в баке первоначально?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4704():
    '''Генерация аналогичных задач № 4704 с портала https://kuzovkin.info/one_exercise_1/4704
    В библиотеке имеются книги на английском, французском и немецком языках.
    Английские книги составляют 36% всех книг на иностранных языках, французские − 75% английских, а остальные 185 книг − немецкие.
    Сколько книг на иностранных языках в библиотеке?'''
    lang, lang_1, lang_2 = random.sample(generate_context('./text_tasks/context.json', 'language'), 3)
    while True:
        percent, percent_1 = np.random.randint(10, 100, size=2)
        books = np.random.randint(10, 500)
        result = books / (1 - ((percent / 100) + (percent / 100 * percent_1 / 100)))
        if result % 1 == 0 and 0 < result:
            answer = int(result)
            break
    task = f'В библиотеке имеются книги на {choosing_declension_form(lang, "loct")}, {choosing_declension_form(lang_1, "loct")} и {choosing_declension_form(lang_2, "loct")} языках. Книги на {choosing_declension_form(lang, "loct")} составляют {percent}% всех книг на иностранных языках, {lang_1} язык − {percent_1}% книг на {choosing_declension_form(lang, "loct")}, а остальные {books} книги на {choosing_declension_form(lang_2, "loct")}. Сколько книг на иностранных языках в библиотеке?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4714():
    '''Генерация аналогичных задач № 4714 с портала https://kuzovkin.info/one_exercise_1/4714
    Брюки на 20% дешевле пиджака и на 20% дороже рубашки. На сколько процентов пиджак дороже рубашки?'''
    cloth, cloth_1, cloth_2 = random.sample(generate_context('./text_tasks/context.json', 'clothes'), 3)
    while True:
        percent, percent_1 = np.random.randint(10, 100, size=2)
        result = ((1 + percent_1 / 100) / (1 - percent / 100) - 1) * 100
        if result % 1 == 0 and 0 < result < 100:
            answer = int(result)
            break
    task = f'{cloth.capitalize()} на {percent}% дешевле {choosing_declension_form(cloth_1)} и на {percent_1}% дороже {choosing_declension_form(cloth_2)}. На сколько процентов {cloth_1} дороже {choosing_declension_form(cloth_2)}?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4727():
    '''Генерация аналогичных задач № 4727 с портала https://kuzovkin.info/one_exercise_1/4727
    Цена на товар два раза увеличилась на 10%. На сколько процентов увеличилась цена по сравнению с первоначальной?'''
    value = np.random.choice(['два', 'три', 'четыре'])
    while True:
        percent = np.random.randint(1, 100)
        if value == 'два':
            result = ((1 + percent / 100) ** 2 - 1) * 100
        elif value == 'четыре':
            result = ((1 + percent / 100) ** 4 - 1) * 100
        else:
            result = ((1 + percent / 100) ** 3 - 1) * 100

        if result % 1 != 0 and len(str(result)) <= 6:
            answer = result
            break
        elif result % 1 == 0:
            answer = int(result)
            break
    task = f'Цена на товар {value} раза увеличилась на {percent}%. На сколько процентов увеличилась цена по сравнению с первоначальной?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4729():
    '''Генерация аналогичных задач № 4729 с портала https://kuzovkin.info/one_exercise_1/4729
    Население города N в среднем увеличивается на 2% в год. На сколько процентов увеличится население за три года?'''
    value = np.random.choice(['два', 'три', 'четыре'])
    while True:
        percent = np.random.randint(1, 100)
        if value == 'два':
            result = ((1 + percent / 100) ** 2 - 1) * 100
        elif value == 'четыре':
            result = ((1 + percent / 100) ** 4 - 1) * 100
        else:
            result = ((1 + percent / 100) ** 3 - 1) * 100

        if result % 1 != 0 and len(str(result)) <= 6:
            answer = result
            break
        elif result % 1 == 0:
            answer = int(result)
            break
    task = f'Население города N в среднем увеличивается на {percent}% в год. На сколько процентов увеличится население за {value} года?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4732():
    '''Генерация аналогичных задач № 4732 с портала https://kuzovkin.info/one_exercise_1/4732
    В связи с поступлением новой коллекции одежды цена на старую коллекцию снизилась сначала на 10%, а потом ещё на 30%.
    На сколько процентов снизилась цена по сравнению с первоначальной?'''
    while True:
        percent, percent_1 = np.random.randint(10, 100, size=2)
        result = 100 - ((100 - percent) * (100 - percent_1) / 100)
        if result % 1 == 0:
            answer = int(result)
            break
    task = f'В связи с поступлением новой коллекции одежды цена на старую коллекцию снизилась сначала на {percent}%, а потом ещё на {percent_1}%. На сколько процентов снизилась цена по сравнению с первоначальной?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4739():
    '''Генерация аналогичных задач № 4739 с портала https://kuzovkin.info/one_exercise_1/4739
    Вкладчик вложил деньги в банк на 3 года под 20% годовых с капитализацией. На сколько процентов увеличится вклад по итогам трёх лет?'''
    while True:
        percent, year = np.random.randint(10, 100), np.random.randint(3, 10)
        result = ((1 + percent / 100)**year - 1) * 100
        if result % 1 != 0 and len(str(result)) <= 6:
            answer = result
            break
        elif result % 1 == 0:
            answer = int(result)
            break
    task = f'Вкладчик вложил деньги в банк на {year} {"года" if 2 <= year <= 4 else "лет"} под {percent}% годовых с капитализацией. На сколько процентов увеличится вклад по окончанию срока?'
    return {
      "condition": task,
      "answer": answer
    }



def task_4740():
    '''Генерация аналогичных задач № 4740 с портала https://kuzovkin.info/one_exercise_1/4740
    Вкладчик вложил деньги в банк на вклад «До востребования» под 4% годовых.
    За сколько лет сумма вклада увеличится в два раза? При решении данной задачи можете использовать калькулятор.'''
    while True:
        percent = np.random.randint(3, 20)
        result =  -(-log(2) / log(1 + percent / 100) // 1)
        if result % 1 == 0:
            answer = int(result)
            break
    task = f'Вкладчик вложил деньги в банк на вклад «До востребования» под {percent}% годовых. За сколько лет сумма вклада увеличится в два раза?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4744():
    '''Генерация аналогичных задач № 4744 с портала https://kuzovkin.info/one_exercise_1/4744
    Акционер компании “Математика Forever” решил уберечь деньги во время финансового кризиса и вложить их в какой-нибудь надёжный банк.
    Он выбрал ММБ − Московский Математический Банк (там работают только математики, так что банк очень надёжный).
    В ММБ есть много видов вкладов, но наш акционер остановил свой выбор на двух.
    А) Вклад на два года, 12% годовых, проценты выплачиваются в конце срока.
    Б) Вклад на два года, 11% годовых, проценты выплачиваются в конце каждого года и причисляются к сумме вклада (капитализация).
    Какую прибыль получит наш акционер, если положит 1000000000 рублей на второй вклад?'''
    value = np.random.choice(["второй", "первый"])
    while True:
        percent, percent_1 = np.random.randint(10, 20, size=2)
        if percent <= percent_1:
            continue
        money = np.random.randint(100000, 10000000)
        if money % 1000 != 0:
            continue

        if value == "первый":
            result_A = ((money / 100) * percent) * 2
            if result_A % 1 == 0:
                answer = int(result_A)
                break
        else:
            result_B = money * (1 + percent_1 / 100) ** 2 - money
            if result_B % 1 == 0:
                answer = int(result_B)
                break

    task = f'Акционер компании решил вложить деньги в банк. В банке есть много видов вкладов, но акционер остановил свой выбор на двух. А) Вклад на два года, {percent}% годовых, проценты выплачиваются в конце срока. Б) Вклад на два года, {percent_1}% годовых, проценты выплачиваются в конце каждого года и причисляются к сумме вклада (капитализация). Какую прибыль получит наш акционер, если положит {money} рублей на {value} вклад?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4760():
    '''Генерация аналогичных задач № 4760 с портала https://kuzovkin.info/one_exercise_1/4760
    В течение года завод дважды увеличивал выпуск продукции на одно и то же число процентов.
    Найдите это число процентов, если известно, что в начале года завод ежемесячно выпускал 600 изделий, а в конце года стал ежемесячно выпускать 726 изделий.'''
    thing = np.random.choice(generate_context('./text_tasks/context.json', 'things'))
    while True:
        number, number_1 =  np.random.randint(100, 10000, size=2)
        if number >= number_1:
            continue
        result = ((number_1 / number) ** 0.5 - 1) * 100
        if result % 1 != 0 and len(str(result)) <= 6 and result < 100:
            answer = result
            break
        elif result % 1 == 0 and result < 100:
            answer = int(result)
            break
    task = f'В течение года завод дважды увеличивал выпуск {choosing_declension_form(thing)} на одно и то же число процентов. Найдите это число процентов, если известно, что в начале года завод ежемесячно выпускал {number} изделий, а в конце года стал ежемесячно выпускать {number_1} изделий.'
    return {
      "condition": task,
      "answer": answer
    }


def task_4761():
    '''Генерация аналогичных задач № 4761 с портала https://kuzovkin.info/one_exercise_1/4761
    Цена на товар снижена на 40%, а зарплата дважды увеличивалась на 20%.
    На сколько процентов больше можно купить товара после снижения цен и повышения зарплаты?'''
    thing = np.random.choice(generate_context('./text_tasks/context.json', 'things'))
    while True:
        percent, percent_1 = np.random.randint(10, 100, size=2)
        result = 100 * (1 + percent_1 / 100) ** 2 / (1 - percent / 100) - 100
        if result % 1 != 0 and len(str(result)) <= 6:
            answer = result
            break
        elif result % 1 == 0:
            answer = int(result)
            break
    task = f'Цена на {choosing_declension_form(thing, "accs")} снижена на {percent}%, а зарплата дважды увеличивалась на {percent_1}%. На сколько процентов больше можно купить {choosing_declension_form(thing)} после снижения цен и повышения зарплаты?'
    return {
      "condition": task,
      "answer": answer
    }



def task_4790():
    '''Генерация аналогичных задач № 4790 с портала https://kuzovkin.info/one_exercise_1/4790
    За досрочное выполнение пахоты правление колхоза постановило премировать бригаду в размере 20% от числа выработанных трудодней.
    Сколько трудодней надо прибавить колхознику, который выработал по наряду 17,2 трудодня?'''
    while True:
        percent, days = np.random.randint(10, 100), round(np.random.uniform(1, 30), 1)
        if days % 1 == 0:
            days = int(days)
        result = days * percent / 100
        if result % 1 != 0 and len(str(result)) <= 5:
            answer = result
            break
        elif result % 1 == 0:
            answer = int(result)
            break
    task = f'За досрочное выполнение пахоты правление колхоза постановило премировать бригаду в размере {percent}% от числа выработанных трудодней. Сколько трудодней надо прибавить колхознику, который выработал по наряду {days} трудодня?'
    return {
      "condition": task,
      "answer": answer
    }


def task_4792():
    '''Генерация аналогичных задач № 4792 с портала https://kuzovkin.info/one_exercise_1/4792
    2/5 вражеских танков, участвовавших в бою, было уничтожено нашей штурмовой авиацией;
    42 танка было уничтожено нашей противотанковой артиллерией; 22,5% вражеских танков было повреждено связками гранат;
    остальные 18 вражеских танков повернули обратно. Определить: сколько вражеских танков было выведено из строя в этом бою?
    Какой процент составляют танки, уничтоженные нашей штурмовой авиацией? противотанковой артиллерией? связками гранат?'''
    while True:
        enemy_t, enemy_t_1 = np.random.randint(1, 20, size=2)
        if enemy_t >= enemy_t_1:
            continue
        percent, go_t, destroy_t = round(np.random.uniform(1, 100), 1), np.random.randint(10, 100) , np.random.randint(10, 100)
        if percent % 1 == 0:
            percent = int(percent)
        all_t =(go_t + destroy_t) / (1 - ((enemy_t / enemy_t_1) + (percent / 100)))
        result_1 = (enemy_t / enemy_t_1) * 100
        result_2 = destroy_t / all_t * 100
        result_3 = go_t / all_t * 100
        if len(str(result_1)) <= 6 and result_1 > 0 and len(str(result_2)) <= 6 and result_2 > 0 and len(str(result_3)) <= 6 and result_3 > 0:
            if result_1 % 1 == 0:
                result_1 = int(result_1)
            else:
                result_1 = result_1
            if result_2 % 1 == 0:
                result_2 = int(result_2)
            else:
                result_2 = result_2
            if result_3 % 1 == 0:
                result_3 = int(result_3)
            else:
                result_3 = result_3
                answer = f'{result_1};{result_2};{result_3}'
                break
    task = f'$\\frac{{{enemy_t}}}{{{enemy_t_1}}}$ вражеских танков, участвовавших в бою, было уничтожено нашей штурмовой авиацией; {destroy_t} танка было уничтожено нашей противотанковой артиллерией; {percent}% вражеских танков было повреждено связками гранат; остальные {go_t} вражеских танков повернули обратно. Определить: какой процент составляют танки, уничтоженные нашей штурмовой авиацией? противотанковой артиллерией? повернули обратно?'
    return {
      "condition": task,
      "answer": answer
    }


def task_8337():
    '''Генерация аналогичных задач № 8337 с портала https://kuzovkin.info/one_exercise_1/8337
    Килограмм соли растворили в 10 л воды. Какова концентрация полученного раствора? Известно, что масса одного литра воды равна 1 кг.'''
    product = np.random.choice(generate_context('./text_tasks/context.json', 'products'))
    while True:
        weight, weight_1 = np.random.randint(1, 100, size=2)
        if weight >= weight_1:
            continue
        result = (weight / (weight + weight_1)) * 100
        if result % 1 != 0 and len(str(result)) <= 6:
            answer = result
            break
        elif result % 1 == 0:
            answer = int(result)
            break
    task = f'{weight} кг {choosing_declension_form(product)} растворили в {weight_1} л воды. Какова концентрация полученного раствора? Известно, что масса одного литра воды равна 1 кг.'
    return {
      "condition": task,
      "answer": answer
    }


def task_8351():
    '''Генерация аналогичных задач № 8351 с портала https://kuzovkin.info/one_exercise_1/8351
    Сколько чистого спирта надо добавить к 276 г воды, чтобы получить восьмипроцентный раствор спирта?'''
    product = np.random.choice(generate_context('./text_tasks/context.json', 'products'))
    percent = np.random.choice(["восьмипроцентный", "двенадцатипроцентный", "пятнадцатипроцентный"])
    while True:
        weight = np.random.randint(100, 1000)
        if percent == "восьмипроцентный":
            result = (weight * 8) / (100 - 8)
        elif percent == "двенадцатипроцентный":
            result = (weight * 12) / (100 - 12)
        else:
            result = (weight * 15) / (100 - 15)
        if result % 1 == 0:
            answer = int(result)
            break
    task = f'Сколько {choosing_declension_form(product)} надо добавить к {weight} г воды, чтобы получить {percent} раствор {choosing_declension_form(product)}?'
    return {
      "condition": task,
      "answer": answer
    }


def task_8364():
    '''Генерация аналогичных задач № 8364 с портала https://kuzovkin.info/one_exercise_1/8364
    Вкладчик положил в банк некоторую сумму под 8,5% годовых. Через год проценты по вкладу составили 2720 евро. Какую сумму вкладчик положил в банк?'''
    currency = np.random.choice(["eвро", "рублей", "долларов"])
    while True:
        percent, money = round(np.random.randint(5, 15), 1), np.random.randint(1000, 100000)
        if money % 100 != 0:
            continue
        if percent % 1 == 0:
            percent = int(percent)
        result = money / (percent / 100)
        if result % 1 == 0:
            answer = int(result)
            break
    task = f'Вкладчик положил в банк некоторую сумму под {percent}% годовых. Через год проценты по вкладу составили {money} {currency}. Какую сумму вкладчик положил в банк?'
    return {
      "condition": task,
      "answer": answer
    }


def task_8370():
    '''Генерация аналогичных задач № 8370 с портала https://kuzovkin.info/one_exercise_1/8370
    Предприниматель взял в банке кредит в размере 1200000 рублей под 15,5% годовых. Какую сумму он должен вернуть банку через год?'''
    currency = np.random.choice(["eвро", "рублей", "долларов"])
    while True:
        percent, money = round(np.random.randint(10, 20), 1), np.random.randint(1000000, 10000000)
        if percent % 1 == 0:
            percent = int(percent)
        if money % 10000 != 0:
            continue
        result = money * (1 + percent / 100)
        if result % 1 == 0:
            answer = int(result)
            break
    task = f'Предприниматель взял в банке кредит в размере {money} {currency} под {percent}% годовых. Какую сумму он должен вернуть банку через год?'
    return {
      "condition": task,
      "answer": answer
    }


def task_8386():
    '''Генерация аналогичных задач № 8386 с портала https://kuzovkin.info/one_exercise_1/8386
    Найдите целое, если 231% равны 2079'''
    while True:
        number, number_1 = np.random.randint(100, 1000), np.random.randint(1000, 10000)
        result = number_1 / (number / 100)
        if result % 1 == 0:
            answer = int(result)
            break
    task = f'Найдите целое, если {number}% равны {number_1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_8388():
    '''Генерация аналогичных задач № 8388 с портала https://kuzovkin.info/one_exercise_1/8388
    Товар стоит 2000 рублей. Цена на товар увеличилась сначала на 10%, а потом ещё на 20% от новой цены.
    На сколько процентов увеличилась цена товара по сравнению с первоначальной?'''
    thing = np.random.choice(generate_context('./text_tasks/context.json', 'things'))
    while True:
        percent, percent_1 = np.random.randint(1, 100, size=2)
        money = np.random.randint(1000, 10000)
        if money % 100 != 0:
            continue
        result = (((money * (1 + percent / 100)) * (1 + percent_1 / 100)) - money) / money * 100
        if result % 1 == 0:
            answer = int(result)
            break
    task = f'Товар стоит {money} рублей. Цена на {choosing_declension_form(thing, "accs")} увеличилась сначала на {percent}%, а потом ещё на {percent_1}% от новой цены. На сколько процентов увеличилась цена {choosing_declension_form(thing)} по сравнению с первоначальной?'
    return {
      "condition": task,
      "answer": answer
    }


def task_8393():
    '''Генерация аналогичных задач № 8393 с портала https://kuzovkin.info/one_exercise_1/8393
    Бронза − это сплав меди с оловом.
    Монетная бронза содержит 3,9% олова, оружейная бронза − 10,2% олова, а колокольная бронза содержит 22,4% олова.
    В каждом случае определите, сколько процентов меди содержится в сплаве.'''
    metal, metal_1 = random.sample(generate_context('./text_tasks/context.json', 'metals'), 2)
    while True:
        percent, percent_1, percent_2 = np.round(np.random.uniform(1, 100, size=3), 1)
        result, result_1, result_2 = 100 - percent, 100 - percent_1, 100 - percent_2
        if result % 1 != 0 and len(str(result)) <= 6 and len(str(result_1)) <= 6 and len(str(result_2)) <= 6:
            answer = f'{result};{result_1};{result_2}'
            break
    task = f'Композит − это сплав {choosing_declension_form(metal)} с {choosing_declension_form(metal_1, "ablt")}. Первый композит содержит {percent}% {choosing_declension_form(metal_1)}, второй композит − {percent_1}% {choosing_declension_form(metal_1)}, а третий композит содержит {percent_2}% {choosing_declension_form(metal_1)}. В каждом случае определите, сколько процентов {choosing_declension_form(metal)} содержится в сплаве.'
    return {
      "condition": task,
      "answer": answer
    }


def task_8395():
    '''Генерация аналогичных задач № 8395 с портала https://kuzovkin.info/one_exercise_1/8395
    Нихром − общее название группы сплавов на основе никеля, содержащих хром, алюминий, кремний, а также микродобавки редкоземельных элементов (лантан, церий, самарий и др.)
    Такие сплавы обладают высокой жаростойкостью в сочетании с высоким электрическим сопротивлением.
    Нихром содержит 20% никеля, 3,5% алюминия, 1,5% кремния и 0,1% РЗЭ. Сколько процентов хрома содержится в таком сплаве?'''
    metal, metal_1, metal_2, metal_3 = random.sample(generate_context('./text_tasks/context.json', 'metals'), 4)
    while True:
        percent, percent_1, percent_2 = np.round(np.random.uniform(1, 100, size=3), 1)
        if percent % 1 == 0 or percent_1 == 0 or percent_2 == 0:
            continue
        other_perc = np.round(np.random.uniform(0, 1), 2)
        if percent + percent_1 + percent_2 + other_perc >= 100 or percent < 20:
            continue
        result = 100 - (percent + percent_1 + percent_2 + other_perc)
        if result % 1 != 0 and len(str(result)) <= 6:
            answer = result
            break
    task = f'Группа сплавов на основе {choosing_declension_form(metal)}, содержащих {metal_1}, {metal_2}, {metal_3}, а также микродобавки редкоземельных элементов (лантан, церий, самарий и др.) Сплав содержит {percent}% {choosing_declension_form(metal)}, {percent_1}% {choosing_declension_form(metal_2)}, {percent_2}% {choosing_declension_form(metal_3)} и {other_perc}% РЗЭ. Сколько процентов {choosing_declension_form(metal_1)} содержится в таком сплаве?'
    return {
      "condition": task,
      "answer": answer
    }


def task_8398():
    '''Генерация аналогичных задач № 8398 с портала https://kuzovkin.info/one_exercise_1/8398
    Найдите число, если известно, что после прибавления к нему 12% его получится 420.'''
    while True:
        number, number_1 = np.random.randint(1, 100), np.random.randint(100, 1000)
        result = number_1 / (1 + number / 100)
        if result % 1 == 0:
            answer = int(result)
            break
    task = f'Найдите число, если известно, что после прибавления к нему {number}% его получится {number_1}.'
    return {
      "condition": task,
      "answer": answer
    }


def task_8402():
    '''Генерация аналогичных задач № 8402 с портала https://kuzovkin.info/one_exercise_1/8402
    Найдите: 23% от 4,5'''
    while True:
        number, number_1 = np.random.randint(1, 100), round(np.random.uniform(1, 99), 1)
        if number_1 % 1 == 0:
            continue
        result = number_1 * (number / 100)
        if result % 1 != 0 and len(str(result)) <= 8:
            answer = result
            break
    task = f'Найдите: {number}% от {number_1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_8404():
    '''Генерация аналогичных задач № 8404 с портала https://kuzovkin.info/one_exercise_1/8404
    Найдите: 58% от 22,3'''
    while True:
        number, number_1 = np.random.randint(1, 100), round(np.random.uniform(1, 99), 1)
        if number_1 % 1 == 0:
            continue
        result = number_1 * (number / 100)
        if result % 1 != 0 and len(str(result)) <= 8:
            answer = result
            break
    task = f'Найдите: {number}% от {number_1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_8406():
    '''Генерация аналогичных задач № 8406 с портала https://kuzovkin.info/one_exercise_1/8406
    Найдите: 9,2% от 4,5'''
    while True:
        number, number_1 = np.round(np.random.uniform(1, 100, size=2), 1)
        if number % 1 == 0 or number_1 % 1 == 0:
            continue
        result = number_1 * (number / 100)
        if result % 1 != 0 and len(str(result)) <= 8:
            answer = result
            break
    task = f'Найдите: {number}% от {number_1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_8407():
    '''Генерация аналогичных задач № 8407 с портала https://kuzovkin.info/one_exercise_1/8407
    Найдите: 20% от 45,5'''
    while True:
        number, number_1 = np.random.randint(1, 100), round(np.random.uniform(1, 99), 1)
        if number_1 % 1 == 0:
            continue
        result = number_1 * (number / 100)
        if result % 1 != 0 and len(str(result)) <= 8:
            answer = result
            break
    task = f'Найдите: {number}% от {number_1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_8408():
    '''Генерация аналогичных задач № 8408 с портала https://kuzovkin.info/one_exercise_1/8408
    Найдите: 45% от 340'''
    while True:
        number, number_1 = np.random.randint(1, 100), np.random.randint(100, 1000)
        result = number_1 * (number / 100)
        if result % 1 == 0:
            answer = int(result)
            break
    task = f'Найдите: {number}% от {number_1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_8409():
    '''Генерация аналогичных задач № 8409 с портала https://kuzovkin.info/one_exercise_1/8409
    Найдите: 23,87% от 550'''
    while True:
        number, number_1 = round(np.random.uniform(1, 100), 2), np.random.randint(100, 1000)
        if number % 1 == 0:
            continue
        result = number_1 * (number / 100)
        if result % 1 != 0 and len(str(result)) <= 8:
            answer = result
            break
    task = f'Найдите: {number}% от {number_1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_8410():
    '''Генерация аналогичных задач № 8410 с портала https://kuzovkin.info/one_exercise_1/8410
    Найдите: 1,034% от 320'''
    while True:
        number, number_1 = round(np.random.uniform(1, 10), 3), np.random.randint(100, 1000)
        if number % 1 == 0:
            continue
        result = number_1 * (number / 100)
        if result % 1 != 0 and len(str(result)) <= 8:
            answer = result
            break
    task = f'Найдите: {number}% от {number_1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_8412():
    '''Генерация аналогичных задач № 8412 с портала https://kuzovkin.info/one_exercise_1/8412
    Найдите: 150% от 342'''
    while True:
        number, number_1 = np.random.randint(100, 1000, size=2)
        if number % 100 == 0:
            continue
        result = number_1 * (number / 100)
        if result % 1 == 0:
            answer = int(result)
            break
    task = f'Найдите: {number}% от {number_1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_8416():
    '''Генерация аналогичных задач № 8416 с портала https://kuzovkin.info/one_exercise_1/8416
    Найдите: 100,01% от 200'''
    while True:
        number, number_1 = round(np.random.uniform(100, 1000), 2), np.random.randint(100, 1000)
        if number % 1 == 0:
            continue
        result = number_1 * (number / 100)
        if result % 1 != 0 and len(str(result)) <= 6:
            answer = result
            break
        elif result % 1 == 0:
            answer = int(result)
            break
    task = f'Найдите: {number}% от {number_1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_8419():
    '''Генерация аналогичных задач № 8419 с портала https://kuzovkin.info/one_exercise_1/8419
    Найдите: 8% от 1250'''
    while True:
        number, number_1 = np.random.randint(1, 100), np.random.randint(1000, 10000)
        if number % 1000 == 0:
            continue
        result = number_1 * (number / 100)
        if result % 1 != 0 and len(str(result)) <= 6:
            answer = result
            break
        elif result % 1 == 0:
            answer = int(result)
            break
    task = f'Найдите: {number}% от {number_1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_8433():
    '''Генерация аналогичных задач № 8433 с портала https://kuzovkin.info/one_exercise_1/8433
    Найдите целое, если 3% равны 15'''
    while True:
        number, number1 = np.random.randint(1, 100, size=2)
        if number == number1:
          continue
        result = number1 / (number / 100)
        if result % 1 == 0:
            answer = int(result)
            break
    task = f'Найдите целое, если {number}% равны {number1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_8437():
    '''Генерация аналогичных задач № 8437 с портала https://kuzovkin.info/one_exercise_1/8437
    Найдите целое, если 20% равны 140'''
    while True:
        number, number1 = np.random.randint(1, 100), np.random.randint(100, 1000)
        result = number1 / (number / 100)
        if result % 1 == 0:
            answer = int(result)
            break
    task = f'Найдите целое, если {number}% равны {number1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_8445():
    '''Генерация аналогичных задач № 8445 с портала https://kuzovkin.info/one_exercise_1/8445
    Найдите целое, если 9,9% равны 396'''
    while True:
        number, number1 = round(np.random.uniform(1, 100),2), np.random.randint(100, 1000)
        if number % 1 == 0:
            continue
        result = number1 / (number / 100)
        if result % 1 != 0 and len(str(result)) <= 6:
            answer = result
            break
        elif result % 1 == 0:
            answer = int(result)
            break
    task = f'Найдите целое, если {number}% равны {number1}'
    return {
      "condition": task,
      "answer": answer
    }


def task_8450():
    '''Генерация аналогичных задач № 8450 с портала https://kuzovkin.info/one_exercise_1/8450
    Найдите целое, если 2 2/3 % равны 16'''
    while True:
        number, number1, number2 = np.random.randint(1, 20, size=3)
        number3 = np.random.randint(1, 100)
        if number1 >= number2:
          continue
        fract = number + (number1 / number2)
        result = number3 / (fract / 100)
        if result % 1 != 0 and len(str(result)) <= 6:
            answer = fraction_latex_format(result)
            break
    task = f'Найдите целое, если ${number}\\frac{{{number1}}}{{{number2}}}$% равны {number3}'
    return {
      "condition": task,
      "answer": answer
    }


def task_8451():
    '''Генерация аналогичных задач № 8451 с портала https://kuzovkin.info/one_exercise_1/8451
    Найдите целое, если 14 1/7 % равны 7 8/13'''
    while True:
        number, number1, number2 = np.random.randint(1, 20, size=3)
        number3, number4, number5 = np.random.randint(1, 20, size=3)
        if number1 >= number2 or number4 >= number5:
          continue
        fract = number + (number1 / number2)
        fract1 = number3 + (number4 / number5)
        result = fract1 / (fract / 100)
        if result % 1 != 0 and len(str(result)) <= 6:
            answer = fraction_latex_format(result)
            break
    task = f'Найдите целое, если ${number}\\frac{{{number1}}}{{{number2}}}$% равны ${number3}\\frac{{{number4}}}{{{number5}}}$'
    return {
      "condition": task,
      "answer": answer
    }


def task_8462():
    '''Генерация аналогичных задач № 8462 с портала https://kuzovkin.info/one_exercise_1/8462
    В библиотеке 20000 книг, из них 1500 книг – это словари для перевода с одного языка на другой,
    из них 75 книг – это англо-русские и русско-английские словари.
    Сколько процентов от всех книг в библиотеке составляют словари?'''
    while True:
        book, book_1, book_2 = np.random.randint(10000, 50000), np.random.randint(1000, 10000), np.random.randint(50, 1000)
        result = (book_1 / book) * 100
        if result % 1 != 0 and len(str(result)) <= 6:
            answer = result
            break
        elif result % 1 == 0:
            answer = int(result)
            break
    task = f'В библиотеке {book} книг, из них {book_1} книг – это словари для перевода с одного языка на другой, из них {book_2} книг – это англо-русские и русско-английские словари. Сколько процентов от всех книг в библиотеке составляют словари?'
    return {
      "condition": task,
      "answer": answer
    }


def task_8469():
    '''Генерация аналогичных задач № 8469 с портала https://kuzovkin.info/one_exercise_1/8469
    Переведите проценты в десятичную дробь: 2%'''
    while True:
        number = np.random.randint(1, 100)
        result = number / 100
        if len(str(result)) <= 6:
            answer = result
            break
    task = f'Переведите проценты в десятичную дробь: {number}%'
    return {
      "condition": task,
      "answer": answer
    }


def task_8470():
    '''Генерация аналогичных задач № 8470 с портала https://kuzovkin.info/one_exercise_1/8470
    Переведите проценты в десятичную дробь: 75%'''
    while True:
        number = np.random.randint(1, 100)
        result = number / 100
        if len(str(result)) <= 6:
            answer = result
            break
    task = f'Переведите проценты в десятичную дробь: {number}%'
    return {
      "condition": task,
      "answer": answer
    }


def task_8473():
    '''Генерация аналогичных задач № 8473 с портала https://kuzovkin.info/one_exercise_1/8473
    Переведите проценты в десятичную дробь: 1,7%'''
    while True:
        number = round(np.random.uniform(0,10),1)
        if number % 1 == 0:
            continue
        result = number / 100
        if len(str(result)) <= 6:
            answer = result
            break
    task = f'Переведите проценты в десятичную дробь: {number}%'
    return {
      "condition": task,
      "answer": answer
    }


def task_8475():
    '''Генерация аналогичных задач № 8475 с портала https://kuzovkin.info/one_exercise_1/8475
    Переведите проценты в десятичную дробь: 0,03%'''
    while True:
        number = round(np.random.uniform(0,1),2)
        if number % 1 == 0:
            continue
        result = number / 100
        if len(str(result)) <= 6:
            answer = result
            break
    task = f'Переведите проценты в десятичную дробь: {number}%'
    return {
      "condition": task,
      "answer": answer
    }


def task_8484():
    '''Генерация аналогичных задач № 8484 с портала https://kuzovkin.info/one_exercise_1/8484
    Переведите проценты в десятичную дробь: 0,03%'''
    while True:
        number = round(np.random.uniform(100,1000),1)
        if number % 1 == 0:
            continue
        result = number / 100
        if len(str(result)) <= 6:
            answer = result
            break
    task = f'Переведите проценты в десятичную дробь: {number}%'
    return {
      "condition": task,
      "answer": answer
    }


def task_8487():
    '''Генерация аналогичных задач № 8487 с портала https://kuzovkin.info/one_exercise_1/8487
    Переведите проценты в десятичную дробь: 1 2/3%'''
    while True:
        number, number_1, number_2 = np.random.randint(1, 10, size=3)
        if number_1 >= number_2:
            continue
        result = (number + (number_1 / number_2)) / 100
        if len(str(result)) <= 6:
            answer = result
            break
    task = f'Переведите проценты в десятичную дробь: ${number}\\frac{{{number_1}}}{{{number_2}}}$%'
    return {
      "condition": task,
      "answer": answer
    }


def task_8488():
    '''Генерация аналогичных задач № 8488 с портала https://kuzovkin.info/one_exercise_1/8488
    Переведите проценты в десятичную дробь: 66 2/3%'''
    while True:
        number, number_1, number_2 = np.random.randint(1, 100, size=3)
        if number_1 >= number_2:
            continue
        result = (number + (number_1 / number_2)) / 100
        if len(str(result)) <= 6:
            answer = result
            break
    task = f'Переведите проценты в десятичную дробь: ${number}\\frac{{{number_1}}}{{{number_2}}}$%'
    return {
      "condition": task,
      "answer": answer
    }



def task_8492():
    '''Генерация аналогичных задач № 8492 с портала https://kuzovkin.info/one_exercise_1/8492
    Переведите проценты в десятичную дробь: 2,34%'''
    while True:
        number = round(np.random.uniform(0,10),2)
        if number % 1 == 0:
            continue
        result = number / 100
        if len(str(result)) <= 6:
            answer = result
            break
    task = f'Переведите проценты в десятичную дробь: {number}%'
    return {
      "condition": task,
      "answer": answer
    }



def task_8500():
    '''Генерация аналогичных задач № 8500 с портала https://kuzovkin.info/one_exercise_1/8500
    Переведите дроби в проценты: 0,1'''
    while True:
        number = round(np.random.uniform(0,10),1)
        if number % 1 == 0:
            continue
        result = number * 100
        if result % 1 == 0:
            answer = int(result)
            break
    task = f'Переведите дроби в проценты: {number}'
    return {
      "condition": task,
      "answer": answer
    }


def task_8501():
    '''Генерация аналогичных задач № 8501 с портала https://kuzovkin.info/one_exercise_1/8501
    Переведите дроби в проценты: 0,25'''
    while True:
        number = round(np.random.uniform(0,10),2)
        if number % 1 == 0:
            continue
        result = number * 100
        if result % 1 == 0:
            answer = int(result)
            break
    task = f'Переведите дроби в проценты: {number}'
    return {
      "condition": task,
      "answer": answer
    }


def task_8502():
    '''Генерация аналогичных задач № 8502 с портала https://kuzovkin.info/one_exercise_1/8502
    Переведите дроби в проценты: 0,4'''
    while True:
        number = round(np.random.uniform(0,10),2)
        if number % 1 == 0:
            continue
        result = number * 100
        if result % 1 == 0:
            answer = int(result)
            break
    task = f'Переведите дроби в проценты: {number}'
    return {
      "condition": task,
      "answer": answer
    }


def task_8506():
    '''Генерация аналогичных задач № 8506 с портала https://kuzovkin.info/one_exercise_1/8506
    Переведите дроби в проценты: 0,0005'''
    while True:
        number = round(np.random.uniform(0,1),4)
        if number % 1 == 0:
            continue
        result = number * 100
        if result % 1 != 0 and len(str(result)) <= 6:
            answer = result
            break
    task = f'Переведите дроби в проценты: {number}'
    return {
      "condition": task,
      "answer": answer
    }



def task_8512():
    '''Генерация аналогичных задач № 8512 с портала https://kuzovkin.info/one_exercise_1/8512
    Переведите дроби в проценты: 1,23'''
    while True:
        number = round(np.random.uniform(1,100),2)
        if number % 1 == 0:
            continue
        result = number * 100
        if result % 1 == 0:
            answer = int(result)
            break
    task = f'Переведите дроби в проценты: {number}'
    return {
      "condition": task,
      "answer": answer
    }


def task_8515():
    '''Генерация аналогичных задач № 8515 с портала https://kuzovkin.info/one_exercise_1/8515
    Переведите дроби в проценты: 1,8'''
    while True:
        number = round(np.random.uniform(1,100),2)
        if number % 1 == 0:
            continue
        result = number * 100
        if result % 1 == 0:
            answer = int(result)
            break
    task = f'Переведите дроби в проценты: {number}'
    return {
      "condition": task,
      "answer": answer
    }


def task_8539():
    '''Генерация аналогичных задач № 8539 с портала https://kuzovkin.info/one_exercise_1/8539
    Переведите дроби в проценты: 3/4'''
    while True:
        number, number_1 = np.random.randint(1, 10, size=2)
        if number >= number_1:
            continue
        result = (number / number_1) * 100
        if result % 1 == 0:
            answer = int(result)
            break
    task = f'Переведите дроби в проценты: \\frac{{{number}}}{{{number_1}}}$'
    return {
      "condition": task,
      "answer": answer
    }


def task_8542():
    '''Генерация аналогичных задач № 8542 с портала https://kuzovkin.info/one_exercise_1/8542
    Банк начисляет ежегодно 9% от вложенной суммы. Сколько рублей будет начислено через год на вклад 450000 рублей?'''
    while True:
        percent, money = np.random.randint(5, 15), np.random.randint(100000, 1000000)
        if money % 1000 != 0:
            continue
        year = np.random.choice(["год", "два года", "три года"])
        if year == "год":
            result = money * (1 + percent / 100)
        elif year == "два года":
            result = money * (1 + percent / 100)**2
        else:
            result = money * (1 + percent / 100)**3
        if result % 1 == 0:
            answer = int(result)
            break
    task = f'Банк начисляет ежегодно {percent}% от вложенной суммы. Сколько рублей будет начислено через {year} на вклад {money} рублей?'
    return {
      "condition": task,
      "answer": answer
    }


def task_8544():
    '''Генерация аналогичных задач № 8542 с портала https://kuzovkin.info/one_exercise_1/8542
    Продавец купил товар по цене 1100 рублей за единицу товара и планирует получить при продаже прибыль 15%. По какой цене он должен продавать товар?'''
    while True:
        thing = np.random.choice(generate_context('./text_tasks/context.json', 'things'))
        if thing == generate_context('./text_tasks/context.json', 'things')[4]:
            continue
        percent, money = np.random.randint(10, 60), np.random.randint(1000, 10000)
        result = (money * (percent / 100)) + money
        if result % 1 == 0:
            answer = int(result)
            break
    task = f'Продавец купил {choosing_declension_form(thing, "accs")} по цене {money} рублей за единицу {choosing_declension_form(thing)} и планирует получить при продаже прибыль {percent}%. По какой цене он должен продавать {choosing_declension_form(thing, "accs")}?'
    return {
      "condition": task,
      "answer": answer
    }


def task_9327():
    """
    Генерация аналогичных задач № 9327 с портала https://kuzovkin.info/one_exercise_1/9327
    Переведите проценты в десятичную дробь: 87,5%
    """
    while True:
        random_percent = round(np.random.uniform(1, 100), 2)
        if random_percent % 1 == 0:
            continue
        answer = random_percent / 100
        if len(str(answer).split('.')[1]) <= 4:
            if answer % 1 == 0:
                answer = int(answer)
            break
    task = f"Переведите проценты в десятичную дробь: {random_percent}%"
    return {
        "condition": task,
        "answer": answer
    }


def task_9346():
    """
    Генерация аналогичных задач № 9346 с портала https://kuzovkin.info/one_exercise_1/9346
    Переведите дроби в проценты: 1,451
    """
    while True:
        random_fraction = round(np.random.uniform(0.01, 1.6), 3)
        if random_fraction % 1 == 0:
            continue
        answer = random_fraction * 100
        if len(str(answer).split('.')[1]) <= 2:
            if answer == int(answer):
                answer = int(answer)
            break
    task = f"Переведите дроби в проценты: {random_fraction}"
    return {
        "condition": task,
        "answer": answer
    }


def task_9350():
    """
    Генерация аналогичных задач № 9350 с портала https://kuzovkin.info/one_exercise_1/9350
    Переведите дроби в проценты: 2
    """
    while True:
        random_fraction = round(np.random.uniform(1, 10), 1)
        if random_fraction % 1 == 0:
            continue
        result = random_fraction * 100
        if result % 1 == 0:
            answer = int(result)
            break
    task = f"Переведите дроби в проценты: {random_fraction}"
    return {
        "condition": task,
        "answer": answer
    }


def task_9351():
    """
    Генерация аналогичных задач № 9351 с портала https://kuzovkin.info/one_exercise_1/9351
    Переведите дроби в проценты: 10
    """
    while True:
        random_fraction = round(np.random.uniform(10, 100), 1)
        if random_fraction % 1 == 0:
            continue
        result = random_fraction * 100
        if result % 1 == 0:
            answer = int(result)
            break
    task = f"Переведите дроби в проценты: {random_fraction}"
    return {
        "condition": task,
        "answer": answer
    }


def task_9356():
    """
    Генерация аналогичных задач № 9356 с портала https://kuzovkin.info/one_exercise_1/9356
    Переведите дроби в проценты: 1/4
    """
    while True:
        random_fraction = round(np.random.uniform(0.01, 0.99), 2)
        fraction = Fraction(random_fraction).limit_denominator()
        result = random_fraction * 100
        if result % 1 == 0:
            answer = int(result)
            break
    task = (
        r"Переведите дроби в проценты: \(\frac{"
        + f"{fraction.numerator}"
        + r"}{"
        + f"{fraction.denominator}"
        + r"}\)"
    )
    return {
        "condition": task,
        "answer": answer
    }
