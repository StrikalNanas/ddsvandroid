import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


class FloatingWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(FloatingWindow, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        self.border = (5, 5, 5, 5)  # Добавляем рамку
        self.button = Button(text='Click me!', size_hint=(0.2, 0.2))
        self.add_widget(self.button)

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            self.parent.pos_hint = {'x': touch.x / Window.width, 'y': touch.y / Window.height}

    def button_clicked(self, instance):
        print("Button clicked!")


class MyApp(App):
    def build(self):
        Window.size = (300, 200)
        Window.top = 100
        Window.left = 100
        Window.borderless = False  # Отключаем полноэкранный режим

        floating_window = FloatingWindow()
        return floating_window


if __name__ == '__main__':
    MyApp().run()
