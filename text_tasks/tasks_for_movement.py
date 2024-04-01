from random import randint, choice
import numpy as np


def input_parameters_movements(i=None):
    """Функция возвращает набор входных параметров в задачи на движение"""
    i = randint(0, 2)
    values = {
        'pers1': ["спортсмен", "мотоциклист", "дельфин"],
        'action': ['выбежал', 'выехал', "выплыл"],
        'action1': ['пробегает', 'проезжает', "проплывает"],
        'place': ['круговой дорожки', "круглой трассы", "кругового бассейна"],
        'direction': ['в противоположных направлениях', 'в одном направлении']
    }
    return values['pers1'][i], values['action'][i], values['action1'][i], values['place'][i], choice(values['direction'])


def task_940():
    """Генерация аналогичной задачи с портала https://kuzovkin.info/one_exercise_1/940:
    Из двух диаметрально противоположных точек круговой беговой дорожки одновременно в одном направлении стартовали два
    спортсмена. Первый пробегает полный круг за 15 мин, а второй – за 20 мин. Через какое время после старта они встретятся первый раз?"""
    pers, action, action1, place, direction = input_parameters_movements()
    time1, time2 = (randint(10, 45) for _ in range(2))
    answer = 1.234
    if direction == 'в противоположных направлениях':
        while int(answer) - answer != 0:
            time1, time2 = np.random.randint(4, 100, size=2)
            answer = float(1 / (1 / time1 + 1 / time2) / 2)
    else:
        while int(answer * 1) - answer * 1 != 0:
            time1, time2 = np.random.randint(4, 100, size=2)
            time2 += time1
            answer = 1 / (1 / time1 - 1 / time2)
        # answer = str((Fraction(1, time1) - Fraction(1, time2)) ** (-1) / 2)

    return {
        "condition": f"Из двух диаметрально противоположных точек {place} одновременно {direction} {action}и два "
                     f"{pers}а. Первый {action1} полный круг за {time1} мин, второй - за {time2} мин. Через какое "
                     f"время они первый раз встретятся?",
        "answer": answer
    }
