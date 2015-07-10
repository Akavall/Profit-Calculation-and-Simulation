from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import logging

from calc_profit import calc_profit

logging.getLogger().setLevel(logging.INFO)

def generate_plot_data():
    days_before_break_up_list = []
    prob_down_list = []
    profits_list = []
    for days_before_break in xrange(1, 126, 5):
        logging.info("On day : {}".format(days_before_break))
        for prob_down in np.linspace(0.5, 1, 25):
            days_before_break_up_list.append(days_before_break)
            prob_down_list.append(prob_down)
            profits_list.append(calc_profit(125, days_before_break, prob_down)['profit'])
    return days_before_break_up_list, prob_down_list, profits_list

def make_3d_scatter_plot(x, y, z, x_label, y_label, z_label):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(xs=x, ys=y, zs=z, zdir='z', label='ys=0, zdir=z')

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_zlabel(z_label)

    plt.show()

if __name__ == "__main__":
    x, y, z = generate_plot_data()
    make_3d_scatter_plot(x, y, z, "Days Before Break Up", "Probability to Converge", "Profit")



