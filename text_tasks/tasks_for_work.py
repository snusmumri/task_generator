import math
from fractions import Fraction
from random import randint, choice
import numpy as np
from pprint import pprint

#from input_parameters import input_parameters_work, morph, correct_word, gent_pers
from task_generator.text_tasks.input_parameters import input_parameters_work, morph, correct_word, gent_pers

def task_9515():
    """Генерация аналогичной задачи с портала https://kuzovkin.info/one_exercise_1/9515:
     Лев съел овцу за 2 ч, волк съел овцу за 3 ч, а пёс съел овцу за 6 ч. Как скоро они втроём съели бы одну овцу?
     """
    i = randint(0, 10)
    # получаем сюжет задачи
    pers1, pers2, pers3, (task, _) = input_parameters_work(i)
    # случайным образом получаем ответ к задаче
    while True:
        time1, time2, time3 = np.random.randint(4, 100, size=3)
        answer = 1 / (1 / time1 + 1 / time2 + 1 / time3)
        if int(answer) - answer == 0:
            break
    return f"{pers1.title()} может {task} за {time1} ч, {pers2} может {task} за {time2} ч, {pers3} - за {time3} ч. " \
           f"За какое время они втроем могут {task}?", answer


def task_9517():
    """Генерация аналогичной задачи с портала https://kuzovkin.info/one_exercise_1/9517:
     Маша и Оля пропалывают грядку за 12 мин, а одна Оля – за 15 мин. За сколько минут пропалывает грядку одна Маша?
     """
    # получаем сюжет задачи
    i = randint(0, 10)
    pers1, pers2, _, (task, _) = input_parameters_work(i)
    while True:
        time1, time2 = np.random.randint(5, 100, size=2)
        time2 += time1
        answer = time1 * time2 / (time2 - time1)
        if int(answer) - answer == 0:
            break
    return f"{pers1.title()} и {pers2} могут {task} за {time1} мин, а 1 {pers1} - за {time2} мин. За сколько минут " \
           f"может {task} {pers2}?", answer


def task_11101():
    """Генерация аналогичной задачи с портала https://kuzovkin.info/one_exercise_1/11101:
    Бассейн при одновременном включении трех труб может наполниться за 4 ч, через одну первую трубу – за 10 ч,
    а через одну вторую – за 15 ч. За сколько часов может наполниться бассейн через одну третью трубу?"""
    # получаем сюжет задачи
    i = randint(0, 10)
    pers1, pers2, pers3, (task, _) = input_parameters_work(i)
    # случайным образом получаем ответ к задаче
    while True:
        time1, time2, time3 = sorted(np.random.randint(4, 100, size=3))
        answer = 1 / (1 / time1 - 1 / time2 - 1 / time3)
        if answer <= 0:
            answer = 1.23456
        if int(answer) - answer == 0:
            break
    return f"{pers1.title()}, {pers2} и {pers3} вместе могут {task} за {time1} ч. {pers1} может {task} за {time2} ч, " \
           f"а {pers2} – за {time3} ч. За сколько часов это сделает {pers3}?", answer


def task_11108():
    """Генерация аналогичной задачи с портала https://kuzovkin.info/one_exercise_1/11108:
    Вася и Лева могут покрасить забор за 3 часа, Лева и Петя могут покрасить этот же забор за 6 часов,
    а Петя и Вася – за 4 часа. За какое время мальчики покрасят забор, работая втроем?"""
    i = randint(0, 10)
    pers1, pers2, pers3, (task, _) = input_parameters_work(i)
    # случайным образом получаем ответ к задаче
    while True:
        time1, time2, time3 = np.random.randint(4, 100, size=3)
        answer = 2 / (1 / time1 + 1 / time2 + 1 / time3)
        if int(answer) - answer == 0:
            break
    return f"{pers1.title()} и {pers2} могут {task} за {time1} ч. {pers2} и {pers3} могут {task} за {time2} ч, " \
           f"а {pers1} и {pers3} - за {time3} ч. За какое время они могут {task}, работая вместе?", answer


