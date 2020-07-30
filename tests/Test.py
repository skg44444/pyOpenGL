from libraries import Gui

class Test:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def OnUpdate(self, deltaTime):
        pass

    def OnRender(self):
        pass

    def OnImGuiRender(self):
        pass


class TestMenu(Test):
    def __init__(self):
        self.m_CurrentTest = None
        self.m_Tests = {}

    def RegisterTest(self, name, testName):
        self.m_Tests[name] = testName
        print(f"Registered test : {name} : {self.m_Tests[name]}")

    def __del__(self):
        pass

    def OnUpdate(deltaTime):
        pass

    def OnRender(self):
        pass

    def OnImGuiRender(self):
        for name in self.m_Tests:
            if(Gui.button(name)):
                self.m_CurrentTest = self.m_Tests[name]()