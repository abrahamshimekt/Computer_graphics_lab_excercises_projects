import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from OpenGL.GL.shaders import *
import numpy as np
import os
import time
import pyrr

VAO, program, = None, None


def getFileContents(filename):
    p = os.path.join(os.getcwd(), "shaders", filename)
    return open(p, 'r').read()

def rotationMatrix(degree):
    radian = degree * np.pi / 180.0
    mat = np.array([
        [np.cos(radian), -np.sin(radian), 0.0, 0.0],
        [np.sin(radian), np.cos(radian), 0.0, 0.6],
        [0.0, 0.0, 1.0, 0.4],
        [0.0, 0.0, 0.0, 1.0]
    ], dtype=np.float32)
    return mat

def init():
    global VAO, program
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-10.0, 10.0, -10.0, 10.0)


    vertexShader = compileShader(getFileContents(
        "cube.vertex.shader"), GL_VERTEX_SHADER)
    fragmentShader = compileShader(getFileContents(
        "cube.fragment.shader"), GL_FRAGMENT_SHADER)

    program = glCreateProgram()
    glAttachShader(program, vertexShader)
    glAttachShader(program, fragmentShader)
    glLinkProgram(program)

    # 36 vertices and 12 triangles to draw cube
    vertexes = np.array([
        # bottom face
        -0.5, -0.5, -0.5, 1.0, 0.0,0.0,
        0.5, -0.5, -0.5, 1.0, 0.0,0.0,
        0.5, 0.5, -0.5, 1.0, 0.0,0.0,

        0.5, 0.5, -0.5, 1.0, 0.0,0.0,
        -0.5, 0.5, -0.5, 1.0, 0.0,0.0,
        -0.5, -0.5, -0.5, 1.0, 0.0,0.0,
        # top face
        -0.5, -0.5, 0.5, 1.0, 1.0,0.0,
        0.5, -0.5, 0.5, 1.0, 1.0,0.0,
        0.5, 0.5, 0.5, 1.0, 1.0,0.0,

        0.5, 0.5, 0.5, 1.0, 1.0,0.0,
        -0.5, 0.5, 0.5, 1.0, 1.0,0.0,
        -0.5, -0.5, 0.5, 1.0, 1.0,0.0,
        # back face
        -0.5, 0.5, 0.5, .0, 1.0,0.0,
        -0.5, 0.5, -0.5, .0, 1.0,0.0,
        -0.5, -0.5, -0.5, .0, 1.0,0.0,

        -0.5, -0.5, -0.5, .0, 1.0,0.0,
        -0.5, -0.5, 0.5, .0, 1.0,0.0,
        -0.5, 0.5, 0.5, .0, 1.0,0.0,
        # front face
        0.5, 0.5, 0.5, 0.0, 0.0,0.0,
        0.5, 0.5, -0.5, 0.0, 0.0,0.0,
        0.5, -0.5, -0.5, 0.0, 0.0,0.0,

        0.5, -0.5, -0.5, 0.0, 0.0,0.0,
        0.5, -0.5, 0.5, 0.0, 0.0,0.0,
        0.5, 0.5, 0.5, 0.0, 0.0,0.0,
        # left face
        -0.5, -0.5, -0.5, 0.0, 0.0,1.0,
        0.5, -0.5, -0.5,  0.0, 0.0,1.0,
        0.5, -0.5, 0.5,  0.0, 0.0,1.0,

        0.5, -0.5, 0.5,  0.0, 0.0,1.0,
        -0.5, -0.5, 0.5,  0.0, 0.0,1.0,
        -0.5, -0.5, -0.5,  0.0, 0.0,1.0,
        # right face
        -0.5, 0.5, -0.5,  1.0, 0.0,1.0,
        0.5, 0.5, -0.5,  1.0, 0.0,1.0,
        0.5, 0.5, 0.5,  1.0, 0.0,1.0,

        0.5, 0.5, 0.5, 1.0, 0.0, 1.0,
        -0.5, 0.5, 0.5, 1.0, 0.0, 1.0,
        -0.5, 0.5, -0.5, 1.0, 0.0, 1.0,


    ], dtype=np.float32)

    VAO = glGenVertexArrays(1)
    VBO = glGenBuffers(1)

    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, vertexes.nbytes, vertexes, GL_STATIC_DRAW)
    glBindVertexArray(VAO)

    position= glGetAttribLocation(program, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE,
                          6 * vertexes.itemsize, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(program, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE,
                          6* vertexes.itemsize, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)

def draw():
    global VAO, program
    # enable clearing depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glUseProgram(program)
    # enable depth test
    glEnable(GL_DEPTH_TEST)
    # apply depth checking function
    glDepthFunc(GL_LESS)
    glBindVertexArray(VAO)

    rotation = glGetUniformLocation(program, "transform")
    # rotation = rotationMatrix(30)
    rot_x =rotationMatrix(10 * time.time()) # rotation along axis (0, 0.6, 0.4)
    rot_y = rotationMatrix(10 * time.time()) # rotation along axis (0, 0.6, 0.4)
    glUniformMatrix4fv(rotation, 1, GL_FALSE, pyrr.matrix44.multiply( rot_x,rot_y))
    glDrawArrays(GL_TRIANGLES, 0, 36)


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