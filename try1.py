# Aight so this gonna be ector code
# Gonna set u some code to solve certain things
# Maybe attempt a nice interface to use it so can be professional and stuff, why not
# EQuatiion of a line between 2 points, 2D and 3D
# Distance between 2 pointsm 2D and 3D
# Shotest distance from line point

import math
import os


def distance3D():
    while True:
        print("Here is a vector calc. Fristly we have distance between 2 points.")
        print()
        print("Input the x y and z coords of the first point, pressing enter after inputting each one.")
        print()

        x1 = int(input("X Coordinate = "))
        y1 = int(input("Y Coordinate = "))
        z1 = int(input("Z Coordinate = "))

        print()
        print("Input the x y and z coords of the second point, pressing enter after inputting each one.")
        print()

        x2 = int(input("X Coordinate = "))
        y2 = int(input("Y Coordinate = "))
        z2 = int(input("Z Coordinate = "))

        finalx = x2 - x1
        finaly = y2 - y1
        finalz = z2 - z1

        distance = math.sqrt(finalx**2 + finaly**2 + finalz**2)

        print()
        print(distance)
        input("Press enter to continue")



os.system('cls')
distance3D()
