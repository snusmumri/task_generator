import random
from fractions import Fraction
import math


def random_logarythm():
  '''
  функция дает простейший пример логарифма с ответом с портала https://kuzovkin.info/one_exercise_1/9596
  9596, 10991,11644,11890,14383,14503
  вычислите: log_{2}{1}
  '''
  degree_of_logarithm = 1239999
  while degree_of_logarithm>15000:
    base_of_logarythm = random.randint(2,21)
    answer = random.randint(0,9)
    degree_of_logarithm = base_of_logarythm**answer
    task = r'Вычислите: \(log_{'+ str(base_of_logarythm)+"}{"+str(degree_of_logarithm)+"} \)"

  return {
      "condition": task,
      "answer": answer
    }


def logarithm_with_fractions():  # 1
    '''
    id 9682, 9965 12242, 12712
    логарифм с аргументом в виде обыкновенной дроби (1/x)
    '''
    denominator = float('+inf')
    while denominator > 1000:
        base = random.randint(2, 21)
        answer = random.randint(-9, -1)
        numerator = 1
        denominator = base ** abs(answer)
        task = f"Вычислите: $\\log_{{{base}}}{{\\frac{{{numerator}}}{{{denominator}}}}}$"
    return {
      "condition": task,
      "answer": answer
    }


