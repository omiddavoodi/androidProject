import kivy
kivy.require('1.1.1')
import random
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
    ],
    [
    [0,1,1,1,0],
    [1,0,0,0,1],
    [1,0,1,0,1],
    [1,0,0,0,1],
    [0,1,1,1,0]
    ],
    [
    [0,1,0,1,0],
    [1,1,1,1,1],
    [0,1,1,1,0],
    [1,1,1,1,1],
    [0,1,0,1,0]
    ],
    [
    [0,0,1,0,0],
    [0,1,1,1,0],
    [0,1,1,1,0],
    [1,1,1,1,1],
    [0,0,1,0,0]
    ],
    [
    [1,1,1,1,1],
    [0,0,1,0,0],
    [0,0,0,0,0],
    [0,0,1,0,0],
    [1,1,1,1,1]
    ],
    [
    [1,1,1,1,1],
    [1,1,0,0,1],
    [1,1,0,0,1],
    [0,0,1,1,1],
    [1,0,1,1,1]
    ],
    [
    [1,1,1,0,0],
    [0,0,0,0,1],
    [1,1,1,1,1],
    [0,0,0,0,1],
    [1,1,1,0,0]
    ],
    [
    [0,0,0,1,0],
    [0,0,0,1,0],
    [0,1,1,0,0],
    [0,0,1,0,0],
    [0,1,1,1,0]
    ],
    [
    [0,1,0,1,0],
    [1,0,0,0,1],
    [0,0,0,0,0],
    [1,0,0,0,1],
    [0,1,0,1,0]
    ],
    [
    [1,1,0,0,1],
    [1,0,1,1,0],
    [0,1,0,0,0],
    [0,1,0,1,1],
    [1,0,0,1,0]
    ],
    [
    [0,0,0,0,1],
    [0,1,1,1,1],
    [1,0,1,0,1],
    [1,0,1,0,1],
    [0,1,0,0,0]
    ],
    [
    [0,0,0,0,0],
    [0,0,0,1,0],
    [0,0,0,1,1],
    [0,1,0,1,0],
    [0,1,1,0,1]
    ],
    [
    [0,1,1,1,0],
    [1,0,0,0,1],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [1,0,0,0,1]
    ],
    [
    [1,1,0,1,0],
    [0,0,1,1,0],
    [1,0,0,1,1],
    [0,1,0,1,0],
    [0,1,0,1,0]
    ],
    [
    [0,0,0,1,0],
    [1,0,0,1,0],
    [0,0,1,0,0],
    [0,1,0,0,1],
    [0,1,0,0,0]
    ],
    [
    [0,0,0,0,0],
    [0,0,0,1,1],
    [0,1,0,0,0],
    [1,0,0,0,1],
    [0,1,1,0,0]
    ]
    ]

class MyPaintWidget(Widget):
    
    rects = [] #this holds the state of 25 different areas
    started = False #determines whether the game is started or not
    level = 0 #current level
    random = False #if the level is random...
    
    def update_screen(self):
        '''updates the screen'''
        #we redraw everything at each update so that the game can support them rotation of the device
        with self.canvas:
            #clear everthing
            self.canvas.clear()
            Color(0, 0, 0)
            Rectangle(pos=self.pos, size=self.size)
            for i in range(5):
                for j in range(5):
                    if (self.rects[i][j] == 1): #on
                        Color(0.5, 0.35, 0.95)
                    else: #off
                        Color(0.2, 0.2, 0.2)
                    #it will draw new rectangles over the older ones.
                    Rectangle(pos=[self.pos[0] + 2 + 
                    (i * self.size[0] / 5.0), self.pos[1] + 2 + self.size[1] / 10.0 + (j * (self.size[1] * 9.0 / 10.0) / 5.0)]
                    , size=[self.size[0] / 5.0 - 4, (self.size[1] * 9.0 / 10.0) / 5.0 - 4])
            Color(1, 0 ,0)
            Rectangle(pos = [self.pos[0] + 2, self.pos[1] + 2], 
                    size=[self.size[0] / 2.0 - 4, self.size[1] / 10.0 - 4])
            Color(1, 1, 0)
            Rectangle(pos = [self.pos[0] + 2 + self.size[0] / 2.0 , self.pos[1] + 2], 
                    size=[self.size[0] / 2.0 - 4, self.size[1] / 10.0 - 4])

    def update_map(self, i, j):
        '''updates the map according to touch'''
        self.rects[i][j] = not self.rects[i][j] #the touched tile...
        if i - 1 >= 0 : self.rects[i - 1][j] = not self.rects[i - 1][j] # And
        if i + 1 <= 4 : self.rects[i + 1][j] = not self.rects[i + 1][j] # the
        if j - 1 >= 0 : self.rects[i][j - 1] = not self.rects[i][j - 1] # adjected
        if j + 1 <= 4 : self.rects[i][j + 1] = not self.rects[i][j + 1] # tiles

    def restart_level():
        pass
    
    def check_button(self, touch):
        '''finds out with button has been touched'''
        #not the most accurate way but effective still --> hamine k has omid :P :P :D 
        #moshkeli dari bia be khodam begu chera posh saram comment mizari??? >:(

        if touch.y < self.size[1] / 10.0:
            if touch.x > self.size[0] / 2.0:
                self.levels_start(self.level)
                return
            exit()
        i = int (touch.x / self.size[0] * 5.0)
        j = int (touch.y / (self.size[1] - 2) * 9.0 / 10.0 * 5.0)        
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

    def levels_start(self, level):
        '''upon start, load the first level'''
        self.rects = []
        self.load_level(level)

    def random_start(self): #creating a ranodm map
        '''randomly generates a level'''
        self.rects = [[0,0,0,0,0],
                     [0,0,0,0,0],
                     [0,0,0,0,0],
                     [0,0,0,0,0],
                     [0,0,0,0,0]]
        for i in range(random.randint(6,9)):
            self.update_map(random.randint(0,4),random.randint(0,4))            
        self.update_screen()
        
    def on_touch_down(self, touch):
        '''handles the touch event'''
        #TODO: a splash screen should replace the black one. should be done in mypaint.kv --- Omid ---
	if (not self.started):
            if (touch.y / self.size[1] <= 0.5):
                self.random = False
                self.levels_start(0)
                self.started = True
            else:
                self.random = True
                self.random_start()
                self.started = True
	else: #only check buttons if we have really started the game.
            self.check_button(touch)
            self.update_screen()
            if self.next_level():
                if (self.random or self.level == len(mapdata)):
                    exit() #TODO: some screen, etc. --- Unassigned --- maybe Reza?
                self.levels_start(self.level)
        
class MyPaintApp(App):
    def build(self):
        return MyPaintWidget() #start the game

if __name__ == '__main__':
    MyPaintApp().run()
