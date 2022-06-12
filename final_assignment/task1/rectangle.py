import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from OpenGL.GL.shaders import *
import numpy as np
import os

program = None

"""function to read shader files"""
def getFileContents(filename):
    p = os.path.join(os.getcwd(), "shaders", filename)
    return open(p, 'r').read()

"""function to initialize the pygame window"""
def init():
    global  program
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glViewport(0, 0, 500, 500)

    vertexShaderContent = getFileContents("rectangle.vertex.shader")
    fragmentShaderContent = getFileContents("rectangle.fragment.shader")

    vertexShader = compileShader(vertexShaderContent, GL_VERTEX_SHADER)
    fragmentShader = compileShader(fragmentShaderContent, GL_FRAGMENT_SHADER)

    program = glCreateProgram()
    glAttachShader(program, vertexShader)
    glAttachShader(program, fragmentShader)
    glLinkProgram(program)

    # rectangle using 6 vertices
    # vertices = np.array(
    #     [0.5, 0.5, 0.0,0.0, 1.0, 0.0,
    #      0.5,-0.5, 0.0,0.0, 1.0, 0.0,
    #      -0.5, 0.5,0.0, 0.0, 1.0, 0.0,

    #      0.5, -0.5, 0.0,0.0, 1.0, 0.0,
    #      - 0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
    #      - 0.5, 0.5, 0.0,0.0, 1.0, 0.0],
    #     dtype=np.float32)

    # rectangle using 4 vertices
    vertices =np.array( [0.5, 0.5, 0.0, 0.0, 0.0, 1.0,
                0.5, -0.5, 0.0, 0.0, 0.0, 1.0,
                -0.5, -0.5, 0.0, 0.0, 0.0, 1.0,
                -0.5, 0.5, 0.0, 0.0, 0.0, 1.0, ],dtype=np.float32)

    # index to repeat the vertices
    indices =np.array( [0, 1, 3,
               1, 2, 3, ],dtype=np.uint32)

    VBO = glGenBuffers(1) # create vertex buffer object
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    EBO = glGenBuffers(1) # create element buffer object
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

    # vertex position
    position = glGetAttribLocation(program, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    # vertex color
    color = glGetAttribLocation(program,"color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)

def draw():
    global  program
    glClear(GL_COLOR_BUFFER_BIT)
    glUseProgram(program)

    # wire framing function
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    # draw vertex arrays
    # glDrawArrays(GL_TRIANGLES, 0, 6)

    # draw element using index
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
