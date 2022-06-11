import pygame
from OpenGL.GL import *
from pygame.locals import *
from OpenGL.GL.shaders import *
import numpy as np
import os
import time
import pyrr

vao, program, rotation_loc = None, None, None


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
    global vao, program ,rotation_loc
    pygame.init()
    display = (700, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glViewport(0, 0, 500, 500)

    vertexShader = compileShader(getFileContents(
        "triangle.vertex.shader"), GL_VERTEX_SHADER)
    fragmentShader = compileShader(getFileContents(
        "triangle.fragment.shader"), GL_FRAGMENT_SHADER)

    program = glCreateProgram()
    glAttachShader(program, vertexShader)
    glAttachShader(program, fragmentShader)
    glLinkProgram(program)

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

    vao = glGenVertexArrays(1)
    vbo = glGenBuffers(1)

    glBindBuffer(GL_ARRAY_BUFFER, vbo)

    glBufferData(GL_ARRAY_BUFFER, vertexes.nbytes, vertexes, GL_STATIC_DRAW)
    glBindVertexArray(vao)

    positionLocation = glGetAttribLocation(program, "position")
    glVertexAttribPointer(positionLocation, 3, GL_FLOAT, GL_FALSE,
                          6 * vertexes.itemsize, ctypes.c_void_p(0))
    glEnableVertexAttribArray(positionLocation)

    colorLocation = glGetAttribLocation(program, "color")
    glVertexAttribPointer(colorLocation, 3, GL_FLOAT, GL_FALSE,
                          6* vertexes.itemsize, ctypes.c_void_p(12))
    glEnableVertexAttribArray(colorLocation)
    rotation_loc = glGetUniformLocation(program, "rotation")

def draw():
    global vao, program ,rotation_loc
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glUseProgram(program)
    glEnable(GL_DEPTH_TEST)
    glBindVertexArray(vao)
    rotation_loc = glGetUniformLocation(program, "rotation")
    # rotation = rotationMatrix(30)
    rot_x =rotationMatrix(15 * time.time())
    rot_y = rotationMatrix(10 * time.time())
    glUniformMatrix4fv(rotation_loc, 1, GL_FALSE, pyrr.matrix44.multiply( rot_x,rot_y))
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