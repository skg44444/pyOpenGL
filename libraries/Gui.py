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


    def endGui(self):
        self.impl.shutdown()


def slider(count, label, value, minvalue, maxvalue):
    if count == 1:
        _, value = imgui.slider_float(label, value, minvalue, maxvalue, "%.0f", 1.0)
        return value
    elif count == 2:
        _, value = imgui.slider_float2(label, *value, minvalue, maxvalue, "%.0f", 1.0)
        return value
    elif count == 3:
        _, value = imgui.slider_float3(label, *value, minvalue, maxvalue, "%.0f", 1.0)
        return value

def color_edit(count, label, color):
    if count==4:
        _, color = imgui.color_edit4(label, *color)
        return color

def framerate():
    imgui.text(f"Frame Rate : {int(imgui.get_io().framerate)}")
    pass

def button(label):
    return imgui.button(label)

def begin(label):
    imgui.begin(label)

def end():
    imgui.end()