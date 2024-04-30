import math
import random
import numpy as np


def trigonometry_14174():

    ''' Задание на портале kuzovkin.info № 14174 '''

    def generate_angles(start=-360, end=361, step=15):
        return range(start, end, step)

    angles = generate_angles()

    while True:
        num1, num2, num3 = np.random.choice(angles, 3)
        a, b = np.random.randint(1, 99, 2)
        c = math.sqrt(b) * math.tan(num1) * math.sin(num2) * math.cos(num3)

        task = f"Вычислите: $\\frac{{{a}}}{{\\sqrt{{{b}}}}} \\cdot \\tan({num1}^\\circ) \\cdot \\sin({num2}^\\circ) \\cdot \\cos({num3}^\\circ)$"

        if c == 0:
            continue

        answer = a / c

        try:
            answer = int(a / c)
            if abs(answer) == 1 or answer == 0:
                break
        except (ValueError, OverflowError):
            continue

    return {
        "condition": task,
        "answer": answer
    }


def trigonometry_14175():

    ''' Задание на портале kuzovkin.info № 14175 '''

    def generate_angles(start=-9990, end=10000, step=45):
        return range(start, end, step)

    angles = generate_angles()

    while True:
        num = random.choice(angles)

        task = f"Вычислите:  $ctg({num})^\\circ$"
        rad = math.radians(num)

        try:
            answer = math.cos(rad) / math.sin(rad)
            if -1 <= answer <= 1 :
                break
        except (ValueError, ZeroDivisionError):
            continue

    return {
        "condition": task,
        "answer": round(answer, 2)
    }


def trigonometry_14176():

    ''' Задание на портале kuzovkin.info № 14176 '''

    def generate_angles(start=-9990, end=10000, step=45):
        return range(start, end, step)

    angles = generate_angles()

    while True:
        num = random.choice(angles)

        task = f"Вычислите:  $tan({num})^\\circ$"
        rad = math.radians(num)

        try:
            answer = math.sin(rad) / math.cos(rad)
            if -1 <= answer <= 1 :
                break
        except (ValueError, ZeroDivisionError):
            continue

    return {
        "condition": task,
        "answer": round(answer, 2)
    }


def trigonometry_14177():

    ''' Задание на портале kuzovkin.info № 14177 '''

    while True:

        a, b, num1, num2, num3 = np.random.randint(1, 99, 5)
        rad1, rad2, rad3 = num1 * math.pi, num2 * math.pi / a, num3 * math.pi / b

        task = fr"Вычислите: $\cos({num1}^\circ\pi) + 2 \sin\\left(\frac{{{num2}^\circ\pi}}{{{a}}}\right) - \cot\\left(\frac{{{num3}^\circ\pi}}{{{b}}}\right)$"

        answer = math.cos(rad1) + 2 * math.sin(rad2) - math.cos(rad3) / math.sin(rad3)

        if answer == 1 or answer == -1 or answer == 0 and rad1 % 15 == 0 and rad2 % 15 == 0 and rad3 % 15 == 0:
            break

    return {
        "condition": task,
        "answer": answer
    }


def trigonometry_14178():

    ''' Задание на портале kuzovkin.info № 14178 '''

    def generate_angles(start=-720, end=721, step=3):
        return range(start, end, step)
    
    angles = generate_angles()

    while True:

        a, b, c, d, e, f, g, h = np.random.choice(angles, 8)
        num1 = (math.cos(np.radians(a)) * math.cos(np.radians(b))) - (math.cos(np.radians(c)) * math.cos(np.radians(d)))
        num2 = (math.cos(np.radians(e)) * math.cos(np.radians(f))) + (math.cos(np.radians(g)) * math.cos(np.radians(h)))

        if num2 == 0:
            continue
        
        task = f"Вычислите: $\\frac{{\\cos({a}^\\circ) \\cdot \\cos({b}^\\circ) - \\cos({c}^\\circ) \\cdot \\cos({d}^\\circ)}}{{\\cos({e}^\\circ) \\cdot \\cos({f}^\\circ) + \\cos({g}^\\circ) \\cdot \\cos({h}^\\circ)}}$"

        answer = num1 / num2

        if abs(answer) in range(0,2):
            break

    return {
        "condition": task,
        "answer": answer
    }


def trigonometry_14179():

    ''' Задание на портале kuzovkin.info № 14179 '''
    
    while True:

        num = random.randint(20, 72) * 5
        angles = [num + i * 20 for i in range(9)]
        
        task = rf"Вычислите: $\sin({angles[0]}^\circ) + \sin({angles[1]}^\circ) + \sin({angles[2]}^\circ) + \dots + \sin({angles[-3]}^\circ) + \sin({angles[-2]}^\circ) + \sin({angles[-1]}^\circ)$"

        answer = sum(math.sin(angle) for angle in angles)

        try:
            answer = int(sum(math.sin(angle) for angle in angles))
            if abs(answer*100 - int(answer*100) < 0.000001):
                break
        except (ZeroDivisionError, ValueError):
            continue

    return {
        "condition": task,
        "answer": answer
    }



