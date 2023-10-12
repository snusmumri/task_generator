import random
import pymorphy2

"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Растворы:

№ 4774
В 2 литра 10-процентного раствора уксусной кислоты добавили 8 л чистой воды.
Определите процентное содержание уксусной кислоты в полученном растворе.

№ 4787
Какое количество 8%-го раствора соли надо взять,
чтобы его можно было развести чистой водой до получения 100 г 3%-го раствора соли?

№ 4789
Сколько воды надо выпарить из 350 г 42%-го раствора соли, чтобы получить 60%-ый раствор?

№ 9487
К 40% раствору серной кислоты добавили 50 г чистой серной кислоты,
после чего концентрация раствора стала равна 60%. Найдите первоначальный вес раствора.

№ 17645
В 2 литра 10-процентного раствора уксусной кислоты добавили 8л чистой воды.
Определить процентное соотношение уксусной кислоты в полученном растворе.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Органические соединения:

4770
Сколько килограммов воды нужно выпарить из 0,5 т целлюлозной массы,
содержащей 85% воды, чтобы получить массу с содержанием 75% воды?

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Еда:

4772
Свежие грибы содержат по весу 90% воды, а сухие − 12% воды.
Сколько получится сухих грибов из 22 кг свежих?

4782
Из 10 кг свежих фруктов получают 3,5 кг сушёных фруктов, содержащих 20% воды.
Каково процентное содержание воды в свежих фруктах?

9481
Свежие грибы содержат по массе 90% воды, а сухие − 20%.
Сколько надо собрать свежих грибов, чтобы из них получить 4,5 кг сухих грибов?

9491
Собрали 100 кг грибов. Оказалось, что их влажность 99%.
Когда их подсушили, то влажность снизилась до 98%.
Какой стала масса этих грибов после того, как их подсушили?

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""


def input_parameters_mix(task_type, i=None):
    """Генерирует случайные входные параметры для задачи."""

    if task_type == 'liquids':
        concentrates = ['уксусная кислота', 'соль', 'серная кислота']
        solution_type = 'раствор'
        water = 'вода'
        pure = 'чистая'
        i = random.randint(0, 2)
        concentrate = concentrates[i]

        return concentrate, solution_type, water, pure

    elif task_type == 'organic compound':
        concentrates = ['целлюлозная масса']
        water = 'вода'
        i = random.randint(0, len(concentrates) - 1)
        concentrate = concentrates[i]

        return concentrate, water

    elif task_type == 'food':
        ingredients = ['грибы', 'фрукты']
        fresh = 'свежие'
        dried = 'сухие'
        water = 'вода'
        i = random.randint(0, len(ingredients) - 1)
        ingredient = ingredients[i]

        return ingredient, fresh, dried, water


def inflect_word(words, case):
    """Склоняет заданное слово или фразу в указанный грамматический падеж."""
    morph = pymorphy2.MorphAnalyzer()
    parsed_words = [morph.parse(word)[0] if len(word) > 1 else word for word in words.split()]
    genitive_words = [word.inflect({case})[0] if len(word) > 1 else word for word in parsed_words]
    genitive_phrase = ' '.join(genitive_words)
    return genitive_phrase


def generate_task_4774():
    """Генерирует задачу 4774 со случайно сгенерированными входными параметрами и вычисленным ответом."""

    concentrate, solution_type, water, pure = input_parameters_mix(task_type='liquids')
    substance = f'{solution_type} {concentrate}'
    diluent = f'{pure} {water}'

    while True:
        mass_of_substance_before = random.randint(1, 10)
        concentrate_perc = random.randint(1, 99)
        mass_of_diluent_added = random.randint(1, 10)

        if mass_of_substance_before == 1:
            liter = 'литр'
        elif 1 < mass_of_substance_before < 5:
            liter = 'литра'
        else:
            liter = 'литров'

        task = (
                f'В {mass_of_substance_before} {liter} {concentrate_perc}-процентного {inflect_word(substance, "gent")} добавили {mass_of_diluent_added} л {inflect_word(diluent, "gent")}. '
                f'Определите процентное содержание {inflect_word(concentrate, "gent")} в полученном растворе. '
                )

        answer = 100 * (mass_of_substance_before * concentrate_perc / 100) / (mass_of_diluent_added + mass_of_substance_before)

        if abs(answer * 10 - int(answer * 10)) < 0.0001:
            break

    return task, round(answer, 2)


