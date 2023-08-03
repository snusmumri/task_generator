import math
from random import randint, choice
import numpy as np
from pprint import pprint
from pymorphy2 import MorphAnalyzer
from fractions import Fraction


def input_parameters(i=None, direction=False):
    """Функция возвращает набор входных параметров в текстовые задачи"""
    if direction:
        i = randint(0, 2)
        values = {
            'pers1': ["спортсмен", "мотоциклист", "дельфин"],
            'action': ['выбежал', 'выехал', "выплыл"],
            'action1': ['пробегает', 'проезжает', "проплывает"],
            'place': ['круговой дорожки', "круглой трассы", "кругового бассейна"],
            'direction': ['в противоположных направлениях', 'в одном направлении']
        }
        return values['pers1'][i], values['action'][i], values['action1'][i], values['place'][i], choice(values['direction'])

    # случайным образом получаем сюжет задачи
    i = i if i is not None else randint(0, 11)
    values = {
        'pers1': ["студент Саша", "Карлсон", 'дровосек Миша', "блогер Коля", "Федя", "певец Паша", "медбрат Вова", "лев", "первый рабочий", "токарь Миша", "швея Аня", "первая труба"],
        'pers2': ["студент Петя", "Малыш", "дровосек Коля", "блогер Толя", "Паша", "певец Саша", "медбрат Рома", "волк", "второй рабочий", "токарь Вася", "швея Оля", "вторая труба"],
        'pers3': ["студентка Кристина", "Фрекен Бок", "дровосек Саша", "блогер Лева", "Вася", "певица Настя",  "медсестра Вика", "пес", "третий рабочий", "токарь Гера", "швея Юля", "третья труба"],
        'task': [["изготовить образец для измерений", "съесть пиццу", "провести измерения", "решить задачу", "выплавить сплав", 'отшлифовать образцы'],
                 ["распугать воров", "сварить варенье", "съесть торт", "съесть плюшки"],
                 ["снять обзор на топоры", "наколоть дров", "срубить дерево", "донести хворост"],
                 [f'снять видео {choice(["в TikTok", "на YouTube", "в Инстаграм"])}', 'написать для публикации текст',
                  f'снять обзор на {choice(["машину", "ресторан", "игру", "квартиру"])}', "снять фильм"],
                 ["прополоть грядку", "покрасить забор", 'сделать заготовки на зиму', "отремонтировать машину"],
                 ["сыграть концерт", "сочинить песню", "выступить на фестивале", "сочинить к музыке стихи"],
                 ["оказать помощь пациенту", "поставить укол", "смешать физраствор", "сменить повязку больному", "сделать перевязку"],
                 ["съесть овцу", "съесть курицу"],
                 ["покрасить забор", "выполнить заказ", "починить санузел"],
                 ["выточить деталь", "починить станок", "обработать деталь", "заточить сверло"],
                 ["сшить кофту", "сшить костюм на хэллоуин", "сшить костюм на ComicCon", "сшить костюм для кота"],
                 ["наполнить бассейн"],
                 ]
        }
    return values['pers1'][i], values['pers2'][i], values['pers3'][i], choice(values['task'][i])


def task_9515():
    """Генерация аналогичной задачи с портала https://kuzovkin.info/one_exercise_1/9515:
     Лев съел овцу за 2 ч, волк съел овцу за 3 ч, а пёс съел овцу за 6 ч. Как скоро они втроём съели бы одну овцу?
     """
    # получаем сюжет задачи
    pers1, pers2, pers3, task = input_parameters()
    answer = 1.2345678
    # случайным образом получаем ответ к задаче
    while int(answer * 1) - answer * 1 != 0:
        time1, time2, time3 = np.random.randint(4, 100, size=3)
        answer = 1 / (1 / time1 + 1 / time2 + 1 / time3)
    return answer, f"{pers1.title()} может {task} за {time1} ч, {pers2} может {task} за {time2} ч, " \
                   f"{pers3} - за {time3} ч. За какое время они втроем могут {task}?"


def task_9517():
    """Генерация аналогичной задачи с портала https://kuzovkin.info/one_exercise_1/9517:
     Маша и Оля пропалывают грядку за 12 мин, а одна Оля – за 15 мин. За сколько минут пропалывает грядку одна Маша?
     """
    # получаем сюжет задачи
    pers1, pers2, _, task = input_parameters()
    answer = 1.2345678
    while int(answer * 1) - answer * 1 != 0:
        time1, time2 = np.random.randint(5, 100, size=2)
        time2 += time1
        answer = time1 * time2 / (time2 - time1)
    return answer, f"{pers1.title()} и {pers2} могут {task} за {time1} мин, " \
           f"а 1 {pers1} - за {time2} мин. За сколько минут может {task} {pers2}?"


