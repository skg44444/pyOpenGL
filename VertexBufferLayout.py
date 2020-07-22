from OpenGL.GL import GL_FLOAT, GL_FALSE, GL_UNSIGNED_INT, GL_UNSIGNED_BYTE, GL_TRUE
import ctypes

class VertexBufferLayout:

    def __init__(self):
        self.m_Elements = []
        self.m_Stride = 0

    def GLtype(self, ctype):
        if ctype == ctypes.c_float:
            return GL_FLOAT, GL_FALSE
        elif ctype == ctypes.c_uint:
            return GL_UNSIGNED_INT, GL_FALSE
        elif ctype == ctypes.c_char:
            return GL_UNSIGNED_BYTE, GL_TRUE

    def push(self, ctype, count):
        GLtype, normalized = self.GLtype(ctype)
        self.m_Elements.append([GLtype, count, normalized])
        self.m_Stride += count * self.GetSizeOfType(GLtype)
        
    def GetSizeOfType(self, GLtype):
        if GLtype == GL_FLOAT:
            return 4
        elif GLtype == GL_UNSIGNED_INT:
            return 4
        elif GLtype == GL_UNSIGNED_BYTE:
            return 1
        else:
            return 0

    def GetStride(self):
        return self.m_Stride

    def GetElements(self):
        return self.m_Elements
        