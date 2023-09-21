from pprint import pprint
from random import randint, choice

from input_parameters import input_parameters_work, morph, correct_word, gent_pers


def task_13021():
    """Генерация аналогичных задач 13.021 М.И. Сканави:
    Одна бригада может убрать поле за 12 дней. Другой бригаде на выполнение этой же работы нужно 75% этого времени.
    После того как в течение 5 дней работала одна первая бригада, к ней присоединилась вторая, и обе вместе закончили
    работу. Сколько дней бригады работали вместе ?
    """
    # находим параметры к задаче и ответ
    while True:
        # delta_t, t1 = 5, 12
        # k = 75
        delta_t, t1 = sorted(randint(1, 100) for _ in range(2))
        k = randint(10, 99)
        t2 = k / 100 * t1
        t = (1 - delta_t / t1) / (1 / t1 + 1 / t2)
        if int(t) - t == 0 and t != 0:
            break

    answer = t

    # выбираем контекст
    # i = 1
    i = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16])
    pers1, pers2, _, (task, measure) = input_parameters_work(i)

    pers1 = pers1.split()[1] if 'перв' in pers1 else pers1
    pers2 = pers2.split()[1] if 'втор' in pers2 else pers2

    if morph.parse(pers1.split()[0])[0].tag.gender == 'femn':
        gender = ('работала', 'ней', 'присоединилась', 'обе', 'Первая', 'Вторая')
    else:
        gender = ('работал', 'нему', 'присоединился', 'оба', 'Первый', 'Второй')

    if pers1 == pers2:
        return f"{gender[4]} {pers1} может {task} за {t1} {correct_word('день', t1)}. {gender[5]} {pers2} может выполнить " \
               f"ту же работу за {k}% этого времени. После того, как {delta_t} {correct_word('день', delta_t)} " \
               f"{gender[0]} только {gender[4].lower()} {pers1}, к {gender[1]} {gender[2]} {gender[5].lower()} {pers2}, " \
               f"и {gender[3]} закончили работу вместе. Сколько дней они работали вместе?", answer
    else:
        return f"{pers1.title()} может {task} за {t1} {correct_word('день', t1)}. {pers2.title()} может выполнить ту же работу за {k}% этого времени. " \
               f"После того, как {delta_t} {correct_word('день', delta_t)} {gender[0]} только {pers1}, к {gender[1]} {gender[2]} {pers2}, " \
               f"и {gender[3]} закончили работу вместе. Сколько дней {pers1} и {pers2} работали вместе?", answer


def task_13023():
    """ Генерация аналогичных задач 13.023 М.И. Сканави:
    Однотипные детали обрабатываются на двух станках. Производительность первого станка на 40 % больше производительности
    второго. Сколько деталей было обработано за смену каждым станком, если первый работал в эту смену 6 ч, а второй - 8 ч,
    причём оба изготовили 820 деталей.
    """
    # находим решение
    while True:
        k = randint(50, 99)  # / 100
        s = randint(10, 1000)
        t1, t2 = sorted(randint(1, 100) for _ in range(2))
        v2 = s / ((1 + k / 100) * t1 + t2)
        v1 = (1 + k / 100) * v2
        s1, s2 = v1 * t1, v2 * t2
        if int(v2) - v2 == 0 and int(v1) - v1 == 0:
            break
    # выбираем контекст
    while True:
        i = choice([0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 12, 14, 15, 16])
        pers1, pers2, _, (task, measure) = input_parameters_work(i)
        if measure and pers1 != pers2:
            meas_word, unit = measure
            break
        else:
            pers1, pers2, _, (task, measure) = input_parameters_work(i)

    pers1_gent, pers2_gent = gent_pers((pers1, pers2))

    if unit in ('м3', 'м2', 'км'):
        word1, word2, new_unit = unit, unit, meas_word + ' '
        task1 = task
    else:
        new_unit = ''

    task1, (word1, word2) = correct_word(key=task, values=(10, s))

    if morph.parse(pers1.split()[0])[0].tag.gender == 'femn':
        gender = ('каждой', 'должна', 'каждая', 'первая', 'работала', 'вторая')
    else:
        gender = ('каждого', 'должен', 'каждый', 'первый', 'работал', 'второй')

    question, answer = choice([
        (f'Какова скорость {gender[0]} из них', (v1, v2)),
        (f'Сколько {gender[1]} {word1} {task1} {gender[2]} из них', (s1, s2))
    ])

    return f"{pers1.title()} и {pers2} должны {task1} несколько {word1}. Производительность {pers1_gent} на {k}% выше " \
           f"производительности {pers2_gent}. {question}, если {gender[3]} {gender[4]} {t1} ч, " \
           f"а {gender[5]} - {t2} ч, причём всего они смогли {task1} {new_unit}{s} {word2}", answer


