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