def task_936():
    """Генерация аналогичных задач 936, 9518 с портала https://kuzovkin.info/one_exercise_1/936:
    Каждый из двух рабочих одинаковой квалификации может выполнить заказ за 12 часов. Через 4 часа после того,
    как один из них приступил к выполнению заказа, к нему присоединился второй рабочий, и работу над заказом они довели
    до конца уже вместе. За сколько часов был выполнен весь заказ?"""
    # исключаем женский род персонажей
    i = randint(0, 9)
    # выбираем сюжет
    pers1, pers2, _, (task, _) = input_parameters_work(i)
    time1 = choice([i for i in range(1, 20) if not i % 2])
    time2 = time1 * randint(1, 10)
    # получаем ответ
    answer = time1 + (time2 - time1) / 2
    return f"{pers1.title()} и {pers2} должны {task}. Каждый из них способен сделать это за {time2} ч. " \
           f"Через {time1} ч после того, как {pers1} начал делать это в одиночку, к нему присоединился {pers2}, " \
           f"и они закончили вместе. За сколько часов задача была выполнена?", answer


def choose_discr() -> tuple:
    """Функция подбора коэффициентов квадратного уравнения для получения целых корней
    s - производительность
    x - изменение скорости
    y - изменение времени"""
    discr = choice(tuple(i ** 2 for i in range(100)))
    # счетчик на случай, если к случайно выбранному значению дискриминанта нельзя подобрать подходящие коэффициенты
    cnt = 0
    while True:
        x, y = (randint(2, 15) for _ in range(2))
        s = (discr - (x * y) ** 2) / (4 * x * y)
        cnt += 1
        if s <= 0:
            s = 1.234
        if cnt > 100:
            return choose_discr()
        if int(s) - s == 0:
            break
    return discr, x, y, s


def task_2610():
    """Генерация аналогичных задач 2610, 2611, 6482, 17611 с портала https://kuzovkin.info/one_exercise_1/2610:
    Токарь должен был обработать 120 деталей к определённому сроку. Применив новый резец, он стал обтачивать в час
    на 20 деталей больше и поэтому закончил работу на 1ч раньше срока. Сколько деталей он должен был обрабатывать по плану?"""
    # исключаем женский род персонажей
    i = randint(0, 9)
    # выбираем сюжет
    pers, _, _, (task, unit) = input_parameters_work(i)
    if pers.split()[0] == 'первый':
        pers = pers.split()[1]
    # подбираем дискриминант, чтобы получить ответ в целых числах
    discr, x, y, s = choose_discr()  # 100**2, 20, 1, 120
    v = (-(x * y) + math.sqrt(discr)) / (2 * y)
    t = s / v
    # делаем множественное число
    task1, (word1, word2) = correct_word(key=task, values=(int(s), x))
    # выбираем вопрос и ответ к задаче
    answer, question = choice([
        (t, 'За сколько дней он выполнит задачу'),
        (v, 'Сколько раз в день он должен был делать это по плану')
    ])
    return f"{pers.title()} должен {task1} {int(s)} {word1} - по несколько в день. Когда он приступил к работе, оказалось, " \
           f"что он может {task1} на {x} {word2} больше запланированного количества в день " \
           f"и завершить процесс на {y} {correct_word('день', y)} раньше срока. {question}?", answer


def task_17612():
    """Генерация аналогичных задач 17612 с портала https://kuzovkin.info/one_exercise_1/17612:
    Колхоз должен был засеять поле за 4 дня. Перевыполняя ежедневно норму сева на 12 га, колхозники закончили сев
    за 1 день до срока. Сколько гектаров засевал колхоз ежедневно?"""
    # исключаем женский род персонажей
    i = randint(0, 9)
    # выбираем сюжет
    pers, _, _, (task, _) = input_parameters_work(i)
    # подбираем целочисленный ответ
    while True:
        x, y, t = (randint(1, 20) for _ in range(3))
        v = (x * t - x * y) / y
        if v <= 0:
            v = 1.2345
        if int(v) - v == 0:
            break
    # получаем ответ
    answer = v + x
    # делаем множественное число
    task1, (word1, word2) = correct_word(key=task, values=(10, x))
    return f"{pers.title()} должен был за {t} {correct_word('день', t)} {task1} несколько {word1}. " \
           f"Перевыполняя ежедневную норму на {x} {word2}, он закончил на {y} " \
           f"{correct_word('день', y)} раньше срока. Сколько раз в день он делал поставленную задачу?", answer


