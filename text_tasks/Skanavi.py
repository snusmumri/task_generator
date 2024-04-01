from pprint import pprint
from random import randint, choice

from text_tasks.input_parameters import input_parameters_work, morph, correct_word, gent_pers, start_title
from text_tasks.task_solutions import (solution_task_13135, solution_task_13137, solution_task_13140,
                                       solution_task_13170, solution_task_13185, solution_task_13195,
                                       solution_task_13292, solution_task_13328)


def task_13021():
    """Генерация аналогичных задач 13.021 М.И. Сканави:
    Одна бригада может убрать поле за 12 дней. Другой бригаде на выполнение этой же работы нужно 75% этого времени.
    После того как в течение 5 дней работала одна первая бригада, к ней присоединилась вторая, и обе вместе закончили
    работу. Сколько дней бригады работали вместе ?
    """
    # находим параметры к задаче и ответ
    while True:

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
        return {
            "condition": f"{gender[4]} {pers1} может {task} за {t1} {correct_word('день', t1)}. {gender[5]} {pers2} "
                         f"может выполнить ту же работу за {k}% этого времени. После того, как {delta_t} "
                         f"{correct_word('день', delta_t)} {gender[0]} только {gender[4].lower()} {pers1}, к "
                         f"{gender[1]} {gender[2]} {gender[5].lower()} {pers2}, "
                         f"и {gender[3]} закончили работу вместе. Сколько дней они работали вместе?",
            "answer": answer
        }
    else:
        return {
            "condition": f"{start_title(pers1)} может {task} за {t1} {correct_word('день', t1)}. {start_title(pers2)} "
                         f"может выполнить ту же работу за {k}% этого времени. После того, как {delta_t} "
                         f"{correct_word('день', delta_t)} {gender[0]} только {pers1}, к {gender[1]} {gender[2]} "
                         f"{pers2}, и {gender[3]} закончили работу вместе. Сколько дней {pers1} и {pers2} работали "
                         f"вместе?",
            "answer": answer
        }


def task_13023():
    """ Генерация аналогичных задач 13.023 М.И. Сканави:
    Однотипные детали обрабатываются на двух станках. Производительность первого станка на 40% больше производительности
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

    return {
        "condition": f"{start_title(pers1)} и {pers2} должны {task1} несколько {word1}. Производительность "
                     f"{pers1_gent} на {k}% выше производительности {pers2_gent}. {question}, если {gender[3]} "
                     f"{gender[4]} {t1} ч, а {gender[5]} - {t2} ч, причём всего они смогли {task1} {new_unit}{s} "
                     f"{word2}",
        "answer": answer
    }


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
        'км': (s, f'Найдите длину дороги.')
    }
    try:
        answer, question = units.get(unit, '')
        return {
            "condition": f"{start_title(pers)} может выполнить {a}/{b} заказа за {time1}. {start_title(pers)} "
                         f"работал(а) {time2}, после чего осталось {task1} еще {delta_s} {word2}. {question}",
            "answer": answer
        }
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

    # выбираем контекст
    while True:
        pers1, pers2, pers3, (task, measure) = input_parameters_work()
        if not pers1 == pers2 == pers3 and not pers1 == pers2 and not pers3 == pers2:
            break

    pers2_gent, pers3_gent = gent_pers((pers2, pers3))

    return {
        "condition": f"{start_title(pers1)}, {pers2} и {pers3} должны {task}. За {t1} работы {pers1} может выполнить "
                     f"{k1}% всей работы. {start_title(pers2)} за {t2} выполнит {k2}% всей работы. Скорости выполнения "
                     f"работы {pers2_gent} и {pers3_gent} относятся как {a}:{b}. За какое время будет выполнена вся "
                     f"работа, если они будут работать вместе?",
        "answer": answer
    }


def task_13033():
    """Генерация аналогичных задач 13.033, 13.226 М.И. Сканави:
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
    # выбираем контекст
    while True:
        i = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14])
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

    return {
        "condition": f"{start_title(pers1)} и {pers2} должны {task1} {new_unit}несколько {word2} - по {s} {word1} "
                     f"{gender[0]}. {gender[1]} может {task1} {a} {unit} за то же время, за которое {gender[2]} может "
                     f"{task1} {b} {unit}. Сколько {word2} может {task1} {gender[0]}, если {gender[1].lower()} "
                     f"{gender[3]} работу на {delta_t} ч быстрее?",
        "answer": answer
    }


