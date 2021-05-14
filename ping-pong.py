import pygame
import random
pygame.init()
class Color:
    black=(0,0,0)
    white=(255,255,255)
    red=(255,0,0)
    blue=(50,0,200)

class Rocket:
    def __init__(self,x,y,color):
        self.w=10
        self.h=50
        self.x=x
        self.y=y
        self.speed=5.5
        self.score=0
        self.color=color
        self.area=pygame.draw.rect(Game.screen,self.color,[self.x,self.y,self.w,self.h])
    def show(self):
        self.area=pygame.draw.rect(Game.screen,self.color,[self.x,self.y,self.w,self.h])
    def move(self,ball=None):
        if ball==None:
            self.y=pygame.mouse.get_pos()[1]
            if self.y>Game.height-self.h:
                self.y=Game.height-self.h
        else:
            if self.y<ball.y:
                self.y+=self.speed
            elif self.y>ball.y:
                self.y-=self.speed
            if self.y<0:
                self.y=0
            elif self.y>Game.height-self.h:
                self.y=Game.height-self.h
        
class Ball:
    def __init__(self):
        self.dir=random.choice(['ru','rd','lu','ld'])
        self.r=10
        self.x=Game.width/2
        self.y= Game.height/2
        self.speed=6
        self.color=Color.blue
        if self.dir=='ru':
            self.x_dir=1
            self.y_dir=-1
        elif self.dir=='rd':
            self.x_dir=1
            self.y_dir=1
        elif self.dir=='lu':
            self.x_dir=-1
            self.y_dir=-1
        elif self.dir=='ld':
            self.x_dir=-1
            self.y_dir=1
        self.area=pygame.draw.circle(Game.screen,Color.white,(self.x,self.y),self.r)
    def show(self):
        self.area=pygame.draw.circle(Game.screen,Color.white,(self.x,self.y),self.r)
    def move(self):
        self.x+=self.speed*self.x_dir
        self.y+=self.speed*self.y_dir
        if self.y+10>Game.height or self.y-10<0:
            self.y_dir*=-1
    

    def new(self):
        self.x=Game.width/2
        self.y= Game.height/2

class Game:
    global f
    f=0
    width=700
    height=400
    screen=pygame.display.set_mode((width,height))
    pygame.display.set_caption('Ping-Pong')
    clock=pygame.time.Clock()
    fps=30
    @staticmethod
    def play():
        me=Rocket(10,Game.height/2,Color.red)
        cmptr=Rocket(Game.width-20,Game.height/2,Color.blue)
        ball=Ball()
        while True:
            for event in pygame.event.get():
                if event.type==pygame.MOUSEMOTION:
                    me.move()
            Game.screen.fill(Color.black)
            me.show()
            cmptr.show()
            ball.show()
            ball.move()
            cmptr.move(ball)
            if ball.x<0:
                cmptr.score+=1
                ball.new()
            if ball.x>Game.width:
                me.score+=1
                ball.new()
            if pygame.Rect.colliderect(ball.area,me.area) or pygame.Rect.colliderect(ball.area,cmptr.area):
                f+=1
                if f==1:
                    ball.x_dir*=-1 
            else:
                f=0
            pygame.draw.rect(Game.screen,Color.white,[0,0,Game.width,Game.height],10)
            pygame.draw.aaline(Game.screen,Color.white,(Game.width/2,0),(Game.width/2,Game.height))
            pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
            font=pygame.font.SysFont('comicsansms',35)
            me_score=font.render(str(me.score),True,(255,215,0))
            Game.screen.blit(me_score,(300,50))
            cmptr_score=font.render(str(cmptr.score),True,(255,215,0))
            Game.screen.blit(cmptr_score,(400,50))
            pygame.display.update()
            Game.clock.tick(Game.fps)



if __name__=='__main__':
    Game.play()