import imgui
from imgui.integrations.glfw import GlfwRenderer

class Gui:

    def __init__(self, window):
        imgui.create_context()
        self.impl = GlfwRenderer(window)
        self.color = 0.45, 0.55, 0.60, 1.00


    def NewFrame(self):
        self.impl.process_inputs()
        imgui.new_frame()
    
    def EndFrame(self):
        imgui.end_frame()
        imgui.render()
        self.impl.render(imgui.get_draw_data())

    def slider(self, label, value, minvalue, maxvalue):
        _, value = imgui.slider_float(label, value, minvalue, maxvalue, "%.0f", 1.0)
        return value

    def framerate(self):
        imgui.text(f"Frame Rate : {int(imgui.get_io().framerate)}")
        pass

    def endGui(self):
        self.impl.shutdown()