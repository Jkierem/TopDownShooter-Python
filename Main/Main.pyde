from GraphicEngine import GraphicEngine as Graphics
from GameEngine import GameEngine as Game
from PhysicsEngine import PhysicsEngine as Physics
from Entity import Entity
import Enemies 

screenWidth = 400
screenHeight = 400
rotation = 0
game = Game()
graph = Graphics()
physics = Physics(screenWidth,screenHeight)

bg = [255,255,255]

def setup():
    background( bg[0], bg[1], bg[2] )
    size( screenWidth , screenHeight )

def draw():
    global rotation
    clear()
    background( bg[0], bg[1], bg[2] )
    fill(255,0,0)
    stroke(0,0,0)
    graph.drawRegularPolygon(PVector(200,200),20,6,rotation)
    rotation += 1