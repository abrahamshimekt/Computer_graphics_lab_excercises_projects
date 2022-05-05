import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import numpy as np


def init():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


"""drawing rectangle width 0.6 and height 0.4"""


def draw_rectangle():
    v1 = np.array([0.3, 0.2])
    v2 = np.array([0.3, -0.2])
    v3 = np.array([-0.3, -0.2])
    v4 = np.array([-0.3, 0.2])
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINE_LOOP)
    glVertex(v1)
    glVertex(v2)
    glVertex(v3)
    glVertex(v4)
    glEnd()


def draw():
    """x-y coordinate axis"""
    v = np.array([0.0, 1])
    po = np.array((0.0, -1.0))
    v1 = np.array([-1.0, 0.0])
    p1 = np.array((1.0, 0.0))
    """y - axis"""
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex(v)
    glVertex(po)
    glEnd()
    """x - axis"""
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex(v1)
    glVertex(p1)
    glEnd()
    draw_rectangle()
    """Try to program this in PyOpenGL. Start with the basic.py file and follow the instructions.
1. Create a numpy vector that contains [0.3, 0.4]
2. Create a point with numpy that is (0.1, 0.2)
3. Calculate P using P = Po + tV with t = 1
4. Draw the line with PyOpenGL
5. Recalculate and draw the line with t = 0.5 and t = 1.2 and see the difference
6. Draw a grid line X-Axis and Y-Axis with different color"""
    # v = np.array([0.3, 0.4])
    # po = np.array((0.1, 0.2))
    # p = np.add(po, v)  # when t =1
    # glColor3f(0.0, 0.0, 1.0)
    # glBegin(GL_LINES)
    # glVertex(po)
    # glVertex(p)
    # glEnd()
    glFlush()


def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw()
        pygame.display.flip()
        pygame.time.wait(10)


main()
