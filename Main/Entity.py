from PhysicsEngine import Collider, PhysicsEngine
# Clase base Entity. NO DEBE SER INSTANCIADA
class Entity:
    def __init__(self):
        self.pos = PVector(0,0)
        self.vel = PVector(0,0)
        self.acc = PVector(0,0)
        self.maxVel = 1
        self.alive = True
        self.collider = Collider(self.hit)
    
    def stop(self):
        self.acc = PVector(0,0)
        self.vel = PVector(0,0)
    
    def update(self,t,physics):
        self.updateVelocity(t,physics)
        self.updatePosition(t,physics)
    
    def updateVelocity(self,t,p):
        self.vel.add( PVector.mult(self.acc , t) )
        if self.vel.mag() > self.maxVel :
            self.vel.normalize()
            self.vel.mult(self.maxVel)
    
    def updatePosition(self,t,p):
        # Vector auxiliar para evitar movimiento ilicito
        aux = PVector( self.pos.x , self.pos.y )
        aux.add( PVector.mult(self.vel , t) )
        if( p.isOutOfBounds(aux) ):
            self.boundControl()
        else:
            self.pos = aux
            
    def die( self ):
        self.alive = False
    
    # Funciones abstractas
    def hit( self , who ):
        pass
    def boundControl(self):
        pass
#end def