def trigonometry_14180():

    ''' Задание на портале kuzovkin.info № 14180 '''

    def generate_angles(start=-3600, end=3601, step=30):
        return range(start, end, step)
    angles = generate_angles()

    while True:
        num = random.choice(angles)
        task = f"Вычислите c помощью формул приведения: $cos({num})^\\circ$"
        answer = math.cos(math.radians(num))
        if abs(answer * 100 - int(answer * 100) )< 0.000001:
            break
    return {
        "condition": task,
        "answer": round(answer, 2)
    }


def trigonometry_14181():

    ''' Задание на портале kuzovkin.info № 14181 '''

    def generate_angles(start=-3600, end=3601, step=45):
        return range(start, end, step)
    angles = generate_angles()

    while True:
        num = random.choice(angles)
        task = f"Вычислите c помощью формул приведения: $sin({num})^\\circ$"
        answer = math.sin(math.radians(num))
        if abs(answer * 100 - int(answer * 100) )< 0.000001:
            break
    return {
        "condition": task,
        "answer": round(answer, 2)
    }


def trigonometry_14182():

    ''' Задание на портале kuzovkin.info № 14182 '''

    while True:
        num1, num2 = np.random.randint(1, 99, 2)
        rad = num1 * math.pi / num2
        task = f"Вычислите c помощью формул приведения: $\\sin\\left(\\frac{{{num1}^\\circ\\pi}}{{{num2}}}\\right)$"
        answer = math.sin(rad)
        if abs(answer * 100 - int(answer * 100) )< 0.000001:
            break
    return {
        "condition": task,
        "answer": round(answer, 2)
    }


def trigonometry_14183():

    ''' Задание на портале kuzovkin.info № 14183 '''

    def generate_angles(start=-3600, end=3601, step=45):
        return range(start, end, step)
    
    angles = generate_angles()

    while True:
        num = random.choice(angles)
        task = f"Вычислите c помощью формул приведения: $tan({num})^\\circ$"
        answer = math.tan(math.radians(num))
        if -1 <= answer <= 1:
            break
    return {
        "condition": task,
        "answer": round(answer, 2)
    }


def trigonometry_14184():

    ''' Задание на портале kuzovkin.info № 14184 '''

    while True:
        num1, num2 = np.random.randint(1, 99, 2)
        rad = num1 * math.pi / num2
        task = f"Вычислите c помощью формул приведения: $\\cos\\left(\\frac{{{num1}^\\circ\\pi}}{{{num2}}}\\right)$"
        answer = math.cos(rad)
        if abs(answer * 100 - int(answer * 100) )< 0.000001:
            break
    return {
        "condition": task,
        "answer": round(answer, 2)
    }


def trigonometry_14185():

    ''' Задание на портале kuzovkin.info № 14185 '''

    def generate_angles(start=-360, end=361, step=10):
        return range(start, end, step)
    
    angles = generate_angles()

    while True:
        a, b, c, d = np.random.choice(angles, 4)

        if b % 180 not in {90, 270} and d % 180 not in {90, 270}:
           rad1, rad2, rad3, rad4 = np.radians(a), np.radians(b), np.radians(c), np.radians(d)

           task = f"Вычислите: \\sin({a}^\\circ) \\cdot \\cos({b}^\\circ) + \\sin({c}^\\circ) \\cdot \\cos({d}^\\circ) + \\tan({b}^\\circ) \\cdot \\tan({d}^\\circ)"

           answer = (np.sin(rad1) * np.cos(rad2)) + (np.sin(rad3) * np.cos(rad4)) + (np.tan(rad2) * np.tan(rad4))

           if abs(answer) == 0.5 or abs(answer) == 1 or answer == 0:
               break

    return {
        "condition": task,
        "answer": answer
    }


def trigonometry_14186():

    ''' Задание на портале kuzovkin.info № 14186 '''

    def generate_angles(start=0, end=361, step=6):
        return range(start, end, step)
    
    angles = generate_angles()

    while True:
        a, b, c, d, e, f = np.random.choice(angles, 6)

        if a % 180 not in {90, 270} and b % 180 not in {90, 270}:
           rad1, rad2, rad3, rad4, rad5, rad6 = np.radians(a), np.radians(b), np.radians(c), np.radians(d), np.radians(e), np.radians(f)

           task = f"Вычислите: \\tan({a}^\\circ) \\cdot \\tan({b}^\\circ) + \\sin({c}^\\circ) \\cdot \\sin({d}^\\circ) - \\sin({e}^\\circ) \\cdot \\sin({f}^\\circ)"

           answer = (np.tan(rad1) * np.tan(rad2)) + (np.sin(rad3) * np.sin(rad4)) - (np.sin(rad5) * np.sin(rad6))

           if abs(answer) == 0.5 or abs(answer) == 1 or answer == 0:
               break

    return {
        "condition": task,
        "answer": answer
    }


def trigonometry_14187():

    ''' Задание на портале kuzovkin.info № 14187 '''

    def generate_angles(start=0, end=361, step=5):
        return range(start, end, step)
    
    angles = generate_angles()

    while True:
        a, b, c, d, e, f = np.random.choice(angles, 6)

        if e % 180 not in {90, 270} and f % 180 not in {90, 270}:
           rad1, rad2, rad3, rad4, rad5, rad6 = np.radians(a), np.radians(b), np.radians(c), np.radians(d), np.radians(e), np.radians(f)

           task = f"Вычислите: \\sin({a}^\\circ) \\cdot \\sin({b}^\\circ) + \\cos({c}^\\circ) \\cdot \\cos({d}^\\circ) - \\tan({e}^\\circ) \\cdot \\tan({f}^\\circ)"

           answer = (np.sin(rad1) * np.sin(rad2)) + (np.cos(rad3) * np.cos(rad4)) - (np.tan(rad5) * np.tan(rad6))

           if abs(answer) == 0.5 or abs(answer) == 1 or answer == 0:
               break

    return {
        "condition": task,
        "answer": answer
    }