def choose_discr_without_s() -> tuple:
    """Функция подбора коэффициентов квадратного уравнения для получения целых корней
    t - затраченное время
    x - изменение времени"""
    discr = choice(tuple(i ** 2 for i in range(100)))
    result = -1
    # счетчик на случай, если к случайно выбранному значению дискриминанта нельзя подобрать подходящие коэффициенты
    cnt = 0
    while result != discr:
        cnt += 1
        t, x = (randint(2, 15) for _ in range(2))
        result = (x - 2 * t) ** 2 + 4 * x * t
        if cnt > 100:
            return choose_discr_without_s()
    return discr, t, x


def task_17610():
    """Генерация аналогичных задач 17610, 17617, 17618, 17620
    Два экскаватора, работая одновременно, могут вырыть котлован за 4 часа. Один первый экскаватор затратит на эту
    работу на 6 часов больше, чем один второй. За какое время может вырыть котлован каждый экскаватор, работая отдельно?"""

    # исключаем женский род персонажей
    i = choice([0, 1, 2, 3, 5, 6, 7, 12, 13])
    # выбираем сюжет
    pers1, pers2, _, (task, _) = input_parameters_work(i)
    # подбираем дискриминант, чтобы получить ответ в целых числах
    discr, t, x = choose_discr_without_s()
    t2 = (2 * t - x + math.sqrt(discr)) / 2
    t1 = t2 + x
    return f"{pers1.title()} и {pers2}, работая одновременно, могут {task} за {t} ч. Один {pers1.title()} " \
           f"затратит на эту работу на {x} ч больше, чем {pers2}. За какое время могут {task} каждый из них, " \
           f"работая отдельно?", (t1, t2)


def task_17613():
    """Генерация аналогичной задачи 17613
    После усовершенствования технологии цех стал выпускать на 4 изделия в час больше, чем прежде.
    Поэтому за 6 часов работы цех начал выполнять 1,2 прежней 7-часовой нормы. Сколько изделий
    в час начал выпускать цех?"""
    i = choice([0, 4, 6, 9, 12])
    # выбираем сюжет
    pers, _, _, (task, _) = input_parameters_work(i)
    # подбираем ответ
    while True:
        k = choice([i / 10 for i in range(1, 21)])
        t1, t2 = sorted(randint(1, 50) for _ in range(2))
        x = randint(1, 10)
        try:
            answer = x / (1 - t1 / (k * t2))
        except ZeroDivisionError:
            answer = 1.2345
        if answer <= 0:
            answer = 1.2345
        if int(answer) - answer == 0:
            break
    # делаем множественное число
    task1, (word1, word2) = correct_word(key=task, values=(x, 5))

    return f"{pers.title()} усовершенствовал свои навыки и теперь может за час {task1} на {x} {word1} больше, " \
           f"чем прежде. Поэтому за {t1} ч работы он начал выполнять {k} прежней {t2}-часовой нормы. " \
           f"Сколько {word2} в час теперь может {task1} {pers}?", answer


def choose_discr_with_two_s() -> tuple:
    """Функция подбора коэффициентов квадратного уравнения для получения целых корней
    s1, s2 - производительность первого и второго персонажа соответственно
    x - изменение скорости
    y - изменение времени"""
    discr = choice(tuple(i ** 2 for i in range(100)))
    result = -1
    # счетчик на случай, если к случайно выбранному значению дискриминанта нельзя подобрать подходящие коэффициенты
    cnt = 0
    while result != discr:
        cnt += 1
        s1, s2 = sorted((randint(10, 100) for _ in range(2)), reverse=True)
        y, x = (randint(1, 15) for _ in range(2))
        result = (s2 - s1 - x * y) ** 2 + 4 * x * y * s2
        if cnt > 100:
            return choose_discr_with_two_s()
    return discr, s1, s2, x, y


