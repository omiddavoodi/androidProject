import kivy
kivy.require('1.1.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.properties import ObjectProperty

class MyPaintWidget(Widget):
	
	rects = []
	started = False
	
	def init(self):
        #self.size = [self.get_root_window().width, self.get_parent_window().height]
                return self
    
	def start(self):
                for i in range(5):
                    self.rects.append([])
                    for j in range(5):
                        self.rects[i].append([])
                with self.canvas:
                    Color(1, 0, 0)
                    for i in range(5):
                        for j in range(5):
                            self.rects[i][j] = Rectangle(pos=[self.pos[0] + 2 + 
                            (i * self.size[0] / 5.0), self.pos[1] + 2 + (j * self.size[1] / 5.0)]
                            , size=[self.size[0] / 5.0 - 4, self.size[1] / 5.0 - 4])
                
	def on_touch_down(self, touch):
		if (not self.started):
			self.start()
			self.started = True

class MyPaintApp(App):

    def build(self):
        #game = MyPaintWidget()
        #game.init()
        return MyPaintWidget()

if __name__ == '__main__':
    MyPaintApp().run()
