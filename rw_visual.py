import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Новые блужданя строятся до тех пор, пока программа остаётся активной.
while True:
    # Построение случайного блуждания.
    rw = RandomWalk()
    rw.fill_walk()

    # Нанесение точек на диаграмму.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds, edgecolors='none', s=15)

    # Выделение первой и последней точек.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolors='none', s=100)
    plt.show()

    keep_running = input("Make another walk? (y/n): ").lower()
    if keep_running == 'n':
        break

