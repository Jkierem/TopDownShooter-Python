class Collider:
    def __init__(self, onCollision):
        self.isColliding = False
        self.onCollision = onCollision
        #Adicionar atributos necesarios

    def collide(self,who):
        self.isColliding = true
        self.onCollision(who)
        self.isColliding = false
    
    def didCollide(self,collider):
        # Agregar logica de colision
        pass
        
#end class Collider

class PhysicsEngine:
    def __init__(self,w,h):
        self.w = w
        self.h = h
    
    #Funcion que engloba la actualizacion de una entidad
    # t: tiempo transcurrido (normalmente 1)
    # e: entidad a actualizar
    def updateEntity(self,t,e):
        if type(e) is Entity:
            e.update(t,self)
    
    def isOutOfBounds(self,vector):
        x = vector.x
        y = vector.y
        if x > self.w or x < 0 :
            return True
        elif y > self.h or y < 0 :
            return True
        return False
    
    def checkCollision(ents):
        if type(ents) is list:
            count = len(ents)
            for i in range(count):
                for j in range(i,count):
                    e1 = ents[i]
                    e2 = ents[j]
                    if( e1.collider.didCollide(e2.collider) ):
                        e1.collide(e2)
                        e2.collide(e1)
                    #end if
                #end for
            #end for
        #end if
    #end def
    
#end class PhysicsEngine