def generate_task_4787():
    """Генерирует задачу 4787 со случайно сгенерированными входными параметрами и вычисленным ответом."""

    concentrate, solution_type, water, pure = input_parameters_mix(task_type='liquids')
    substance = f'{solution_type} {concentrate}'
    diluent = f'{pure} {water}'

    while True:
        concentrate_perc_before = random.randint(1, 100)
        mass_of_substance_after = random.randint(1, 1000)
        concentrate_perc_after = random.randint(1, concentrate_perc_before)

        task = (
            f'Какое количество {concentrate_perc_before}%-го {inflect_word(substance, "gent")} надо взять, '
            f'чтобы его можно было развести {inflect_word(diluent, "ablt")} до получения {mass_of_substance_after} г {concentrate_perc_after}%-го {inflect_word(substance, "gent")}?. '
            )

        answer = 100 * (mass_of_substance_after * concentrate_perc_after / 100) / concentrate_perc_before

        if abs(answer * 10 - int(answer * 10)) < 0.0001:
            break

    return task, round(answer, 2)


def generate_task_4789():
    """Генерирует задачу 4789 со случайно сгенерированными входными параметрами и вычисленным ответом."""

    concentrate, solution_type, water, pure = input_parameters_mix(task_type='liquids')
    substance = f'{solution_type} {concentrate}'
    diluent = f'{water}'

    while True:
        mass_of_substance_before = random.randint(1, 100)
        concentrate_perc_after = random.randint(1, 100)
        concentrate_perc_before = random.randint(1, concentrate_perc_after - 1)

        task = (
            f'Сколько {inflect_word(diluent, "gent")} надо выпарить из {mass_of_substance_before} г {concentrate_perc_before}%-го {inflect_word(substance, "gent")}, чтобы получить {concentrate_perc_after}%-ый раствор?'
            )

        answer = mass_of_substance_before - ((mass_of_substance_before * concentrate_perc_before / 100) * 100 / concentrate_perc_after)

        if abs(answer * 10 - int(answer * 10)) < 0.0001:
            break

    return task, round(answer, 2)


def generate_task_9487():
    """Генерирует задачу 9487 со случайно сгенерированными входными параметрами и вычисленным ответом."""

    concentrate, solution_type, water, pure = input_parameters_mix(task_type='liquids')
    pure_substance = f'{pure} {concentrate}'

    while True:
        concentrate_perc_before = random.randint(1, 80)
        concentrate_perc_after = random.randint(concentrate_perc_before, 100)
        concentrate_mass_added = random.randint(1, 1000)

        task = (
            f'К {concentrate_perc_before}% {inflect_word(solution_type, "datv")} {inflect_word(concentrate, "gent")} добавили {concentrate_mass_added} г {inflect_word(pure_substance, "gent")}, '
            f'после чего концентрация раствора стала равна {concentrate_perc_after}%. Найдите первоначальный вес раствора.'
            )

        answer = ((concentrate_mass_added / (concentrate_perc_after - concentrate_perc_before)) * concentrate_perc_after) - concentrate_mass_added

        if abs(answer * 10 - int(answer * 10)) < 0.0001:
            break

    return task, round(answer, 2)


def generate_task_17645():
    """Генерирует задачу 17645 со случайно сгенерированными входными параметрами и вычисленным ответом."""

    concentrate, solution_type, water, pure = input_parameters_mix(task_type='liquids')
    substance = f'{solution_type} {concentrate}'
    diluent = f'{pure} {water}'

    while True:
        mass_of_substance_before = random.randint(1, 10)
        concentrate_perc = random.randint(1, 99)
        mass_of_diluent_added = random.randint(1, 10)

        if mass_of_substance_before == 1:
            liter = 'литр'
        elif 1 < mass_of_substance_before < 5:
            liter = 'литра'
        else:
            liter = 'литров'

        task = (
                f'В {mass_of_substance_before} {liter} {concentrate_perc}-процентного {inflect_word(substance, "gent")} добавили {mass_of_diluent_added} л {inflect_word(diluent, "gent")}. '
                f'Определите процентное соотношение {inflect_word(concentrate, "gent")} в полученном растворе. '
                )

        answer = 100 * (mass_of_substance_before * concentrate_perc / 100) / (mass_of_diluent_added + mass_of_substance_before)

        if abs(answer * 10 - int(answer * 10)) < 0.0001:
            break

    return task, round(answer, 2)


def generate_task_4770():
    """Генерирует задачу 4770 со случайно сгенерированными входными параметрами и вычисленным ответом."""

    concentrate, water = input_parameters_mix(task_type = 'organic compound')

    while True:
        mass_of_substance_before_t = round(random.uniform(0, 10), 1)
        mass_of_substance_before_kg = mass_of_substance_before_t * 1000
        water_perc_before = random.randint(1, 100)
        water_perc_after = random.randint(1, water_perc_before)

        task = (
            f'Сколько килограммов {inflect_word(water, "gent")} нужно выпарить из {mass_of_substance_before_t} т {inflect_word(concentrate, "gent")}, '
            f'содержащей {water_perc_before}% {inflect_word(water, "gent")}, чтобы получить массу с содержанием {water_perc_after}% {inflect_word(water, "gent")}?'
        )

        answer = mass_of_substance_before_kg - ((mass_of_substance_before_kg * (100 - water_perc_before) / 100) * 100 / (100 - water_perc_after))

        if abs(answer * 10 - int(answer * 10)) < 0.0001:
            break

    return task, round(answer, 2)


