#Special objects are Green objects that search and eat black holes, pulsators, and hunters in order to protect the prey
#They only target the black holes, pulsators, and hunters


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
from blackhole import Black_Hole
from hunter import Hunter


class Special(Pulsator, Mobile_Simulton):
    Vision = 200
    def __init__(self,x,y,width,height,angle,speed):
        Pulsator.__init__(self, x, y, width, height)
        Mobile_Simulton.__init__(self,x,y,width,height,angle,speed)
        self.radius = 15
        
    def update(self, model):
        Mobile_Simulton.move(self)
        
        all_hole = model.find(lambda x: type(x) in [Black_Hole, Pulsator, Hunter])
        closest_hole = ''
        for hole in all_hole:
            if self.distance(hole.get_location()) <= Special.Vision:
                if closest_hole == '':
                    closest_hole = hole
                else:
                    if self.distance(hole.get_location()) < self.distance(closest_hole.get_location()):
                        closest_hole = hole
        #change angle towards closest hole
        if closest_hole != '':
            y = closest_hole.get_location()[1] - self.get_location()[1] 
            x = closest_hole.get_location()[0] - self.get_location()[0]
            self.set_angle(atan2(y,x))
        for hole in all_hole:
            if self.contains(hole.get_location()):
                model.remove(hole)
                
        
    def display(self, canvas):
        canvas.create_oval(self._x-self.radius      , self._y-self.radius,
                                self._x+self.radius, self._y+self.radius,
                                fill='Green')