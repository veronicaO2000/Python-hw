#!/usr/bin/python3

# Class:     CSCI 656
# Program:   Assignment 1
# Author:    Veronica Olvera
# Z-number:  z1845587
# Date Due:  03/04/22

# Purpose:   A*

# Execution: ./hw1.py

import sys
from Data import france_latlong
from Node import Node
from Hfns import H_zero, H_east_west, H_north_south, H_straight_line

def plain_city_string(city_list):
    base_city_string = " ".join([city for city in city_list])
    full_city_string = base_city_string + " "
    return full_city_string    

    
def city_string(node_list):
    base_city_string = " ".join([node.name for node in node_list])
    full_city_string = " " + base_city_string + " "
    return full_city_string    

def city_f_string(node_list):
    base_city_string = " ".join([" " + node.name + " " + str(node.f) + " " for node in node_list])
    full_city_string = " " + base_city_string + " "
    return full_city_string    


# Function: astar(from_city, to_city, franceroads, h)
#
# Inputs:  from_city:    departure city
#          to_city:      destination city
#          france_roads: road list
#          france_latlong:   city latitude and longitude
#          h:            h function used in search
#
# Outputs:  None           
#
# Notes:    Look for shortest path between two cities using A* search.

def astar(from_city, to_city, france_roads, h):
    found_path = False
    open_list = [from_city]
    closed_list = []
    nodes_expanded = 0
    path_length = 0

    # set inital cities f, g and h values
    from_city.h = h.h((france_latlong[from_city.name]['long']), (france_latlong[to_city.name]['long']),
                        (france_latlong[from_city.name]['lat']), (france_latlong[to_city.name]['lat']))
    from_city.f = from_city.h + from_city.g

    #print("A* with ", h.name(), ":\n", sep='')
    print(h.name(), " for ", from_city.name, "-", to_city.name, sep='')

    # while open list is not empty
    while len(open_list) != 0:

        # pop front of openlist and set current node
        current_node = open_list.pop(0)

        # if current node is destination, set path length and break
        if current_node.name == to_city.name:
            path_length = current_node.f
            found_path = True
            break

        nodes_expanded += 1
        
        # get current node's children and calculate their f, g and h values
        # sort by name and print

        children = [Node(name, current_node.name,
                          float(france_roads[current_node.name][name]) + current_node.g,
                          h.h(france_latlong[current_node.name]['long'],
                            france_latlong[to_city.name]['long'],
                            france_latlong[current_node.name]['lat'],
                            france_latlong[to_city.name]['lat'])) for name in france_roads[current_node.name].keys()]

        children = sorted(children, key=lambda x: x.name)

        # for every child
        for child in children:
            if child not in closed_list:
                if child not in open_list:
                    # add to open list
                    open_list.append(child)

                # else if child has smaller value then openlist, replace openlist city with child
                elif child.f < open_list[open_list.index(child)].f:
                    open_list[open_list.index(child)] = child

            # else if child has smaller value then closed_list,
            # remove from closed_list and add child back onto open_list
            elif child.f < closed_list[closed_list.index(child)].f:
                open_list.append(child)
                closed_list.remove(child)

        # sort openlist by name and by f value and print
        open_list = sorted(open_list, key=lambda x: x.name)
        open_list = sorted(open_list, key=lambda x: x.f)

        # add current node to closed list and print
        closed_list.append(current_node)
        
    # if solution found
    #  backtrack through the closed list using parent references to
    #  construct the full path

    if found_path:
        solution_path = []
        while current_node != from_city:
            solution_path.insert(0, current_node.name)
            current_node = closed_list[closed_list.index(Node(current_node.parent))]
        solution_path.insert(0, from_city.name)
        print(plain_city_string(solution_path), sep='')
        print("Path length: {:.2f}".format(path_length))
    else:
        print("\nA* has no solution")
        
    print(nodes_expanded, "nodes expanded\n\n")

france_roads = {}

france_roads_file = open("france-roads1.txt")

for input_line in france_roads_file:
    input_line = input_line.strip()

    if input_line != "" and input_line[0] != "#":

        # ':' indicates new city, make new inner dict
        if ":" in input_line:
            cur_city = input_line.replace(":", "").lower().capitalize()
            france_roads[cur_city] = {}
        else:
            city_distance = input_line.split()
            france_roads[cur_city][city_distance[0]] = city_distance[1]

# close file
france_roads_file.close()

from_city = Node('Calais')
city_list = ['Bordeaux', 'Toulouse', 'Montpellier', 'Avignon', 'Marseille', 'Nice', 'Grenoble']

# find the optimal path betwen these cities using each of the four algorithms
for city in city_list:
    to_city = Node(city)

    astar(from_city, to_city, france_roads, H_zero())

    astar(from_city, to_city, france_roads, H_east_west())

    astar(from_city, to_city, france_roads, H_north_south())

    astar(from_city, to_city, france_roads, H_straight_line())