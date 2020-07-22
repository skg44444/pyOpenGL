from OpenGL.GL import (glCreateShader, glShaderSource, glCompileShader, glGetShaderiv, GL_COMPILE_STATUS,
                       GL_FALSE, glGetShaderInfoLog, GL_VERTEX_SHADER, glDeleteShader, glCreateProgram,
                       GL_FRAGMENT_SHADER, glAttachShader, glLinkProgram, glValidateProgram, glUseProgram, 
                       glDeleteProgram, glGetUniformLocation, glUniform4f, glUniform1i)

class Shader:

    def __init__(self, filepath):
        self.filepath = filepath
        vertexShader, fragmentShader = self.ParseShader(self.filepath)
        self.m_RendererID = self.CreateShader(vertexShader, fragmentShader)
        self.m_UniformLocationCache = {}

    def __del__(self):
        glDeleteProgram(self.m_RendererID)

    def Bind(self):
        glUseProgram(self.m_RendererID)

    def Unbind(self):
        glUseProgram(0)

    def ParseShader(self, filepath):
        file = open(filepath , 'r')
        shadercode = file.readlines() 

        shader = ["", "", ""]
        writeIndex = 0

        for line in shadercode:
            if line.find("#shader")!=-1:
                if line.find("vertex")!=-1:
                    writeIndex = 1
                elif line.find("fragment")!=-1:
                    writeIndex = 2
            else:
                shader[writeIndex] += line
                
        return shader[1], shader[2]

    def CompileShader(self, type, source):
        id = glCreateShader(type)
        glShaderSource(id, source)
        glCompileShader(id)

        result = glGetShaderiv(id, GL_COMPILE_STATUS)
        if (result==GL_FALSE):
            message = glGetShaderInfoLog(id).decode('utf-8')
            shadertype = "Vertex" if type==GL_VERTEX_SHADER else "Fragment"
            print(f"Failed to compile {shadertype} shader!")
            print(message)
            glDeleteShader(id)
            return 0
        return id

    def CreateShader(self, VertexShader, FragmentShader):
        program = glCreateProgram()
        vs = self.CompileShader(GL_VERTEX_SHADER, VertexShader)
        fs = self.CompileShader(GL_FRAGMENT_SHADER, FragmentShader)

        glAttachShader(program, vs)
        glAttachShader(program, fs)
        glLinkProgram(program)
        glValidateProgram(program)

        glDeleteShader(vs)
        glDeleteShader(fs)

        return program

    def SetUniform1i(self, name, value):
        glUniform1i(self.GetUniformLocation(name), value)

    def SetUniform4f(self, name, v0, v1, v2, v3):
        glUniform4f(self.GetUniformLocation(name), v0, v1, v2, v3)

    def GetUniformLocation(self, name):
        if name in self.m_UniformLocationCache:
            return self.m_UniformLocationCache[name]
        location = glGetUniformLocation(self.m_RendererID, "u_Color")
        if location == -1:
            print(f"Warning: Uniform {name} does not exist!")
        self.m_UniformLocationCache[name] = location
        return location

    
