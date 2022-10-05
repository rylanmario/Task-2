# Name: Task 2.py
# Author: Rylan
# Date created: October 4th, 2022
# Date last modified: October 4th, 2022
# Purpose: The purpose of this program is to take the geometric calculator and add a function to it.
'''
Peudocode:
1. Program will ask users input for what shape the program should calculate for.
2. The Program will then ask the user for the Length and width, if a rectangle;
Radius if a circle, and the base, both sides, and the height if a triangle
3. The program will then use functions to calculate the area and perimeter for all shapes.
'''
def circlearea():
    print("The area of the circle is", pi * radius**2, "cm2")

def circumference():
    print("The circumference of the circle is", 2 * pi * radius, "cm")
    
def recpermimeter():
    print("The perimeter of the rectangle is", (reclength + recwidth) * 2, "cm" )

def recarea():
    print("The area of the rectangle is",  recwidth * reclength, "cm2" )
 
def triarea():
    print("The area of the triangle is", base * height / 2, "cm2")

def triperimeter():
    print("The perimeter of the triangle is", base + side1 + side2, "cm")
#Functions for the calculator.

from math import pi

#Main menu for the program.
print("Geometry Calculator")
print("\n")
print("1. Calculate the area of a circle")
print("2. Calculate the area of a rectangle")
print("3. Calculate the area of a triangle")
print("4. Quit")
print("\n")
selection = float(input("Enter your choice (1-4): "))

#If statements for selections.
if (selection == 1):
    radius = float(input("What is the radius of the circle in cm: "))
    print("\n")
    circumference()
    circlearea()
#Using circle functions to calculate area and circumference.

elif (selection == 2):
    recwidth = float(input("What is the width of the rectangle in cm: "))
    reclength = float(input("What is the length of the rectangle in cm: "))
    print("\n")
    recpermimeter()
    recarea()
#Using rectangle functions to calculate area and permimeter.

elif (selection == 3):
    base = float(input("What is the length of the triangles base: "))
    side1 = float(input("What is the length of the triangles second side: "))
    side2 = float(input("What is the length of the triangles third side: "))
    height = float(input("what is the height of the triangle: "))
    print("\n")
    triperimeter()
    triarea()
# Using triangle functions to calculate area and peremeter.

elif (selection == 4):
    quit()
# Quit command for user if they want to leave

else:
    print("Invalid Number. Please choose option 1-4")
# What will be displayed if the user types a number that is not 1-4.

#Exit for program after calculations.
print("\n")
input("Press enter to quit: ")
quit()