def task_13037():
    """Генерация аналогичных задач 13.037 М.И. Сканави:
    Одна мельница может смолоть 19 ц пшеницы за 3 ч., другая 32 ц за 5 ч.а третья 10 ц за 2 часа. Как распределить 133
    тонны пшеницы между этими мельницами чтобы одновременно начав работу они окончили её также одновременно?"""
    # ищем ответ
    while True:
        # s = 133
        s = randint(10, 200)
        s1, s2, s3 = (randint(1, 100) for _ in range(3))
        t1, t2, t3 = (randint(1, 10) for _ in range(3))
        t = s / (s1/t1 + s2/t2 + s3/t3)
        x1, x2, x3 = s1 / t1 * t * 10, s2 / t2 * t * 10, s3 / t3 * t * 10
        if int(t * 60) - t * 60 == 0 and int(x1) - x1 == 0 and int(x2) - x2 == 0 and int(x3) - x3 == 0:
            break
    answer = (x1, x2, x3)
    # выбираем контекст
    while True:
        pers1, pers2, pers3, (task, measure) = input_parameters_work()
        if not pers1 == pers2 == pers3 and not pers1 == pers2 and not pers3 == pers2:
            break
    while True:
        i = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        # i = 11
        pers1, pers2, pers3, (task, measure) = input_parameters_work(i)
        if measure and (not pers1 == pers2 == pers3 or (not pers1 == pers2 and not pers3 == pers2)):
            meas_word, unit = measure
            break
        else:
            pers1, pers2, pers3, (task, measure) = input_parameters_work(i)

    task1, (word1, word2, word3, word4) = correct_word(key=task, values=(s1, s2, s3, s))

    if unit in ('м3', 'м2', 'км'):
        word1, word2, word3, word4, new_unit = unit, unit, unit, unit, meas_word + ' '
        task1 = task
    else:
        new_unit = ''

    return {
        "condition": f"{start_title(pers1)} может {task1} {new_unit}{s1} {word1} за {t1} ч, {pers2} - {s2} {word2} за "
                     f"{t2} ч, а {pers3} - {s3} {word3} за {t3} ч. Как распределить {s} {word4} между ними, чтобы "
                     f"одновременно начав работу, они закончили её также одновременно?",
        "answer": answer
    }


def task_13075():
    """Генерация аналогичных задач 13.075 М.И. Сканави:
    Двое рабочих за одну смену изготовили 72 детали. После увеличения производительности первого рабочего на 15%,
    а второго на 25%, они вместе за смену изготовили 86 деталей. Сколько деталей изготовляет каждый рабочий за смену
    после (или до) повышения производительности труда?"""
    # находим ответ
    while True:
        k1, k2 = (randint(5, 50) for _ in range(2))  # / 100
        if k1 == k2:
            k2 = 51 - k2
        s1, s2 = sorted(randint(10, 100) for _ in range(2))

        x2 = (s2 - (1 + k1 / 100) * s1) / (k2 - k1) * 100  # до
        x1 = s1 - x2  # до
        x2_new, x1_new = (1 + k2 / 100) * x2, (1 + k1 / 100) * x1  # после повышения производительности

        if int(x2) - x2 == 0 and int(x2_new) - x2_new == 0 and x1 > 0 and x2 > 0:
            break
    # выбираем вопрос
    question, answer = choice([
        ("до повышения производительности труда?", (x2, x1)),
        ("после повышения производительности труда?", (x2_new, x1_new)),
    ])
    # выбираем контекст
    i = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14])
    pers1, pers2, _, (task, _) = input_parameters_work(i)
    task1, (word1, word2, word3) = correct_word(key=task, values=(s1, s2, 10))
    pers1_gent, pers2_gent = gent_pers((pers1, pers2))

    word4 = 'каждая' if morph.parse(pers1.split()[0])[0].tag.gender == 'femn' else 'каждый'

    return {
        "condition": f"{start_title(pers1)} и {pers2} могут вместе {task1} {s1} {word1}. После увеличения "
                     f"производительности {pers1_gent} на {k1}%, а {pers2_gent} на {k2}%, они могут вместе {task1} "
                     f"{s2} {word2}. Сколько {word3} может {task1} {word4} из них {question}",
        "answer": answer
    }


