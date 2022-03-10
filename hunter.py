# A Hunter class is derived from a Pulsator and then Mobile_Simulton base.
#   It inherits updating+displaying from Pusator/Mobile_Simulton: it pursues
#   any close prey, or moves in a straight line (see Mobile_Simultion).


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):  
    Vision = 200
    
    def __init__(self,x,y,width,height,angle,speed):
        Pulsator.__init__(self, x, y, width, height)
        Mobile_Simulton.__init__(self,x,y,width,height,angle,speed)
        
    def update(self, model):
        Mobile_Simulton.move(self)
        all_prey = model.find(lambda x: isinstance(x, Prey))
        closest_prey = ''
        for prey in all_prey:
            if self.distance(prey.get_location()) <= Hunter.Vision:
                if closest_prey == '':
                    closest_prey = prey
                else:
                    if self.distance(prey.get_location()) < self.distance(closest_prey.get_location()):
                        closest_prey = prey
        #change angle towards closest prey
        if closest_prey != '':
            y = closest_prey.get_location()[1] - self.get_location()[1] 
            x = closest_prey.get_location()[0] - self.get_location()[0]
            self.set_angle(atan2(y,x))
        Pulsator.update(self, model)
                
        