def task_17583():
    """Генерация аналогичной задачи 17583
    Один рабочий должен был изготовить 36 деталей, второй - 20 деталей. Первый делал в день на 2 детали больше, чем второй,
    и затратил на изготовление своего заказа на 1 день меньше, чем второй. По сколько деталей в день делают рабочие?"""
    # исключаем женский род персонажей
    l = list(range(0, 9))
    l.extend([12, 13, 14])
    i = choice(l)
    # выбираем сюжет
    pers1, pers2, _, (task, _) = input_parameters_work(i)
    # подбираем ответ
    discr, s1, s2, x, y = choose_discr_with_two_s()
    v2 = (s1 - s2 + x * y + math.sqrt(discr)) / (2 * y)
    v1 = v2 + x
    # делаем множественное число
    task1, (word1, word2, word3, word4) = correct_word(key=task, values=(s1, x, s2, 10))
    # task1, word3, word4 = correct_word(key=task, values=(s2, 10))
    return f"{pers1.title()} должен {task1} {s1} {word1}, a {pers2} - {s2} {word3}. Первый может {task1} в день " \
           f"на {x} {word2} больше, чем второй, и закончить на {y} {correct_word('день', y)} раньше, чем второй. " \
           f"По сколько {word4} в день может {task1} каждый из них?", (v1, v2)


def choose_discr_with_delta_s() -> tuple:
    """Функция подбора коэффициентов квадратного уравнения для получения целых корней
    s - запланированная производительность
    s1 - превышение s
    x - изменение скорости
    y - изменение времени"""
    discr = choice(tuple(i ** 2 for i in range(1000)))
    # счетчик на случай, если к случайно выбранному значению дискриминанта нельзя подобрать подходящие коэффициенты
    cnt = 0
    while True:
        cnt += 1
        s, s1 = randint(1000, 10000), randint(10, 100)
        y, x = randint(10, 100), randint(1, 12)
        velocity = (-(s1 + x * y) + math.sqrt(discr)) / (2 * x)
        if velocity <= 0:
            return choose_discr_with_delta_s()
        t = s / velocity
        if cnt > 100:
            return choose_discr_with_delta_s()
        if not 0 <= t <= 100:
            t = 1.2345
        if int(t) - t == 0:
            break
    return s, s1, t, x, y


def task_17596():
    """Генерация аналогичных задач 17594, 17596, 5.157
    Предприятие должно было изготовить за несколько месяцев 6000 насосов. Увеличив производительность труда, предприятие
    стало изготавливать в месяц на 70 насосов больше, и на 1 месяц раньше срока перевыполнило задание на 30 насосов.
    За какой срок было изготовлено 6030 насосов?"""
    # i = choice([1, 4, 9, 12, 13])
    i = randint(0, 17)
    pers, _, _, (task, measure) = input_parameters_work(i)
    if measure:
        meas_word, unit = measure
        if unit != 'шт':
            pers, _, _, (task, measure) = input_parameters_work(i)
    s, s1, t, x, y = choose_discr_with_delta_s()
    answer = t - x
    task1, (word1, word2, word3, word4) = correct_word(key=task, values=(s, y, s1, s + s1))
    question = choice([
        f"За какой срок {pers} может {task1} {s + s1} {word4}?",
        f"За какой срок {pers} может {task1} на {s1} {word3} больше запланированного количества?"
    ])
    return f"{pers.title()} может {task1} {s} {word1}. Увеличив производительность, {pers} теперь может {task1} " \
           f"в месяц на {y} {word2} больше, и на {x} мес. раньше срока, перевыполнив задание на {s1} {word3}. " \
           f"{question}", answer


def task_17621():
    """Генерация аналогичной задачи 17621
    Бассейн, содержащий 30 м3 воды, сначала был опорожнен, а затем наполнен до прежнего уровня. На все это потребовалось 8 часов.
    Сколько времени шло заполнение бассейна, если при наполнении насос перекачивает на 4 м3 воды меньше, чем при опорожнении?"""
    while True:
        discr, x, y, s = choose_discr()  # 68**2, 4, 8, 30
        v = (2 * s - y * x + math.sqrt(discr)) / (2 * y)
        t = s / v
        if v <= 0:
            t = 1.2345
        if int(t) - t != 0:
            break
    return f"Бассейн, содержащий {s} м3 воды, сначала был опорожнен, а затем наполнен до прежнего уровня. " \
           f"На все это потребовалось {y} ч. Сколько времени шло заполнение бассейна, если при наполнении " \
           f"насос перекачивает на {x} м3 воды меньше, чем при опорожнении?", t


