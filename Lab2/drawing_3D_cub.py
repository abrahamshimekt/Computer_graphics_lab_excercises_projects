import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

"""initialize the pygame window"""


def init():
    pygame.init()
    display = (900, 400)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)


vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)
t = 1  # scaling factor
x, y, z = (-1, -1, -1)  # The vector V added to the initial points of the cube
"""X - coordinates of the new cube"""
px0 = 1 + t * x
px1 = 1 + t * x
px2 = -1 + t * x
px3 = -1 + t * x
px4 = 1 + t * x
px5 = 1 + t * x
px6 = -1 + t * x
px7 = -1 + t * x
"""Y - coordinates of the new cube"""
py0 = -1 + t * y
py1 = 1 + t * y
py2 = 1 + t * y
py3 = -1 + t * y
py4 = -1 + t * y
py5 = 1 + t * y
py6 = -1 + t * y
py7 = 1 + t * y
"""Z - coordinates of the new cube"""
pz0 = -1 + t * z
pz1 = -1 + t * z
pz2 = -1 + t * z
pz3 = -1 + t * z
pz4 = 1 + t * z
pz5 = 1 + t * z
pz6 = 1 + t * z
pz7 = 1 + t * z
"""the new cube vertices"""
vertices_translated = (
    (px0, py0, pz0),
    (px1, py1, pz1),
    (px2, py2, pz2),
    (px3, py3, pz3),
    (px4, py4, pz4),
    (px5, py5, pz5),
    (px6, py6, pz6),
    (px7, py7, pz7)
)
"""Connects vertices of the cube"""
edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

"""function to draw cube with given vertices and edges"""


def cube():
    glRotatef(1, 3, 1, 1)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3f(vertex, 0.0, 1.0)  # colors the edge cube, blue
            glVertex3fv(vertices[vertex])
    glEnd()


"""function to draw a cube translated by a vector '(-1, -1, -1)' from the original cube"""


def translated_cub():
    glRotatef(1, 3, 1, 1)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3f(vertex, 1.0, 0.0)  # colors the edge cube ,yellow
            glVertex3fv(vertices_translated[vertex])
    glEnd()


"""display the pygame window """


def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        cube()
        translated_cub()
        pygame.display.flip()
        pygame.time.wait(10)


main()
