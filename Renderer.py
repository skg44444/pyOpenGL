from OpenGL.GL import glDrawElements, GL_TRIANGLES, GL_UNSIGNED_INT, GL_COLOR_BUFFER_BIT, glClear
import VertexArray
import IndexBuffer
import Shader


class Renderer:
    def Draw(self, va, ib, shader):
        shader.Bind()
        va.Bind()
        ib.Bind()

        glDrawElements(GL_TRIANGLES, ib.GetCount(),  GL_UNSIGNED_INT, None)

    def Clear(self):
        glClear(GL_COLOR_BUFFER_BIT)