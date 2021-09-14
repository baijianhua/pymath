from pylab import *
from scipy import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import scipy.constants as const

skr = const.pi * const.epsilon_0 * 4


class DraggablePoint:
    global Polje

    def __init__(self, p, q0, ind):
        self.q = q0
        self.point = p
        self.c_kruznice = p.center
        self.press = None
        self.indeks = ind

    def connect(self):
        self.cidpress = self.point.figure.canvas.mpl_connect('button_press_event', self.button_press_event)
        self.cidrelease = self.point.figure.canvas.mpl_connect('button_release_event', self.button_release_event)
        self.cidmotion = self.point.figure.canvas.mpl_connect('motion_notify_event', self.motion_notify_event)

    def disconnect(self):
        self.point.figure.canvas.mpl_disconnect(self.cidpress)
        self.point.figure.canvas.mpl_disconnect(self.cidrelease)
        self.point.figure.canvas.mpl_disconnect(self.cidmotion)

    def button_press_event(self, event):
        if event.inaxes != self.point.axes:
            return
        contains = self.point.contains(event)[0]
        if not contains: return
        self.press = self.point.center, event.xdata, event.ydata

    def button_release_event(self, event):
        self.press = None
        self.point.figure.canvas.draw()
        # This is the part which will erase field
        # and draw for us new one
        self.c_kruznice = self.point.center[0], self.point.center[1]
        if self.indeks == 0:
            racun = polje(drs, X, Y)
            ax.cla()
            circles = []
            circles.append(ax.add_patch(circle1))
            circles.append(ax.add_patch(circle))
            circles.append(ax.add_patch(circle2))
            circles.append(ax.add_patch(circle3))
            ax.quiver(X, Y, racun[0], racun[1], color='r', alpha=0.5)
            ax.quiver(X, Y, racun[0], racun[1], edgecolor='k', facecolor='None', linewidth=.5)
            plt.draw()

    def motion_notify_event(self, event):
        if self.press is None: return
        if event.inaxes != self.point.axes: returnO
        self.point.center, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        self.point.center = (self.point.center[0] + dx, self.point.center[1] + dy)
        self.point.figure.canvas.draw()


if __name__ == '__main__':
    f_s = 0.3


    def R(x, y):
        r = np.sqrt(x ** 2 + y ** 2) + f_s
        return r


    def polje(tela, X, Y):
        Ex = 0
        Ey = 0
        for i in range(len(tela)):
            r = R(tela[i].c_kruznice[0] - X, tela[i].c_kruznice[1] - Y)
            ex = X - tela[i].c_kruznice[0]
            ey = Y - tela[i].c_kruznice[1]
            Ex += (tela[i].q / skr) * (1 / (r + f_s) ** 3) * ex
            Ey += (tela[i].q / skr) * (1 / (r + f_s) ** 3) * ey
        return Ex, Ey


    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_axes([0.05, 0.05, 0.92, 0.92])
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    scale = 0.2
    X, Y = np.mgrid[-5:5:scale, -5:5:scale]

    circles = []
    q = 3 * const.e
    s = abs(q)
    sx = sqrt(s / np.pi) * 1e8 * 5
    circle2 = patches.Circle((2, 3), 0.3, fc='r', alpha=0.5, picker=True)
    circle1 = patches.Circle((2, -3), 0.3, fc='r', alpha=0.5, picker=True)
    circle = patches.Circle((-2, 3), 0.3, fc='b', alpha=0.5, picker=True)
    circle3 = patches.Circle((-2, -3), 0.3, fc='b', alpha=0.5, picker=True)
    circles.append(ax.add_patch(circle1))
    circles.append(ax.add_patch(circle))
    circles.append(ax.add_patch(circle2))
    circles.append(ax.add_patch(circle3))
    drs = []

    i = 0
    q = [-1, 1, -1, 1]
    for c in circles:
        dr = DraggablePoint(c, q[i], i)
        dr.connect()
        drs.append(dr)
        i += 1

    racun = polje(drs, X, Y)
    ax.quiver(X, Y, racun[0], racun[1], color='r', alpha=0.5)
    ax.quiver(X, Y, racun[0], racun[1], edgecolor='k', facecolor='None', linewidth=.5)
    plt.show()
