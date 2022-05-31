#version 330 core

in vec3 newColor;
in vec2 outTextCoord;


out vec4 outColor;
uniform sampler2D texSampler;




void main()
{
    outColor = vec4(newColor, 1.0);
	outColor = texture(texSampler, outTextCoord);
}