def task_13135():
    """Генерация аналогичных задач 13.135 М.И. Сканави:
    Бригада слесарей может выполнить некоторое задание по обработке деталей на 15 ч быстрее, чем бригада учеников.
    Если бригада учеников отработает 18 ч, выполняя это задание, а потом бригада слесарей продолжит выполнение задания
    в течение 6 часов, будет выполнено только 0,6 всего задания. Сколько времени требуется бригаде учеников для
    самостоятельного выполнения этого задания?"""
    i = choice([0, 1, 2, 3, 4, 7, 9, 10, 11, 14])
    pers1, pers2, _, (task, _) = input_parameters_work(i)
    t1, t2, delta_t, k, (x, y) = solution_task_13135()
    word = 'каждой' if morph.parse(pers1.split()[0])[0].tag.gender == 'femn' else 'каждому'
    question, answer = choice([
        (f"Сколько времени потребуется {word} из них для самостоятельного выполнения всего задания?", (x, y)),
        (f"Сколько времени потребуется {gent_pers((pers1,), padej='datv')[0]} для самостоятельного выполнения всего "
         f"задания?", y),
        (f"Сколько времени потребуется {gent_pers((pers2,), padej='datv')[0]} для самостоятельного выполнения всего "
         f"задания?", x),
    ])
    return {
        "condition": f"{start_title(pers1)} и {pers2} должны выполнить задание: {task}, причем {pers1} может сделать "
                     f"это на {delta_t} мин быстрее, чем {pers2}. Если {pers2} будет выполнять задание {t1} мин, а "
                     f"потом {pers1} продолжит выполнение задания в течение {t2} мин, будет выполнено {k}% всей "
                     f"работы. {question}",
        "answer": answer
    }


def task_13137():
    """Генерация аналогичных задач 13.137 М.И. Сканави:
    Три машины разных систем выполняют некоторую счетную работу. Если всю работу поручить только одной второй или одной
    первой машине, то одна вторая машина затратит на выполнение всей работы двумя минутами больше, чем одна первая.
    Одна третья машина может выполнить всю работу за срок, вдвое больший, чем одна первая. Так как части работы однотипны,
    то всю работу можно поделить между тремя машинами. Тогда, работая вместе и закончив работу одновременно,
    они выполнят ее за 2 мин 40 с. За какое время может выполнить эту работу каждая машина, действуя отдельно?"""
    i = choice([0, 1, 2, 3, 4, 7, 9, 10, 14])
    pers1, pers2, pers3, (task, _) = input_parameters_work(i)
    delta_t, t, k, (x1, x2, x3) = solution_task_13137()
    word, word2 = ('каждой', 'одна') if morph.parse(pers1.split()[0])[0].tag.gender == 'femn' else ('каждому', 'один')
    question, answer = choice([
        (f"Сколько времени потребуется {word} из них для самостоятельного выполнения всей работы?", (x1, x2, x3)),
        (f"Сколько времени потребуется {gent_pers((pers1,), padej='datv')[0]} для самостоятельного выполнения всей "
         f"работы?", x1),
        (f"Сколько времени потребуется {gent_pers((pers2,), padej='datv')[0]} для самостоятельного выполнения всей "
         f"работы?", x2),
        (f"Сколько времени потребуется {gent_pers((pers3,), padej='datv')[0]} для самостоятельного выполнения всей "
         f"работы?", x3),
    ])
    return {
        "condition": f"{start_title(pers1)}, {pers2} и {pers3} должны выполнить работу: {task}. {word2.title()} "
                     f"{pers2} выполнит всю работу на {delta_t} мин дольше, чем {word2} {pers1}. {word2.title()} "
                     f"{pers3} может выполнить всю работу за время в {k} {correct_word('раз', k)} больше, чем {word2} "
                     f"{pers1}. Считаем, что работу между ними можно разделить на 3 равных части. {question}",
        "answer": answer
    }


