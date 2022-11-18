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


"""rotating function"""


def rotation_matrix(degree):
    radian = degree * np.pi / 180
    mat = np.array([[np.cos(radian), -1 * np.sin(radian)], [np.sin(radian), np.cos(radian)]])
    return mat


"""drawing rectangle width 0.6 and height 0.4"""


def draw_rectangle():
    t = 1  # scaling factor
    """v1,v2,v3 and v4 are vector"""
    p0 = np.array((0.3, 0.2))
    v1 = np.array([0.0, -0.4])
    p0f = np.add(p0, t * v1)
    p1 = np.array((0.3, -0.2))
    v2 = np.array([-0.6, 0.0])
    p1f = np.add(p1, t * v2)
    p2 = np.array((-0.3, -0.2))
    v3 = np.array([0.0, 0.4])
    p2f = np.add(p2, t * v3)
    p3 = np.array((-0.3, 0.2))
    v4 = np.array([0.6, 0.0])
    p3f = np.add(p3, t * v4)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINE_LOOP)
    glVertex(p0)
    glVertex(p0f)
    glVertex(p1)
    glVertex(p1f)
    glVertex(p2)
    glVertex(p2f)
    glVertex(p3)
    glVertex(p3f)
    glEnd()


"""drawing rectangle width 0.6 and height 0.4 and rotated by 60 degree from the positive x - axis"""


def rotate_rectangle():
    mat = rotation_matrix(60)
    translation_vector = np.array([0.4, 0.4])
    p0f = np.array((0.3, -0.2))
    p1f = np.array((-0.3, -0.2))
    p2f = np.array((-0.3, 0.2))
    p3f = np.array((0.3, 0.2))
    mat_p0f = np.dot(p0f, mat)
    mat_p1f = np.dot(p1f, mat)
    mat_p2f = np.dot(p2f, mat)
    mat_p3f = np.dot(p3f, mat)
    t_p0f = np.add(mat_p0f, translation_vector)
    t_p1f = np.add(mat_p1f, translation_vector)
    t_p2f = np.add(mat_p2f, translation_vector)
    t_p3f = np.add(mat_p3f, translation_vector)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINE_LOOP)
    glVertex(t_p0f)
    glVertex(t_p1f)
    glVertex(t_p2f)
    glVertex(t_p3f)
    glEnd()


""" since translation preserves distance this function draws a rectangle width 0.6 and height 0.4"""


def translate_rectangle():
    mat = rotation_matrix(60)
    p0f = np.array((0.3, -0.2))
    p1f = np.array((-0.3, -0.2))
    p2f = np.array((-0.3, 0.2))
    p3f = np.array((0.3, 0.2))
    new_p0f = np.dot(p0f, mat)
    new_p1f = np.dot(p1f, mat)
    new_p2f = np.dot(p2f, mat)
    new_p3f = np.dot(p3f, mat)
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINE_LOOP)
    glVertex(new_p0f)
    glVertex(new_p1f)
    glVertex(new_p2f)
    glVertex(new_p3f)
    glEnd()


def draw_coordinates():
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


def draw():
    draw_coordinates()
    draw_rectangle()
    rotate_rectangle()
    translate_rectangle()
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