def trigonometry_14188():

    ''' Задание на портале kuzovkin.info № 14188 '''
    
    while True:
        num = random.randint(0, 18) * 20
        angles = sorted([(num + i * 20) % 360 for i in range(9)])
        
        task = rf"Упростите выражениe: $\tan({angles[0]}^\circ) + \tan({angles[1]}^\circ) + \tan({angles[2]}^\circ) + \dots + \tan({angles[-2]}^\circ) + \tan({angles[-1]}^\circ)$"

        answer = int(sum(math.tan(math.radians(angle)) for angle in angles))
        if abs(answer*100 - int(answer*100) < 0.000001):
            break

    return {
        "condition": task,
        "answer": answer
    }


def trigonometry_14189():

    ''' Задание на портале kuzovkin.info № 14189 '''

    def generate_angles(start=-360, end=360, step=15):
        return range(start, end, step)
    
    angles = generate_angles()

    while True:

        an1, an2, an3, an4, an5, an6, an7, an8, an9, an10, an11, an12, an13, an14 = np.random.choice(angles, 14)
        rad1, rad2, rad3, rad4, rad5, rad6, rad7, rad8, rad9, rad10, rad11, rad12, rad13, rad14 = [np.radians(a) for a in [an1, an2, an3, an4, an5, an6, an7, an8, an9, an10, an11, an12, an13, an14]]
        num = np.random.randint(1, 100)

        num1 = (np.cos(rad1) * np.cos(rad2)) - (np.cos(rad3) * np.cos(rad4))
        num2 = (np.cos(rad5) * np.cos(rad6)) + (np.cos(rad7) * np.cos(rad8))
        num3 = (np.sin(rad9) * np.cos(rad10)) + (np.sin(rad11) * np.cos(rad12))
        num4 = (0.5 * np.sqrt(num) * np.cos(rad13)) + (0.5 * np.sin(rad14))

        if num2 == 0 or num4 == 0:
            continue

        task = f"Вычислите: $\\frac{{\\cos({{{an1}}}^\\circ) \\cdot \\cos({{{an2}}}^\\circ) - \\cos({{{an3}}}^\\circ) \\cdot \\cos({{{an4}}}^\\circ)}}{{\\cos({{{an5}}}^\\circ) \\cdot \\cos({{{an6}}}^\\circ) + \\cos({{{an7}}}^\\circ) \\cdot \\cos({{{an8}}}^\\circ)}} - \\frac{{\\sin({{{an9}}}^\\circ) \\cdot \\cos({{{an10}}}^\\circ) + \\sin({{{an11}}}^\\circ) \\cdot \\cos({{{an12}}}^\\circ)}}{{0.5 \\cdot \\sqrt{{{num}}} \\cdot \\cos({{{an13}}}^\\circ) + 0.5 \\cdot \\sin({{{an14}}}^\\circ)}}$"

        answer = (num1 / num2) - (num3 / num4)

        if abs(answer) in range(0,10):
            break

    return {
        "condition": task,
        "answer": answer
    }


def trigonometry_14190():

    ''' Задание на портале kuzovkin.info № 14190 '''

    while True:
        n1, n2, n3, n4, n5, n6, n7, n8 = np.random.randint(1, 20, 8)
        rad1, rad2, rad3, rad4, rad5, rad6, rad7, rad8 = n1 * np.pi / n2, n1 * np.pi / n3, n4 * np.pi / n3, n5 * np.pi / n2, n6 * np.pi / n2, n5 * np.pi / n3, n7 * np.pi / n3, n8 * np.pi / n3
        
        num1 = (np.sin(rad1) + np.sin(rad2)) * (np.sin(rad3) - np.sin(rad4))
        num2 = (np.sin(rad5) + np.sin(rad6)) * (np.cos(rad7) - np.cos(rad8))
        
        task = task = f"Вычислите: $\\left(\\sin\\left(\\frac{{{n1} \\pi}}{{{n2}}}\\right) + \\sin\\left(\\frac{{{n1} \\pi}}{{{n3}}}\\right)\\right) \\cdot \\left(\\sin\\left(\\frac{{{n4} \\pi}}{{{n3}}}\\right) - \\sin\\left(\\frac{{{n5} \\pi}}{{{n2}}}\\right)\\right) - \\left(\\sin\\left(\\frac{{{n6} \\pi}}{{{n2}}}\\right) + \\sin\\left(\\frac{{{n5} \\pi}}{{{n3}}}\\right)\\right) \\cdot \\left(\\cos\\left(\\frac{{{n7} \\pi}}{{{n3}}}\\right) - \\cos\\left(\\frac{{{n8} \\pi}}{{{n3}}}\\right)\\right)#"

        answer = num1 - num2
        if abs(answer) in range(0,10):
            break

    return {
        "condition": task,
        "answer": answer
    }


