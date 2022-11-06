#File:       Hfns.py

#Purpose:    Contains function objects for the A* search method.
#            h_zero returns a zero as a h function
#            h_east_west estimates a distance based on longitude
#            h_north_south estimates a distance based on latitude
#            h_straight_line estimates a straight-line distance 

import math

class H_zero:
    def name(self):
        return "h = 0"

    def h(self, long1, long2, lat1, lat2):
        return 0

class H_east_west:
    def name(self):
        return "h = east-west distance"

    def h(self, long1, long2, lat1, lat2):
        return 7.87 * abs(float(long1) - float(long2))

class H_north_south:
    def name(self):
        return "h = north-south distance"

    def h(self, long1, long2, lat1, lat2):
        return 7.87 * abs(float(lat1) - float(lat2))

class H_straight_line:
    def name(self):
        return "h = straight-line distance"

    def h(self, long1, long2, lat1, lat2):
        a = abs(lat1 - lat2)
        b = abs(long1 - long2)
        return 7.87 * math.sqrt((a * a) + (b * b))