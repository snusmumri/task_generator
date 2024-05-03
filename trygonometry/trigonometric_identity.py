from string import Template
import random
import math

from sympy import *


template_task = Template(f'Вычислить $$ \$goal \\alpha $$, если $$ \$known \\alpha = $value$$\
  и  $$ \\alpha \\in [$segment] $$')

segment_q = lambda x: latex(UnevaluatedExpr(S.One*pi*(math.floor(x*2/pi))/2)) + ", " + latex(UnevaluatedExpr(S.One*pi*(math.floor(x*2/pi)+1)/2))


def get_task(radian, answer_100, target, known):
    target_ = '\\'*target.endswith('g')+target
    known_ = '\\'*known.endswith('g')+known

    f1 = lambda func: f'{"-" if func(radian)<0 else ""}' + latex(sqrt(10000-answer_100*answer_100)/100)
    f2 = lambda func: latex(sqrt(10000-answer_100*answer_100)/answer_100*(-1 if func(radian)<0 else 1))
    f3 = lambda func: latex(answer_100 / sqrt(10000-answer_100*answer_100)*(-1 if func(radian)<0 else 1))
    f4 = lambda func: latex(answer_100*sqrt(10000 + answer_100*answer_100)/(10000 + answer_100*answer_100)*(-1 if func(radian)<0 else 1))
    f5 = lambda func: f'{"-" if func(radian)<0 else ""}'+latex(sqrt(10000 + answer_100*answer_100)/(10000 + answer_100*answer_100)*100)
    f6 = lambda: latex(Rational(100, answer_100))

    values = {
        'cos': {'sin': f1(sin),  'tg': f2(sin), 'ctg': f3(sin)},
        'sin': {'cos': f1(cos), 'ctg': f2(cos),  'tg': f3(cos)},
        'ctg': {'cos': f4(sin), 'sin': f5(sin),  'tg': f6()},
         'tg': {'sin': f4(cos), 'cos': f5(cos), 'ctg': f6()}
    }
    return template_task.substitute(goal=target_, known=known_, value=values[target][known], segment=segment_q(radian))


def trig_identity(target_known='cos-sin'):
  '''функция trig_identity('target-known'):
  аргумент:
   -target - что вычислить
   -known - что дано
  возможные значения: 'sin', 'cos', 'tg', 'ctg'

  возвращает кортеж из
  1.задания вида: Вычислить target α, если known α = ... и α ∈ [..., ...]
  2.ответа в десятичной дроби
  '''
  target, known = target_known.split('-')
  target_func = {
    'cos': cos,
    'sin': sin,
    'tg': tan,
    'ctg': lambda x: 1/tan(x)
  }.get(target)

  if target_func is None:
    raise Exception(f'Unsupported target function')

  while True:
    radian = random.randint(-20,20)
    answer_100 = random.randint(-100,100)
    try:
      if target_func(radian)*answer_100 > 0:
        break
    except:
      pass

  task = get_task(radian, answer_100, target, known)
  return {
      "condition": task,
      "answer": answer_100/100
  }