def trigonometry_14191():

    ''' Задание на портале kuzovkin.info № 14191 '''

    def generate_angles(start=-1000, end=1001, step=10):
        return range(start, end, step)

    angles = generate_angles()
    
    while True:
        num1, num2, num3, num4 = np.random.choice(angles, 4)
        rad1, rad2, rad3, rad4 = np.radians(num1), np.radians(num2), np.radians(num3), np.radians(num4)

        task = f"Вычислите: $\\sin({{{num1}}}^\\circ) \\cdot \\cos({{{num2}}}^\\circ) + \\sin({{{num3}}}^\\circ) \\cdot \\cos({{{num4}}}^\\circ)$"
        
        answer = np.sin(rad1) * np.cos(rad2) + np.sin(rad3) * np.cos(rad4)
        if abs(answer) in range(0,10):
            break

    return {
        "condition": task,
        "answer": answer
    }


def trigonometry_14192():

    ''' Задание на портале kuzovkin.info № 14192 '''

    def generate_angles(start=-3600, end=3601, step=45):
        return range(start, end, step)
    
    angles = generate_angles()

    while True:
        num = np.random.choice(angles)
        task = f"Вычислите c помощью формул приведения: $sin({num})^\\circ$"
        answer = np.sin(np.radians(num))
        if abs(answer * 100 - int(answer * 100) )< 0.000001:
            break
    return {
        "condition": task,
        "answer": round(answer, 2)
    }


def trigonometry_14193():

    ''' Задание на портале kuzovkin.info № 14193 '''

    def generate_angles(start=-3600, end=3601, step=30):
        return range(start, end, step)
    
    angles = generate_angles()

    while True:
        num = np.random.choice(angles)
        task = f"Вычислите c помощью формул приведения: $cos({num})^\\circ$"
        answer = np.cos(np.radians(num))
        if abs(answer * 100 - int(answer * 100) )< 0.000001:
            break
    return {
        "condition": task,
        "answer": round(answer, 2)
    }


def trigonometry_14194():

    """Задание на портале https://kuzovkin.info/one_exercise_1/14194"""

    while True:
        num1, num2 = np.random.randint(-40, 40, 2)
        if num2<2:
            continue
        try:
            answer = 1 / math.tan(num1 * math.pi / num2)
        except ZeroDivisionError:
            continue
        task = f"Вычислите c помощью формул приведения: $\\ctg\\left(\\frac{{{int(num1)}\pi}}{{{int(num2)}}}\\right)$"
        if round(answer,3)==1 or round(answer,3)==0 or round(answer,3)==-1:
            break

    return {
        "condition": task,
        "answer": int(round(answer,3))
    }


def trigonometry_14195():

    ''' Задание на портале kuzovkin.info № 14195 '''

    def generate_angles_1(start=-360, end=361, step=10):
        return range(start, end, step)
    
    def generate_angles_2(start=-360, end=361, step=3):
        return range(start, end, step)
    
    angles_1 = generate_angles_1()
    angles_2 = generate_angles_2()

    while True:

        a1, b1, c1, d1 = np.random.choice(angles_1, 4)
        a2, b2, c2, d2 = np.random.choice(angles_2, 4)

        num1 = (np.sin(np.radians(a1)) * np.cos(np.radians(b1))) - (np.cos(np.radians(c1)) * np.cos(np.radians(d1)))
        num2 = (np.sin(np.radians(a2)) * np.cos(np.radians(b2))) + (np.cos(np.radians(c2)) * np.cos(np.radians(d2)))

        if num2 == 0:
            continue
        
        task = f"Вычислите: $\\frac{{\\sin({a1}^\\circ) \\cdot \\cos({b1}^\\circ) - \\cos({c1}^\\circ) \\cdot \\cos({d1}^\\circ)}}{{\\sin({a2}^\\circ) \\cdot \\cos({b2}^\\circ) + \\cos({c2}^\\circ) \\cdot \\cos({d2}^\\circ)}}$"
        
        answer = num1 / num2

        if abs(answer) in [0, 1]:
            break

    return {
        "condition": task,
        "answer": answer
    }


def trigonometry_14196():

    ''' Задание на портале kuzovkin.info № 14196 '''
    
    while True:
        x = np.random.rand()
        angles = [f'np.pi - x', f'x - np.pi/2', f'np.pi + x', f'x + np.pi/2']
        rad1, rad2, rad3, rad4 = np.random.choice(angles, size=4, replace=True)
    
        task = f"Упростите упражнение: $\\sin({rad1}) \\cdot \\cos({rad2}) - \\sin({rad3}) \\cdot \\cos({rad4})$"

        answer = (np.sin(eval(rad1)) * np.cos(eval(rad2))) - (np.sin(eval(rad3)) * np.cos(eval(rad4)))

        if abs(answer) in range(0, 2):
            break

    return {
        "condition": task,
        "answer": answer
    }


