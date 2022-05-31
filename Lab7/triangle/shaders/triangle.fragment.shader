#version 330 core

in vec3 newColor;
out vec4 color;


void main()
{
    color = vec4(newColor, 1.0);
}
