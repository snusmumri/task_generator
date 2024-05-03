import math
import random


def cos_of_diff_in_degrees():
    """
    Для задач на вычисление косинуса разности, id = 14089, 14102, 14123
    """
    difference = random.choice([-90, -60, 60, 90, 120, 180])
    while True:
        x = random.randint(1, 200)
        y = x - difference
        if y > 0:
            break

    task = f"Вычислите \(\cos{x}^0\\cos{y}^0 + \sin{x}^0\sin{y}^0\)"
    answer = f"{round(math.cos(math.radians(x - y)), 1):g}"
    solution = (
        f"Решение: используем формулу косинуса разности "
        f"\(\cos(\\alpha - \\beta) = "
        f"\cos(\\alpha)\cos(\\beta) + \sin(\\alpha)\sin(\\beta)\). "
        f"\\\\"
        f"\(\cos{x}^0\\cos{y}^0 + \sin{x}^0\sin{y}^0 = "
        f"\cos({x}^0 - {y}^0) = "
        f"\cos{x - y}^0 = {answer}\)"
    )
    return {
        "condition": task,
        "answer": answer,
        "solution": solution
    }


def sin_of_summ_in_degrees():
    """
    Для задач на вычисление синуса суммы, id = 14101, 14104, 14105
    """
    s = random.choice([30, 90, 150, 180])
    x = random.randint(1, s - 1)
    y = s - x

    task = f"Вычислите \(\sin{x}^0\cos{y}^0 + \cos{x}^0\sin{y}^0\)"
    answer = f"{round(math.sin(math.radians(x + y)), 1):g}"
    solution = (
        f"Решение: используем формулу синуса суммы "
        f"\(\sin(\\alpha + \\beta) = "
        f"\sin(\\alpha)\cos(\\beta) + \cos(\\alpha)\sin(\\beta)\). "
        f"\\\\"
        f"\(\sin{x}^0\cos{y}^0 + \cos{x}^0\sin{y}^0 = "
        f"\sin({x}^0 + {y}^0) = "
        f"\sin{x + y}^0 = {answer}\)"
    )
    return {
        "condition": task,
        "answer": answer,
        "solution": solution
    }


def cos_of_sum_in_degrees():
    """
    Для задач на вычисление косинуса суммы, id = 14093, 14099, 14120
    """
    s = random.choice([60, 90, 120, 180])
    x = random.randint(1, s - 1)
    y = s - x

    task = f"Вычислите \(\cos{x}^0\cos{y}^0 - \sin{x}^0\sin{y}^0\)"
    answer = f"{round(math.cos(math.radians(x + y)), 1):g}"
    solution = (
        f"Решение: используем формулу косинуса суммы "
        f"\(\cos(\\alpha + \\beta) = "
        f"\cos(\\alpha)\cos(\\beta) - \sin(\\alpha)\sin(\\beta)\). "
        f"\\\\"
        f"\(\cos{x}^0\cos{y}^0 - \sin{x}^0\sin{y}^0 = "
        f"\cos({x}^0 + {y}^0) = "
        f"\cos{x + y}^0 = {answer}\)"
    )
    return {
        "condition": task,
        "answer": answer,
        "solution": solution
    }


def sin_of_diff_in_degrees():
    """
    Для задач на вычисление синуса разности, id = 14100, 14106, 14121
    """
    difference = random.choice([-90, -30, 30, 90, 150, 180])
    while True:
        x = random.randint(1, 200)
        y = x - difference
        if y > 0:
            break

    task = f"Вычислите \(\sin{x}^0\cos{y}^0 - \cos{x}^0\sin{y}^0\)"
    answer = f"{round(math.sin(math.radians(x - y)), 1):g}"
    solution = (
        f"Решение: используем формулу синуса суммы "
        f"\(\sin(\\alpha - \\beta) = "
        f"\sin(\\alpha)\cos(\\beta) - \cos(\\alpha)\sin(\\beta)\). "
        f"\\\\"
        f"\(\sin{x}^0\cos{y}^0 - \cos{x}^0\sin{y}^0 = "
        f"\sin({x}^0 - {y}^0) = "
        f"\sin{x - y}^0 = {answer}\)"
    )
    return {
        "condition": task,
        "answer": answer,
        "solution": solution
    }


def cos_of_diff_with_pi():
    """
    Для задач на вычисление косинуса разности в радианах, id = 14090
    """
    fraction = random.choice([1, 2, 3])  # для получения pi, pi/2 или pi/3

    a = random.randint(2, 10 // fraction)
    b = random.randint(1, min((10 - a) // fraction, 2))
    divisor = (a + b) * fraction

    b_str = "" if b == 1 else f"{b}"

    task = (f"Вычислите \("
            f"cos\\frac{{{a}\pi }}{{{divisor}}}"
            f"cos\\frac{{{b_str}\pi }}{{{divisor}}}"
            f"+sin\\frac{{{a}\pi }}{{{divisor}}}"
            f"sin\\frac{{{b_str}\pi }}{{{divisor}}}"
            f"\)")
    answer = f"{round(math.cos(math.pi / fraction), 1):g}"

    return {
        "condition": task,
        "answer": answer,
    }