def trigonometry_14197():

    ''' Задание на портале kuzovkin.info № 14197 '''

    while True:
        a = np.random.rand()
        angles = [f'3 * (np.pi / 2 + a)', f'a - 2 * np.pi', f'-a', f'a - (3 * np.pi / 2)', f'3 * (np.pi + a) + np.pi',  f'a - 2 * np.pi + np.pi', f'-a + np.pi',  f'a - (3 * np.pi / 2) + np.pi']
        rad1, rad2, rad3, rad4 = np.random.choice(angles, size=4, replace=True)
        ctg_1, ctg_2 = np.cos(eval(rad2)) / np.sin(eval(rad2)), np.cos(eval(rad4)) / np.sin(eval(rad4))
        
        num1 = np.sin(eval(rad1))**2 / ctg_1**2
        num2 = np.sin(eval(rad3))**2 / ctg_2**2

        task = f"Упростите упражнение: \\frac{{\\sin^2({rad1})}}{{\\cot^2({rad2})}} + \\frac{{\\sin^2({rad3})}}{{\\cot^2({rad4})}}"

        answer = num1 + num2

        if abs(answer) in range(0,2):
            break

    return {
        "condition": task,
        "answer": answer
    }


def trigonometry_14198():

    ''' Задание на портале kuzovkin.info № 14198 '''

    while True:
        a = np.random.rand()
        angles = [f'np.pi - a', f'(3 * np.pi / 2) - a', f'np.pi + a', f'(3 * np.pi / 2) + a']
        rad1, rad2 = np.random.choice(angles, size=2, replace=True)
        
        task = f"Упростите упражнение: \\cos^2({rad1}) + \\cos^2({rad2})"

        answer = np.cos(eval(rad1))**2 + np.cos(eval(rad2))**2

        if abs(answer) in range(0, 2):
            break

    return {
        "condition": task,
        "answer": answer
    }


def trigonometry_14199():

    ''' Задание на портале kuzovkin.info № 14199 '''

    while True:
        a = np.random.rand()
        angles = [f'np.pi - a', f'(3 * np.pi / 2) - a', f'np.pi + a', f'(3 * np.pi / 2) + a', '2 * a', f'a - 2 * np.pi', f'-a', f'a - (3 * np.pi / 2)', f'3 * (np.pi + a) + np.pi',  f'a - 2 * np.pi + np.pi', f'-a + np.pi',  f'a - (3 * np.pi / 2) + np.pi']
        rad1, rad2, rad3 = np.random.choice(angles, size=3, replace=True)
        
        task = f"Упростите упражнение: 1 + \\cos({rad1}) \\cdot \\sin({rad2}) + \\frac{{1 + \\cos({rad3})}}{{2}}"

        answer = 1 + np.cos(eval(rad1)) * np.sin(eval(rad2)) + (1 + np.cos(eval(rad3)) / 2)

        if abs(answer) in [1.5, 2.5]:
            break

    return {
        "condition": task,
        "answer": answer
    }


def trigonometry_14200():

    ''' Задание на портале kuzovkin.info № 14200 '''

    def generate_angles(start=-1000, end=1001, step=10):
        return range(start, end, step)
    
    angles = generate_angles()

    while True:

        a, b, c, d, e, f, g, h = np.random.choice(angles, 8)
        num1 = (np.sin(np.radians(a)) * np.cos(np.radians(b))) - (np.sin(np.radians(c)) * np.sin(np.radians(d)))
        num2 = (np.cos(np.radians(e)) * np.cos(np.radians(f))) - (np.cos(np.radians(g)) * np.cos(np.radians(h)))

        if num2 == 0:
            continue
        
        task = f"Вычислите: $\\frac{{\\sin({a}^\\circ) \\cdot \\cos({b}^\\circ) - \\sin({c}^\\circ) \\cdot \\sin({d}^\\circ)}}{{\\cos({e}^\\circ) \\cdot \\cos({f}^\\circ) - \\cos({g}^\\circ) \\cdot \\cos({h}^\\circ)}}$"

        answer = num1 / num2

        if abs(answer) in range(0,2):
            break

    return {
        "condition": task,
        "answer": answer
    }


def trigonometry_14242():

    ''' Задание на портале kuzovkin.info № 14242 '''

    while True:
        angles = np.random.randint(-180, 180, 2)
        a = np.random.randint(1, 10)
        
        if angles[0] % 15 == 0 or angles[1] % 15 == 0:
            continue

        task = f"Вычислите: $\\frac{{1}}{{\\cos({angles[0]}^\\circ)}} - {a} \\cdot \\sin({angles[1]}^\\circ)$"

        answer = (1 / np.cos(np.radians(angles[0]))) - (a * np.sin(np.radians(angles[1])))
        if abs(answer * 10000 - int(answer * 10000) )< 0.000001 and abs(answer)>0.01:
            break

    return {
        "condition": task,
        "answer": round(answer, 4)
    }


def trigonometry_14243():
    ''' Задание на портале kuzovkin.info № 14243 '''

    while True:
        angles =np.random.randint(10, 360, 3)

        if angles[0] % 15 == 0 or angles[1] % 15 == 0 or angles[2] % 15 == 0:
            continue

        task = f"Вычислите: $\\cos({angles[0]}^\\circ) \\cdot \\cos({angles[1]}^\\circ) \\cdot \\cos({angles[2]}^\\circ)$"

        answer = np.cos(np.radians(angles[0])) * np.cos(np.radians(angles[1])) * np.cos(np.radians(angles[2]))
        if abs(answer * 10000 - int(answer * 10000) )< 0.000001 and abs(answer)>0.01:
            break

    return {
        "condition": task,
        "answer": round(answer, 4)
    }


