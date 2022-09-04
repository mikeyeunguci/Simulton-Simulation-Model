# Simulton-Simulation-Model

## Description
• Developed an application which allows the user to place different kinds of objects, which behave/display differently,
into a simulation and watch them interact
• Practiced the visualization of code through hierarchy diagrams in order to implement code using advanced classes
and inheritance
• Worked with Tkinter library to write general GUI applications by using the Model-View-Controller pattern

## Installation
Make sure all files are in the same folder
Run script.py

## Usage
Commands to click
Start - Begins the cycle counter and simulton counter on the top right
Reset - Resets the simultons and cycles back to 0 
Stop - Pauses the cycle counter and freezes all the simultons. You can still add simultons (more on that later)
Step - Increments the simulton by 1 cycle each press


Select the following simultons and click on the simulation canvas to add them: 
Ball - "Edible" simultons that travel in straight lines (can be eaten by Black Holes, Pulsators, Hunters)
Floater - "Edible" simultons that travel eratically (can be eaten by Black Holes, Pulsators, Hunters)
Black Hole - stationary simultons that eat Ball/Floater simultons
Pulsator - Special kind of Black Hole that gets bigger as it eats and smaller if it starves; if it gets too small it will remove itself from the simulation
Hunter - A Pulsator that is mobile and moves towards and eats the closest Ball/Floater simulton
Special - A Hunter that is mobile and moves towards and eats the closest Hunter/Pulsator/Black Hole (their goal is to protect the Ball/Floaters)

Reminder to Start after placing simultons
Remove - After selecting Remove click on the specific simulton on the simulation canvas that you want to remove

## Credits
UCI ICS-33: Intermediate Programming Winter 2021-2022
