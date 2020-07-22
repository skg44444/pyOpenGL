from OpenGL.GL import  glGenBuffers, glBindBuffer, glBufferData, glDeleteBuffers, GL_ELEMENT_ARRAY_BUFFER, GL_STATIC_DRAW, GLuint
import ctypes

class IndexBuffer:
    def __init__(self, data, count):
        self.m_Count = count
        self.m_RendererID = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.m_RendererID)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, count*ctypes.sizeof(GLuint), data, GL_STATIC_DRAW)

    def __del__(self):
        glDeleteBuffers(1, self.m_RendererID)

    def Bind(self):
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.m_RendererID)

    def Unbind(self):
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

    def GetCount(self):
        return self.m_Count