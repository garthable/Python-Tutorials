from os import close
from classes import *

# Note: by pressing control c you will cancel whatever the termianl is doing.

# GAME EXPLANATION:
#
# Dumb muncher is hungry.
# The muncher feasts on # symbols.
# The muncher has 1000 turns to collect as much food as he can.
# You must create a brain for this dumb muncher who is represented by the @ symbol.
# Note: The map also wraps so no need to worry about edges :)

# How to control the muncher:
#
# The muncher automatically moves forward.
# To change the direction the muncher moves type muncher.direction = Direction.<desired direction>
# The different directions are:
# Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT

# Map Nodes:
#
# Map nodes are stored in the Map.
# They countain their x and y coordinate
# They also countain their state which can either be MapNodeState.EMPTY, MapNodeState.MUNCHER, or MapNodeState.FOOD.
# You could in theory spawn food directly in front of your guy but that would be cheating.
# This information is relevant as you can use it to find Food on the map as well as find out distances.

# How to access the map:
#
# The muncher has a reference to the map used.
# To access it type muncher.map
# To get a specific node type muncher.getNode(x, y)
# To get the list of all map nodes type map.mapNodes

# For more info DM me or look at the classes.py file to see functions

# When true this no longer clears the terminal each turn allowing you to use prints and check out the game history
debugMode: bool = False
# The time inbetween frames in seconds.
speed: float = 0.01
# How many turns before the game ends
amountOfTurns: int = 1000

# Finds the distance between two map nodes
# https://en.wikipedia.org/wiki/Taxicab_geometry
# ^ formula for manhattan distance can be found here.
# Absolute values in python can be done with abs() function.
def getDistance(mapNodeA: MapNode, mapNodeB: MapNode) -> int:
    xDist = abs(mapNodeA.x - mapNodeB.x)
    yDist = abs(mapNodeA.y - mapNodeB.y)
    return xDist + yDist

# Finds the distance between two map nodes while also account for the wrapping of the map
def getDistanceAdvance(mapNodeA: MapNode, mapNodeB: MapNode,
                       sizeX: int, sizeY: int) -> int:
    xDist = abs(mapNodeA.x - mapNodeB.x)
    yDist = abs(mapNodeA.y - mapNodeB.y)
    xDist1 = sizeX - xDist
    yDist1 = sizeY - yDist
    if xDist1 + yDist1 < xDist + yDist:
        return xDist1 + yDist1
    return xDist + yDist

# Calculates a weight for how dense an area is with food
def calculateFoodDensityWeightsAdvance(map: Map) -> None:
    for mapNode in map.mapNodes:
        mapNode.weight = 0
    for mapNodeA in map.mapNodes:
        if mapNodeA.state != MapNodeState.FOOD:
            continue
        for mapNodeB in map.mapNodes:
            if mapNodeA == mapNodeB:
                continue
            if mapNodeB.state == MapNodeState.FOOD:
                mapNodeA.weight += 1/getDistanceAdvance(mapNodeA, mapNodeB, map.sizeX, map.sizeY)

# Finds all the nodes in the map parameter that have the state of being food
def getAllFood(map: Map) -> list:
    foodList: list = []
    for mapNode in map.mapNodes:
        if mapNode.state == MapNodeState.FOOD:
            foodList.append(mapNode)
    return foodList
        

# Given a list of MapNodes and a target MapMode this function returns the MapMode in the list that is the closest to the targetMapMode
def findClosestNode(mapNodeList: list, targetMapMode: MapNode, map: Map) -> MapNode:
    closestNode = MapNode(-1, -1)
    closestDistance = 900000
    for mapNode in mapNodeList:
        distance = getDistanceAdvance(targetMapMode, mapNode, map.sizeX, map.sizeY)
        if closestDistance - closestNode.weight > distance - mapNode.weight:
            closestNode = mapNode
            closestDistance = distance
            continue

    return closestNode

# CONTROLS MUNCHER
target: MapNode = MapNode(-1, -1)
def muncherBrain(muncher: Muncher) -> None:
    global target
    calculateFoodDensityWeightsAdvance(muncher.map)
    foodList = getAllFood(muncher.map)
    if target.x == -1 or target == muncher.mapNode:
        target = findClosestNode(foodList, muncher.mapNode, muncher.map)
    if muncher.y != target.y:
        yDist: int = abs(muncher.y - target.y)
        if (muncher.y < target.y) != (yDist > (muncher.map.sizeY-1) - yDist):
            muncher.direction = Directions.UP
        elif yDist == muncher.map.sizeY - yDist:
            muncher.direction = Directions.DOWN
        else:
            muncher.direction = Directions.DOWN
    else:
        xDist: int = abs(muncher.x - target.x)
        if (muncher.x < target.x) != (xDist > (muncher.map.sizeX-1) - xDist):
            muncher.direction = Directions.RIGHT
        elif xDist == muncher.map.sizeX - xDist:
            muncher.direction = Directions.LEFT
        else:
            muncher.direction = Directions.LEFT