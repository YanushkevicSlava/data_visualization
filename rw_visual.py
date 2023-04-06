import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Новые блужданя строятся до тех пор, пока программа остаётся активной.
while True:
    # Построение случайного блуждания.
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Нанесение точек на диаграмму.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds, edgecolors='none', s=1)
    # ax.plot(rw.x_values, rw.y_values, c='red', linewidth=3)
    # Выделение первой и последней точек.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolors='none', s=100)

    # Удаление осей.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n): ").lower()
    if keep_running == 'n':
        break

