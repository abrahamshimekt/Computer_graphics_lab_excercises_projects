import os
import numpy as np
import pygame
from OpenGL.GL import *
from OpenGL.GL.shaders import *
from pygame.locals import *

triangleVAO, program ,program1= None, None,None


def getFileContent(filename):
    path = os.path.join(os.getcwd(), "shaders", filename)
    return open(path, "r").read()


def init():
    global triangleVAO, program,program1
    pygame.init()
    display = (600, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.0, 0.0, 0.0, 0.1)
    glViewport(0, 0, 600, 500)
    vertex_shader_content = getFileContent("triangle.vertex.shader")
    fragment_shader_content = getFileContent("triangle.fragment.shader")

    vertex_shader = compileShader(vertex_shader_content, GL_VERTEX_SHADER)
    fragment_shader = compileShader(fragment_shader_content, GL_FRAGMENT_SHADER)
    program = glCreateProgram()

    glAttachShader(program, vertex_shader)
    glAttachShader(program, fragment_shader)
    glLinkProgram(program)

    vertexes_1 = np.array([[0.5, 0.0, 0.0], [-0.5, 0.0, 0.0], [0.0, 0.5, 0.0]], dtype=np.float32)
    triangleVBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, triangleVBO)

    glBufferData(GL_ARRAY_BUFFER, vertexes_1.nbytes, vertexes_1, GL_STATIC_DRAW)
    triangleVAO = glGenVertexArrays(1)
    glBindVertexArray(triangleVAO)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * vertexes_1.itemsize, None)
    glEnableVertexAttribArray(0)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)
    glUseProgram(program)
    vertex_shader_content1 = getFileContent("triangle.vertex.shader1")
    fragment_shader_content1 = getFileContent("triangle.fragment.shader1")
    vertex_shader1 = compileShader(vertex_shader_content1, GL_VERTEX_SHADER)
    fragment_shader1 = compileShader(fragment_shader_content1, GL_FRAGMENT_SHADER)
    program1 = glCreateProgram()
    glAttachShader(program1, vertex_shader1)
    glAttachShader(program1, fragment_shader1)
    glLinkProgram(program1)
    vertexes_2 = np.array([[0.8, 0.0, 0.0], [-0.8, 0.0, 0.0], [0.0, 0.8, 0.0]], dtype=np.float32)
    triangleVBO1 = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, triangleVBO1)
    glBufferData(GL_ARRAY_BUFFER, vertexes_2.nbytes, vertexes_2, GL_STATIC_DRAW)
    triangleVAO1 = glGenVertexArrays(1)
    glBindVertexArray(triangleVAO1)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * vertexes_2.itemsize, None)
    glEnableVertexAttribArray(0)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)
    glUseProgram(program1)
def draw():
    global triangleVAO, program
    glClear(GL_COLOR_BUFFER_BIT)
    glBindVertexArray(triangleVAO)
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glBindVertexArray(0)


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