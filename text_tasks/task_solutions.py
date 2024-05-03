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


def solution_task_17610() -> tuple:
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
            return solution_task_17610()
    return discr, t, x


def solution_task_17596() -> tuple:
    """Функция подбора коэффициентов квадратного уравнения для получения целых корней
    s - запланированная производительность
    s1 - превышение s
    x - изменение времени
    y - изменение скорости"""
    while True:
        s, s1 = randint(1000, 10000), randint(10, 100)
        y, x = randint(10, 100), randint(1, 12)
        # s, s1 = 6000, 30
        # y, x = 70, 1
        # discr = 1300 ** 2
        a, b, c = y, -(s1 + x * y), -s * x
        discr = math.sqrt(b ** 2 - 4 * a * c)
        try:
            d = int(discr)
            if d - discr == 0 and discr < 10 ** 6:
                t = (-b + discr) / (2 * a)
                if int(t) - t == 0 and 0 < t <= 10 ** 4:
                    return s, s1, t, x, y
        except Exception:
            continue


def solution_task_17583() -> tuple:
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
            return solution_task_17583()
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


def solution_task_13170():
    cnt = 0
    while True:
        cnt += 1
        if cnt > 1000:
            return 240, 35, 3, 2, 10, 24
        s = randint(10, 500)
        k = randint(10, 99)
        s2 = s * (1 + k / 100)
        if int(s2) - s2 == 0:
           delta_x, delta_t = randint(1, 10), randint(1, 10)
           a = delta_x
           b = s2 - s + delta_x * delta_t
           c = s * delta_t
           discr = b**2 - 4 * a * c
           if discr >= 0:
               discr = math.sqrt(discr)
               if int(discr) - discr == 0:
                t = (b - discr) / (2 * a)
                x = s / t
                if int(x) - x == 0 and int(t) - t == 0 and x > 0 and t > 0:
                    return s, k, delta_x, delta_t, int(t), int(x)


def solution_task_13185():
    cnt = 0
    while True:
        cnt += 1
        if cnt > 1000:
            return 450, 288, 6, 3, (30, 24)
        s1, s2 = sorted((randint(10, 1000), randint(10, 1000)), reverse=True)
        delta_x, delta_t = randint(1, 10), randint(1, 10)
        a, c = delta_t, s1 * delta_x
        b = -(delta_x * delta_t + s1 - s2)
        discr = b ** 2 - 4 * a * c
        if discr >= 0:
            discr = math.sqrt(discr)
            if int(discr) - discr == 0:
                x1, x2 = (-b + discr) / (2 * a), (-b - discr) / (2 * a)
                if int(x1) - x1 == 0 and x1 > 0:
                    return s1, s2, delta_x, delta_t, (int(x1), int(x1 - delta_x))
                elif int(x2) - x2 == 0 and x2 > 0:
                    return s1, s2, delta_x, delta_t, (int(x2), int(x2 - delta_x))


def solution_task_13195():
    cnt = 0
    while True:
        cnt += 1
        if cnt > 1000:
            return 8, 6, 2, 2, (96, 14)
        x1, x2 = sorted((randint(1, 10), randint(1, 10)), reverse=True)
        delta_t = randint(1, 10)
        k = randint(2, 9)
        t = x2 * delta_t / ((1 / k) * (x1 - x2))
        if int(t) - t == 0 and t > 0:
            s = x1 * t
            return x1, x2, k, delta_t, (s, t + delta_t)


def solution_task_13292():
    cnt = 0
    while True:
        cnt += 1
        if cnt > 5000:
            return 5, 10, 3, (15, 7.5)
        k = randint(2, 10)
        k1, k2 = 1 / k, (k - 1) / k
        t1, t2 = sorted((randint(1, 100), randint(1, 100)))
        a = t1 * t2
        b = t1 * (k1 - k2) - t2
        c = k2
        discr = b ** 2 - 4 * a * c
        if discr >= 0:
            discr = math.sqrt(discr)
            if int(discr * k) - discr * k == 0:
                y1, y2 = (-b + discr) / (2 * a), (-b - discr) / (2 * a)
                x1, x2 = 1 / t1 - y1, 1 / t1 - y2
                if y1 > 0 and x1 > 0:
                    x, y = x1, y1
                elif y2 > 0 and x2 > 0:
                    x, y = x2, y2
                else:
                    x, y = None, None
                if x:
                    tx, ty = 1 / x, 1 / y
                    if int(tx) - tx == 0 and int(ty) - ty == 0:
                        return t1, t2, k, (tx, ty)


def solution_task_13328():
    cnt = 0
    while True:
        cnt += 1
        if cnt > 5000:
            return 1800, 20, 3, 100
        s, delta_s = randint(100, 5000), randint(10, 100)
        k = randint(2, 10)
        k1, k2 = 1 / k, (k - 1) / k
        b = delta_s
        c = s * delta_s * (k1 - k2)
        discr = b ** 2 - 4 * c
        if discr >= 0:
            discr = math.sqrt(discr)
            if int(discr) - discr == 0:
                x = (-b + discr) / 2
                if x > 0:
                    return s, delta_s, k, x
