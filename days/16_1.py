# OOP (Object Oriented Programming)

# one can import other python files as modules
# One can access/fetch its variable and functions through using dot(.) operator

import test_16

print(test_16.test_variable)
print(test_16.ap_natural_numbers(test_16.test_variable))


# Turtle Library

# use of turtle which is module form python itself
# Turtle is graphic library used to create vector graphics, it is pre provided by python developers
# Here Turtle() is a class in turtle module

import turtle
#instead once can dircetly import the turtle class 
# from turtle import Turtle

#creating object tut as Turtle class object
tut = turtle.Turtle() # tut = Turtle()
print(tut) # it prints the memory location of object
tut.shape("turtle")
tut.color("blue")

tut.forward(200)
tut.left(120)
tut.forward(200)
tut.left(120)
tut.forward(200)

my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()














