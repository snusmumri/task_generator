import numpy as np
from sympy import *
import matplotlib.pyplot as plt
from utilities.converting import save_to_base64


def plot_graph_function_sixth_degree_and_draw_tangent_to_graph_at_point():
    x = Symbol('x')
    while True:
        x1 = np.random.randint(-10, 10)
        y1 = np.random.randint(-10, 10)
        x2 = np.random.randint(-10, 10)
        while x2 == x1:
            x2 = np.random.randint(-10, 10)
        y2 = np.random.randint(-10, 10)
        while y2 == y1:
            y2 = np.random.randint(-10, 10)
        frac = Rational(y2 - y1, x2 - x1)
        if frac.is_finite and ask(Q.integer(frac * 10000)) is True and abs(frac) < 2.25:
            break
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    curve_tangent = k * x + b
    x0 = np.random.uniform(x1, x2)
    while x0 == x1 or x0 == x2:
        x0 = np.random.uniform(x1, x2)
    y0 = curve_tangent.subs(x, x0)
    while True:
        C1 = np.random.uniform(-0.0001, 0.0001)
        while C1 == 0:
            C1 = np.random.uniform(-0.0001, 0.0001)
        C2 = np.random.uniform(-0.001, 0.001)
        while C2 > -0.0001 and C2 < 0.0001:
            C2 = np.random.uniform(-0.001, 0.001)
        C3 = np.random.uniform(-0.01, 0.01)
        while C3 > -0.001 and C3 < 0.001:
            C3 = np.random.uniform(-0.01, 0.01)
        C4 = np.random.uniform(-0.1, 0.1)
        while C4 > -0.01 and C4 < 0.01:
            C4 = np.random.uniform(-0.1, 0.1)
        C5 = np.random.uniform(-1, 1)
        while C5 > -0.1 and C5 < 0.1:
            C5 = np.random.uniform(-1, 1)
        C6 = k - C1 * (x0 ** 5) - C2 * (x0 ** 4) - C3 * (x0 ** 3) - C4 * (x0 ** 2) - C5 * x0
        C7 = y0 - k * x0 + 5 * (C1 / 6) * (x0 ** 6) + 4 * (C2 / 5) * (x0 ** 5) + 3 * (C3 / 4) * (x0 ** 4) + 2 * (C4 / 3) * (x0 ** 3) + (C5 / 2) * (x0 ** 2)
        curve = (C1 / 6) * (x ** 6) + (C2 / 5) * (x ** 5) + (C3 / 4) * (x ** 4) + (C4 / 3) * (x ** 3) + (C5 / 2) * (x ** 2) + C6 * x + C7
        values = []
        prime = curve.diff(x)
        eq_diff = Eq(prime, 0)
        critical_points = solve(eq_diff, x)
        for number in critical_points:
            if im(number) == 0:
                values.append(curve.subs(x, number))
        condition = all(abs(point) < 10 for point in values)
        if condition is True:
            break
    curve_fn = lambdify(x, curve, 'numpy')
    curve_tangent_fn = lambdify(x, curve_tangent, 'numpy')
    x_vals = np.linspace(-16, 16, 20000)
    y_vals_curve_final = curve_fn(x_vals)
    y_vals_tangent = curve_tangent_fn(x_vals)
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    arrow_length = 10
    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(0, arrow_length), textcoords='offset points',
                ha='center', va='bottom')
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(arrow_length, 0), textcoords='offset points',
                ha='center', va='bottom')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.grid(True, linewidth=0.5, linestyle='dotted')
    plt.axis('equal')
    ax.set_xticks(range(-17, 17))
    ax.set_yticks(range(-17, 17))
    ax.set_xticklabels([i if i % 2 == 0 else '' for i in range(-17, 17)])
    ax.set_yticklabels([i if i % 2 == 0 else '' for i in range(-17, 17)])
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.scatter(x1, y1, color='green', label='')
    plt.scatter(x2, y2, color='green', label='')
    plt.plot(x_vals, y_vals_curve_final, color='orange', label='y = f(x)')
    plt.plot(x_vals, y_vals_tangent, color='purple', label='')
    plt.scatter(x0, y0, color='red', label='')
    plt.plot([x0, x0], [y0, 0], ':', color='red')
    plt.text(x0, 0, "x\u2092", ha='center', va='bottom')
    plt.title('')
    plt.legend()
    plt_base64 = save_to_base64(plt)
    plt.close()
    task = r'Найдите значение производной функции f(x) в точке ' + r"\(x_0 \)"
    answer = float(k)
    return {
        "condition": task,
        "answer": answer,
        "image": plt_base64,
        }
