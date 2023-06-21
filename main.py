from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.behaviors import DragBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton

kv = '''
<DraggableButton>:
    canvas.before:
        PushMatrix
        Translate:
            xy: self.pos
    canvas.after:
        Translate:
            xy: -self.pos
        PopMatrix

FloatWindow:
    BoxLayout:
        orientation: "vertical"
        size_hint: None, None
        size: 200, 150
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

        MDRaisedButton:
            text: "Click me!"
            on_release: app.button_clicked()

'''


class DraggableButton(DragBehavior, MDFlatButton):
    pass


class FloatWindow(FloatLayout):
    def __init__(self, **kwargs):
        super(FloatWindow, self).__init__(**kwargs)
        self.add_widget(DraggableButton(text='Click me!', pos_hint={"center_x": 0.5, "center_y": 0.5}))


class MainScreen(Screen):
    pass


class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(MainScreen(name="main"))

    def build(self):
        return Builder.load_string(kv)

    def on_start(self):
        self.open_float_window()

    def open_float_window(self):
        float_window = FloatWindow()
        self.float_window_screen = MDScreen()
        self.float_window_screen.add_widget(float_window)
        self.screen_manager.add_widget(self.float_window_screen)
        self.screen_manager.current = "main"

    def button_clicked(self):
        print("Button clicked!")


if __name__ == '__main__':
    MyApp().run()