def task_17622():
    """Генерация аналогичных задач 17622
    Две трубы наполнили бассейн объемом 54 м3. При этом первая труба открыта 3 часа, а вторая - 2 часа.
    Какова пропускная способность первой трубы, если 1 м3 она заполняет на 1 минуту медленнее, чем вторая?"""
    # i = 10
    while True:
        i = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16])
        pers1, pers2, _, (task, measure) = input_parameters_work(i)
        if measure:
            meas_word, unit = measure
            break
        else:
            pers1, pers2, _, (task, measure) = input_parameters_work(i)

    while True:
        t = choice([1, 2, 3, 4, 5, 6, 10, 12, 15, 30, 60])
        t1, t2 = randint(1, 20), randint(1, 20)
        v = randint(1, 100)
        discr = choice(tuple(i ** 2 for i in range(500)))
        v1 = (v + t * t1 + t * t2 + math.sqrt(discr)) / (2 * t1)
        v2 = (v - t1 * v1) / t2
        if v1 <= 0:
            v1 = 1.23
        if v2 <= 0:
            v1 = (v + t * t1 + t * t2 - math.sqrt(discr)) / (2 * t1)
            v2 = (v - t1 * v1) / t2
            if v1 <= 0 or v2 <= 0:
                v1 = 1.2345
        if int(v1) - v1 == 0:
            break

    task1, (word1, word2) = correct_word(key=task, values=(v, 1))

    if unit in ('м3', 'м2', 'км'):
        word1, word2, new_unit = unit, unit, meas_word + ' '
        task1 = task
    else:
        new_unit = ''

    pers1_gent = gent_pers((pers1,))

    if morph.parse(pers1.split()[0])[0].tag.gender == 'femn':
        gender = ('первая', 'вторая', 'первой', 'она', 'каждой', 'Две')
    else:
        gender = ('первый', 'второй', 'первого', 'он', 'каждого', 'Два')

    questions = {
        'equal': [
            (v1, f'Какова {choice(["производительность", "скорость работы"])} {gender[2]} {pers1_gent}, если 1 {word2} '  
                 f'{gender[3]} может {task.split()[0]} на {t} мин медленнее, чем {gender[1]}?'),
            ((v1, v2), f'Какова {choice(["производительность", "скорость работы"])} {gender[4]} {pers1_gent}, если '
                       f'{gender[0]} {pers1} может {task.split()[0]} 1 {word2} на {t} мин медленнее, чем {gender[1]}?')
        ],
        'different': [
            (v1, f'Какова {choice(["производительность", "скорость работы"])} {pers1_gent}, если 1 {word2} {gender[3]} '
                 f'может {task.split()[0]} на {t} мин медленнее, чем {pers2}?'),
            ((v1, v2), f'Какова {choice(["производительность", "скорость работы"])} {gender[4]} из них, если {pers1} '
                       f'может {task.split()[0]} 1 {word2} на {t} мин медленнее, чем {pers2}?')
        ]
    }

    if pers1 == pers2:
        answer, question = choice(questions['equal'])
        return f"{gender[5]} {pers1_gent} могут {task1} {new_unit}{v} {word1}. При этом {gender[0]} {pers1} работает " \
               f"{t1} ч, а {gender[1]} {pers2} - {t2} ч. {question}", answer
    else:
        answer, question = choice(questions['different'])
        return f"{pers1.title()} и {pers2} могут вместе {task1} {new_unit}{v} {word1}. " \
               f"При этом {pers1} работает {t1} ч, а {pers2} - {t2} ч. {question}", answer


def task_17624():
    """
    Генерация аналогичных задач 17624
    Три одинаковых комбайна, работая вместе, убрали первое поле, а затем 2 из них убрали второе поле (другой площади).
    Вся работа заняла 12 часов. Если бы 3 комбайна выполнили половину всей работы, а затем оставшуюся часть сделал один
    из них, то работа заняла бы 20 часов. За какое время два комбайна могут убрать первое поле?
    """
    i = choice([0, 2, 3, 4, 8, 9, 10])
    pers1, pers2, pers3, _ = input_parameters_work(i)
    x, y = 1.23, 1.23
    while True:
        t1, t2 = sorted([randint(1, 36) for _ in range(2)])
        y = t1 * 6 - t2 * 3
        x = t2 * 3 / 2 - y
        if x <= 0 or y <= 0:
            x, y = 1.23, 1.23
        if int(x) - x == 0:
            break

    answer, question = choice([(x/2, 'сделают первый заказ'), (y/2, 'сделают второй заказ')])

    res = f'{pers1.title()}, {pers2} и {pers3} вместе выполнили первый заказ, а потом {pers2} и {pers3} выполнили ' \
          f'второй заказ (заказы разные по объему). Вся работа заняла {t1} ч. Если бы они вместе сделали половину всей ' \
          f'работы, а оставшуюся часть делал бы кто-то один из них, работа заняла бы {t2} ч. ' \
          f'За какое время двое из них {question}?'
    return res, answer