def generate_task_4772():
    """Генерирует задачу 4772 со случайно сгенерированными входными параметрами и вычисленным ответом."""

    ingredient, fresh, dried, water = input_parameters_mix(task_type='food')

    while True:
        mass_of_ingredients_before = random.randint(1, 1000)
        water_perc_before = random.randint(1, 99)
        water_perc_after = random.randint(1, water_perc_before)

        task = (
            f'{fresh.capitalize()} {inflect_word(ingredient, "nomn")} содержат по весу {water_perc_before}% {inflect_word(water, "gent")}, '
            f'а {dried} − {water_perc_after}% {inflect_word(water, "gent")}. '
            f'Сколько получится {inflect_word(dried, "gent")} {inflect_word(ingredient, "gent")} из {mass_of_ingredients_before} кг свежих?'
            )


        answer = (mass_of_ingredients_before * (100 - water_perc_before) / 100) * 100 / (100 - water_perc_after)

        if abs(answer * 10 - int(answer * 10)) < 0.0001:
            break

    return task, round(answer, 2)


def generate_task_4782():
    """Генерирует задачу 4782 со случайно сгенерированными входными параметрами и вычисленным ответом."""

    ingredient, fresh, dried, water = input_parameters_mix(task_type='food')

    while True:
        total_mass_before = random.randint(1, 1000)
        total_mass_after = random.randint(1, total_mass_before)
        water_perc_after = random.randint(1, 99)

        task = (
            f'Из 10 кг {inflect_word(fresh, "gent")} {inflect_word(ingredient, "gent")} получают 3,5 кг {inflect_word(dried, "gent")} {inflect_word(ingredient, "gent")}, содержащих 20% {inflect_word(water, "gent")}.  '
            f'Каково процентное содержание {inflect_word(water, "gent")} в {inflect_word(fresh, "loct")} {inflect_word(ingredient, "loct")}? '
            )


        answer = 100 - ((total_mass_after - (total_mass_after / 100 * water_perc_after)) * 100 / total_mass_before)

        if abs(answer * 10 - int(answer * 10)) < 0.0001:
            break

    return task, round(answer, 2)


def generate_task_9481():
    """Генерирует задачу 9481 со случайно сгенерированными входными параметрами и вычисленным ответом."""

    ingredient, fresh, dried, water = input_parameters_mix(task_type='food')

    while True:

        water_perc_before = random.randint(1, 99)
        water_perc_after = random.randint(1, water_perc_before)
        total_mass_after = random.randint(1, 1000)

        task = (
            f'{fresh.capitalize()} {inflect_word(ingredient, "nomn")} содержат по массе {water_perc_before}% {inflect_word(water, "gent")}, а {dried} − {water_perc_after}%. '
            f'Сколько надо собрать {inflect_word(fresh, "gent")} {inflect_word(ingredient, "gent")}, чтобы из них получить {total_mass_after} кг {inflect_word(dried, "gent")} {inflect_word(ingredient, "gent")}? '
            )

        answer = (total_mass_after - (total_mass_after * water_perc_after / 100)) * 100 / (100 - water_perc_before)

        if abs(answer * 10 - int(answer * 10)) < 0.0001:
            break

    return task, round(answer, 2)


def generate_task_9491():
    """Генерирует задачу 9491 со случайно сгенерированными входными параметрами и вычисленным ответом."""

    ingredient, fresh, dried, water = input_parameters_mix(task_type='food')

    while True:

        total_mass_before = random.randint(1, 1000)
        moisture_before = random.randint(2, 99)
        moisture_after = random.randint(1, moisture_before)

        task = (
            f'Собрали {total_mass_before} кг {inflect_word(ingredient, "gent")}. Оказалось, что их влажность {moisture_before}%. '
            f'Когда их подсушили, то влажность снизилась до {moisture_after}%. '
            f'Какой стала масса этих {inflect_word(ingredient, "gent")} после того, как их подсушили? '
            )

        answer = (total_mass_before - (total_mass_before * moisture_before / 100)) * 100 / (100 - moisture_after)

        if abs(answer * 10 - int(answer * 10)) < 0.0001:
            break

    return task, round(answer, 2)


if __name__ == "__main__":
    print('Задача 4774:\n', generate_task_4774())
    print('Задача 4787:\n', generate_task_4787())
    print('Задача 4789:\n', generate_task_4789())
    print('Задача 9487:\n', generate_task_9487())
    print('Задача 17645:\n', generate_task_17645())
    print('Задача 4770:\n', generate_task_4770())
    print('Задача 4772:\n', generate_task_4772())
    print('Задача 4782:\n', generate_task_4782())
    print('Задача 9481:\n', generate_task_9481())
    print('Задача 9491:\n', generate_task_9491())