def task_11101():
    """Генерация аналогичной задачи с портала https://kuzovkin.info/one_exercise_1/11101:
    Бассейн при одновременном включении трех труб может наполниться за 4 ч, через одну первую трубу – за 10 ч,
    а через одну вторую – за 15 ч. За сколько часов может наполниться бассейн через одну третью трубу?"""
    # получаем сюжет задачи
    pers1, pers2, pers3, task = input_parameters()
    answer = 1.23456
    # случайным образом получаем ответ к задаче
    while int(answer * 1) - answer * 1 != 0:
        time1, time2, time3 = sorted(np.random.randint(4, 100, size=3))
        answer = 1 / (1 / time1 - 1 / time2 - 1 / time3)
        if answer <= 0:
            answer = 1.23456
    return answer, f"{pers1.title()}, {pers2} и {pers3} вместе могут {task} за {time1} ч. {pers1} может {task} за {time2} ч, " \
                   f"а {pers2} – за {time3} ч. За сколько часов это сделает {pers3}?"


def task_11108():
    """Генерация аналогичной задачи с портала https://kuzovkin.info/one_exercise_1/11108:
    Вася и Лева могут покрасить забор за 3 часа, Лева и Петя могут покрасить этот же забор за 6 часов,
    а Петя и Вася – за 4 часа. За какое время мальчики покрасят забор, работая втроем?"""
    pers1, pers2, pers3, task = input_parameters()
    answer = 1.2345678
    # случайным образом получаем ответ к задаче
    while int(answer * 1) - answer * 1 != 0:
        time1, time2, time3 = np.random.randint(4, 100, size=3)
        answer = 2 / (1 / time1 + 1 / time2 + 1 / time3)
    return answer, f"{pers1.title()} и {pers2} могут {task} за {time1} ч. {pers2} и {pers3} могут {task} за {time2} ч, " \
                   f"а {pers1} и {pers3} - за {time3} ч. За какое время они могут {task}, работая вместе?"


def task_940():
    """Генерация аналогичной задачи с портала https://kuzovkin.info/one_exercise_1/940:
    Из двух диаметрально противоположных точек круговой беговой дорожки одновременно в одном направлении стартовали два
    спортсмена. Первый пробегает полный круг за 15 мин, а второй – за 20 мин. Через какое время после старта они встретятся первый раз?"""
    pers, action, action1, place, direction = input_parameters(direction=True)
    time1, time2 = (randint(10, 45) for _ in range(2))
    answer = 1.234
    if direction == 'в противоположных направлениях':
        while int(answer * 1) - answer * 1 != 0:
            time1, time2 = np.random.randint(4, 100, size=2)
            answer = float(1 / (1 / time1 + 1 / time2) / 2)
    else:
        while int(answer * 1) - answer * 1 != 0:
            time1, time2 = np.random.randint(4, 100, size=2)
            time2 += time1
            answer = 1 / (1 / time1 - 1 / time2)
        # answer = str((Fraction(1, time1) - Fraction(1, time2)) ** (-1) / 2)
    return answer, f"Из двух диаметрально противоположных точек {place} одновременно {direction} {action}и два {pers}а. " \
                   f"Первый {action1} полный круг за {time1} мин, второй - за {time2} мин. Через какое время они первый раз встретятся?"


def task_936():
    """Генерация аналогичных задач 936, 9518 с портала https://kuzovkin.info/one_exercise_1/936:
    Каждый из двух рабочих одинаковой квалификации может выполнить заказ за 12 часов. Через 4 часа после того,
    как один из них приступил к выполнению заказа, к нему присоединился второй рабочий, и работу над заказом они довели
    до конца уже вместе. За сколько часов был выполнен весь заказ?"""
    # исключаем женский род персонажей
    i = choice([0, 1, 2, 3, 5, 6, 7])
    # выбираем сюжет
    pers1, pers2, _, task = input_parameters(i)
    time1 = choice([i for i in range(1, 20) if not i % 2])
    time2 = time1 * randint(1, 10)
    # получаем ответ
    answer = time1 + (time2 - time1) / 2
    return answer, f"{pers1.title()} и {pers2} должны {task}. Каждый из них способен сделать это за {time2} ч. " \
                   f"Через {time1} ч после того, как {pers1} начал делать это в одиночку, к нему присоединился {pers2}, " \
                   f"и они закончили вместе. За сколько часов задача была выполнена?"


