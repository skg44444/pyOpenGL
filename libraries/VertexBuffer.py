from OpenGL.GL import  glGenBuffers, glBindBuffer, glBufferData, glDeleteBuffers, GL_ARRAY_BUFFER, GL_STATIC_DRAW
import ctypes

class VertexBuffer:
    def __init__(self, data, size):
        self.m_RendererID = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.m_RendererID)
        glBufferData(GL_ARRAY_BUFFER, size, data, GL_STATIC_DRAW)

    def __del__(self):
        glDeleteBuffers(1, self.m_RendererID)

    def Bind(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.m_RendererID)

    def Unbind(self):
        glBindBuffer(GL_ARRAY_BUFFER, 0)