def task_13140():
    """Генерация аналогичных задач 13.140 М.И. Сканави:
    На одном из двух станков обрабатывают партию деталей на три дня дольше, чем на другом. Сколько дней продолжалось
    бы обработка этой партии деталей каждым станком в отдельности, если при совместной работе на этих станках в 3 раза
    большая партия деталей была обработана за 20 дней?"""
    i = choice([0, 1, 2, 3, 4, 7, 9, 10, 14])
    pers1, pers2, pers3, (task, _) = input_parameters_work(i)
    delta_t, t, k, (x1, x2) = solution_task_13140()
    word = 'каждой' if morph.parse(pers1.split()[0])[0].tag.gender == 'femn' else 'каждому'
    question, answer = choice([
        (f"Сколько дней потребуется {word} из них для самостоятельного выполнения всего заказа", (x1, x2)),
        (f"Сколько дней потребуется {gent_pers((pers1,), padej='datv')[0]} для самостоятельного выполнения всего "
         f"заказа", x1),
        (f"Сколько дней потребуется {gent_pers((pers2,), padej='datv')[0]} для самостоятельного выполнения всего "
         f"заказа", x2),
    ])
    return {
        "condition": f"{start_title(pers1)} может выполнить заказ ({task}) на {delta_t} "
                     f"{correct_word('день', delta_t)} быстрее, чем {pers2}. {question}, если при совместной работе за "
                     f"{t} {correct_word('день', t)} будет выполнена работа объемом в {k} {correct_word('раз', k)} "
                     f"больше?",
        "answer": answer
    }


def task_13170():
    """Генерация аналогичных задач 13.170 М.И. Сканави:
    Одна тракторная бригада должна вспахать 240 га, а другая на 35% больше, чем первая. Первая бригада, вспахивая
    ежедневно на 3 га меньше второй, закончила работу на 2 дня раньше, чем вторая бригада. Сколько гектаров вспахивала
    каждая бригада ежедневно?"""
    while True:
        # i = 8
        i = choice([0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 14])
        pers1, pers2, _, (task, measure) = input_parameters_work(i)
        if measure:
            meas_word, unit = measure
            break
        else:
            pers1, pers2, _, (task, measure) = input_parameters_work(i)

    s, k, delta_x, delta_t, t, x = solution_task_13170()
    task1, (word1, word2) = correct_word(key=task, values=(s, 10))

    if unit in ('м3', 'м2', 'км'):
        word1, word2, new_unit = unit, unit, meas_word + ' '
        task1 = task
    else:
        new_unit = ''

    if morph.parse(pers1.split()[0])[0].tag.gender == 'femn':
        gender = ('должна', 'Первая', 'второй', 'вторая', 'каждая', 'работала')
    else:
        gender = ('должен', 'Первый', 'второго', 'второй', 'каждый', 'работал')

    question, answer = choice([
        (f"Сколько {word2} может {task1} {gender[4]} из них ежедневно?", (x, x + delta_x)),
        (f"Сколько дней {gender[5]} {gender[4]} из них?", (t, t + delta_t)),
    ])
    return {
        "condition": f"{start_title(pers1)} {gender[0]} {task1} {new_unit}{s} {word1}, а {pers2} на {k}% больше. "
                     f"{gender[1]} может {task1} на {x} {unit} в день меньше {gender[2]} и закончить работу на "
                     f"{delta_t} {correct_word('день', delta_t)} раньше, чем {gender[3]}. {question}",
        "answer": answer
    }


