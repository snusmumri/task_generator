from random import randint
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

from utilities.converting import save_to_base64
def func_matrix():
  n = randint(5, 10)
  while True:
    def graf_2():
      A =[[0]*n for _ in range(n)]
      for i in range(n):
        for j in range(n):
          A[i][j] = random.uniform(0, 1)

          if A[i][j] > 0.75:
            A[i][j] = randint(0, 20)
          else:
            A[i][j] = 0
      for i in range(n):
          for j in range(i + 1, n):
              A[j][i] = A[i][j]
      for i in range(n):
          A[i][i] = 0
      return A

    matrix = graf_2()

    def is_connected(matrix):
      n = len(matrix)
      visited = [False] * n
      queue = [0]  # Начинаем с первой вершины
      visited[0] = True

      while queue:
        u = queue.pop(0)
        for v in range(n):
          if matrix[u][v] != 0 and not visited[v]:
            visited[v] = True
            queue.append(v)
      return all(visited)

    if is_connected(matrix):
      break

  return matrix

def func_graph():
  tops = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
  edges = []
  answer_list = []
  tops_dic = {
      1:'A',
      2:'B',
      3:'C',
      4:'D',
      5:'E',
      6:'F',
      7:'G',
      8:'H',
      9:'I',
      0:'J',
      }
  A = func_matrix()
  n = len(A)
  for i in range(n):
    for j in range(n):
      edge = ()
      if A[i][j] != 0:
        edge = (tops_dic.get(i), tops_dic.get(j))
        edges.append(edge)
        answer_list.append(A[i][j])

  answer = answer_list[0] + answer_list[-1]
  task = "На рисунке справа схема дорог Н-ского района изображена в виде графа,  звёздочка в ячейке таблицы обозначает наличие дороги между двумя пунктами. Так как таблицу и схему рисовали независимо друг от друга, то нумерация населённых пунктов в таблице никак не связана с буквенными обозначениями на графе. Определите сумму протяженностей дорог из пункта "+str(edges[0][0])+" в пункт "+str(edges[0][1])+" и из пункта "+str(edges[-1][0])+" в пункт "+str(edges[-1][1])+". В ответе запишите целое число."

# Строим таблицу
  columns_list = ['П1', 'П2', 'П3', 'П4', 'П5', 'П6', 'П7', 'П8', 'П9', 'П10']
  df = pd.DataFrame(A, columns= columns_list[0: n])
  df.insert(0, ' ', columns_list[0: n])

# Строим граф G = nx.DiGraph(np.matrix(A))
  G = nx.DiGraph()
  G.add_nodes_from(tops[0: n-1])
  G.add_edges_from(edges)

  pos = nx.planar_layout(G)

#Выводим на печать
  fig, ax = plt.subplots(1, 2, figsize=(10, 5), constrained_layout=True)
  plt.subplot(1, 2, 1)
  plt.axis('off')
  table = plt.table (cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')
  table.scale(1, 3)
  fig. tight_layout ()
  plt.subplot(1, 2, 2)
  nx.draw(G, with_labels=True, pos=pos, node_size=300, arrows=True)
  # plt.show()
  plt_base64 = save_to_base64(plt)
  plt.close()

  return {
      'task': task,
      'answer': answer,
      'image': plt_base64,
  }
