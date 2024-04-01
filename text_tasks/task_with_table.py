from math import ceil
import random
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal

from .utils import capitalize_word, choosing_declension_form


def task_35629():
    '''Генерация аналогичных задач № 35629 с портала https://kuzovkin.info/one_exercise_1/35629
    В июле 2017 года был взят кредит в банке на три года в размере S млн рублей, где S — целое число.
    Условия его возврата таковы: каждый январь долг увеличивается на 25% по сравнению с концом предыдущего года;
    — с февраля по июнь каждого года необходимо выплатить одним платежом часть долга;
    — в июле каждого года долг должен составлять часть кредита в соответствии со следующей таблицей (см. рис. ниже).
    Найдите наименьшее значение S, при котором каждая из выплат будет больше 3 млн рублей.'''
    months = ["апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
    month = months[random.randint(0, 7)]
    next_month = months[months.index(month) + 1]
    while True:
        years = random.randint(3, 7)
        per = random.randint(5, 30)
        pay = random.randint(1, 10)
        k_for_task = sorted([random.randint(3, 7) / 10 for i in range(1, years)], reverse = True)
        k_for_solution = k_for_task.copy()
        k_for_solution.insert(0, 1)
        k_for_solution.append(0)
        s_list = []
        for index in range(0, years):
          s = 100 * pay / ((100 + per) * k_for_solution[index] - 100 * k_for_solution[index+1])
          s_list.append(ceil(s))
          answer = max(s_list)
        line1 = ["Месяц и год"]
        line2 = ["Долг", "S"]
        for i in range(1, years+2):
          line1.append(f'{capitalize_word(next_month)} {2016+i}')
        for j in range(1, years):
          line2.append(f'{k_for_task[j-1]}S')
        line2.append("0")
        table_data = [line1, line2]
        break
    task = f'В {choosing_declension_form(next_month, "loct")} 2017 года был взят кредит в банке на {years} {"года" if years in [3, 4] else "лет"} в размере S млн рублей, где S — целое число. Условия его возврата таковы: каждый январь долг увеличивается на {per}% по сравнению с концом предыдущего года; — с февраля по {month} каждого года необходимо выплатить одним платежом часть долга; — в {choosing_declension_form(next_month, "loct")} каждого года долг должен составлять часть кредита в соответствии со следующей таблицей (см. рис. ниже). Найдите наименьшее значение S, при котором каждая из выплат будет больше {pay} млн рублей.'
    fig, ax = plt.subplots(figsize=(10, 2))
    if years < 6:
        plt.rcParams['font.size'] = '8'
    else:
        plt.rcParams['font.size'] = '10'
    # plt.text(0.0, 0.7, task, fontsize=8)
    ax.table(cellText=table_data, loc='center', cellLoc='center', cellColours=[['#D3D3D3' for i in range(1, years+3)], ['#E0FFFF' for i in range(1, years+3)]])
    ax.axis('off')
    # plt.savefig('TABLE/table_35629.png')
    plt.show()
    return {
      "condition": task,
      "answer": answer
    }

def task_35630():
    '''Генерация аналогичных задач № 35630 с портала https://kuzovkin.info/one_exercise_1/35630
    15 мая был выдан кредит на развитие бизнеса. В таблице представлен график его погашения. Текущий долг
    выражается в процентах от кредита (см. рис. ниже). В конце каждого месяца, начиная с мая, текущий долг
    увеличивается на 5%, а выплаты по погашению кредита должны происходить в первой половине каждого месяца,
    начиная с июня. На сколько процентов общая сумма выплат при таких условиях больше суммы самого кредита?'''
    while True:
        months = random.randint(3, 8)
        per = random.randint(2, 10)
        current_debt = sorted([random.randint(10, 90) for i in range(1, months)], reverse = True)
        current_debt.insert(0, 100)
        current_debt.append(0)
        s_list = []
        for index in range(0, months):
          s = Decimal(str((current_debt[index] / 100))) * Decimal(str(((100 + per) / 100))) - Decimal(str((current_debt[index + 1] / 100)))
          s_list.append(s)
        x = float(sum(s_list) * 100 - 100)
        if x * 1000 % 1000 == 0:
          answer = int(x)
        else:
          answer = x
        day = random.randint(5, 25)
        month_start = random.randint(1, 12 - months)
        month_task = {1: "январь", 2: "февраль", 3: "март", 4: "апрель", 5: "май", 6: "июнь", 7: "июль", 8: "август", 9: "сентябрь", 10: "октябрь"}
        line1 = ["Дата"]
        line2 = ["Текущий долг"]
        for i in range(0, months+1):
          line1.append(f'{day}.{"0"if (month_start+i)//10==0 else ""}{month_start+i}')
          line2.append(f'{current_debt[i]}%')
        table_data = [line1, line2]
        break
    task = f'{day} {choosing_declension_form(month_task[month_start])} был выдан кредит на развитие бизнеса. В таблице представлен график его погашения. Текущий долг выражается в процентах от кредита (см. рис. ниже). В конце каждого месяца, начиная с {choosing_declension_form(month_task[month_start])}, текущий долг увеличивается на {per}%, а выплаты по погашению кредита должны происходить в первой половине каждого месяца, начиная с {choosing_declension_form(month_task[month_start+1])}. На сколько процентов общая сумма выплат при таких условиях больше суммы самого кредита?'
    fig, ax = plt.subplots(figsize=(10, 2))
    if months < 6:
        plt.rcParams['font.size'] = '8'
    else:
        plt.rcParams['font.size'] = '10'
    # plt.text(0.0, 0.7, task, fontsize=8)
    ax.table(cellText=table_data, loc='center', cellLoc='center', cellColours=[['#D3D3D3' for i in range(1, months+3)], ['#E0FFFF' for i in range(1, months+3)]])
    ax.axis('off')
    # plt.savefig('TABLE/table_35630.png')
    plt.show()
    return {
      "condition": task,
      "answer": answer
    }

def task_35631():
    '''Генерация аналогичных задач № 35631 с портала https://kuzovkin.info/one_exercise_1/35631
    В июле 2017 года был взят кредит в банке в размере S тыс. рублей, где S — натуральное число, на 3 года. Условия его возврата таковы:
    - каждый январь долг увеличивается на 20% по сравнению с концом предыдущего года; - с февраля по июнь каждого года необходимо
    выплатить одним платежом часть долга; в июле каждого года долг должен составлять часть кредита в соответствии со следующей
    таблицей (см. рис. ниже). Найдите наименьшее значение S, при котором каждая из выплат будет составлять целое число тысяч рублей.'''
    months = ["апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
    month = months[random.randint(0, 7)]
    next_month = months[months.index(month) + 1]
    while True:
        years = random.randint(3, 7)
        per = random.randint(5, 30)
        k_for_task = sorted([random.randint(20, 80) / 100 for i in range(1, years)], reverse = True)
        k_for_solution = k_for_task.copy()
        k_for_solution.insert(0, 1)
        k_for_solution.append(0)
        pay_list = []
        for index in range(0, years):
          a1 = 100 + per
          a2 = a1 * Decimal(str(k_for_solution[index]))
          a3 = Decimal(str(k_for_solution[index+1])) * 100
          pay = (a2 - a3) / 100
          pay_list.append(pay)
        s = 1
        while True:
          count = 0
          for index in range(0, years):
            if pay_list[index]*s * 10000 % 10000 == 0:
              count += 1
          if count == years:
            break
          else:
            s += 1
        answer = s
        line1 = ["Месяц и год"]
        line2 = ["Долг", "S"]
        for i in range(1, years+2):
          line1.append(f'{capitalize_word(next_month)} {2016+i}')
        for j in range(1, years):
          line2.append(f'{k_for_task[j-1]}S')
        line2.append("0")
        table_data = [line1, line2]
        break
    task = f'В {choosing_declension_form(next_month, "loct")} 2017 года был взят кредит в банке в размере S тыс. рублей, где S — натуральное число, на {years} {"года" if years in [3, 4] else "лет"}. Условия его возврата таковы: - каждый январь долг увеличивается на {per}% по сравнению с концом предыдущего года; - с февраля по {month} каждого года необходимо выплатить одним платежом часть долга; в {choosing_declension_form(next_month, "loct")} каждого года долг должен составлять часть кредита в соответствии со следующей таблицей (см. рис. ниже). Найдите наименьшее значение S, при котором каждая из выплат будет составлять целое число тысяч рублей.'
    fig, ax = plt.subplots(figsize=(10, 2))
    if years < 6:
        plt.rcParams['font.size'] = '8'
    else:
        plt.rcParams['font.size'] = '10'
    # plt.text(0.0, 0.7, task, fontsize=8)
    ax.table(cellText=table_data, loc='center', cellLoc='center', cellColours=[['#D3D3D3' for i in range(1, years+3)], ['#E0FFFF' for i in range(1, years+3)]])
    ax.axis('off')
    # plt.savefig('TABLE/table_35631.png')
    plt.show()
    return {
      "condition": task,
      "answer": answer
    }

def task_35633():
    '''В июле планируется взять кредит в банке на сумму 10 млн рублей на некоторый срок (целое число лет). Условия его возврата таковы:
    — каждый январь долг возрастает на 20% по сравнению с концом предыдущего года; — с февраля по июнь каждого года необходимо выплатить
    часть долга; — в июле каждого года долг должен быть на одну и ту же сумму меньше долга на июль предыдущего года. На сколько лет
    планируется взять кредит, если известно, что общая сумма выплат после его полного погашения составит 18 млн рублей?'''
    months = ["апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
    month = months[random.randint(0, 7)]
    next_month = months[months.index(month) + 1]
    while True:
        s, pay = np.random.randint(2, 20, size=2)
        per = random.randint(10, 40)
        if s < pay:
          n = ((2 * 100 * (pay - s)) / (s * per)) - 1
          if n > 2 and n * 1000 % 1000 == 0:
            answer = int(n)
            break
    task = f'В {choosing_declension_form(next_month, "loct")} планируется взять кредит в банке на сумму {s} млн рублей на некоторый срок (целое число лет). Условия его возврата таковы: — каждый январь долг возрастает на {per}% по сравнению с концом предыдущего года; — с февраля по {month} каждого года необходимо выплатить часть долга; — в {choosing_declension_form(next_month, "loct")} каждого года долг должен быть на одну и ту же сумму меньше долга на {next_month} предыдущего года. На сколько лет планируется взять кредит, если известно, что общая сумма выплат после его полного погашения составит {pay} млн рублей?'
    return {
      "condition": task,
      "answer": answer
    }
