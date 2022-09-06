# Simulton-Simulation-Model

## Description
• Developed an application which allows the user to place different kinds of objects, which behave/display differently,
into a simulation and watch them interact
<br />• Practiced the visualization of code through hierarchy diagrams in order to implement code using advanced classes
and inheritance
<br />• Worked with Tkinter library to write general GUI applications by using the Model-View-Controller pattern

## Installation
Make sure all files are in the same folder
<br />Run script.py

## Usage
Commands to click
<br />Start - Begins the cycle counter and simulton counter on the top right
<br />Reset - Resets the simultons and cycles back to 0 
<br />Stop - Pauses the cycle counter and freezes all the simultons. You can still add simultons (more on that later)
<br />Step - Increments the simulton by 1 cycle each press


<br />Select the following simultons and click on the simulation canvas to add them: 
<br />Ball - "Edible" simultons that travel in straight lines (can be eaten by Black Holes, Pulsators, Hunters)
<br />Floater - "Edible" simultons that travel eratically (can be eaten by Black Holes, Pulsators, Hunters)
<br />Black Hole - stationary simultons that eat Ball/Floater simultons
<br />Pulsator - Special kind of Black Hole that gets bigger as it eats and smaller if it starves; if it gets too small it will remove itself from the simulation
<br />Hunter - A Pulsator that is mobile and moves towards and eats the closest Ball/Floater simulton
<br />Special - A Hunter that is mobile and moves towards and eats the closest Hunter/Pulsator/Black Hole (their goal is to protect the Ball/Floaters)

<br />Reminder to Start after placing simultons
<br />Remove - After selecting Remove click on the specific simulton on the simulation canvas that you want to remove

## Credits
UCI ICS-33: Intermediate Programming Winter 2021-2022
