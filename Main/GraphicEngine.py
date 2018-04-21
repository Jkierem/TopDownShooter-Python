class GraphicEngine:
    def __init__(self):
        self.someValue = 0
    
    def drawSin(self,enemy):
        fill(255,0,0)
        stroke(0,0,0)
        self.drawRegularPolygon( enemy.pos , 10 , 5 )
    
    def drawRegularPolygon(self,pos,radius,vertices,rotation=0):
        ratio = TWO_PI / vertices
        pushMatrix()
        translate(pos.x,pos.y)
        rotate(radians(rotation))
        beginShape()
        count = 0
        currentPos = PVector(radius,0)
        while( count != vertices ):
            count = count + 1
            vertex( currentPos.x , currentPos.y )
            currentPos.rotate(ratio)
        endShape(CLOSE)
        popMatrix()
#end class GraphicEngine