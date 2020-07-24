import Texture
import glfw
from OpenGL.GL import GL_VERSION, glGetString, GLError, glEnable, GL_BLEND, glBlendFunc, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA
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
import pyrr
import Gui


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
    glfw.swap_interval(2)
    version = glGetString(GL_VERSION).decode('utf-8')
    print(version)
    
    positions = np.array(
        [
           -0.5, -0.5, 0.0, 0.0, 
           0.5, -0.5, 1.0, 0.0,
           0.5, 0.5, 1.0, 1.0,
           -0.5, 0.5, 0.0, 1.0
        ],np.float32)

    indicies = np.array([
        0, 1, 2,
        2, 3, 0], np.int32)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    va = VertexArray.VertexArray()
    vb  = VertexBuffer.VertexBuffer(positions, 4 * 4 * ctypes.sizeof(ctypes.c_float))

    layout = VertexBufferLayout.VertexBufferLayout()
    layout.push(ctypes.c_float, 2)
    layout.push(ctypes.c_float, 2)
    va.AddBuffer(vb, layout)

    ib = IndexBuffer.IndexBuffer(indicies, 6)

    

    shader = Shader.Shader("res/shaders/Basic.shader")
    shader.Bind()
    
    
    va.Unbind()
    shader.Unbind()
    vb.Unbind()
    ib.Unbind()
    value1 = 1
    renderer = Renderer.Renderer()

    gui = Gui.Gui(window)

    while not glfw.window_should_close(window):
        renderer.Clear()

        gui.NewFrame()

        shader.Bind()
        proj = pyrr.Matrix44.orthogonal_projection(-1.0*value1, 1.0*value1, -0.75*value1, 0.75*value1, -1.0, 1.0)
        shader.SetUniformMat4f("u_MVP", proj)

        texture = Texture.Texture("res/textures/image.png")
        texture.Bind()

        shader.SetUniform1i("u_Texture", 0)
        value1 = gui.slider("value 1", value1, 1.0, 20.0)
        gui.framerate()
        renderer.Draw(va, ib, shader)
        gui.EndFrame()
        glfw.swap_buffers(window)
        glfw.poll_events()

    del vb, ib, va, shader
    try:
        del texture
    except:
        pass
    # impl.shutdown()
    gui.endGui()
    glfw.terminate()

    return 0


try:
    main()
except GLError as Error:
    tb = sys.exc_info()[-1]
    info = traceback.extract_tb(tb)
    print(f"[OpenGL Error] {(Error.err)} occurred at operation : {Error.baseOperation.__name__} at line : {info[1][1]}")