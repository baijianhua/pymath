import matplotlib.pyplot as plt


def build_cartesian_plane(max_quadrant_range):
    """ The quadrant range controls the range of the quadrants"""
    l = []
    zeros = []
    plt.grid(True, color='b', zorder=0,)
    ax = plt.axes()
    head_width = float(0.1) * max_quadrant_range
    head_length = float(0.1) * max_quadrant_range
    ax.arrow(0, 0, max_quadrant_range, 0, head_width=head_width, head_length=head_length, fc='k', ec='k',zorder=100)
    ax.arrow(0, 0, -max_quadrant_range, 0, head_width=head_width, head_length=head_length, fc='k', ec='k', zorder=100)
    ax.arrow(0, 0, 0, max_quadrant_range, head_width=head_width, head_length=head_length, fc='k', ec='k', zorder=100)
    ax.arrow(0, 0, 0, -max_quadrant_range, head_width=head_width, head_length=head_length, fc='k', ec='k', zorder=100)
    counter_dash_width = max_quadrant_range * 0.02
    dividers = [0,.1,.2,.3,.4, .5, .6, .7, .8, .9, 1]
    for i in dividers:
        plt.plot([-counter_dash_width, counter_dash_width], [i*max_quadrant_range, i*max_quadrant_range], color='k')
        plt.plot([i * max_quadrant_range, i*max_quadrant_range], [-counter_dash_width, counter_dash_width], color='k')
        plt.plot([-counter_dash_width, counter_dash_width], [-i * max_quadrant_range, -i * max_quadrant_range], color='r')
        plt.plot([-i * max_quadrant_range, -i * max_quadrant_range], [-counter_dash_width, counter_dash_width], color='r')

        l.append(i * max_quadrant_range)
        l.append(-i * max_quadrant_range)
        zeros.append(0)
        zeros.append(0)


build_cartesian_plane(10)
plt.show()