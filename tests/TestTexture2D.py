from . import Test
from OpenGL.GL import (glClearColor, glClear, GL_COLOR_BUFFER_BIT, glEnable, glBlendFunc,
                       GL_BLEND, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
import numpy as np
from libraries import *
import ctypes
import pyrr

class TestTexture2D(Test.Test):
    def __init__(self):
        self.positions = np.array(
        [
            -50, -50, 0.0, 0.0, 
            50, -50, 1.0, 0.0,
            50,  50, 1.0, 1.0,
            -50,  50, 0.0, 1.0
        ],np.float32)

        self.indicies = np.array([
            0, 1, 2,
            2, 3, 0], np.int32)

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        self.vb  = VertexBuffer.VertexBuffer(self.positions, 4 * 4 * ctypes.sizeof(ctypes.c_float))
        self.ib = IndexBuffer.IndexBuffer(self.indicies, 6)
        self.va = VertexArray.VertexArray()
        self.layout = VertexBufferLayout.VertexBufferLayout()
        self.shader = Shader.Shader("res/shaders/Basic.shader")
        self.shader.Bind()
        self.renderer = Renderer.Renderer()
        self.texture = Texture.Texture("res/textures/image.png")
        self.texture.Bind()

        self.layout.push(ctypes.c_float, 2)
        self.layout.push(ctypes.c_float, 2)
        self.va.AddBuffer(self.vb, self.layout)

        self.proj = pyrr.Matrix44.orthogonal_projection(0, 960, 0, 540, -1.0, 1.0)
        self.view = pyrr.Matrix44.from_translation(pyrr.Vector3([0, 0, 0])) 

        self.va.Unbind()
        self.shader.Unbind()
        self.vb.Unbind()
        self.ib.Unbind()
        self.translation1 = 0, 0, 0
        self.translation2 = 100, 100, 0
        print("Created Instance of Texture2D")


    def __del__(self):
        del self.vb, self.va, self.ib, self.shader, self.texture, self.layout
        print("Deleted Texture2D instance")

    def OnUpdate(self):
        pass

    def OnRender(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        self.model = pyrr.Matrix44.from_translation(pyrr.Vector3([self.translation1[0], self.translation1[1], 0]))
        self.mvp = self.proj*self.view*self.model
        self.shader.Bind()
        self.shader.SetUniform1i("u_Texture", 0)
        self.shader.SetUniformMat4f("u_MVP", self.mvp)
        self.renderer.Draw(self.va, self.ib, self.shader)
        
        self.model = pyrr.Matrix44.from_translation(pyrr.Vector3([self.translation2[0], self.translation2[1], 0]))
        self.mvp = self.proj*self.view*self.model
        self.shader.SetUniformMat4f("u_MVP", self.mvp)
        self.renderer.Draw(self.va, self.ib, self.shader) 

    def OnImGuiRender(self):
        self.translation1 = Gui.slider(3, "obj1", self.translation1, 0, 960)
        self.translation2 = Gui.slider(3, "obj2", self.translation2, 0, 960)