def logarithm_fractions():  # 2
    '''
    id 139093, 14012
    логарифм с дробным аргументом и основанием
    '''

    base = Fraction(1, 1)
    argument = Fraction(100000, 100000)
    answer = 0

    while answer in [0, 1] or base.numerator == base.denominator or argument.denominator >= 1000 or \
            argument.numerator >= 1000 or argument.denominator == 1:

        answer = random.randint(-8, 8)
        base = Fraction(random.randint(1, 10), random.randint(2, 15))
        argument = base ** answer

        if base.numerator / base.denominator in [0.1, 0.15, 0.125, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
            formatted_base = f"{base.numerator / base.denominator}"
        else:
            formatted_base = f"\\frac{{{base.numerator}}}{{{base.denominator}}}"

        if argument.numerator / argument.denominator in [0.1, 0.15, 0.125, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8,
                                                         0.9]:
            formatted_argument = f"{argument.numerator / argument.denominator}"
        else:
            formatted_argument = f"\\frac{{{argument.numerator}}}{{{argument.denominator}}}"

    task = f"Вычислите: $\\log_{{{formatted_base}}}{{{formatted_argument}}}$"

    return {
      "condition": task,
      "answer": answer
    }


def logarithm_summ():  # 3
    '''
    id 14069
    сумма простейших логарифмов
    '''
    argument = float('+inf')
    while argument >= 1000:
        answer = random.randint(2, 8)
        base = random.randint(2, 16)
        argument = base ** answer

        factors = []
        divisor = 2
        tmp = argument
        while tmp > 1:
            while tmp % divisor == 0:
                factors.append(divisor)
                tmp //= divisor
            divisor += 1

        factor_pairs = []
        for factor in factors:
            pair = (factor, argument // factor)
            factor_pairs.append(pair)

        unique_factor_pairs = list(set(factor_pairs))
        selected_pair = random.choice(unique_factor_pairs)

        if random.choice([True, False]):
            selected_pair = (selected_pair[1], selected_pair[0])

    task = f"Вычислите: $\\log_{{{base}}}{{{selected_pair[0]}}} + \\log_{{{base}}}{{{selected_pair[1]}}}$"
    return {
      "condition": task,
      "answer": answer
    }


def logarithm_difference():  # 4
    '''
    id 14510
    разница простейших логарифмов
    '''
    num1, num2 = 1, 1
    while num1 >= 1000 or num2 >= 1000 or num2 == 1:
        base = random.randint(2, 16)
        answer = random.randint(-8, -1)
        argument = Fraction(1, base ** abs(answer))
        coefficient = random.randint(2, 10)
        num1 = argument.numerator * coefficient
        num2 = argument.denominator * coefficient
    task = f"Вычислите: $\\log_{{{base}}}{{{num1}}} - \\log_{{{base}}}{{{num2}}}$"
    return {
      "condition": task,
      "answer": answer
    }


def logarithm_summ_with_coefficient():  # 5
    '''
    id 14514
    сумма логарифмов с коэффициентом
    '''
    base, degree_arg, argument, degree = 1000000, 1, 1, 1,
    while math.gcd(base ** degree_arg, argument) != 1 or math.gcd(base,
                                                                  argument ** degree) != 1 or argument ** degree >= 1000 or base ** degree_arg >= 1000:
        base = random.randint(2, 16)
        degree = random.randint(2, 6)
        argument = random.randint(2, 10)
        degree_arg = random.randint(2, 6)
        task = f"Вычислите: $log_{{{base}}}({{{argument ** degree}}}) + {degree}log_{{{base}}}\\frac{{{base ** degree_arg}}}{{{argument}}}$"
        answer = round(degree * round(math.log(base ** degree_arg, base)))
    return {
      "condition": task,
      "answer": answer
    }


def logarithm_difference_with_coefficient():  # 6
    '''
    id 14515
    сумма логарифмов с коэффициентом
    '''

    argument = (100000, 10000)
    while argument[0] >= 1000 or argument[1] >= 1000:
        base = random.randint(2, 16)
        argument = (base ** random.randint(2, 9), 1)
        answer = round(math.log(argument[0], base))
        coefficient = random.choice([4, 9, 16, 25, 36])
        argument = argument[0] * coefficient, argument[1] * coefficient
        task = f"Вычислите: $log_{{{base}}}({{{argument[0]}}}) - {int(argument[1] ** 0.5)}log_{{{base}}}({{{int(argument[1] ** 0.5)}}})$"

    return {
      "condition": task,
      "answer": answer
    }


def logarithm_difference_summ():  # 7
    '''
    id 14516
    сумма и разница трех логарифмов
    '''
    argument = 1000
    base = 2
    num1, num2, num3 = 2, 2, 2
    while argument >= 1000 or math.log(num1, base) == round(math.log(num1, base)) or math.log(num2, base) == round(
            math.log(num2, base)) or math.log(num3, base) == round(math.log(num3, base)):
        base = random.randint(2, 16)
        argument = base ** random.randint(2, 9)
        answer = round(math.log(argument, base))
        num2 = random.randint(2, argument - 1)
        gcd = math.gcd(argument, num2)
        while gcd == 1:
            num2 = random.randint(2, argument - 1)
            gcd = math.gcd(argument, num2)

        num1 = argument // gcd
        num2 = num2 // gcd
        num3 = num2 * gcd
        task = f"Вычислите: $log_{{{base}}}({{{num1}}}) - log_{{{base}}}({{{num2}}}) + log_{{{base}}}({{{num3}}}) $"
    return {
      "condition": task,
      "answer": answer
    }


def logarithm_of_logarithm():  # 8
    '''
    id 14518, 14520, 14522
    взятие логарифма от логарифма
    '''
    situation = random.randint(1, 2)
    if situation == 1:
        base_first = Fraction(1, 1)
        base_second = Fraction(1, 1)
        while base_first.numerator >= base_first.denominator or base_first.numerator > 100 or base_first.denominator > 100 or base_second.denominator >= 1000 or base_second.numerator >= 1000 or base_second >= 1000:
            base_first = Fraction(random.randint(1, 10), random.randint(2, 10))
            if random.choice([True, False]):
                num = random.randint(2, 9)
                base_second = num ** base_first.denominator
                argument_second = num ** base_first.numerator

                base_second_formatted = str(base_second)
                argument_second_formatted = str(argument_second)
            else:
                num = Fraction(1, random.randint(2, 10))
                base_second = Fraction(1, num.denominator ** base_first.denominator)
                argument_second = Fraction(1, num.denominator ** base_first.numerator)

                base_second_formatted = f"\\frac{{{base_second.numerator}}}{{{base_second.denominator}}}"
                argument_second_formatted = f"\\frac{{{argument_second.numerator}}}{{{argument_second.denominator}}}"

            degree = random.randint(1, 3)
            base_first **= degree
            bases_first_formatted = f"\\frac{{{base_first.numerator}}}{{{base_first.denominator}}}"
            answer = degree

        task = f"Вычислите: $\\log_{{{bases_first_formatted}}}\\left(\\log_{{{base_second_formatted}}}{{{argument_second_formatted}}}\\right)$"
    if situation == 2:
        argument_second = Fraction(1, 100000)

        while argument_second.denominator >= 1000:
            base_first = random.randint(2, 10)
            base_second = Fraction(1, random.randint(2, 10))
            argument_second = Fraction(1, base_second.denominator ** base_first)
            root = random.randint(2, 8)
            answer = root
            base_second_formatted = f"\\frac{{{base_second.numerator}}}{{{base_second.denominator}}}"
            argument_second_formatted = f"\\frac{{{argument_second.numerator}}}{{{argument_second.denominator}}}"
            base_first_formatted = f"\\sqrt[{root}]{{{base_first}}}"
        task = f"Вычислите: $\\log_{{{base_first_formatted}}}\\left(\\log_{{{base_second_formatted}}}{{{argument_second_formatted}}}\\right)$"

    return {
      "condition": task,
      "answer": answer
    }


def logarithmic_identity():  # 9
    '''
    id 14525, 14526, 14528
    сумма и разница трех логарифмов
    '''
    answer, base = 0, 0
    while answer == base:
        answer = random.randint(2, 50)
        if random.choice([True, False]):
            base = random.randint(2, 16)
        else:
            base = random.choice([[0.1, 0.15, 0.125, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8,
                                   0.9]])
        task = f"Вычислите: ${{{base}}}^{{log_{{{base}}}({{{answer}}})}}$"
    return {
      "condition": task,
      "answer": answer
    }


def logarithmic_identity_with_multiplication():  # 10
    '''
    id 14536
    основное тождество + произведение логарифмов
    '''
    base_first, base_second, argument_first = 0, 0, 0
    while base_first == base_second or argument_first >= 1000:
        base_first = random.randint(2, 50)
        base_second = random.randint(2, 50)
        argument_first = random.randint(4, 16)
        coefficient = random.randint(2, 6)
        argument_first *= coefficient
        argument_second = Fraction(1, coefficient)
        answer = float(argument_first * argument_second)
        if answer % 1 == 0:
            answer = int(answer)

    task = f"Вычислите: ${{{base_first}}}^{{log_{{{base_first}}}({{{argument_first}}})}} ⋅ {{{base_second}}}^{{log_{{{base_second}}}({{{argument_second}}})}}$"
    return {
      "condition": task,
      "answer": answer
    }


def logarithmic_identity_with_difference():  # 11
    '''
    id 14537
    основное тождество + разница логарифмов
    '''

    start = 0.05
    stop = 1
    step = 0.05
    sample = []

    current = start
    while current <= stop:
        sample.append(round(current, 3))
        current += step

    base_first, base_second = 0, 0
    while base_first == base_second:
        base_first = random.choice(sample)
        base_second = random.randint(2, 16)
        argument_first = random.randint(2, 50)
        argument_second = random.randint(2, 50)
        answer = argument_first - argument_second
    task = f"Вычислите: $({{{base_first}}})^{{log_{{{base_first}}}({{{argument_first}}})}} - {{{base_second}}}^{{log_{{{base_second}}}({{{argument_second}}})}}$"
    return {
      "condition": task,
      "answer": answer
    }


def simple_calculation_logarithms():  # 12
    '''
    id 14542 - 14547
    вычисление одиночного логарифма с корнем
    '''
    answer = 10000

    situation = random.randint(1, 4)
    if situation == 1:
        while answer >= 1000 or answer <= -800 or before_root >= 1000 or answer != round(answer,
                                                                                         2) or in_root ** 0.5 == int(
            in_root ** 0.5):
            base = random.randint(2, 15)
            before_root = base ** random.randint(1, 2)
            in_root = base
            part_first = f"\\frac{{1}}{{{{{base}}}}}"
            part_second = f"{{{before_root}}}\\sqrt{{{{{in_root}}}}}"
            answer = round(math.log(before_root ** 2 * in_root, 1 / base)) * (1 / 2)
    if situation == 2:
        while answer >= 1000 or answer <= -800 or argument >= 1000 or in_root ** 0.5 == int(in_root ** 0.5):
            in_root = random.randint(2, 15)
            argument = in_root ** random.randint(2, 4)
            part_first = f"\\frac{{1}}{{\\sqrt{{{{{in_root}}}}}}}"
            part_second = f"{{{argument}}}"
            answer = round(math.log(argument, 1 / in_root)) * 2
    if situation == 3:
        while answer >= 1000 or answer <= -800 or argument >= 1000 or in_root ** 0.5 == int(
                in_root ** 0.5) or argument >= 1000:
            in_root = random.randint(2, 15)
            before_root = in_root
            argument = (in_root * before_root ** 2) ** random.randint(2, 3)
            part_first = f"{{{before_root}}}\\sqrt{{{{{in_root}}}}}"
            part_second = f"\\frac{{1}}{{{{{argument}}}}}"
            answer = round(math.log(1 / argument, before_root ** 2 * in_root)) * 2
    if situation == 4:
        while answer >= 1000 or answer <= -800 or in_root >= 1000 or in_root ** 0.5 == int(in_root ** 0.5):
            base = random.randint(2, 15)
            in_root = base ** random.randint(2, 5)
            part_first = f"{{{base}}}"
            part_second = f"\\frac{{1}}{{\\sqrt{{{{{in_root}}}}}}}"
            answer = round(math.log(1 / in_root, base)) * (1 / 2)

    if answer == int(answer):
        answer = int(answer)

    task = f"Вычислите: $\\log_{{{part_first}}}{{{part_second}}}$"

    return {
      "condition": task,
      "answer": answer
    }


def simple_logarithm_with_root():  # 13
    '''
    id 14551, 14552
    сумма чисел под корнем с логарифмами в степени
    '''

    while True:
        numerator_square = random.choice([True, False])
        argument_root = random.choice([True, False])
        inverse_ratio = random.choice([True, False])
        degree = 3
        if numerator_square:
            numerator = random.randint(2, 16) ** 2
            denominator = random.randint(2, 16)
        else:
            numerator = random.randint(2, 16)
            denominator = random.randint(2, 16) ** 2

        base = Fraction(numerator, denominator)

        is_numerator_fourth_power = numerator ** 0.25 == int(numerator ** 0.25)
        is_denominator_fourth_power = denominator ** 0.25 == int(denominator ** 0.25)

        is_numerator_square = numerator ** 0.5 == int(numerator ** 0.5)
        is_denominator_square = denominator ** 0.5 == int(denominator ** 0.5)

        are_coprime = math.gcd(numerator, denominator) == 1

        if argument_root and inverse_ratio:
            answer = -degree
        elif inverse_ratio:
            answer = -2 * degree
        elif argument_root:
            answer = degree
        else:
            answer = 2 * degree

        if are_coprime and ((is_numerator_square and not is_denominator_square and not is_numerator_fourth_power)
                            or (not is_numerator_square and is_denominator_square and not is_denominator_fourth_power)) \
                and base.numerator ** degree < 1000 and base.denominator ** degree < 1000 and base.numerator != 1 and base.denominator != 1:
            break

    if numerator_square and argument_root and inverse_ratio:
        task = f"Вычислите: $log_{{\\frac{{{{{round(base.numerator ** 0.5)}}}}}{{\\sqrt{{{base.denominator}}}}}}}{{\\frac{{{{{base.denominator}}}\\sqrt{{{base.denominator}}}}}{{{{{round((base.numerator ** degree) ** 0.5)}}}}}}}$"
    elif numerator_square and argument_root:
        task = f"Вычислите: $log_{{\\frac{{{{{round(base.numerator ** 0.5)}}}}}{{\\sqrt{{{base.denominator}}}}}}}{{\\frac{{{{{round((base.numerator ** degree) ** 0.5)}}}}}{{{{{base.denominator}}}\\sqrt{{{base.denominator}}}}}}}$"
    elif numerator_square and inverse_ratio:
        task = f"Вычислите: $log_{{\\frac{{{{{round(base.numerator ** 0.5)}}}}}{{\\sqrt{{{base.denominator}}}}}}}{{\\frac{{{{{base.denominator ** degree}}}}}{{{{{base.numerator ** degree}}}}}}}$"
    elif numerator_square:
        task = f"Вычислите: $log_{{\\frac{{{{{round(base.numerator ** 0.5)}}}}}{{\\sqrt{{{base.denominator}}}}}}}{{\\frac{{{{{base.numerator ** degree}}}}}{{{{{base.denominator ** degree}}}}}}}$"
    elif argument_root and inverse_ratio:
        task = f"Вычислите: $log_{{\\frac{{\\sqrt{{{base.numerator}}}}}{{{{{round(base.denominator ** 0.5)}}}}}}}{{\\frac{{{{{round((base.denominator ** degree) ** 0.5)}}}}}{{{{{base.numerator}}}\\sqrt{{{base.numerator}}}}}}}$"
    elif argument_root:
        task = f"Вычислите: $log_{{\\frac{{\\sqrt{{{base.numerator}}}}}{{{{{round(base.denominator ** 0.5)}}}}}}}{{\\frac{{{{{base.numerator}}}\\sqrt{{{base.numerator}}}}}{{{{{round((base.denominator ** degree) ** 0.5)}}}}}}}$"
    elif inverse_ratio:
        task = f"Вычислите: $log_{{\\frac{{\\sqrt{{{base.numerator}}}}}{{{{{round(base.denominator ** 0.5)}}}}}}}{{\\frac{{{{{(base.denominator ** degree)}}}}}{{{{{base.numerator ** degree}}}}}}}$"
    else:
        task = f"Вычислите: $log_{{\\frac{{\\sqrt{{{base.numerator}}}}}{{{{{round(base.denominator ** 0.5)}}}}}}}{{\\frac{{{{{(base.numerator ** degree)}}}}}{{{{{base.denominator ** degree}}}}}}}$"
    return {
      "condition": task,
      "answer": answer
    }


def simplification_logarithms_with_equal_base():  # 14
    '''
    id 14557-14560
    упрощение логарифмов (основание степени и основание логарифма одинаковые)
    '''
    situation = random.randint(1, 3)
    answer = 1000
    if situation == 1:
        while answer >= 1000:
            base = Fraction(1, random.randint(2, 10))
            gcd = math.gcd(base.numerator, base.denominator)
            base = Fraction(base.numerator // gcd, base.denominator // gcd)
            argument = random.randint(1, 10)
            degree = random.randint(1, 10)
            answer = argument ** degree

            if base.numerator / base.denominator in [0.1, 0.125, 0.2, 0.25, 0.5] and random.choice([True, False]):
                formatted_base = f"{base.numerator / base.denominator}"
            else:
                formatted_base = f"\\frac{{{base.numerator}}}{{{base.denominator}}}"

            task = f"Упростите: ${{{formatted_base}}}^{{ {degree} \\log_{{{formatted_base}}}{{{argument}}}}}$"

    elif situation == 2:
        while answer >= 1000:
            base = random.randint(2, 10)
            degree = random.choice([Fraction(1, 2), Fraction(1, 3)])
            argument = random.randint(2, 9)
            if degree == Fraction(1, 2):
                argument **= 2
            elif degree == Fraction(1, 3):
                argument **= 3
            answer = round(argument ** degree)
            task = f"Упростите: ${{{base}}}^{{ \\frac{{{degree.numerator}}}{{{degree.denominator}}} \\log_{{{base}}}{{{argument}}}}}$"

    elif situation == 3:
        argument, base = 2, 2
        while answer >= 1000 or argument == base:
            base = random.randint(2, 10)
            degree = random.randint(2, 10)
            argument = random.randint(2, 10)
            answer = round(argument ** degree)
            task = f"Упростите: ${{{base}}}^{{ {degree} \\log_{{{base}}}{{{argument}}}}}$"

    return {
      "condition": task,
      "answer": answer
    }


def simplification_logarithms():  # 15
    '''
    id 14561-14564
    упрощение логарифмов (основание степени и основание логарифма разные)
    '''
    situation = random.randint(1, 2)
    answer = 1000
    if situation == 1:
        degree = 5
        x = 0
        while answer >= 1000 or degree in [0, 1] or x.denominator < 0.0001 or x >= 1000 or x.denominator >= 1000:
            base = Fraction(1, random.randint(2, 9))
            degree = random.randint(2, 6)
            x = Fraction(1, base.denominator ** degree)
            argument = random.randint(1, 16)
            answer = round(argument ** round(math.log(x, base)))

            if base.numerator / base.denominator in [0.1, 0.125, 0.2, 0.25, 0.5] and random.choice([True, False]):
                formatted_base = f"{base.numerator / base.denominator}"
            else:
                formatted_base = f"\\frac{{{base.numerator}}}{{{base.denominator}}}"

            if x.numerator / x.denominator in [0.1, 0.125, 0.2, 0.25, 0.5] and random.choice([True, False]):
                formatted_x = f"{x.numerator / x.denominator}"
            else:
                formatted_x = f"\\frac{{{x.numerator}}}{{{x.denominator}}}"

            task = f"Упростите: ${{{formatted_x}}}^{{log_{{{formatted_base}}}{{{argument}}}}}$"

    elif situation == 2:
        argument, base = 2, 2
        x = 0
        while answer >= 1000 or argument == base or x >= 1000 or math.log(argument, base) == round(
                math.log(argument, base)):
            base = random.randint(2, 10)
            argument = random.randint(2, 20)
            x = base ** random.randint(2, 4)
            answer = round(argument ** round(math.log(x, base)))
            task = f"Упростите: ${{{x}}}^{{log_{{{base}}}{{{argument}}}}}$"
    return {
      "condition": task,
      "answer": answer
    }


def simplification_logarithm_power_with_coefficient():  # 16
    '''
    id 14572
    упрощение выражения вида: x^(k*log)
    '''
    answer = 10000
    while answer >= 1000 or k % degree_second != 0 or x >= 1000 or base >= 1000 or base == x:
        k = random.randint(2, 6)
        argument = random.randint(2, 8)
        num = random.randint(2, 9)
        degree_first = random.randint(2, 4)
        degree_second = random.randint(2, 4)
        x = num ** degree_first
        base = num ** degree_second
        answer = argument ** (k * (degree_first / degree_second))

    task = f"Упростите: ${{{x}}}^{{ {{{k}}}\\log_{{{base}}}{{{argument}}}}}$"
    return {
      "condition": task,
      "answer": round(answer)
    }


def logarithm_sum():  # 17
    '''
    id 14573-14576
    сумма чисел с логарифмами в показателе
    '''
    answer = 1000
    while answer >= 1000 or base_first == argument_first or argument_first == x1 \
            or base_second == argument_second or base_second == x2 or round(answer,
                                                                            2) != answer or x1 >= 1000 or x2 >= 1000 or answer <= -900:
        sitution = random.randint(1, 2)
        base_first = random.randint(2, 9)
        degree_first = random.randint(1, 4)
        x1 = base_first ** degree_first
        k1 = random.randint(1, 4)
        argument_first = random.randint(2, 40)

        base_second = random.randint(2, 9)
        degree_second = random.randint(1, 4)
        x2 = base_second ** degree_second
        k2 = random.choice([-1, 1])
        argument_second = random.randint(2, 40)

        tmp1 = (x1 ** k1) / (argument_first ** round(math.log(x1, base_first)))

        if sitution == 1:
            tmp2 = argument_second ** (round(math.log(x2, base_second)) * k2)
        else:
            tmp2 = argument_second ** (round(math.log(1 / x2, base_second)) * k2)

        answer = tmp1 + tmp2
        if k2 == 1 and sitution == 1:
            task = f"Упростите: ${{{x1}}}^{{{{{k1}}}-\\log_{{{base_first}}}{{{argument_first}}}}} + {{{x2}}}^{{\\log_{{{base_second}}}{{{argument_second}}}}}$"
        elif k2 == -1 and sitution == 1:
            task = f"Упростите: ${{{x1}}}^{{{{{k1}}}-\\log_{{{base_first}}}{{{argument_first}}}}} + {{{x2}}}^{{-\\log_{{{base_second}}}{{{argument_second}}}}}$"
        elif k2 == 1 and sitution == 2:
            task = f"Упростите: ${{{x1}}}^{{{{{k1}}}-\\log_{{{base_first}}}{{{argument_first}}}}} + \\frac{{1}}{{{x2}}}^{{\\log_{{{base_second}}}{{{argument_second}}}}}$"
        else:
            task = f"Упростите: ${{{x1}}}^{{{{{k1}}}-\\log_{{{base_first}}}{{{argument_first}}}}} + \\frac{{1}}{{{x2}}}^{{-\\log_{{{base_second}}}{{{argument_second}}}}}$"

    if answer == int(answer):
        answer = int(answer)
    return {
      "condition": task,
      "answer": answer
    }


def logarithms_simplification_in_degree_with_multiplication():  # 18
    '''
    id 14590
    упрощение произведения логарифмов в степени числа
    '''

    start = 0.05
    stop = 1
    step = 0.05
    sample = []

    current = start
    while current <= stop:
        sample.append(round(current, 3))
        current += step

    if random.choice([True, False]):
        answer = random.choice(sample)
    else:
        answer = random.randint(1, 50)
    base_first, argument_first, argument_second, base_second = 0, 0, 0, 0
    while base_first == argument_first or base_second == argument_second or base_second >= 1000 or argument_second >= 1000:
        degree = random.randint(2, 3)
        base_first = random.randint(2, 9)
        argument_first = random.randint(2, 9)
        argument_second = base_first ** degree
        base_second = argument_first ** degree
    task = f"Упростите: ${{{answer}}}^{{log_{{{base_first}}}{{{argument_first}}}⋅log_{{{base_second}}}{{{argument_second}}}}}$"
    return {
      "condition": task,
      "answer": answer
    }


def simplification_logarithm_degree():  # 19
    '''
    id 14593, 14592
    упрощение выражение вида k*x^(+/-log -/+b)
    '''
    situation = random.randint(1, 2)
    if situation == 1:
        x = 10
        b = 3
        answer = 0
        while x ** abs(b) >= 1000 or answer >= 500 or answer != round(answer, 2):
            b = random.randint(-8, -1)
            x = random.randint(2, 40)
            argument = random.randint(2, 15)
            k = random.randint(1, 100)
            answer = k * argument / x ** abs(b)
        if k != 1:
            task = f"Упростить: ${{{k}}} \\cdot {{{x}}}^{{\\log_{{{x}}}{{{argument}}}-{abs(b)}}}$"
        else:
            task = f"Упростить: ${{{x}}}^{{\\log_{{{x}}}{{{argument}}}-{abs(b)}}}$"
    elif situation == 2:
        answer = 0.542
        while answer != round(answer, 2) or answer >= 1000:
            k = random.randint(1, 100)
            b = random.randint(1, 8)
            x = random.randint(2, 40)
            argument = random.randint(2, 15)
            answer = (k * x ** b) / argument
        if k != 1:
            task = f"Упростить: ${{{k}}} \\cdot {{{x}}}^{{{{{b}}}-\\log_{{{x}}}{{{argument}}}}}$"
        else:
            task = f"Упростить: ${{{x}}}^{{{{{b}}}-\\log_{{{x}}}{{{argument}}}}}$"
    if answer == int(answer):
        answer = int(answer)

    return {
      "condition": task,
      "answer": answer
    }


def logarithms_simplification_in_degree_with_summ():  # 20
    '''
    id 14600
    упрощение суммы логарифмов в степени числа
    '''
    answer = 10000
    base, argument_first, argument_second = 10, 2, 2
    while answer >= 1000 or math.log(argument_first, base ** 2) == int(math.log(argument_first, base ** 2)) or math.log(
            argument_second, base) == int(math.log(argument_second, base)):
        base = random.randint(2, 15)
        argument_first = random.randint(1, 8) ** 2
        argument_second = random.randint(1, 20)
        answer = round(argument_first ** 0.5 * argument_second)
    task = f"Упростите: ${{{base}}}^{{log_{{{base ** 2}}}{{{argument_first}}}+log_{{{base}}}{{{argument_second}}}}}$"
    return {
      "condition": task,
      "answer": answer
    }


def simplification_expression():  # 21
    '''
    id 14603
    упрощение выражения с логарифмами
    '''
    answer = 100000
    base_first, argument_first = 0, 0
    base_second, argument_second = 0, 0
    while answer >= 1000 or math.log(argument_first, base_first) == int(
            math.log(argument_first, base_first)) or math.log(argument_second, base_second) == int(
        math.log(argument_second, base_second)) or base_second >= 1000 or base_first >= 1000:
        argument_second = random.randint(2, 9)
        num1 = Fraction(1, argument_second)
        argument_second *= random.randint(1, 3)
        num2 = random.randint(1, 6)
        base_first = random.randint(2, 8)
        x = base_first ** random.randint(2, 3)
        argument_first = random.randint(2, 10)
        base_second = argument_first ** round(math.log(x, base_first)) + num2
        answer = round(num1.numerator * argument_second / num1.denominator)
        if num1.numerator / num1.denominator in [0.125, 0.2, 0.25, 0.5] and random.choice([True, False]):
            num1_formatted = f"{num1.numerator / num1.denominator}"
        else:
            num1_formatted = f"\\frac{{{num1.numerator}}}{{{num1.denominator}}}"

    task = f"Упростите: ${{{num1_formatted}}} \\left({{{num2}}} + {{{x}}}^{{\\left(\\log_{{{base_first}}}{{{argument_first}}}\\right)^{{\\log_{{{base_second}}}{{{argument_second}}}}}}}\\right)$"
    return {
      "condition": task,
      "answer": answer
    }


def simplification_logarithm_power():  # 22
    '''
    id 14605, 14606
    упрощение выражения вида: x^(k/log)
    '''
    situation = random.randint(1, 2)
    if situation == 1:
        answer = 100000
        x = 1
        while answer >= 1000 or x >= 1000:
            k = random.randint(1, 4)
            base = random.randint(2, 10)
            argument = random.randint(2, 15)
            degree = random.randint(1, 3)
            x = argument ** degree
            answer = base ** (k * degree)
    elif situation == 2:
        base = 100000
        argument = 1
        answer = 1
        degree = 1
        while base ** degree >= 1000 or argument >= 1000 or answer >= 1000:
            k = random.randint(1, 4)
            x = random.randint(2, 8)
            degree = random.randint(2, 4)
            argument = x ** degree
            base = random.randint(2, 10)
            answer = base ** k
    task = f"Упростите: ${{{x}}}^{{\\frac{{\\large{k}}}{{\\large\\log_{{{base ** degree}}}{{{argument}}}}}}}$"
    return {
      "condition": task,
      "answer": answer
    }


def root_expression():  # 23
    '''
    id 14614
    сумма чисел под корнем с логарифмами в степени
    '''
    answer = 10000
    while answer >= 1000 or answer != round(answer, 3) or argument >= 1000 or x1 >= number or \
            x2 >= number or x1 >= 1000 or base_first ** 2 == x1:
        root_main = random.randint(3, 6)
        number = (random.randint(2, 8) ** root_main)
        x1 = random.randint(2, 6) ** 2
        x2 = number - x1

        base_first = random.randint(2, 8)
        under_root = random.choice([2, 3, 5, 6, 7, 8, 9, 15])
        before_root = random.randint(2, 7)
        argument = under_root * before_root ** 2
        answer = (1 / number) ** (1 / root_main)
    task = f"Вычислите: $\\sqrt[{{{root_main}}}]{{({{{base_first ** 2}}}^{{\\frac{{1}}{{\\log_{{{round(x1 ** 0.5)}}}{base_first}}}}}+ (\\sqrt{{{argument}}})^{{log_{{{x2}}}({{{before_root}}}\\sqrt{{{under_root}}})}})^{{-1}}}}$ "
    return {
      "condition": task,
      "answer": answer
    }


def successive_product_logarithms():  # 24
    '''
    id 14615
    последоватльное произведение логарифмов
    '''
    answer, argument_last = 10000, 10000
    while answer >= 1000 or argument_last >= 1000:
        base_first = random.randint(2, 15)
        num = random.randint(2, 10)
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        d3 = random.randint(1, 6)
        d4 = random.randint(1, 6)
        d5 = random.randint(1, 6)
        argument_last = base_first ** 2
        answer = round(math.log(argument_last, base_first), 2) * num
        task = f"Вычислите: ${{{num}}}⋅\\log_{{{base_first}}}{{{base_first + d1}}}⋅\\log_{{{base_first + d1}}}{{{base_first + d1 + d2}}}⋅\\log_{{{base_first + d1 + d2}}}{{{base_first + d1 + d2 + d3}}}⋅\\log_{{{base_first + d1 + d2 + d3}}}{{{base_first + d1 + d2 + d3 + d4}}}⋅\\log_{{{base_first + d1 + d2 + d3 + d4}}}{{{base_first + d1 + d2 + d3 + d4 + d5}}}⋅\\log_{{{base_first + d1 + d2 + d3 + d4 + d5}}}{{{argument_last}}}$"

    if int(answer) == answer:
        answer = int(answer)
    return {
      "condition": task,
      "answer": answer
    }


def ratio_logarithm_expressions():  # 25
    '''
    id 14617
    отношение логарифмических выражений
    '''
    x, y = 0, 0
    while x == y or ((x * y) ** 2 >= 1000 and a == 12):
        a, b, c = 3, 1, 2
        coefficient = random.randint(1, 4)
        answer = 1 * coefficient
        a, b, c = a * coefficient, b * coefficient, c * coefficient
        base = random.randint(2, 9)
        x = base
        y = random.randint(2, 15)

        if a == 3 or a == 9:
            part_first = f"{{{a}}}\\log_{{{base}}}{{{x * y}}}\\cdot\\log_{{{base}}}{{{y}}}"
        elif a == 6:
            part_first = f"{{{a // 2}}}\\log_{{{base}}}{{{x * y}}}\\cdot\\log_{{{base}}}{{{y ** 2}}}"
        else:
            part_first = f"{{{a // 4}}}\\log_{{{base}}}{{{(x * y) ** 2}}}\\cdot\\log_{{{base}}}{{{y ** 2}}}"

        if b == 1:
            part_second = f"\\log^{{2}}_{{{base}}}{{{x * y}}}"
        else:
            part_second = f"{{{b}}}\\log^{{2}}_{{{base}}}{{{x * y}}}"

        if c == 4:
            part_third = f"\\log^{{2}}_{{{base}}}{{{y ** 2}}}"
        else:
            part_third = f"{{{c}}}\\log^{{2}}_{{{base}}}{{{y}}}"

        part_fourth = f"\\log_{{{base}}}{{{y ** 2}}} - \\log_{{{base}}}{{{x * y}}}"

    task = f"Вычислите: $\\frac{{{{{part_first}}} - {{{part_second}}} - {{{part_third}}} }} {{ {{{part_fourth}}}}}$"

    return {
      "condition": task,
      "answer": answer
    }


def expression_different_actions_logarithms():  # 26 / 33
    '''
    id 14616
    выражения, в которых от аргумента логарифма берется двойной корней
    '''
    answer = 100000
    while answer >= 1000 or first_root == second_root or x1 == base_first or num_first == num_second or \
            argument_first >= 1000 or first_root >= 1000 or second_root >= 1000 or base_first >= 1000 \
            or base_second >= 1000 or x1 >= 1000 or x1 == base_third or first_root == 2 or second_root == 2:
        argument_first = random.randint(2, 8)
        degree = random.randint(2, 4)
        base_first = argument_first ** degree
        x1 = random.randint(2, 8) ** degree

        base_second = random.randint(2, 8)
        degree_second, degree_third = random.randint(1, 4), random.randint(1, 4)
        first_root = base_second ** degree_second
        second_root = base_second ** degree_third
        base_third = random.randint(2, 15)
        argument_third = base_third

        x2 = math.log(first_root * second_root, base_second)

        num_first = random.randint(2, 9)
        num_second = random.randint(2, 9)
        answer = x1 ** (math.log(argument_first, base_first)) + x2
    task = f"Вычислите: ${{{argument_first}}}^{{\\frac{{1}}{{\\log_{{{x1}}}{{{base_first}}}}}}} - \\log_{{{base_second}}}{{\\log_{{{base_third}}}{{\\sqrt[{{{first_root}}}]{{\\sqrt[{{{second_root}}}]{{{argument_third}}}}}}} + {{{num_first}}}^{{\\lg{{{num_second}}}}} - {{{num_second}}}^{{\\lg{{{num_first}}}}}}}$"
    return {
      "condition": task,
      "answer": round(answer)
    }


def difference_ratios_logarithms():  # 27 / 29
    '''
    id 14625, 14670-14674
    разность отношений логарифмов
    '''
    situation = random.choice([-2, -1, 1, 3, 10])
    if situation == 1:
        x, y = 0, 0
        while x == y or (x * y) ** degree >= 1000 or x ** 3 * y >= 1000 or x * y ** 2 >= 500 or x ** 3 * y ** 2 >= 500:
            x = random.randint(2, 9)
            y = random.randint(2, 9)
            degree = random.randint(2, 4)
        task = f"Вычислите: $\\frac{{\\log_{{{x}}}{{{x * (y ** 2)}}}}}{{\\log_{{{(x * y) ** degree}}}{{{x ** degree}}}}} - \\frac{{\\log_{{{x}}}{{{y}}}}}{{\\log_{{{x ** 3 * y ** 2}}}{{{x}}}}}$"
    elif situation == -1:
        x, y = 0, 0
        while x == y or x ** 2 * y >= 500:
            x = random.randint(2, 9)
            y = random.randint(2, 9)
        task = f"Вычислите: $\\frac{{\\log_{{{x}}}{{{x ** 2 * y}}}}}{{\\log_{{{(y)}}}{{{x}}}}} - \\frac{{\\log_{{{x}}}{{{x * y}}}}}{{\\log_{{{x * y}}}{{{x}}}}}$"

    elif situation == 3:
        x, y = 0, 0
        while x == y or x ** 6 * y >= 800:
            x = random.randint(2, 9)
            y = random.randint(2, 9)
        task = f"Вычислите: $\\frac{{\\log_{{{x}}}{{{x ** 3 * y}}}}}{{\\log_{{{(x ** 5 * y)}}}{{{x}}}}} - \\frac{{\\log_{{{x}}}{{{x ** 6 * y}}}}}{{\\log_{{{x ** 2 * y}}}{{{x}}}}}$"

    elif situation == 10:
        x, y = 0, 0
        while x == y or x ** 7 * y >= 800:
            x = random.randint(2, 9)
            y = random.randint(2, 9)
        task = f"Вычислите: $\\frac{{\\log_{{{x}}}{{{x ** 5 * y}}}}}{{\\log_{{{(x ** 2 * y)}}}{{{x}}}}} - \\frac{{\\log_{{{x}}}{{{y}}}}}{{\\log_{{{x ** 7 * y}}}{{{x}}}}}$"

    elif situation == -2:
        x, y = 0, 0
        if random.choice([True, False]):
            while x == y or x ** 3 * y ** 3 >= 800:
                x = random.randint(2, 9)
                y = random.randint(2, 9)
            task = f"Вычислите: $\\frac{{\\log_{{{x}}}{{{x ** 3 * y ** 3}}}}}{{\\log_{{{(y ** 3)}}}{{{x}}}}} - \\frac{{\\log_{{{x}}}{{{x * y ** 3}}}}}{{\\log_{{{x ** 2 * y ** 3}}}{{{x}}}}}$"
        else:
            while x == y or x ** 3 * y >= 800:
                x = random.randint(2, 9)
                y = random.randint(2, 9)
            task = f"Вычислите: $\\frac{{\\log_{{{x}}}{{{x ** 3 * y}}}}}{{\\log_{{{(y)}}}{{{x}}}}} - \\frac{{\\log_{{{x}}}{{{x ** 2 * y}}}}}{{\\log_{{{x * y}}}{{{x}}}}}$"
    answer = situation
    return {
      "condition": task,
      "answer": answer
    }


def difference_logarithm_and_successive_product():  # 28
    '''
    id 14665-14667
    разность между логарифмом и последовательным произведением логарифмов
    '''
    argument_first, base_first = 100000, 0
    random_prime = 41241243247
    while argument_first >= 999 or base_first % random_prime == 0:
        base_first = random.randint(2, 6)
        base_first_in_product = base_first
        degree = random.randint(1, 2)
        base_first **= degree
        random_prime = random.choice([3, 5, 7, 11, 13, 17, 19, 23])
        coefficient = random.randint(2, 8)
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        d3 = random.randint(1, 6)

        if degree == 2:
            argument_first = random_prime ** 2
            argument_last = random_prime
            answer = round(math.log((argument_first ** 0.5) /argument_last), base_first)
        else:
            argument_first = (random_prime * coefficient * base_first ** random.randint(1, 6))
            argument_last = random_prime * coefficient
            answer = round(math.log(argument_first / (random_prime * coefficient), base_first))
        task = f"Вычислить: $\\log_{{{base_first}}}{{{argument_first}}} -\\log_{{{base_first_in_product}}}{{{base_first_in_product + d1}}}⋅\\log_{{{base_first_in_product + d1}}}{{{base_first_in_product + d1 + d2}}}⋅\\log_{{{base_first_in_product + d1 + d2}}}{{{base_first_in_product + d1 + d2 + d3}}}⋅\\log_{{{base_first_in_product + d1 + d2 + d3}}}{{{argument_last}}}$"
        if int(answer) == answer:
            answer = int(answer)
    return {
      "condition": task,
      "answer": answer
    }

def expression_with_logarithms():  # 30
    '''
    id 14687
    сумма чисел с логарифмами в показателе умножаются на число
    '''
    num = 10
    while num ** 4 >= 1000 or num ** 2 >= 1000 or num <= argument_first or (
            num % argument_first) == 0 or argument_second ** 3 in [num2 ** 3, num2,
                                                                   num2 ** 2] or answer >= 1000 or argument_second ** 3 >= 1000 or base_third == argument_first:
        num = random.randint(2, 6)
        argument_first = random.randint(2, 6) ** 2

        num2 = random.randint(2, 6)
        argument_second = random.randint(2, 6)

        base_third = random.randint(2, 6)
        argument_third = round(argument_first ** 0.5)
        x = base_third ** 2
        answer = num + argument_second ** 2 * argument_first

    task = f"Упростить: $({{{num ** 4}}}^{{\\frac{{1}}{{4}} - \\frac{{1}}{{2}}\\log_{{{num ** 2}}}{{{argument_first}}}}} + {{{num2 ** 2}}}^{{log_{{{num2 ** 3}}}{{{argument_second ** 3}}}}})\\cdot{{{x}}}^{{log_{{{base_third}}}{{{argument_third}}}}}$"
    return {
      "condition": task,
      "answer": answer
    }


def sum_numbers_with_logarithms_in_exponent():  # 31
    '''
    id 14688
    сумма чисел под корнем с логарифмами в степени
    '''
    answer = 10000
    while answer >= 1000 or x1 >= 1000 or x2 >= 1000 or x3 >= 1000 or argument_first >= 1000 or argument_second >= 1000 \
            or base_third >= 1000 or x2 <= base_second or x3 == base_third or x2 == argument_second \
            or base_third == argument_third or base_second >= 1000 or argument_first == base_first \
            or argument_second == base_second or k % degree_second != 0:
        base_first = random.randint(2, 9)
        degree_first = random.randint(2, 5)
        degree_second = random.randint(2, 5)
        base_second = base_first ** degree_first
        base_third = base_first ** degree_second
        x1 = base_first ** random.randint(2, 6)
        argument_first = random.randint(2, 10)

        x2 = base_first ** random.randint(2, 6)
        argument_second = random.randint(2, 10) ** degree_first

        x3 = base_first
        argument_third = random.randint(2, 10)
        k = random.randint(2, 4)
        answer = argument_first ** (math.log(x1, base_first)) + argument_second ** (
            (math.log(x2, base_second))) + argument_third ** (k * (math.log(x3, base_third)))
    answer = round(answer)
    task = f"Упростить ${{{x1}}}^{{\\frac{{1}}{{\\log_{{{argument_first}}}{{{base_first}}}}}}} + {{{x2}}}^{{\\log_{{{base_second}}}{{{argument_second}}}}} + {{{x3}}}^{{\\frac{{{k}}}{{\\log_{{{argument_third}}}{{{base_third}}}}}}}$"
    return {
      "condition": task,
      "answer": answer
    }


def ratio_of_logarithm_expressions():  # 32
    '''
    id 14679
    отношение логарифмических выражений
    '''
    x, y = 0, 0
    while x == y:
        a, b, c = 1, 1, 2
        coefficient = random.randint(1, 4)
        answer = 1 * coefficient
        a, b, c = a * coefficient, b * coefficient, c * coefficient
        base = random.randint(2, 9)
        x = base
        y = random.randint(2, 15)

        if a == 1:
            part_first = f"\\log^{{2}}_{{{base}}}{{{x * y}}}"
        else:
            part_first = f"{{{a}}}\\log^{{2}}_{{{base}}}{{{x * y}}}"

        if b == 1:
            part_second = f"\\log_{{{base}}}{{{x * y}}}\\cdot\\log_{{{base}}}{{{y}}}"
        elif b == 2 and y ** 2 < 1000:
            part_second = f"\\log_{{{base}}}{{{x * y}}}\\cdot\\log_{{{base}}}{{{y ** 2}}}"
        elif b == 3 and y ** 3 < 1000:
            part_second = f"\\log_{{{base}}}{{{x * y}}}\\cdot\\log_{{{base}}}{{{y ** 3}}}"
        elif b == 4 and y ** 4 < 1000:
            part_second = f"\\log_{{{base}}}{{{x * y}}}\\cdot\\log_{{{base}}}{{{y ** 4}}}"
        else:
            part_second = f"{{{b}}}\\log_{{{base}}}{{{x * y}}}\\cdot\\log_{{{base}}}{{{y}}}"

        part_third = f"{{{c}}}\\log^{{2}}_{{{base}}}{{{y}}}"
        part_fourth = f"\\log_{{{base}}}{{{x * y}}} + {{2}}\\log_{{{base}}}{{{y}}}"

    task = f"Вычислите: $\\frac{{{{{part_first}}} + {{{part_second}}} - {{{part_third}}} }} {{ {{{part_fourth}}}}}$"

    return {
      "condition": task,
      "answer": answer
    }


def evaluating_large_logarithm_expression():  # 34
    '''
    id 14641
    сумма и разность логарифмов в скобках с последующим умножением результата на число, преобразованное по
    свойствам логарифмов
    '''

    answer = 10000
    argument_first, argument_second, argument_last, num_third, base = 100000, 0, 0, 0, 0
    while answer >= 1000 or argument_first >= 500 or argument_last == num_third or argument_first in [base ** exponent
                                                                                                      for exponent in
                                                                                                      range(1, 9)] \
            or argument_second in [base ** exponent for exponent in range(1, 7)] or argument_first == argument_second:
        base = random.randint(2, 6)

        coefficient = random.randint(2, 6)
        x, y = random.choice([2, 3, 5]) ** 2, random.randint(2, 8)
        random_sqrt = round(x * y * coefficient)

        argument_first = round(base ** random.randint(2, 4) * (random_sqrt / coefficient))
        argument_second = base ** random.randint(2, 4) * coefficient
        argument_third_part_one = round(x ** 0.5)
        argument_third_part_two = y * coefficient

        num_first = random.randint(2, 4)
        base_second = base ** num_first
        num_second = 2
        num_third = random.randint(2, 10)
        argument_last = random.randint(2, 6)
        answer = round(math.log(argument_first * argument_second / random_sqrt, base)) * argument_last
    task = f"Вычислить: $(\\log_{{{base}}}{{{argument_first}}} + {{{num_first}}}\\log_{{{base_second}}}{{{argument_second}}} - {{{num_second}}}\\log_{{{base}}}{{{{{argument_third_part_one}}} \\sqrt{{{argument_third_part_two}}}}}) \\cdot {{{num_third}}}^{{\\frac{{\\log_{{{base}}}{{{argument_last}}}}}{{\\log_{{{base}}}{{{num_third}}}}}}}$"
    return {
      "condition": task,
      "answer": answer
    }


def root_sum():  # 35
    '''
    id 14687
    сумма чисел под корнем с логарифмами в степени
    '''
    base_first, base_second, pair = 0, 0, [0, 0]
    while base_first == base_second or pair[0] ** 2 >= 1000 or pair[1] ** 2 >= 1000:
        pair = random.choice([[3, 4], [5, 12]])
        coefficient = random.randint(1, 8)
        pair[0], pair[1] = pair[0] * coefficient, pair[1] * coefficient
        base_first = random.randint(2, 9)
        base_second = random.randint(2, 9)
    answer = math.sqrt(pair[0] ** 2 + pair[1] ** 2)
    task = f"Упрости $\\sqrt{{{{{base_first ** 2}^{{\\frac{{1}}{{\\log_{{{pair[0]}}}{base_first}}}}} + {{{base_second ** 2}}}^{{\\frac{{1}}{{\\log_{{{pair[1]}}}{{{base_second}}}}}}}}}}}$"
    return {
      "condition": task,
      "answer": round(answer)
    }


def ratio_and_multiplication_of_logarithm_expressions():  # 36
    '''
    id 14691
    отношение произведения к сумме
    '''
    base_second = 10000
    while base_second >= 1000 or argument_second == base_second or argument_first == x1 or \
            argument_first == base_first or x1 >= 1000 or argument_second >= 1000 \
            or argument_third == base_third or argument_third == x3 or argument_fourth >= 1000 or x3 >= 1000 \
            or base_fourth >= 1000 or argument_fifth >= 1000 or argument_fifth == base_fifth or base_fifth >= 1000 \
            or argument_sixth == x6 or tmp1 >= 1000 or tmp2 >= 1000 or x7 >= 100:
        base_first = random.randint(2, 9)
        degree_first = random.randint(2, 4)
        x1 = base_first ** degree_first
        argument_first = random.randint(2, 20)

        x2 = random.randint(2, 9)
        degree_second = random.randint(2, 4)
        base_second = x2 ** degree_second
        argument_second = random.randint(2, 9) ** degree_second
        tmp1 = argument_first ** degree_first + round(argument_second ** (1 / degree_second))

        part_first = f"({{{x1}}}^{{\\frac{{1}}{{log_{{{argument_first}}}{{{base_first}}}}}}} + {{{x2}}}^{{log_{{{base_second}}}{{{argument_second}}}}})"

        base_third = random.randint(2, 9)
        degree_third = random.randint(2, 4)
        x3 = base_third ** degree_third
        argument_third = random.randint(2, 20)

        x4 = random.randint(2, 9)
        degree_fourth = random.randint(2, 4)
        base_fourth = x4 ** degree_fourth
        argument_fourth = random.randint(2, 9) ** degree_fourth
        tmp2 = argument_third ** degree_third - round(argument_fourth ** (1 / degree_fourth))

        part_second = f"({{{x3}}}^{{\\frac{{1}}{{log_{{{argument_third}}}{{{base_third}}}}}}} - {{{x4}}}^{{log_{{{base_fourth}}}{{{argument_fourth}}}}})"

        x5 = random.randint(2, 9)
        degree_fifth = random.randint(2, 4)
        base_fifth = x5 ** degree_fifth
        argument_fifth = random.randint(2, 9) ** degree_fifth

        x6 = random.randint(2, 9)
        argument_sixth = random.randint(2, 10)

        x7 = tmp1 - argument_sixth * round(argument_fifth ** (1 / degree_fifth))

        part_third = f"{{{x7}}}+{{{x5}}}^{{\\frac{{1}}{{\\log_{{{argument_fifth}}}{{{base_fifth}}}}}}}\\cdot {{{x6}}}^{{\\log_{{{x6}}}{{{argument_sixth}}}}}"

    answer = tmp2
    task = f"Упростить: $\\frac{{{{{part_first}}}\\cdot{{{part_second}}}}}{{{{{part_third}}}}}$"

    return {
      "condition": task,
      "answer": answer
    }