def trigonometry_14244():
    ''' Задание на портале kuzovkin.info № 14244 '''

    while True:
        num1, num2, num3 = np.random.randint(1, 10, 3)
        rad = np.random.randint(1, 50)
        angle1, angle2, angle3 = num1 * np.pi / rad, num2 * np.pi / rad, num3 * np.pi / rad

        if angle1 % np.pi == 0 or angle2 % np.pi == 0 or angle3 % np.pi == 0:
          continue

        task = f"Вычислите: $\\sin(\\frac{{{num1} \\cdot \\pi}}{{{rad}}}) \\cdot \\sin(\\frac{{{num2} \\cdot \\pi}}{{{rad}}}) \\cdot \\sin(\\frac{{{num3} \\cdot \\pi}}{{{rad}}})$"

        answer = np.sin(angle1) * np.sin(angle2) * np.sin(angle3)

        if abs(answer * 100 - int(answer * 100) )< 0.000001 and abs(answer)>0.01:
            break

    return {
        "condition": task,
        "answer": round(answer, 4)
    }


def trigonometry_14245():
    ''' Задание на портале kuzovkin.info № 14245 '''

    while True:
        angles =np.random.randint(10, 360, 2)

        if angles[0] % 15 == 0 or angles[1] % 15 == 0:
            continue

        task = f"Преобразуйте в сумму: $\\cos({angles[0]}^\\circ) \\cdot \\cos({angles[1]}^\\circ)$"

        answer = np.cos(np.radians(angles[0])) * np.cos(np.radians(angles[1]))
        if abs(answer * 10000 - int(answer * 10000) )< 0.000001 and abs(answer)>0.01:
            break

    return {
        "condition": task,
        "answer": round(answer, 4)
    }


def trigonometry_14246():
    ''' Задание на портале kuzovkin.info № 14246 '''

    while True:
        angles = np.random.randint(5, 360, 4)

        task = f"Вычислите: $\\tg({angles[0]}^\\circ) \\cdot \\tg({angles[1]}^\\circ) \\cdot \\tg({angles[2]}^\\circ) \\cdot \\tg({angles[3]}^\\circ)$"

        answer = np.tan(np.radians(angles[0])) * np.tan(np.radians(angles[1])) * np.tan(np.radians(angles[2])) * np.tan(np.radians(angles[3]))

        if abs(answer) in range(0, 10) and angles[0] % 30 != 0 and angles[0] % 45 != 0:
            break

    return {
        "condition": task,
        "answer": answer
    }


def trigonometry_14247():
    ''' Задание на портале kuzovkin.info № 14247 '''

    while True:
        angles = np.random.randint(10, 360, 2)

        task = f"Вычислите: $\\tg^2({angles[0]}^\\circ) \\cdot \\tg^2({angles[1]}^\\circ)$"

        answer = np.tan(np.radians(angles[0]))**2 * np.tan(np.radians(angles[1]))**2

        if abs(answer) in range(0, 10) and angles[0] % 30 != 0 and angles[0] % 45 != 0:
            break

    return {
        "condition": task,
        "answer": answer
    }


def trigonometry_14248():
    ''' Задание на портале kuzovkin.info № 14248 '''

    while True:
        angles = np.random.randint(10, 360, 3)

        task = f"Вычислите: $\\cos({angles[0]}^\\circ) \\cdot \\cos({angles[1]}^\\circ) \\cdot \\cos({angles[2]}^\\circ)$"

        answer = np.cos(np.radians(angles[0])) * np.cos(np.radians(angles[1])) * np.cos(np.radians(angles[2]))

        if abs(answer * 10000 - int(answer * 10000) )< 0.000001 and abs(answer)>0.01 and angles[0] % 30 != 0 and angles[0] % 45 != 0:
            break

    return {
        "condition": task,
        "answer": round(answer, 4)
    }


def trigonometry_14249():
    ''' Задание на портале kuzovkin.info № 14249 '''

    while True:
        angles = np.random.randint(10, 360, 3)

        if angles[0] % 15 == 0 or angles[1] % 15 == 0 or angles[2] % 15 == 0:
            continue

        task = f"Вычислите: $\\sin({angles[0]}^\\circ) \\cdot \\sin({angles[1]}^\\circ) \\cdot \\sin({angles[2]}^\\circ)$"

        answer = np.sin(np.radians(angles[0])) * np.sin(np.radians(angles[1])) * np.sin(np.radians(angles[2]))

        if abs(answer * 10000 - int(answer * 10000) )< 0.000001 and abs(answer)>0.01:
            break

    return {
        "condition": task,
        "answer": round(answer, 4)
    }


def trigonometry_14250():
    ''' Задание на портале kuzovkin.info № 14250 '''

    while True:
        angles = np.random.randint(5, 360, 3)

        task = f"Вычислите: $\\cos({angles[0]}^\\circ) \\cdot \\cos({angles[1]}^\\circ) \\cdot \\cos({angles[2]}^\\circ)$"

        answer = np.cos(np.radians(angles[0])) * np.cos(np.radians(angles[1])) * np.cos(np.radians(angles[2]))

        if abs(answer * 10000 - int(answer * 10000) )< 0.000001 and abs(answer)>0.01 and angles[0] % 30 != 0 and angles[0] % 45 != 0:
            break

    return {
        "condition": task,
        "answer": round(answer, 4)
    }


