import kivy
kivy.require('1.1.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.properties import ObjectProperty

mapdata = [
    [
    [0,0,0,0,0],
    [0,0,1,0,0],
    [0,1,1,1,0],
    [0,0,1,0,0],
    [0,0,0,0,0]
    ],
    [
    [1,1,0,1,1],
    [1,0,0,0,1],
    [0,0,0,0,0],
    [1,0,0,0,1],
    [1,1,0,1,1]
    ],
    [
    [0,0,1,0,0],
    [0,1,1,1,0],
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,1,0,0]
    ],
    [
    [0,0,0,0,0],
    [0,1,0,1,0],
    [0,0,0,0,0],
    [0,1,0,1,0],
    [0,0,0,0,0]
    ]
    ]

class MyPaintWidget(Widget):
	
    rects = []
    started = False

    def update_screen(self):
        with self.canvas:
            for i in range(5):
                for j in range(5):
                    if (mapdata[level][j][i] == 1):
                        Color(1, 0, 0)
                    else:
                        Color(1, 0, 1)
                    Rectangle(pos=[self.pos[0] + 2 + 
                    (i * self.size[0] / 5.0), self.pos[1] + 2 + (j * self.size[1] / 5.0)]
                    , size=[self.size[0] / 5.0 - 4, self.size[1] / 5.0 - 4])


    def check_button(self, touch):
        pass

    def load_level(self, level):
        
        for i in range(5):
            self.rects.append(mapdata[level][i])
        
        with self.canvas:
            for i in range(5):
                for j in range(5):
                    if (mapdata[level][j][i] == 1):
                        Color(1, 0, 0)
                    else:
                        Color(1, 0, 1)
                    Rectangle(pos=[self.pos[0] + 2 + 
                    (i * self.size[0] / 5.0), self.pos[1] + 2 + (j * self.size[1] / 5.0)]
                    , size=[self.size[0] / 5.0 - 4, self.size[1] / 5.0 - 4])

    def init(self):
    #self.size = [self.get_root_window().width, self.get_parent_window().height]
        return self
    
    def start(self):
        self.load_level(0)
                
    def on_touch_down(self, touch):
	if (not self.started):
	    self.start()
	    self.started = True
        self.check_button(touch)
        self.update_screen()
        
class MyPaintApp(App):

    def build(self):
        #game = MyPaintWidget()
        #game.init()
        return MyPaintWidget()

if __name__ == '__main__':
    MyPaintApp().run()
