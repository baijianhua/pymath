import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.axes import Axes
from sympy import plot_implicit, Equality
from sympy.plotting.plot import MatplotlibBackend


def plot_latex(lat=""):
    tex = "$" + lat + "$"
    # 不设置这一行会出现dvipng报错
    rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
    rc('text', usetex=True)
    rc('text.latex', preamble=r'\usepackage{amsmath}')
    plt.text(0.05, 0.5, tex, size=40)
    plt.axis('off')
    plt.show()


# https://stackoverflow.com/questions/36505768/in-sympy-plotting-how-can-i-get-a-plot-with-a-fixed-aspect-ratio
def plot_equation(eq: Equality, x_var=None, y_var=None, ):
    # 创建plot但不绘制
    plot = plot_implicit(eq, x_var, y_var, show=False)
    # 自己初始化一个绘制引擎
    matplot = MatplotlibBackend(plot)
    # backend 给每个plot创建一个单独的坐标系，所以要取出坐标系来单独设置
    ax: Axes = matplot.ax[0]
    ax.set_aspect('equal')
    ax.grid(True)
    matplot.show()


def __ms_init(self: Axes, min_size=-2, max_size=5):
    self.axhline()
    self.axvline()
    self.set_aspect('equal')
    ticks = [i for i in range(min_size, max_size) if i != 0]
    self.xaxis.set_ticks(ticks)
    self.yaxis.set_ticks(ticks)
    self.grid(True)


Axes.ms_init = __ms_init
