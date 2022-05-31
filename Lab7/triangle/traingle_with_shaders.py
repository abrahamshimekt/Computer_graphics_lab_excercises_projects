import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from OpenGL.GL.shaders import *
import numpy as np
import os

triangleVAO, program = None, None
def getFileContents(filename):
    p = os.path.join(os.getcwd(), "shaders", filename)
    return open(p, 'r').read()


def init():
    global triangleVAO, program
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(.30, 0.20, 0.20, 1.0)
    glViewport(0, 0, 500, 500)
    
    vertexShaderContent = getFileContents("triangle.vertex.shader")
    fragmentShaderContent = getFileContents("triangle.fragment.shader")
    
    # print(vertexShaderContent)
    # print(fragmentShaderContent)
 
    vertexShader = compileShader(vertexShaderContent, GL_VERTEX_SHADER)
    fragmentShader = compileShader(fragmentShaderContent, GL_FRAGMENT_SHADER)
    
    program = glCreateProgram()
    glAttachShader(program, vertexShader)
    glAttachShader(program, fragmentShader)
    glLinkProgram(program)
    
    vertexes = np.array([
        [0.5, 0.0, 0.0,   1.0, 0.0, 0.0],
        [-0.5, 0.0, 0.0,  0.0, 1.0, 0.0],
        [0.0, 0.5, 0.0,   0.0, 0.0, 1.0]
    ], dtype=np.float32)
    
    triangleVBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, triangleVBO)
    
    glBufferData(GL_ARRAY_BUFFER, vertexes.nbytes, vertexes, GL_STATIC_DRAW)
    
    triangleVAO = glGenVertexArrays(1)
    glBindVertexArray(triangleVAO)
    
    positionLocation = glGetAttribLocation(program, "position")
    glVertexAttribPointer(positionLocation, 3, GL_FLOAT, GL_FALSE, 6*vertexes.itemsize, ctypes.c_void_p(0))
    glEnableVertexAttribArray(positionLocation)
    
    colorLocation = glGetAttribLocation(program, "color")
    glVertexAttribPointer(colorLocation, 3, GL_FLOAT, GL_FALSE, 6*vertexes.itemsize, ctypes.c_void_p(12))
    glEnableVertexAttribArray(colorLocation)
    
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)
    
    


def draw():
    global triangleVAO, program
    glClear(GL_COLOR_BUFFER_BIT)
    
    glUseProgram(program)
    glBindVertexArray(triangleVAO)
  
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