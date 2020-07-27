from OpenGL.GL import glDrawElements, GL_TRIANGLES, GL_UNSIGNED_INT, GL_COLOR_BUFFER_BIT, glClear
from . import VertexArray
from . import IndexBuffer
from . import Shader


class Renderer:
    def Draw(self, va, ib, shader):
        shader.Bind()
        va.Bind()
        ib.Bind()

        glDrawElements(GL_TRIANGLES, ib.GetCount(),  GL_UNSIGNED_INT, None)

    def Clear(self):
        glClear(GL_COLOR_BUFFER_BIT)