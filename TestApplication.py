from OpenGL.raw.GL.VERSION.GL_1_0 import glClearColor
from libraries import *
import glfw
from OpenGL.GL import GL_VERSION, glGetString, GLError, glEnable, GL_BLEND, glBlendFunc, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA
import numpy as np
import sys
import ctypes
import traceback
import pyrr
from tests import *
import time

def main():
    if not glfw.init():
        return -1

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    window  = glfw.create_window(960, 540, "Window", None, None)

    if not window:
        glfw.terminate()
        return -1

    glfw.make_context_current(window)
    glfw.swap_interval(1)
    version = glGetString(GL_VERSION).decode('utf-8')
    print(version)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    renderer = Renderer.Renderer()

    gui = Gui.Gui(window)

    testMenu = Test.TestMenu()
    testMenu.RegisterTest("Clear Color", TestClearColor.TestClearColor)
    testMenu.RegisterTest("Texture2D", TestTexture2D.TestTexture2D)
    currentTest = testMenu

    while not glfw.window_should_close(window):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        renderer.Clear()
        gui.NewFrame()
        if currentTest:
            currentTest.OnUpdate()
            currentTest.OnRender()
            Gui.begin("Tests")
            if not currentTest == testMenu and Gui.button("<-"):
                currentTest = testMenu
                dummy = testMenu.m_CurrentTest
                testMenu.m_CurrentTest = None
            currentTest.OnImGuiRender()
            if testMenu.m_CurrentTest and not (currentTest == testMenu.m_CurrentTest):
                currentTest = testMenu.m_CurrentTest
            Gui.end()
        Gui.framerate()
        gui.EndFrame()
        glfw.swap_buffers(window)
        glfw.poll_events()
    del currentTest, dummy
    del testMenu
    gui.endGui()
    glfw.terminate()

    return 0


try:
    main()
except GLError as Error:
    tb = sys.exc_info()[-1]
    info = traceback.extract_tb(tb)
    print(Error)
    print(f"[OpenGL Error] {(Error.err)} occurred at operation : {Error.baseOperation.__name__} at line : {info[1][1]}")