def task_5173():
    """Генерация аналогичных задач 5.170, 5.173, 5.156 из задачника для классов Пушкин С.А.:
    Бригада трактористов планировала вспахивать в день по 40 га, но из-за ненастной погоды она вспахивала в день
    по 30 га и закончила работу на 2 дня позже срока. Найдите площадь участка.
    на сайте kuzoviin.info задачи с номерами 51833,51834
    """
    # i = 16
    i = randint(0, 16)
    while True:
        pers, _, _, (task, measure) = input_parameters_work(i)
        if measure:
            meas_word, unit = measure
            meas_word1 = morph.parse(meas_word)[0].inflect({'gent', 'sing'}).word
            break
        else:
            pers, _, _, (task, measure) = input_parameters_work(i)
    pers = pers.split()[1] if 'перв' in pers else pers

    while True:
        t = randint(1, 10)
        v1 = randint(11, 100)
        delta_v = randint(1, 10)
        comparison = choice(['раньше', 'позже'])
        v2 = v1 + delta_v if comparison == 'раньше' else v1 - delta_v
        try:
            s = t / (1 / v1 - 1 / v2)
        except ZeroDivisionError:
            s = 1.2345
        if s <= 0:
            s = 1.2345
        if int(s) - s == 0:
            break

    # делаем множественное число
    task1, (word1, word2, word3) = correct_word(key=task, values=(10, 3, v2))
    # выбираем вопрос к задаче
    units = {
        'шт': (s, f'Сколько всего {word1} {pers} может {task1} за отведенное время?'),
        'м3': (s, f'Найдите объем {word2}.'),
        'м2': (s, f'Найдите площадь {word2}.'),
        'км': (s, f'Найдите длину {morph.parse(word2)[0].inflect({"gent", "sing"}).word}.')
    }
    answer, question = units.get(unit, '')

    if unit in ('м3', 'м2', 'км'):  #
        new_unit, word1, word3 = meas_word + ' ', unit, unit
        task1 = task
    else:
        new_unit = ''

    # ищем правильные формы слов в соответствии с родом персонажа
    if morph.parse(pers.split()[0])[0].tag.gender == 'femn':
        gender = ('должна', 'приступила', 'она')
    else:
        gender = ('планировал', 'приступил', 'он')
    task_condition = choice([
        f'по {v2} {word3} в день ',
        f'на {delta_v} {word1} больше запланированного {meas_word1} в день '
    ])
    return f"{pers.title()} {gender[0]} {task1} {new_unit}несколько {word1} за определенный срок -  по {v1} {unit} " \
           f"в день. Когда {pers} {gender[1]} к работе, оказалось, что {gender[2]} может {task1} {task_condition}" \
           f"и завершить процесс на {t} {correct_word('день', t)} {comparison} срока. {question}", answer


