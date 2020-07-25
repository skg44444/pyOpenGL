import VertexBuffer
import VertexBufferLayout
from OpenGL.GL import glGenVertexArrays, glDeleteVertexArrays, glEnableVertexAttribArray, glVertexAttribPointer, glBindVertexArray
import ctypes

class VertexArray:
    def __init__(self):
        self.m_RendererID = glGenVertexArrays(1)

    def __del__(self):
        glDeleteVertexArrays(1, self.m_RendererID)

    def AddBuffer(self, vb, layout):
        self.Bind()
        vb.Bind()
        elements = layout.GetElements()
        i = 0
        offset = 0
        for element in elements:
            glEnableVertexAttribArray(i)
            glVertexAttribPointer(i, element.count, element.type, element.normalized, layout.GetStride(), ctypes.c_void_p(offset))
            offset += element.count*layout.GetSizeOfType(element.type)
            i += 1

    def Bind(self):
        glBindVertexArray(self.m_RendererID)

    def Unbind(self):
        glBindVertexArray(0)