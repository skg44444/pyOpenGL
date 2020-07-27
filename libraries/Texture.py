from OpenGL.GL import (glGenTextures, glBindTexture, GL_TEXTURE_2D, glTexParameteri, GL_TEXTURE_MIN_FILTER,
                       GL_LINEAR, GL_TEXTURE_MAG_FILTER, GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE,
                       GL_RGBA8, GL_RGBA, GL_UNSIGNED_BYTE, glTexImage2D, glDeleteTextures, glActiveTexture, GL_TEXTURE0, 
                       glPixelStorei, GL_UNPACK_ALIGNMENT)
from PIL import Image

class Texture:

    def __init__(self, path):
        img = Image.open(path)
        img =img.transpose(Image.FLIP_TOP_BOTTOM)
        self.m_Width = img.width
        self.m_Height = img.height
        self.m_LocalBuffer = img.convert("RGBA").tobytes()

        self.m_RendererID = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.m_RendererID)

        # glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)        

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA8, self.m_Width, self.m_Height, 0, GL_RGBA, GL_UNSIGNED_BYTE, self.m_LocalBuffer)
        glBindTexture(GL_TEXTURE_2D, 0)
        
        if self.m_LocalBuffer:
            del self.m_LocalBuffer

    
    def __del__(self):
        glDeleteTextures(1, self.m_RendererID)

    def Bind(self, slot=0):
        glActiveTexture(GL_TEXTURE0+slot)
        glBindTexture(GL_TEXTURE_2D, self.m_RendererID)

    def Unbind(self):
        glBindTexture(GL_TEXTURE_2D, 0)

    def GetWidth(self):
        return self.m_Width

    def GetHeight(self):
        return self.m_Height