def trigonometry_14252():
    ''' Задание на портале kuzovkin.info № 14252 '''

    while True:
        angles = np.random.randint(2, 30, 6)
        angle1, angle2, angle3, angle4, angle5 = angles[1] * np.pi / angles[0], angles[2] * np.pi / angles[0], angles[3] * np.pi / angles[0], angles[4] * np.pi / angles[0], angles[5] * np.pi / angles[0]

        if angle1 % np.pi == 0 or angle2 % np.pi == 0 or angle3 % np.pi == 0 or angle4 % np.pi == 0 or angle5 % np.pi == 0:
            continue

        task = f"Вычислите: $\\cos(\\frac{{{angles[1]} \\cdot \\pi}}{{{angles[0]}}}) \\cdot \\cos(\\frac{{{angles[2]} \\cdot \\pi}}{{{angles[0]}}}) \\cdot \\cos(\\frac{{{angles[3]} \\cdot \\pi}}{{{angles[0]}}}) \\cdot \\cos(\\frac{{{angles[4]} \\cdot \\pi}}{{{angles[0]}}}) \\cdot \\cos(\\frac{{{angles[5]} \\cdot \\pi}}{{{angles[0]}}})$"
        answer = np.cos(angle1) * np.cos(angle2) * np.cos(angle3) * np.cos(angle4) * np.cos(angle5)

        if abs(answer * 10000 - int(answer * 10000) )< 0.000001 and abs(answer)>0.01:
            break

    return {
        "condition": task,
        "answer": round(answer, 4)
    }


def trigonometry_14253():
    ''' Задание на портале kuzovkin.info № 14253 '''

    while True:
        angles = np.random.randint(10, 360, 2)

        if angles[0] % 15 == 0 or angles[1] % 15 == 0:
            continue

        task = f"Преобразуйте в сумму: $\\sin({angles[0]}^\\circ) \\cdot \\sin({angles[1]}^\\circ)$"

        answer = np.sin(np.radians(angles[0])) * np.sin(np.radians(angles[1]))
        if abs(answer * 10000 - int(answer * 10000) )< 0.000001 and abs(answer)>0.01:
            break

    return {
        "condition": task,
        "answer": round(answer, 4)
    }


def trigonometry_14257():
    ''' Задание на портале kuzovkin.info № 14257 '''

    while True:
        angles =np.random.randint(10, 360, 3)


        task = f"Вычислите: $\\sin^2({angles[0]}^\\circ) \\cdot \\sin^2({angles[1]}^\\circ) \\cdot \\sin^2({angles[2]}^\\circ)$"

        answer = np.sin(np.radians(angles[0]))**2 * np.sin(np.radians(angles[1]))**2 * np.sin(np.radians(angles[2]))**2

        if abs(answer * 10000 - int(answer * 10000) )< 0.000001 and abs(answer)>0.01 and angles[0] % 30 != 0 and angles[0] % 45 != 0:
            break

    return {
        "condition": task,
        "answer": round(answer, 4)
    }


def trigonometry_14259(): # похоже на 14260
    ''' Задание на портале kuzovkin.info № 14259 '''

    while True:
        angles = np.random.randint(1, 30, 6)
        angle1, angle2, angle3, angle4, angle5 = angles[0] * np.pi / angles[1], angles[0] * np.pi / angles[2], angles[3] * np.pi / angles[1], angles[4] * np.pi / angles[5], angles[3] * np.pi / angles[2]

        if angle1 % np.pi == 0 or angle2 % np.pi == 0 or angle3 % np.pi == 0 or angle4 % np.pi == 0 or angle5 % np.pi == 0:
            continue

        task = f"Вычислите: $\\sin(\\frac{{{angles[0]} \\cdot \\pi}}{{{angles[1]}}}) \\cdot \\sin(\\frac{{{angles[0]} \\cdot \\pi}}{{{angles[2]}}}) \\cdot \\sin(\\frac{{{angles[3]} \\cdot \\pi}}{{{angles[1]}}}) \\cdot \\sin(\\frac{{{angles[4]} \\cdot \\pi}}{{{angles[5]}}}) \\cdot \\sin(\\frac{{{angles[3]} \\cdot \\pi}}{{{angles[2]}}})$"

        answer = np.sin(angle1) * np.sin(angle2) * np.sin(angle3) * np.sin(angle4) * np.sin(angle5)

        if abs(answer * 10000 - int(answer * 10000) )< 0.000001 and abs(answer)>0.01:
            break

    return {
        "condition": task,
        "answer": round(answer, 4)
    }


def trigonometry_14261():
    ''' Задание на портале kuzovkin.info № 14261 '''

    while True:
        angles = np.random.randint(10, 360, 2)

        if angles[0] % 15 == 0 or angles[1] % 15 == 0:
            continue

        task = f"Преобразуйте в сумму: $\\sin({angles[0]}^\\circ) \\cdot \\cos({angles[1]}^\\circ)$"

        answer = np.sin(np.radians(angles[0])) * np.cos(np.radians(angles[1]))
        if abs(answer * 10000 - int(answer * 10000) )< 0.000001 and abs(answer)>0.01:
            break

    return {
        "condition": task,
        "answer": round(answer, 4)
    }


