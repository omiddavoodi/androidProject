import kivy
kivy.require('1.1.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.properties import ObjectProperty

# a simple solution for the data. not the brightest one. anyone who wants
# something else should do it himself.
 
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
    
    rects = [] #this holds the state of 25 different areas
    started = False #determines whether the game is started or not
    level = 0

    def update_screen(self):
        with self.canvas:
            for i in range(5):
                for j in range(5):
                    if (self.rects[i][j] == 1): #on
                        Color(1, 0, 0)
                    else: #off
                        Color(1, 0, 1)
                    #it will draw new rectangles over the older ones.
                    #TODO: only draw the changed rectangles
                    Rectangle(pos=[self.pos[0] + 2 + 
                    (i * self.size[0] / 5.0), self.pos[1] + 2 + (j * self.size[1] / 5.0)]
                    , size=[self.size[0] / 5.0 - 4, self.size[1] / 5.0 - 4])

    def update_map(self, i, j):
        '''updates the map according to touch'''
        print self.rects
        self.rects[i][j] = 1 if not self.rects[i][j] else 0
        if i - 1 >= 0 : self.rects[i - 1][j] = 1 if not self.rects[i - 1][j] else 0
        if i + 1 <= 4 : self.rects[i + 1][j] = 1 if not self.rects[i + 1][j] else 0
        if j - 1 >= 0 : self.rects[i][j - 1] = 1 if not self.rects[i][j - 1] else 0
        if j + 1 <= 4 : self.rects[i][j + 1] = 1 if not self.rects[i][j + 1] else 0

    def check_button(self, touch):
        '''finds out with button has been touched'''

        i = int (touch.x / self.size[0] * 5.0)
        j = int (touch.y / self.size[1] * 5.0)        
        self.update_map(i, j)

    def load_level(self, level):
        for i in range(5):
            self.rects.append([])
            for j in range(5):
                self.rects[i].append(mapdata[level][i][j])
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

    def next_level(self):
        flag = True
        for i in self.rects:
            for j in i:
                if j: flag = False
        if flag: self.level += 1
        return flag

    def start(self, level):
        #upon start, load the first level               
        self.rects = []
        self.load_level(level)
                
    def on_touch_down(self, touch):
        #TODO: a splash screen should replace the black one. should be done in mypaint.kv
	if (not self.started):
	    self.start(0)
	    self.started = True
	else: #only check buttons if we have really started the game.
            self.check_button(touch)
            self.update_screen()
            if self.next_level():self.start(self.level)
        
class MyPaintApp(App):
    def build(self):
        return MyPaintWidget() #start the game

if __name__ == '__main__':
    MyPaintApp().run()