def task_13185():
    """Генерация аналогичных задач 13.185 М.И. Сканави:
    При испытании двух двигателей было установлено, что первый израсходовал 300 г, а второй 192 г бензина,
    причем второй работал на 2 ч меньше, чем первый. Первый двигатель затрачивает в час на 6 г бензина больше,
    чем второй. Какое количество бензина в час расходует каждый из двигателей?"""
    s1, s2, delta_x, delta_t, answer = solution_task_13185()
    while True:
        i = choice([0, 1, 2, 4, 6, 7, 8, 9, 10, 14])
        pers1, pers2, _, (task, measure) = input_parameters_work(i)
        if measure:
            meas_word, unit = measure
            break
        else:
            pers1, pers2, _, (task, measure) = input_parameters_work(i)

    task1, (word1, word2, word3) = correct_word(key=task, values=(s1, s2, delta_x))

    if unit in ('м3', 'м2', 'км'):
        word1, word2, word3, new_unit = unit, unit, unit, meas_word + ' '
        task1 = task
    else:
        new_unit = ''

    gender = 'каждой' if morph.parse(pers1.split()[0])[0].tag.gender == 'femn' \
        else 'каждого'

    return {
        "condition": f"{start_title(pers1)} может {task1} {new_unit}{s1} {word1}, а {pers2} - {new_unit}{s2} "
                     f"{word2}, причем {pers2} работает на {delta_t} ч меньше, чем {pers1} и может {task1} на "
                     f"{new_unit}{delta_x} {word3} в час больше. Какова скорость работы {gender} из них?",
        "answer": answer
    }


def task_13195():
    """Генерация аналогичных задач 13.195 М.И. Сканави:
    Бригада монтеров должна была прокладывать по 8 м кабеля в час и закончить работу в 4 часа дня. После того как
    половина всего задания была сделана, один рабочий выбыл из бригады, и бригада стала прокладывать по 6 м кабеля
    в час. В результате запланированная работы была выполнена в 6 часов вечера. Сколько метров кабеля было проложено
    и за сколько часов?"""
    x1, x2, k, delta_t, answer = solution_task_13195()
    while True:
        i = choice([0, 2, 4, 6, 9, 10, 14])
        pers, _, _, (task, measure) = input_parameters_work(i)
        if measure:
            meas_word, unit = measure
            break
        else:
            pers, _, _, (task, measure) = input_parameters_work(i)

    task1, (word1, word2, word3) = correct_word(key=task, values=(x1, 10, x2))

    if unit in ('м3', 'м2', 'км'):
        word1, word2, word3, new_unit = unit, unit, unit, meas_word + ' '
        task1 = task
    else:
        new_unit = ''
    gender = ('должна', 'она', 'смогла', 'ее') if morph.parse(pers.split()[0])[0].tag.gender == 'femn' \
        else ('должен', 'он', 'смог', 'его')

    return {
        "condition": f"{start_title(pers)} {gender[0]} {task1} {x1} {word1} в час и закончить работу вовремя. После "
                     f"того, как была выполнена 1/{k} всей работы, {gender[3]} работоспособность снизилась и теперь "
                     f"{gender[1]} может {task1} по {x2} {word3} в час. В результате работа была закончена на "
                     f"{delta_t} ч позже. Сколько всего {word2} {gender[1]} {gender[2]} {task1} и за сколько часов?",
        "answer": answer
    }


