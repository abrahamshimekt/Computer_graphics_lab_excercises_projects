# version 330

layout(location = 0) in vec3 position;
layout(location = 1) in vec3 color;
uniform mat4 transform;
out vec3 v_color;
void main()
{

    gl_Position =transform* vec4(position,1.0);
    v_color = color;
}
