import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from OpenGL.GL.shaders import *
import numpy as np
import os
import time

program, VAO = None, None


def getFileContents(filename):
    p = os.path.join(os.getcwd(), "shaders", filename)
    return open(p, 'r').read()


def rotationMatrix(degree):
    radian = degree * np.pi / 180.0
    mat = np.array([
        [np.cos(radian), -np.sin(radian), 0.0, 0.0],
        [np.sin(radian), np.cos(radian), 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ], dtype=np.float32)
    return mat


def init():
    global program, VAO
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glViewport(0, 0, 500, 500)

    vertexShaderContent = getFileContents("triangle.vertex.shader")
    fragmentShaderContent = getFileContents("triangle.fragment.shader")

    vertexShader = compileShader(vertexShaderContent, GL_VERTEX_SHADER)
    fragmentShader = compileShader(fragmentShaderContent, GL_FRAGMENT_SHADER)

    program = glCreateProgram()
    glAttachShader(program, vertexShader)
    glAttachShader(program, fragmentShader)
    glLinkProgram(program)

    vertices = np.array([
        [0.5, 0.5, 0.0, 1.0, 0.0, 0.0],
        [0.5, -0.5, 0.0, 0.0, 1.0, 0.0],
        [-0.5, -0.5, 0.0, 0.0, 0.0, 1.0]], dtype=np.float32)

    VAO = glGenVertexArrays(1)
    VBO = glGenBuffers(1)

    glBindVertexArray(VAO)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    position = glGetAttribLocation(program, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 6 * vertices.itemsize, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(program, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 6 * vertices.itemsize, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)


def draw():
    global program, VAO
    glClear(GL_COLOR_BUFFER_BIT)
    glUseProgram(program)
    glBindVertexArray(VAO)

    rot_x = rotationMatrix(20 * time.time())
    rotateMatLocation = glGetUniformLocation(program, "transform")
    # rotateMat = rotationMatrix(30)
    # rotateMat = rotationMatrix(-30)
    glUniformMatrix4fv(rotateMatLocation, 1, GL_FALSE, rot_x)
    glDrawArrays(GL_TRIANGLES, 0, 3)


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
