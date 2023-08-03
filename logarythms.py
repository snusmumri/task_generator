import random


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
    task = r'Вычислите: \(log{'+ str(base_of_logarythm)+"}{"+str(degree_of_logarithm)+"} \)"

  return task, answer