def task_13341():
    """Генерация аналогичных задач 13.341 М.И. Сканави:
    Трое рабочих участвовали в конкурсе. Первый и третий из них произвели продукции в 2 раза больше, чем второй,
    а второй и третий — в 3 раза больше, чем первый. Какое место занял каждый рабочий в конкурсе?
    В каком отношении находятся количества выработанной ими продукции?"""
    while True:
        pers1, pers2, pers3, (task, measure) = input_parameters_work()
        if not pers1 == pers2 == pers3 and not pers1 == pers2 and not pers3 == pers2 and measure:
            meas_word, unit = measure
            if unit == 'шт':
                break

    k1, k2 = randint(2, 10), randint(2, 10)
    answer = sorted((k1 + 1, k2 + 1, k1 * k2 - 1))
    task1, (word1, word2) = correct_word(key=task, values=(10, 10))
    return {
        "condition": f"{start_title(pers1)}, {pers2} и {pers3} участвуют в конкурсе. {start_title(pers1)} и {pers3} "
                     f"могут {task1} в {k1} {correct_word('раз', k1)} больше {word1}, чем {pers2}, а {pers2} и "
                     f"{pers3} - в {k2} {correct_word('раз', k2)} больше {word1}, чем {pers1}. Как распределились "
                     f"конкурсные места? В каком отношении находятся количества {word1}, которые они смогли {task1}?",
        "answer": answer
    }


def task_13292():
    """Генерация аналогичных задач 13.292, 13.293, 13.296 М.И. Сканави:
    Два «механических крота» разной мощности при одновременной работе с разных концов тоннеля могли бы прорыть его
    за 5 дней. В действительности оба «крота» были применены последовательно с одной стороны тоннеля, причем первый
    прорыл 1/3, а второй остальные 2/3 его длины. На выполнение всей работы ушло при этом 10 дней. За сколько дней
    каждый «крот», работая самостоятельно, мог бы прорыть тоннель?"""
    while True:
        pers1, pers2, _, (task, measure) = input_parameters_work()
        if not pers1 == pers2 and morph.parse(pers1.split()[0])[0].tag.gender == 'masc':
            break
    t1, t2, k, answer = solution_task_13292()
    return {
        "condition": f"{start_title(pers1)} и {pers2} должны вместе {task} за {t1} {correct_word('день', t1)}. В "
                     f"действительности они работали поочередно: {pers1} выполнил 1/{k} всей работы, а оставшуюся "
                     f"часть выполнил {pers2}. На выполнение всей работы ушло {t2} {correct_word('день', t2)}. За "
                     f"сколько дней каждый из них, работая самостоятельно, может {task}?",
        "answer": answer
    }


def task_13328():
    """Генерация аналогичных задач 13.328 М.И. Сканави:
    Бригада рыбаков намеревалась выловить в определенный срок 1800 ц рыбы. Треть этого срока был шторм, вследствие
    чего плановое задание ежедневно недовыполнялось на 20 ц. Однако в остальные дни бригаде удавалось ежедневно
    вылавливать на 20 ц больше дневной нормы, и плановое задание было выполнено за один день до срока. Сколько
    центнеров рыбы намеревалась вылавливать бригада рыбаков ежедневно?"""
    while True:
        pers1, _, _, (task, measure) = input_parameters_work()
        if morph.parse(pers1.split()[0])[0].tag.gender == 'masc' and measure:
            meas_word, unit = measure
            pers1 = pers1.split()[1] if 'первый' in pers1 else pers1
            if unit == 'шт':
                break

    s, delta_s, k, answer = solution_task_13328()
    task1, (word1, word2, word3) = correct_word(key=task, values=(s, delta_s, 10))
    return {
        "condition": f"{start_title(pers1)} должен {task1} {s} {word1}. 1/{k} рабочего времени его работоспособность "
                     f"была снижена, вследствие чего ежедневно он мог {task1} на {delta_s} {word2} меньше, чем обычно. "
                     f"Однако в остальные дни ему удалось восстановить силы и перевыполнять план на те же {delta_s} "
                     f"{word2} в день. Сколько {word3} изначально планировал {task1} {pers1} каждый день? ",
        "answer": answer
    }
