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
    [0,1,1,1,0],
    [0,1,0,1,0],
    [1,0,1,0,1],
    [0,1,0,1,0],
    [0,1,1,1,0]
    ]
    ]

class MyPaintWidget(Widget):
    
    rects = [] #this holds the state of 25 different areas
    started = False #determines whether the game is started or not
    level = 0 #current level
    temp_rects = [] #holds the canvas rectangles so that we remove the previous ones in each update to avoid memory leaks
    
    def update_screen(self):
        '''updated the screen'''
        #we redraw everything at each update so that the game can support them rotation of the device
        if self.started:
            for i in range(26):
                self.temp_rects.append(0)
        with self.canvas:
            for temp in self.temp_rects:
                self.remove_widget(temp)
            #clear everthing
            Color(0, 0, 0)
            print (self.temp_rects)
            #self.temp_rects[25] = Rectangle(pos=self.pos, size=self.size)
            for i in range(5):
                for j in range(5):
                    if (self.rects[i][j] == 1): #on
                        Color(0.5, 0.35, 0.95)
                    else: #off
                        Color(0.2, 0.2, 0.2)
                    #it will draw new rectangles over the older ones.
                    self.temp_rects[4 * i + j] = Rectangle(pos=[self.pos[0] + 2 + 
                    (i * self.size[0] / 5.0), self.pos[1] + 2 + (j * self.size[1] / 5.0)]
                    , size=[self.size[0] / 5.0 - 4, self.size[1] / 5.0 - 4])

    def update_map(self, i, j):
        '''updates the map according to touch'''
        self.rects[i][j] = not self.rects[i][j] #the touched tile...
        if i - 1 >= 0 : self.rects[i - 1][j] = not self.rects[i - 1][j] # And
        if i + 1 <= 4 : self.rects[i + 1][j] = not self.rects[i + 1][j] # the
        if j - 1 >= 0 : self.rects[i][j - 1] = not self.rects[i][j - 1] # adjected
        if j + 1 <= 4 : self.rects[i][j + 1] = not self.rects[i][j + 1] # tiles
    
    def check_button(self, touch):
        '''finds out with button has been touched'''
        #not the most accurate way but effective still
        i = int (touch.x / self.size[0] * 5.0)
        j = int (touch.y / self.size[1] * 5.0)        
        self.update_map(i, j)

    def load_level(self, level):
        '''loads level data'''
        for i in range(5):
            self.rects.append([])
            for j in range(5):
                self.rects[i].append(mapdata[level][j][i])
        self.update_screen() #visualize the level after we loaded it
        
    def next_level(self):
        '''checks if the level is finished'''
        flag = True
        for i in self.rects:
            for j in i:
                if j: flag = False
        if flag: self.level += 1
        return flag

    def start(self, level):
        '''upon start, load the first level'''
        self.rects = []
        self.load_level(level)
                
    def on_touch_down(self, touch):
        '''handles the touch event'''
        #TODO: a splash screen should replace the black one. should be done in mypaint.kv --- Omid ---
	if (not self.started):
	    self.start(0)
	    self.started = True
	else: #only check buttons if we have really started the game.
            self.check_button(touch)
            self.update_screen()
            if self.next_level():
                if (self.level == len(mapdata)):
                    exit() #TODO: some screen, etc. --- Unassigned --- maybe Reza?
                self.start(self.level)
        
class MyPaintApp(App):
    def build(self):
        return MyPaintWidget() #start the game

if __name__ == '__main__':
    MyPaintApp().run()
