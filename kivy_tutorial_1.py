from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

from kivy.core.window import Window
#Window.size = (300, 100)

class MainWindow(Screen):
    pass
class SecondWindow(Screen):
    school_name = ObjectProperty(None)
    portal_name = ObjectProperty(None)
    date_exam = ObjectProperty(None)
    time_h = ObjectProperty(None)
    time_m = ObjectProperty(None)
    time_s = ObjectProperty(None)



class second_cpaper_window(Screen):
    pass
class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('my.kv')


Window.clearcolor = (1, 1, 1, 1)


class ExamPortal(App):

    def build(self):
        return kv



if __name__ == "__main__":
    ExamPortal().run()