def choose_discr() -> tuple:
    """Функция подбора коэффициентов квадратного уравнения для получения целых корней"""
    discr = choice(tuple(i ** 2 for i in range(100)))
    s = 1.233
    # счетчик на случай, если к случайно выбранному значению дискриминанта нельзя подобрать подходящие коэффициенты
    cnt = 0
    while int(s) - s != 0:
        x, y = (randint(2, 15) for _ in range(2))
        s = (discr - (x * y) ** 2) / (4 * x * y)
        cnt += 1
        if s <= 0:
            s = 1.234
        if cnt > 100:
            return choose_discr()
    return discr, x, y, s


def correct_word(key, values) -> str:
    """Функция для подбора правильных склонений слов"""
    words_collection = {
        'раз': ['раз', 'раза', 'раз'],
        'день': ['день', 'дня', 'дней']
    }
    if key in words_collection:
        words = words_collection.get(key)
        if all((values % 10 == 1, values % 100 != 11)):
            return words[0]
        elif all((2 <= values % 10 <= 4,
                  any((values % 100 < 10, values % 100 >= 20)))):
            return words[1]
        return words[2]
    else:
        task1, task2 = key.rsplit(' ', maxsplit=1)
        morph = MorphAnalyzer()
        result = []
        for value in values:
            if all((value % 10 == 1, value % 100 != 11)):
                result.append(morph.parse(task2)[0].inflect({'accs'}).word)
            elif all((2 <= value % 10 <= 4,
                      any((value % 100 < 10, value % 100 >= 20)))):
                result.append(morph.parse(task2)[0].inflect({'gent'}).word)
            else:
                try:
                    result.append(morph.parse(task2)[0].inflect({'gent', 'plur'}).word)
                except AttributeError:
                    result.append(morph.parse(task2)[0].inflect({'gent'}).word)
        print(result)
        return task1, result[0], result[1]


def task_2610():
    """Генерация аналогичных задач 2610, 2611, 6482 с портала https://kuzovkin.info/one_exercise_1/2610:
    Токарь должен был обработать 120 деталей к определённому сроку. Применив новый резец, он стал обтачивать в час
    на 20 деталей больше и поэтому закончил работу на 1ч раньше срока. Сколько деталей он должен был обрабатывать по плану?"""
    # исключаем женский род персонажей
    i = randint(0, 9)
    # выбираем сюжет
    pers, _, _, task = input_parameters(i)
    # подбираем дискриминант, чтобы получить ответ в целых числах
    discr, x, y, s = choose_discr()
    v = (-(x * y) + math.sqrt(discr)) / (2 * y)
    t = s / v
    # делаем множественное число
    task1, word1, word2 = correct_word(key=task, values=(int(s), x))
    # выбираем вопрос и ответ к задаче
    answer, question = choice([(v, 'За сколько дней он выполнит задачу'), (t, 'Сколько раз в день он должен был делать это по плану')])
    return answer, f"{pers.title()} должен {task1} {int(s)} {word1} - по несколько в день. Когда он приступил к работе, оказалось, " \
                   f"что он может {task1} на {x} {word2} больше запланированного количества в день " \
                   f"и завершить процесс на {y} {correct_word('день', y)} раньше срока. {question}?"


def task_17612():
    """Генерация аналогичных задач 17612 с портала https://kuzovkin.info/one_exercise_1/17612:
    Колхоз должен был засеять поле за 4 дня. Перевыполняя ежедневно норму сева на 12 га, колхозники закончили сев
    за 1 день до срока. Сколько гектаров засевал колхоз ежедневно?"""
    # исключаем женский род персонажей
    i = randint(0, 9)
    # выбираем сюжет
    pers, _, _, task = input_parameters(i)
    # подбираем целочисленный ответ
    v = 1.2345
    while int(v) - v != 0:
        x, y, t = (randint(1, 20) for _ in range(3))
        v = (x * t - x * y) / y
        if v <= 0:
            v = 1.2345
    # получаем ответ
    answer = v + x
    # делаем множественное число
    task1, word1, word2 = correct_word(key=task, values=(10, x))
    return answer, f"{pers.title()} должен был за {t} {correct_word('день', t)} {task1} несколько {word1}. " \
                   f"Перевыполняя ежедневную норму на {x} {word2}, он закончил на {y} " \
                   f"{correct_word('день', y)} раньше срока. Сколько раз в день он делал поставленную задачу? "


if __name__ == "__main__":
    # print(task_9515())
    # print(task_9517())
    # print(task_11101())
    # print(task_11108())
    # print(task_940())
    # pprint(task_936())
    pprint(task_2610())
    pprint(task_17612())