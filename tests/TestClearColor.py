from . import Test
from OpenGL.GL import glClearColor, glClear, GL_COLOR_BUFFER_BIT
from libraries import Renderer, Gui

class TestClearColor(Test.Test):
    def __init__(self):
        self.m_ClearColor = 0.2, 0.3, 0.8, 1.0

    def OnRender(self):
        glClearColor(*self.m_ClearColor)
        glClear(GL_COLOR_BUFFER_BIT)

    def OnImGuiRender(self):
        _, self.m_ClearColor = Gui.color_edit(4, "Clear Color", *self.m_ClearColor)