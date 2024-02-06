from enum import IntEnum
import random as rand
from tracemalloc import start

# dont worry about the "self" variable :)

class MapNodeState(IntEnum):
    EMPTY = 0
    MUNCHER = 1
    FOOD = 2

class MapNode:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y
        self.state: MapNodeState = MapNodeState.EMPTY
        self.weight: float = 0

class Map:
    def __init__(self, sizeX: int, sizeY: int) -> None:
        self.sizeX: int = sizeX
        self.sizeY: int = sizeY
        self.mapNodes: list = [MapNode]*sizeX*sizeY
        for i in range(0, sizeX*sizeY):
            self.mapNodes[i] = MapNode(int(i % sizeX), int(i / sizeX))

    def getNode(self, x: int, y: int) -> MapNode:
        return self.mapNodes[(x % self.sizeX) + (y % self.sizeY)*self.sizeX]

    def makeNodeEmpty(self, x: int, y: int) -> None:
        self.getNode(x, y).state = MapNodeState.EMPTY

    def makeNodeMuncher(self, x: int, y: int) -> None:
        self.getNode(x, y).state = MapNodeState.MUNCHER

    def makeNodeFood(self, x: int, y: int) -> None:
        self.getNode(x, y).state = MapNodeState.FOOD

    def addFoodRand(self) -> None:
        randomVal: int = int(rand.randrange(0, self.sizeX*self.sizeY))
        if self.mapNodes[randomVal].state == MapNodeState.EMPTY:
            self.mapNodes[randomVal].state = MapNodeState.FOOD

    def getMapAsString(self) -> str:
        output: str = ""
        priorY: int = 0
        for mapNode in self.mapNodes:
            if priorY != mapNode.y:
                output += "\n"
                priorY = mapNode.y
            if mapNode.state == MapNodeState.EMPTY:
                output += "-"
            elif mapNode.state == MapNodeState.FOOD:
                output += "#"
            else:
                output += "@"
            output += " "
        return output

class Directions(IntEnum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Muncher:
    def __init__(self, startX, startY, map: Map) -> None:
        self.x: int = startX
        self.y: int = startY
        self.mapNode: MapNode = map.getNode(startX, startY)
        self.map: Map = map
        self.direction: Directions = Directions.UP
        self.score: int = 0
        self.map.makeNodeMuncher(startX, startY)

    def update(self) -> None:
        from muncherBrain import muncherBrain
        muncherBrain(self)
        self.map.makeNodeEmpty(self.x, self.y)
        self.__move()
        self.__eat()
        self.map.makeNodeMuncher(self.x, self.y)
        self.map.addFoodRand()

    def __eat(self) -> None:
        if self.map.getNode(self.x, self.y).state == MapNodeState.FOOD:
            self.score += 1

    def __move(self) -> None:
        if self.direction == Directions.UP:
            self.y = (self.y + 1) % self.map.sizeY
        elif self.direction == Directions.DOWN:
            self.y = (self.y - 1) % self.map.sizeY
        elif self.direction == Directions.RIGHT:
            self.x = (self.x + 1) % self.map.sizeX
        else:
            self.x = (self.x - 1) % self.map.sizeX

        self.mapNode = self.map.getNode(self.x, self.y)