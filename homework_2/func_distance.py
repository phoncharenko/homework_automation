import math

def distance_two_dots(x1, y1, x2, y2):
   ddd = (x1 - x2) ** 2
   ddd += (y1 - y2) ** 2
   return math.sqrt(ddd)