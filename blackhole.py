# A Black_Hole is derived from a Simulton base; it updates by finding+removing
#   any objects (derived from a Prey base) whose center is crosses inside its
#   radius (and returns a set of all eaten simultons); it displays as a black
#   circle with a radius of 10 (e.g., a width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):  
    radius = 10
    
    def __init__(self,x,y,width,height):
        Simulton.__init__(self, x, y, width, height)
        
    def update(self, model):
        set_eaten = set()
        s = model.find(lambda x: isinstance(x, Prey)) 
        for x in set(s):
            if self.contains(x.get_location()):
                set_eaten.add(x)
                model.remove(x)
        return set_eaten
    
    def display(self, canvas):
        canvas.create_oval(self._x-self.radius      , self._y-self.radius,
                                self._x+self.radius, self._y+self.radius,
                                fill='Black')
    
    def contains(self,xy):
        if self.distance(xy) < self.radius:
            return True
        
