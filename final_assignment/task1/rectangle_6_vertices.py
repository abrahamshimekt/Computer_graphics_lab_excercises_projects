import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from OpenGL.GL.shaders import *
import numpy as np
import os

program = None


def getFileContents(filename):
    p = os.path.join(os.getcwd(), "shaders", filename)
    return open(p, 'r').read()


def init():
    global  program
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

    # vertices = np.array(
    #     [0.5, 0.5, 0.0,0.0, 1.0, 0.0,
    #      0.5,-0.5, 0.0,0.0, 1.0, 0.0,
    #      -0.5, 0.5,0.0, 0.0, 1.0, 0.0,
    #      0.5, -0.5, 0.0,0.0, 1.0, 0.0,
    #      - 0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
    #      - 0.5, 0.5, 0.0,0.0, 1.0, 0.0],
    #     dtype=np.float32)
    vertices = [0.5, 0.5, 0.0, 0.0, 0.0, 1.0,
                0.5, -0.5, 0.0, 0.0, 0.0, 1.0,
                -0.5, -0.5, 0.0, 0.0, 0.0, 1.0,
                -0.5, 0.5, 0.0, 0.0, 0.0, 1.0, ]

    indices = [0, 1, 3,
               1, 2, 3, ]
    # VBO = glGenBuffers(1)
    # glBindBuffer(GL_ARRAY_BUFFER, VBO)
    # glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
    #
    # glEnableVertexAttribArray(0)
    # glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    #
    # glEnableVertexAttribArray(1)
    # glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    vertices = np.array(vertices, dtype=np.float32)
    indices = np.array(indices, dtype=np.uint32)

    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    EBO = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))

    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

def draw():
    global  program
    glClear(GL_COLOR_BUFFER_BIT)
    glUseProgram(program)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    # glDrawArrays(GL_TRIANGLES, 0, 6)
    glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, None)

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
