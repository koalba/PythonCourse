import random
import math

coverage_per_can = 5 # Square Meters
wall = {}

def howManyCans( sqMeters ):
    return math.ceil( sqMeters / coverage_per_can )

def generateRandomWall():
    global wall
    wall['width' ] = random.randint(1, 10)
    wall['height'] = random.randint(1, 10)

generateRandomWall()
print( f'You need {howManyCans( wall["width"] * wall["height"] )} cans of paint for a { wall["width"] } x { wall["height"] } wall' )