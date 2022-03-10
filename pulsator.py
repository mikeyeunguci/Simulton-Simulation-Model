# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    counter_constant = 30
    
    def __init__(self,x,y,width,height):
        Black_Hole.__init__(self, x, y, width, height)
        self.counter = 0
        
    def update(self, model):
        self.counter += 1
        set_eaten = Black_Hole.update(self, model)
        for _ in set_eaten:
            self.counter = 0
            self.change_dimension(1, 1)
            self.radius += 1/2
        if self.counter == Pulsator.counter_constant:
            self.counter = 0 
            self.change_dimension(1, 1)
            self.radius -= 1/2
        if self.radius == 0:
            model.remove(self)

        return set_eaten
