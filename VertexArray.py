import VertexBuffer
import VertexBufferLayout
from OpenGL.GL import glGenVertexArrays, glDeleteVertexArrays, glEnableVertexAttribArray, glVertexAttribPointer, glBindVertexArray

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
        for element in elements:
            glEnableVertexAttribArray(i)
            glVertexAttribPointer(i, element[1], element[0], element[2], layout.GetStride(), None)
            i += 1

    def Bind(self):
        glBindVertexArray(self.m_RendererID)

    def Unbind(self):
        glBindVertexArray(0)