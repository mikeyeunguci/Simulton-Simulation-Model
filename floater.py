# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


#from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random, randrange, randint
import math


class Floater(Prey): 
    radius = 5
    
    def __init__(self,x,y,width,height,angle,speed):
        Prey.__init__(self,x,y,width,height,angle,speed)
    
    def random_speed(self):
        numb = randint(1,2)
        if numb == 1:
            if random()/2 + self.get_speed() <= 7:
                return self.set_speed(random()/2+self.get_speed())
        else:
            if self.get_speed() - random()/2   >= 3:
                return self.set_speed(self.get_speed() - random()/2)

    def random_angle(self):
        numb = randint(1,2)
        if numb == 1:
            self.set_angle(random()/2 + self.get_angle())
        else:
            self.set_angle(self.get_angle() - random()/2)
        
        #print(random()*math.pi*2)
        #return random()*math.pi*2

    def update(self, model):
        numb = randint(1,10)
        if numb in [1,2,3]:
            self.random_speed()
            self.random_angle()
        self.move()
        
    def display(self, canvas):
        canvas.create_oval(self._x-Floater.radius      , self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill='Red')
        