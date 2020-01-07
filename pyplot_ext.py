import matplotlib.pyplot as plt


def draw_vector(x, y, to_x, to_y):
    plt.quiver(x, y, to_x, to_y, angles='xy', scale_units='xy', scale=1, color='#FF0000')