def trigonometry_14266():
    """Задание на портале kuzovkin.info № 14266"""

    while True:
        angles = np.random.randint(10, 360, 2)
        operation = np.random.choice(['+', '-'])

        if angles[0] == angles[1]:
            continue
        try:
            cot_1, cot_2 = np.cos(np.radians(angles[0])) / np.sin(np.radians(angles[0])), np.cos(np.radians(angles[1])) / np.sin(np.radians(angles[1]))
        except ZeroDivisionError:
            continue
        task = f"Преобразуйте сумму (или разность) тригонометрических функций в произведение и упростите: $\\ctg({angles[0]}^\\circ) {operation} \\ctg({angles[1]}^\\circ)$"
        answer = eval(f"cot_1 {operation} cot_2")
        if round(answer, 3) == 1 or round(answer, 3) == 0 or round(answer, 3) == -1:
            print(answer)
            break

    return {
        "condition": task,
        "answer":  int(round(answer,3))
    }


def trigonometry_14269():
    ''' Задание на портале kuzovkin.info № 14269 '''

    while True:
        angles = np.random.randint(10, 360, 2)
        operation_1 = np.random.choice(['+', '-'])
        operation_2 = np.random.choice(['+', '-'])
        if angles[0] % 15 == 0 or angles[1] % 15 == 0:
            continue

        num1 = f"np.sin(np.radians({angles[0]})) {operation_1} np.sin(np.radians({angles[1]})"
        num2 = f"np.sin(np.radians({angles[0]})) {operation_2} np.sin(np.radians({angles[1]})"

        task = f"Преобразуйте сумму (или разность) тригонометрических функций в произведение и упростите: $\\frac{{\\sin({angles[0]}) {operation_1} \\sin({angles[1]})}}{{\\sin({angles[0]}) {operation_2} \\sin({angles[1]})}}$"

        answer = eval(f"{num1}) / {num2})")
        if abs(answer) in range(1, 10):
            break

    return {
        "condition": task,
        "answer": answer
    }


def trigonometry_14274(): # тоже самое что и 14276
    ''' Задание на портале kuzovkin.info № 14274 '''

    while True:
        num = np.random.randint(2, 30, 2)
        operation = np.random.choice(['+', '-'])
        angle1, angle2 = np.pi / num[0], np.pi / num[1]


        task = f"Преобразуйте сумму (или разность) тригонометрических функций в произведение и упростите: $\\cos(\\frac{{\\pi}}{{{num[0]}}}) {operation} \\cos(\\frac{{\\pi}}{{{num[1]}}})$"

        answer = eval(f"np.cos({angle1}) {operation} np.cos({angle2})")

        if abs(answer * 10000 - int(answer * 10000) )< 0.000001 and abs(answer)>0.01:
            break

    return {
        "condition": task,
        "answer": round(answer, 4)
    }


def trigonometry_14275():   # тоже самое что и 14278
    ''' Задание на портале kuzovkin.info № 14275 '''

    while True:
        angles = np.random.randint(-360, 361, 2)
        operation = np.random.choice(['+', '-'])

        if angles[0] % 15 == 0 or angles[1] % 15 == 0:
            continue

        task = f"Преобразуйте сумму (или разность) тригонометрических функций в произведение и упростите: $\\cos({angles[0]}) {operation} \\cos({angles[1]})$"

        answer = eval(f"np.cos(np.radians({angles[0]})) {operation} np.cos(np.radians({angles[1]}))")

        if abs(answer * 10000 - int(answer * 10000) )< 0.000001 and abs(answer)>0.01:
            break

    return {
        "condition": task,
        "answer": round(answer, 4)
    }


def trigonometry_14277():  # тоже самое что и 14279
    ''' Задание на портале kuzovkin.info № 14277 '''

    while True:
        angles = np.random.randint(-360, 361, 2)
        operation = np.random.choice(['+', '-'])

        if angles[0] % 15 == 0 or angles[1] % 15 == 0:
            continue

        task = f"Преобразуйте сумму (или разность) тригонометрических функций в произведение и упростите: $\\sin({angles[0]}) {operation} \\sin({angles[1]})$"

        answer = eval(f"np.sin(np.radians({angles[0]})) {operation} np.sin(np.radians({angles[1]}))")

        if abs(answer * 10000 - int(answer * 10000) )< 0.000001 and abs(answer)>0.01:
            break

    return {
        "condition": task,
        "answer": round(answer, 4)
    }


def trigonometry_14280():
    ''' Задание на портале kuzovkin.info № 14280 '''

    while True:
        angles = np.random.randint(-360, 361, 2)
        operation = np.random.choice(['+', '-'])

        if angles[0] % 15 == 0 or angles[1] % 15 == 0:
            continue

        task = f"Преобразуйте сумму (или разность) тригонометрических функций в произведение и упростите: $\\cos({angles[0]}) {operation} \\sin({angles[1]})$"

        answer = eval(f"np.cos(np.radians({angles[0]})) {operation} np.sin(np.radians({angles[1]}))")

        if abs(answer * 10000 - int(answer * 10000) )< 0.000001 and abs(answer)>0.01:
            break

    return {
        "condition": task,
        "answer": round(answer, 4)
    }
