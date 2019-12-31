#https://codereview.stackexchange.com/questions/184687/animation-of-linear-transformations

import pygame
from pygame.locals import *
import time
import numpy

WIDTH, HEIGHT = 600, 600
UNIT = 100
STEP = 0.01
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def transform_point( x_y , a, b, c, d):
    return (a*x_y[0] + b*x_y[1], c*x_y[0] + d*x_y[1])

def transform_point_basis( x_y, e1x_e1y, e2x_e2y ):
    return transform_point( x_y, e1x_e1y[0], e2x_e2y[0], e1x_e1y[1], e2x_e2y[1])

# In case you prefer just points, no lines
#points = [ [(x, y) for x in range(-WIDTH//2, WIDTH//2, UNIT ) ] for y in range(-HEIGHT//2, HEIGHT//2, UNIT) ]

# Builds the grid lines.
# Weird range for computer to cartesian coordinates
points = [ [(x, y) for x in range(-WIDTH//2, WIDTH//2) if x % UNIT == 0 or y % UNIT == 0] \
           for y in range(-HEIGHT//2, HEIGHT//2) ]

def twod_map(f, xss):
    return [ [f(item) for item in xs] for xs in xss]

def color_bases( x_y ):
    """
    Colors the 1-st canonical base (0,1) red,
    The        2-nd canonical base (1,0) green
    """
    if ( distance_from_o( x_y ) < UNIT and x_y[1] == 0 and x_y[0] > 0):
        return (255, 0, 0)
    if ( distance_from_o( x_y ) < UNIT and x_y[0] == 0 and x_y[1] >0):
        return (0, 255 ,0)
    return (255, 255, 255)

def bright_by_distance( x_y ):
    return (255 - distance_from_o( x_y ) // 3 % 256,   \
            255 - distance_from_o( x_y ) // 3 % 256,   \
            255 - distance_from_o( x_y ) // 3 % 256)


def color_up_right( x_y ):
    """
    The most right a point was in the original state, the red-der it is.
    The most height a point was in the original state, the green-er it is.
    Does not work for size > 3*255.
    """
    return (int(x_y[0] + WIDTH//2)//3%255, int(-x_y[1] + HEIGHT//2)//3%255, 0)

def main(final_coefficients, color_func=color_bases):
    for percentage in numpy.arange(0, 1, STEP):
        final_a, final_b, final_c, final_d = final_coefficients

        # In identity matrix, a and d start at one and c and c start from 0
        # In fact transform_point( point , 1, 0, 0, 1) = point
        # So to represent the transformation a and d must start
        # similar to 1 and become more and more similar to the final
        a = 1 * ( (1 - percentage) ) + percentage * final_a
        d = 1 * ( (1 - percentage) ) + percentage * final_d
        b = percentage * final_b
        c = percentage * final_c

        koefficients = (a,b,c,d) #map(lambda k: float(k) * (float(percentage)) , final_coefficients)
        show_points( twod_map(lambda p: transform_point(p, a,b,c,d), points), points, color_func)

    # Be sure final state is precise
    show_points( twod_map(lambda p: transform_point(p, *final_coefficients), points), points, color_func)

def main_basis(base_effect1, base_effect2, color_func=color_bases):
    final_coefficients =base_effect1[0], base_effect2[0], base_effect1[1], base_effect2[1]
    main(final_coefficients, color_func=color_func)

def distance_from_o(p):
    return int ( (p[0]**2 + p[1]**2)**0.5 )

def to_cartesian( x_y, width=WIDTH, height=HEIGHT ):
    return int(x_y[0] + width//2), int(-x_y[1] + height//2)

def draw_basic_grid(screen, grid):
    pygame.display.flip()
    screen.fill( (0,0,0) )
    for l in grid:
        for p in l:
            coords = to_cartesian(p)
            screen.set_at( coords, (50, 50, 50))

def show_points(points, originals, color_func=color_bases):

    draw_basic_grid(screen, originals)

    # Original points are needed for coloring.
    for (line, lineorig) in zip(points, originals):
        for (point, original) in zip(line, lineorig):
            screen.set_at( to_cartesian(point), \
                         color_func( (original) ))


main_basis( (-2, 1),
            (-1, 2),
            color_func = color_bases)