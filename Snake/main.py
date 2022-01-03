from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty
from kivy.graphics.vertex_instructions import Rectangle
from kivy.core.window import Window


class MainWidget(BoxLayout): 

    _width, _height = 600, 600
    
    _rows, _cols = 40, 40
    rows, cols = NumericProperty(_rows), NumericProperty(_cols)
    
    block_width = NumericProperty(_width // _cols)
    block_height = NumericProperty(_height // _rows)
    
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        Window.size = (self._width, self._height)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        with self.canvas:
            self.rect = Rectangle(size=(self.block_width, self.block_height), pos=(self.center_x - self.block_width / 2, self.center_y - self.block_height / 2))


    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'w':
            self.rect.pos = self.rect.pos[0], self.rect.pos[1] + self.block_height
        elif keycode[1] == 's':
            self.rect.pos = self.rect.pos[0], self.rect.pos[1] - self.block_height
        elif keycode[1] == 'a':
            self.rect.pos = self.rect.pos[0] - self.block_width, self.rect.pos[1]
        elif keycode[1] == 'd':
            self.rect.pos = self.rect.pos[0] + self.block_width, self.rect.pos[1]
        return True


class Application(App):

    def build(self):
        return Builder.load_file("main.kv")


if __name__ == "__main__":
    Application().run()