def task_108():
    """Генерация аналогичных задач 108, 118 из учебника Алгебра. 7 класс_Алимов Ш.А.
    В первом мешке было 50 кг сахара, а во втором 80 кг. Из второго мешка взяли сахара в 3 раза больше,
    чем из первого мешка, и тогда в первом мешке сахара осталось вдвое больше, чем во втором.
    Сколько килограммов сахара взяли из каждого мешка?"""
    # выбираем контекст
    i = randint(18, 21)
    place, _, (item, unit) = input_parameters_work(i)
    # item = morph.parse(item)[0].inflect({"gent"}).word
    if len(place.split()) == 1:
        place_gent = morph.parse(place)[0].inflect({"gent"}).word
        place_loct = morph.parse(place)[0].inflect({"loct"}).word
    else:
        place_gent = ' '.join([morph.parse(word)[0].inflect({"gent"}).word for word in place.split()])
        place_loct = ' '.join([morph.parse(word)[0].inflect({"loct"}).word for word in place.split()])

    if morph.parse(place)[0].tag.gender == 'femn':
        start = (f'На одной {place_loct}', 'на другой', f'С первой {place_gent}', 'со второй', f'c каждой {place_gent}', f'На первой {place_loct}', 'на второй', f'на каждой {place_loct}', 'на вторую')
    else:
        start = (f'В одном {place_loct}', 'в другом', f'Из первого {place_gent}', 'из второго', f'из каждого {place_gent}', f'На первом {place_loct}', 'на втором', f'в каждом {place_loct}', 'на второй')

    # выбираем условие задачи, а точнее искомое значение и соответствующее решение
    condition = choice(['time', 'init_volume', 'delta_volume'])

    if condition == 'delta_volume':
        while True:
            vol1, vol2 = (randint(10, 1000) for _ in range(2))
            k1, k2 = (randint(2, 10) for _ in range(2))
            try:
                x = (vol1 - vol2 * k2) / (k1 * k2 - 1)
            except ZeroDivisionError:
                x = 1.2345
            if int(x) - x == 0 and x > 0:
                break

        return f'{start[0]} было {vol1} {unit} {item}, а {start[1]} - {vol2} {unit}. {start[2]} забрали в {k1} раза ' \
               f'больше {item}, чем {start[3]}. Сколько {unit} {item} взяли {start[4]}?', (x, k1 * x)

    elif condition == 'time':
        while True:
            vol1, vol2 = (randint(1000, 10000) for _ in range(2))
            k = randint(1, 10)
            v1, v2 = (randint(min(vol1, vol2) // 100, min(vol1, vol2) // 10) for _ in range(2))
            try:
                t = (vol1 - vol2 * k) / (v1 - k * v2)
            except ZeroDivisionError:
                t = 1.2345
            if int(t) - t == 0 and t > 0:
                break

        question = 'станут равными' if k == 1 else f'{start[5].lower()} станут в {k} {correct_word("раз", k)} меньше, чем {start[6]}'

        return f'{start[0]} было {vol1} {unit} {item}, а {start[1]} - {vol2} {unit}. ' \
               f'{start[5]} ежедневно расходуется {v1} {unit}, а {start[6]} - {v2} {unit} {item}. ' \
               f'Через сколько дней запасы {item} {question}?', t

    elif condition == 'init_volume':
        while True:
            vol1, vol2 = (randint(10, 1000) for _ in range(2))
            k = randint(2, 10)
            # k = 2
            # vol1, vol2 = 750, 350
            x = (vol1 + vol2) / (k - 1)
            if int(x) - x == 0:
                break
        return f'{start[0]} было в {k} {correct_word("раз", k)} больше {item}, чем {start[1]}. ' \
               f'{start[2]} забрали {vol1} {unit} {item}, {start[8]} добавили {vol2} {unit}, ' \
               f'после чего {item} стало поровну. Сколько {item} было первоначально {start[7]}?', (x * k, x)


def task_721():
    """Генерация аналогичных задач 7.21-23 Мордкович 9 класс:
    Две бригады, работая вместе, могут выполнить задание за 8 часов. Первая бригада, работая одна, могла бы выполнить
    задание на 12 часов быстрее, чем вторая бригада. За сколько часов могла бы выполнить работу первая бригада,
    если бы она работала одна?"""
    # i = 11
    i = choice([0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16])
    pers1, pers2, _, (task, measure) = input_parameters_work(i)
    pers1, pers2 = (pers.split()[1] if any(map(lambda x: x in pers, ('перв', 'втор'))) else pers for pers in (pers1, pers2))

    while True:
        t, delta_t = sorted(randint(1, 100) for _ in range(2))
        d = math.sqrt((delta_t - 2 * t) ** 2 + 4 * t * delta_t)
        if int(d) - d == 0:
            break
    t1 = (-(delta_t - 2 * t) + d) / 2
    t2 = t1 + delta_t

    pers1_gent = gent_pers((pers1,))

    if morph.parse(pers1.split()[0])[0].tag.gender == 'femn':
        gender = ('первая', 'вторая', 'каждая', 'одна', 'Две')
    else:
        gender = ('первый', 'второй', 'каждый', 'один', 'Два')

    questions = {
        'equal': [
            (t1, f'За сколько часов {gender[0]} {pers1} может выполнить работу, работая {gender[3]}?'),
            (t2, f'За сколько часов {gender[1]} {pers2} может выполнить работу, работая {gender[3]}?'),
            ((t1, t2), f'За сколько часов {gender[2]} {pers1}, выполнит такую же работу по отдельности?')
        ],
        'different': [
            (t1, f'За сколько часов {pers1} может выполнить работу, работая {gender[3]}?'),
            (t2, f'За сколько часов {pers2} может выполнить работу, работая {gender[3]}?'),
            ((t1, t2), f'За сколько времени {pers1} и {pers2} выполнят задание, работая по отдельности?')
        ]
    }

    if pers1 == pers2:
        answer, question = choice(questions['equal'])
        return f"{gender[4]} {pers1_gent} должны {task} за {t} ч. При этом {gender[0]} {pers1}, работая в одиночку, " \
               f"может выполнить все задание на {delta_t} ч быстрее, чем {gender[1]}. {question}", answer
    else:
        answer, question = choice(questions['different'])
        return f"{pers1.title()} и {pers2} должны {task} за {t} ч. При этом {pers1}, работая в одиночку, " \
               f"может выполнить все задание на {delta_t} ч быстрее, чем {pers2}. {question}", answer


def task_745():
    """Генератор аналогичных заданий 7.28, 7.44-47 Мордкович 9 класс:
    Мастер, работая с учеником, обрабатывает деталь за 2 ч 24 мин. Если мастер будет работать 2ч, а ученик - 1 ч,
    будет выполнено 2/3 всей работы. Сколько времени потребуется мастеру и ученику в отдельности на обработку детали?"""

    i = choice([0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16])
    pers1, pers2, _, (task, measure) = input_parameters_work(i)
    pers1, pers2 = (pers.split()[1] if any(map(lambda x: x in pers, ('перв', 'втор'))) else pers for pers in
                    (pers1, pers2))
    while True:
        # x, y = 4, 6
        x, y = randint(1, 20), randint(1, 20)
        t = x * y / (x + y)
        if int(t * 60) - t * 60 == 0:
            break
    while True:
        t1, t2 = randint(1, 20), randint(1, 20)
        k = Fraction(t1, x) + Fraction(t2, x)
        if k < 1:
            break

    pers1_gent = gent_pers((pers1,))

    if morph.parse(pers1.split()[0])[0].tag.gender == 'femn':
        gender = ('первая', 'вторая', 'каждая', 'одна', 'Две')
    else:
        gender = ('первый', 'второй', 'каждый', 'один', 'Два')

    questions = {
        'equal': [
            (x, f'За сколько часов {gender[0]} {pers1} может выполнить работу, работая {gender[3]}?'),
            (y, f'За сколько часов {gender[1]} {pers2} может выполнить работу, работая {gender[3]}?'),
            ((x, y), f'За сколько часов {gender[2]} {pers1}, выполнит такую же работу по отдельности?')
        ],
        'different': [
            (x, f'За сколько часов {pers1} может выполнить работу, работая {gender[3]}?'),
            (y, f'За сколько часов {pers2} может выполнить работу, работая {gender[3]}?'),
            ((x, y), f'За сколько времени {pers1} и {pers2} выполнят задание, работая по отдельности?')
        ]
    }
    if t > 1:
        time = f'{int(t)} ч' if t * 60 % 60 == 0 else f'{int(t)} ч {int(t * 60 % 60)} мин'
    else:
        time = f'{int(t * 60)} мин'
    if pers1 == pers2:
        answer, question = choice(questions['equal'])
        return f"{gender[4]} {pers1_gent} должны {task} за {time}. Если {gender[0]} {pers1} будет работать {t1} ч, " \
               f"а {gender[1]} - {t2} ч, будет выполнено {k} всей работы. {question}", answer
    else:
        answer, question = choice(questions['different'])
        return f"{pers1.title()} и {pers2} должны {task} за {time}. Если {pers1} будет работать {t1} ч, " \
               f"а {pers2} - {t2} ч, будет выполнено {k} всей работы. {question}", answer


if __name__ == "__main__":
    pprint(task_745())
    # pprint(task_721())
    # pprint(task_17622())
    # pprint(task_17583())
    # pprint(task_5173())
    # pprint(task_17583())
    # pprint(task_17596())