def task_13024():
    """ Генерация аналогичных задач 13.024, 13.010 М.И. Сканави:
    Тракторная бригада может вспахать 5/6 участка земли за 4 ч 15 мин До обеденного перерыва бригада работала 4.5 ч,
    после чего осталось невспаханными ещё 8 га. Как велик был участок?
    """
    while True:
        a, b = sorted(randint(1, 10) for _ in range(2))
        a, b = (a, b) if a != b else (2, 3)
        x = a / b
        delta_s = randint(1, 100)
        t2, t1 = sorted(randint(1, 1000) for _ in range(2))
        t = t1 / x
        s = delta_s * t / (t - t2)
        if int(s) - s == 0:
            break

    while True:
        # i = 15
        i = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16])
        pers, _, _, (task, measure) = input_parameters_work(i)
        if measure:
            meas_word, unit = measure
            break
        else:
            pers, _, _, (task, measure) = input_parameters_work(i)

    task1, (word1, word2) = correct_word(key=task, values=(2, delta_s))

    if unit == 'км':
        word2 = f'{unit} {word2}'

    # корректируем время для условия
    times = []
    for i, time in enumerate((t1, t2)):
        if time / 60 > 1:
            time1 = f'{int(time)} ч' if time % 60 == 0 else f'{int(time)} ч {int(time % 60)} мин'
        else:
            time1 = f'{int(time)} мин'
        times.append(time1)
    time1, time2 = times
    # выбираем вопрос к задаче
    units = {
        'шт': (s, f'Сколько всего {word1} {pers} может {task1} за отведенное время?'),
        'м3': (s, f'Найдите объем {word1}.'),
        'м2': (s, f'Найдите площадь {word1}.'),
        'км': (s, f'Найдите длину {morph.parse(word1)[0].inflect({"gent", "sing"}).word}.')
    }
    try:
        answer, question = units.get(unit, '')
        return f"{pers.title()} может выполнить {a}/{b} заказа за {time1}. {pers.title()} работал(а) {time2}, после чего " \
               f"осталось {task1} еще {delta_s} {word2}. {question}", answer
    except ValueError:
        return task_13024()


def task_13032():
    """Генерация аналогичных задач 13.032 М.И. Сканави:
    За 3,5 ч работы один штамповочный пресс может изготовить 42% всех заказанных деталей. Второй пресс за 9 ч работы
    может изготовить 60% всех деталей, а скорости выполнения работы на третьем и на втором прессах относятся как 6:5.
    За какое время будет выполнен весь заказ, если все три пресса будут работать одновременно?
    """
    # находим ответ к задаче
    while True:
        k1, k2 = (randint(10, 100) for _ in range(2))  # / 100
        t1, t2 = sorted(randint(1, 100) for _ in range(2))
        a, b = (randint(1, 10) for _ in range(2))
        a, b = (a, b) if a != b else (6, 5)
        t = 1 / (k1 / t1 + k2 / t2 * (1 + a/b)) * 60
        if int(t) - t == 0:
            break
    # корректируем время для условия
    times = []
    for i, time in enumerate((t1, t2, t)):
        if time / 60 > 1:
            time1 = f'{int(time)} ч' if time % 60 == 0 else f'{int(time)} ч {int(time % 60)} мин'
        else:
            time1 = f'{int(time)} мин'
        times.append(time1)
    t1, t2, answer = times

    # выбираем условие
    while True:
        pers1, pers2, pers3, (task, measure) = input_parameters_work()
        if not pers1 == pers2 == pers3 or (not pers1 == pers2 and not pers3 == pers2):
            break

    pers2_gent, pers3_gent = gent_pers((pers2, pers3))

    return f"{pers1.title()}, {pers2} и {pers3} должны {task}. За {t1} работы {pers1} может выполнить {k1}% всей работы. " \
           f"{pers2.title()} за {t2} выполнит {k2}% всей работы. Скорости выполнения работы {pers2_gent} и {pers3_gent} " \
           f"относятся как {a}:{b}. За какое время будет выполнена вся работа, если они будут работать вместе?", answer


