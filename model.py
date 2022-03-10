import controller
import model   # Calling update in update_all passes a reference to this model

#Use the reference to this module to pass it to update methods
import math, random
from ball       import  Ball
from blackhole  import  Black_Hole
from floater    import  Floater
from hunter     import  Hunter
from pulsator   import  Pulsator
from special import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False
cycle_count = 0
simultons = set()
object_name = ''


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, simultons
    running = False
    cycle_count = 0
    simultons = set()

#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just one update in the simulation
def step ():
    global running, cycle_count
    if running == True:
        cycle_count += 1
        for b in simultons:
            b.update(model)
        running = False
    else:
        cycle_count += 1
        for b in simultons:
            b.update(model)
    


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global object_name
    object_name = kind

def random_angle():
    #between 0 and 2pi
    return random.random()*math.pi*2

#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y): #will need to use eval
    if object_name in ['Ball', 'Floater']:
        obj = eval(f"{object_name}(x,y,10,10,{random_angle()}, 5)")
        add(obj)
    if object_name in ['Black_Hole', 'Pulsator']:
        obj = eval(f"{object_name}(x,y,20,20)")
        add(obj)
    if object_name in ['Hunter', 'Special']:
        obj = eval(f"{object_name}(x,y,30,30,{random_angle()}, 5)")
        add(obj)
    if object_name == 'Remove':
        for s in set(simultons):
            if s.contains((x,y)):
                remove(s)


#add simulton s to the simulation
def add(s):
    simultons.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    simultons.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    return {s for s in simultons if p(s)}


#Simulation: for each simulton in the model, call its update, passing it model
#Loop over a set containing all the simultons; do not use type or isinstance:
#  let each simulton's update do the needed work, without this function knowing
#  what kinds of simultons are in the simulation
def update_all(): #temp
    global cycle_count
    if running:
        cycle_count += 1
        for b in set(simultons):
            b.update(model)

#Animation: clear then canvas; for each simulton in the model, call display
#  (a) delete all simultons on the canvas; (b) call display on all simultons
#  being simulated, adding back each to the canvas, often in a new location;
#  (c) update the label defined in the controller showing progress 
#Loop over a set containing all the simultons; do not use type or isinstance:
#  let each simulton's display do the needed work, without this function knowing
#  what kinds of simultons are in the simulation
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in simultons:
        b.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(simultons))+" simultons/"+str(cycle_count)+" cycles")
