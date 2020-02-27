# flowers-mazes-and-fractals
This prototype can be used to 'grow' flower-like and tree-like structures using Lindenmayer systems with python and postscript.

a) To specify the Lindenmayer system, you first need to specify the alphabet, the axiom and a set of writing rules in the form of <symbol> -> <chain of symbol>. For example, one can use this very simply alphabet with only one rule
  
 s -> F
 F -> FF-F
 
b) Each symbol in the alphabet correspond to a different drawing action (e.g. draw, move, turnL, turnR, push on stack, pop stack)

c) As additional parameters, you can define the step to take for each draw/move action, the angle for turning at the starting location on the board. 

The above steps a)-c) are defined in a .json file. 

The output is a javascript file an .eps (encapsulated postscript) file that shows the resulting structure. 

Some examples:

$ python lindenmayer.py buisson.json 5

$ python lindenmayer.py plante.json 7

$ python lindenmayer.py hexamaze.json 6

$ python lindenmayer.py sierpinski.json 8

