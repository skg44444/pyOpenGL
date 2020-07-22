import glfw
from OpenGL.GL import GL_VERSION, glGetString, GLError
import numpy as np
import sys
import ctypes
import traceback
import VertexBuffer
import IndexBuffer
import VertexBufferLayout
import VertexArray
import Shader
import Renderer


def main():
    if not glfw.init():
        return -1

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    window  = glfw.create_window(640, 480, "Hello World", None, None)

    if not window:
        glfw.terminate()
        return -1

    glfw.make_context_current(window)
    glfw.swap_interval(1)
    version = glGetString(GL_VERSION).decode('utf-8')
    print(version)
    
    positions = np.array(
        [
           -0.5, -0.5,
            0.5, -0.5,
            0.5,  0.5,
           -0.5,  0.5
        ],np.float32)

    indicies = np.array([
        0, 1, 2,
        2, 3, 0], np.int32)

    va = VertexArray.VertexArray()
    vb  = VertexBuffer.VertexBuffer(positions, 4 * 2 * ctypes.sizeof(ctypes.c_float))

    layout = VertexBufferLayout.VertexBufferLayout()
    layout.push(ctypes.c_float, 2)
    va.AddBuffer(vb, layout)

    ib = IndexBuffer.IndexBuffer(indicies, 6)

    shader = Shader.Shader("res/shaders/Basic.shader")
    shader.Bind()

    shader.SetUniform4f("u_Color", 0.2, 0.3, 0.8, 1.0)
    
    va.Unbind()
    shader.Unbind()
    vb.Unbind()
    ib.Unbind()

    renderer = Renderer.Renderer()

    r = 0.2
    ch = 0.05

    while not glfw.window_should_close(window):
        renderer.Clear()

        shader.Bind()
        shader.SetUniform4f("u_Color", r, 0.0, 0.0, 1.0)
        
        renderer.Draw(va, ib, shader)

        if r >= 1.0:
            ch = -0.05
        elif r <= 0.0:
            ch = 0.05

        r += ch

        glfw.swap_buffers(window)
        glfw.poll_events()

    del vb, ib, va, shader
    glfw.terminate()

    return 0


try:
    main()
except GLError as Error:
    tb = sys.exc_info()[-1]
    info = traceback.extract_tb(tb)
    print(f"[OpenGL Error] {(Error.err)} occurred at operation : {Error.baseOperation.__name__} at line : {info[1][1]}")