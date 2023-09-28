from fractions import Fraction
from random import randint, choice
import math


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


def solution_task_745():
    k, cnt2 = 1, 0
    while True:
        x, y = randint(1, 20), randint(1, 20)
        t = x * y / (x + y)
        if int(t * 60) - t * 60 == 0:
            while not k < 1:
                cnt2 += 1
                t1, t2 = randint(1, 20), randint(1, 20)
                k = Fraction(t1, x) + Fraction(t2, x)

                if cnt2 > 100:
                    return solution_task_745()
            return x, y, t, t1, t2, str(k)


def solution_task_13135():
    """
    x - производительность второго персонажа (он выполняет работу дольше)
    y - производительность первого персонажа (того что быстрее)
    """
    discr = choice(tuple(i ** 2 for i in range(100)))
    cnt = 0
    while True:
        cnt += 1
        t1, delta_t, t2 = (randint(1, 50) for _ in range(3))
        k = randint(10, 99)
        # t1, t2, delta_t = 18, 6, 15
        # k = 60
        a = k / 100
        b = t1 + t2 + a * delta_t
        c = delta_t * t1
        result = b ** 2 - 4 * a * c
        if result == discr:
            x1, x2 = (b + math.sqrt(discr)) / (2 * a), (b - math.sqrt(discr)) / (2 * a)
            y1, y2 = x1 - delta_t, x2 - delta_t
            if x1 > 0 and y1 > 0 and int(x1) - x1 == 0:
                return t1, t2, delta_t, k, (x1, y1)
            elif x2 > 0 and y2 > 0 and int(x2) - x2 == 0:
                return t1, t2, delta_t, k, (x2, y2)
        if cnt == 100:
            discr = choice(tuple(i ** 2 for i in range(100)))
            cnt = 0


def solution_task_13137():
    # delta_t = 2
    # k = 2
    # t = 8 / 3
    while True:
        delta_t, t = (randint(1, 60) for _ in range(2))
        k = choice([2, 3, 4, 5])
        a = k
        b = k * delta_t - t * (2 * k + 1)
        c = - delta_t * t * (k + 1)
        discr = math.sqrt(b ** 2 - 4 * a * c)
        if int(discr) - discr == 0:
            x1 = (- b + discr) / (2 * a)
            x2 = (- b - discr) / (2 * a)
            if (x1 > 0 and int(x1) - x1 == 0) or (x2 > 0 and int(x2) - x2 == 0):
                x = x1 if x1 > 0 else x2
                return delta_t, t, k, (x, delta_t + x, k * x)


def solution_task_13140():
    while True:
        delta_t, t = randint(1, 10), randint(1, 30)
        k = choice([2, 3, 4, 5])
        a, b, c = k, k * delta_t - 2 * t, -delta_t * t
        discr = math.sqrt(b ** 2 - 4 * a * c)
        if int(discr) - discr == 0:
            x1 = (- b + discr) / (2 * a)
            x2 = (- b - discr) / (2 * a)
            if (x1 > 0 and int(x1) - x1 == 0) or (x2 > 0 and int(x2) - x2 == 0):
                x = x1 if x1 > 0 else x2
                return delta_t, t, k, (x, delta_t + x)
