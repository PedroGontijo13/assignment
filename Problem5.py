#Write a Python function which has a list of points as its input parameter.
#  Each point is represented by a dictionary with 3 keys and each key has a value.
#  The keys of the point dictionary is “x”, “y” and “z”. Each point represent a position
#  in the 3D coordination system (space). The function should find and return the point in
#  the input list which has the minimum distance to the center of the coordination system. The
#  center of the coordination system is a point whose values for all the keys are 0 (i.e: center = {“x”=0, “y”=0, “z”=0}

import math
x = [4, 0]
y = [6, 6]
z = [8, 8]

def calculateDistance(x, y, z):
  distance = math.sqrt(((x[0]-x[1])**2 + (y[0]-y[1])**2 + (z[0]-z[1])**2))

  print("%.2f" %distance)

calculateDistance(x, y, z)