def task_13033():
    """Генерация аналогичных задач 13.033 М.И. Сканави:
    Каждая из двух машинисток перепечатывала рукопись объемом 72 страницы. Первая машинистка перепечатывала 6 страниц
    за то же время, за которое вторая перепечатывала 5 страниц. Сколько страниц перепечатывала каждая машинистка в час,
    если первая закончила работу на 1,5 ч быстрее?
    """
    # находим ответ
    while True:
        a, b = sorted(randint(1, 10) for _ in range(2))
        s = randint(1, 100)
        delta_t = randint(1, 10)
        v2 = s / delta_t * (1 - a / b)
        v1 = b / a * v2
        if int(v1) - v1 == 0 and v1 != 0 and int(v2) - v2 == 0:
            break
    answer = (v1, v2)
    # выбираем условие
    while True:
        i = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16])
        pers1, pers2, _, (task, measure) = input_parameters_work(i)
        if measure and pers1 != pers2:
            meas_word, unit = measure
            break
        else:
            pers1, pers2, _, (task, measure) = input_parameters_work(i)

    task1, (word1, word2) = correct_word(key=task, values=(s, 10))

    if unit in ('м3', 'м2', 'км'):
        word1, word2, new_unit = unit, unit, meas_word + ' '
        task1 = task
    else:
        new_unit = ''

    if morph.parse(pers1.split()[0])[0].tag.gender == 'femn':
        gender = ('каждая', 'Первая', 'вторая', 'закончила')
    else:
        gender = ('каждый', 'Первый', 'второй', 'закончил')

    return f"{pers1.title()} и {pers2} должны {task1} {new_unit}несколько {word2} - по {s} {word1} {gender[0]}. {gender[1]} может " \
           f"{task1} {a} {unit} за то же время, за которое {gender[2]} может {task1} {b} {unit}. Сколько {word2} " \
           f"может {task1} {gender[0]}, если {gender[1].lower()} {gender[3]} работу на {delta_t} ч быстрее?"


def task_13037():
    """Генерация аналогичных задач 13.037 М.И. Сканави:
    Одна мельница может смолоть 19 ц пшеницы за 3 ч., другая 32 ц за 5 ч.а третья 10 ц за 2 часа. Как распределить 133
    тонны пшеницы между этими мельницами чтобы одновременно начав работу они окончили её также одновременно?"""
    # s1, s2, s3 = 19, 32, 10
    # t1, t2, t3 = 3, 5, 2
    while True:
        # s = 133
        s = randint(10, 200)
        s1, s2, s3 = (randint(1, 100) for _ in range(3))
        t1, t2, t3 = (randint(1, 10) for _ in range(3))
        t = s / (s1/t1 + s2/t2 + s3/t3)
        x1, x2, x3 = s1 / t1 * t * 10, s2 / t2 * t * 10, s3 / t3 * t * 10
        if int(t * 60) - t * 60 == 0 and int(x1) - x1 == 0 and int(x2) - x2 == 0 and int(x3) - x3 == 0:
            break
    return f'{s} т, {t * 60} min, {x1, x2, x3}'


def task_13075():
    """Генерация аналогичных задач 13.075 М.И. Сканави:
    Двое рабочих за одну смену изготовили 72 детали. После увеличения производительности первого рабочего на 15%,
    а второго на 25%, они вместе за смену изготовили 86 деталей. Сколько деталей изготовляет каждый рабочий за смену
    после (или до) повышения производительности труда?"""
    while True:
        # k1, k2 = 15, 25
        # s1, s2 = 72, 86
        k1, k2 = (randint(5, 50) for _ in range(2))  # / 100
        if k1 == k2:
            k2 = 51 - k2
        s1, s2 = sorted(randint(10, 100) for _ in range(2))

        x2 = (s2 - (1 + k1 / 100) * s1) / (k2 - k1) * 100  # до
        x1 = s1 - x2  # до
        x2_new, x1_new = (1 + k2 / 100) * x2, (1 + k1 / 100) * x1  # после повышения производительности

        if int(x2) - x2 == 0 and int(x2_new) - x2_new == 0 and x1 > 0 and x2 > 0:
            break
    return x2, x1


if __name__ == "__main__":
    # print(correct_word('день', 42))
    pprint(task_13033())
    # print(task_13037())