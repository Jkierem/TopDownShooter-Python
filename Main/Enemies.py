from Entity import Entity

class Enemy(Entity):
    def __init__(self,pos):
        Entity.__init__(self)
        self.pos = pos
        self.hp = 1
#end class Enemy

class BasicEnemy(Enemy):
    def __init__(self,pos):
        Enemy.__init__(self,pos)
    
    def update(self,t,physics,player):
        if player is None :
            self.stop()
        else:
            self.vel = PVector.sub( player.pos , self.pos )
            self.vel.normalize()
            self.vel.mult(self.maxVel)
            Entity.update(self,t,physics)
        #end if
    #end def
#end class Basic

class EnemySin(Enemy):
    def __init__(self, pos):
        Enemy.__init__(self,pos)
        self.rot = 45
        self.up = False
        self.maxVel = 1.8
        self.amp = 45
        self.frec = 2
    
    def update(self,t,physics,player):
        if self.rot > self.amp or self.rot < (self.amp * -1):
            self.up = not self.up
        if player is not None:
            aux = PVector.sub( player.pos , self.pos )
            aux.normalize()
            aux.rotate(radians(self.rot))
            self.vel = aux
        else:
            self.stop()
        if self.up:
            self.rot = self.rot + self.frec
        else:
            self.rot = self.rot - self.frec
        Enemy.update(self,t,physics)
#end class EnemySin