import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
import time
import matplotlib.animation as animation

NUMBER_X: int = 10
NUMBER_Y: int = 10

CANVAS_WIDTH: int = 10
CANVAS_HEIGHT: int = 10


def heatmap_animation1():
    fig, ax_lst = plt.subplots(NUMBER_X, NUMBER_Y)
    ax_lst = ax_lst.ravel()

    def plot(data):
        data = np.random.rand(CANVAS_WIDTH, CANVAS_HEIGHT)
        heatmap = ax_lst[0].imshow(data, cmap='hot')

    ani = animation.FuncAnimation(fig, plot, interval=1)
    plt.show()


def heatmap_animation2():
    fig, ax_lst = plt.subplots(NUMBER_X, NUMBER_Y)
    ax_lst = ax_lst.ravel()

    data = np.random.rand(CANVAS_WIDTH, CANVAS_HEIGHT)
    im = ax_lst[0].imshow(data, cmap='hot')

    while True:
        t_start = time.time()
        data = np.random.rand(CANVAS_WIDTH, CANVAS_HEIGHT)
        im.set_data(data)
        plt.pause(0.001)
        t_end = time.time()
        print("fps = {0}".format(999 if t_end -
              t_start == 0 else 1 / (t_end - t_start)))


def heatmap_animation3():
    fig = plt.figure(figsize=(7, 12))
    # ax_lst = ax_lst.ravel()

    data = np.random.rand(6000, 3000)
    heatmap = plt.imshow(data, cmap='hot')
    fig.canvas.draw()
    plt.show(block=False)

    while True:
        data = np.random.rand(6000, 3000)
        t_start = time.time()
        heatmap.set_data(data)
        plt.pause(0.001)
        t_end = time.time()
        print("fps = {0}".format(999 if t_end -
              t_start == 0 else 1 / (t_end - t_start)))


def main():
    """
    Entry function
    :called when: the program starts
    :param none: no parameter
    :return: none
    :rtype: none
    """
    heatmap_animation3()


if __name__ == '__main__':
    main()
