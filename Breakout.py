import pygame
import random
pygame.init()
class Color:
    black=(0,0,0)
    white=(255,255,255)
    red=(255,0,0)
    blue=(50,0,200)
    green=(124,252,0)
    crimson=(220,20,60)
    pink=(255,105,180)
    yellow=(255,215,0)
    teal=(0,128,128)

class Block:
    def __init__(self,x,y):
        self.w=40
        self.h=10
        self.x=x
        self.y=y
        colorand=random.choice(['blue','red','pink','green','yellow'])
        if colorand=='blue':
            self.color=Color.blue
        elif colorand=='red':
            self.color=Color.red
        elif colorand=='pink':
            self.color=Color.pink
        elif colorand=='green':
            self.color=Color.green
        elif colorand=='yellow':
            self.color=Color.yellow
        self.area=pygame.draw.rect(pygame.display.set_mode((800,400)),self.color,[self.x,self.y,self.w,self.h])
    def show(self):
        self.area=pygame.draw.rect(Game.screen,self.color,[self.x,self.y,self.w,self.h])
    def hunt(self):
        if pygame.Rect.colliderect(ball.area,self.area):
            Rocket.score+=1
            if ball.x>=self.x+self.w and ball.y>=self.y and ball.y<=self.y+self.h:
                ball.x+=10
                ball.y_dir *= -1
                if ball.x+10>Game.width :
                    ball.x-=10
                    ball.x_dir*=-1
            elif ball.x>=self.x and ball.y>=self.y and ball.y<=self.y+self.h:
                ball.x-=11
                ball.y_dir *= -1
                if ball.x-10<0 :
                    ball.x+=11
                    ball.x_dir*=-1
            elif ball.y>=self.y+self.h and ball.x>=self.x and ball.x<=self.x+self.w:
                ball.y_dir *= -1
            elif ball.y<=self.y+self.h and ball.x>=self.x and ball.x<=self.x+self.w:
                ball.y_dir *= -1
            return True

class Game:
    global f,blocks_b
    f=0
    width=800
    height=400
    screen=pygame.display.set_mode((width,height))
    pygame.display.set_caption('Breakout')
    clock=pygame.time.Clock()
    fps=30
    blocks_b=[]
    for j in range(0,120,20):
        for i in range(0,width,50):
            blocks_b.append(Block(i+5,j+5))
            
    @staticmethod
    def play():
        global f,i,blocks_b
        while True:
            Ball.speed+=0.005
            for event in pygame.event.get():
                if event.type==pygame.MOUSEMOTION:
                    Rocket.move()
            Game.screen.fill(Color.black)
            Rocket.show()
            ball.show()
            ball.move()
            if ball.y>Game.height:
                Rocket.new()
                ball.new()   
                ball.count-=1
            if pygame.Rect(ball.x,ball.y,50,10).colliderect(pygame.Rect(Rocket.x,Rocket.y,50,10)):
                f+=1
                if f==1:
                    ball.y_dir*=-1 
            else:
                f=0
            for x in blocks_b:
                x.show()
            
            pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
            font=pygame.font.SysFont('comicsansms',22)
            m_score=font.render('score:'+str(Rocket.score),True,(255,215,0))
            Game.screen.blit(m_score,(30,360))

            m_ball=font.render('ball:'+str(ball.count),True,(255,215,0))
            Game.screen.blit(m_ball,(720,360))
            if Rocket.lose()==True:
                exit()
            for x in blocks_b:
                if x.hunt()==True:
                    blocks_b.remove(x)
            pygame.display.update()
            Game.clock.tick(Game.fps)

class Rocket:
    w=50
    h=10
    x=Game.width/2-w
    y=Game.height-20
    score=0
    color=Color.teal
    area=pygame.draw.rect(Game.screen,color,[x,y,w,h])
    def show():
        area=pygame.draw.rect(Game.screen,Rocket.color,[Rocket.x,Rocket.y,Rocket.w,Rocket.h])
    @staticmethod
    def move():
        Rocket.x=pygame.mouse.get_pos()[0]
        if Rocket.x>Game.width-Rocket.w:
            Rocket.x=Game.width-Rocket.w
    @staticmethod
    def new():
        Rocket.x=Game.width/2-Rocket.w
        Rocket.y=Game.height-20
    @staticmethod
    def lose():
        if ball.count<1:
            return True


        
class Ball:
    speed=3
    x=Game.width/2
    y=Rocket.y-Rocket.h
    def __init__(self):
        self.x=Game.width/2
        self.y=Rocket.y-Rocket.h
        self.count=3
        self.dir=random.choice(['ru','lu','uu'])
        self.r=10
        self.color=Color.white
        self.x_dir=1
        self.y_dir=-1
        if self.dir=='ru':
            self.x_dir=1
            self.y_dir=-1
        elif self.dir=='lu':
            self.x_dir=-1
            self.y_dir=-1
        self.area=pygame.draw.circle(Game.screen,self.color,(self.x,self.y),self.r)
    def show(self):
        self.area=pygame.draw.circle(Game.screen,self.color,(self.x,self.y),self.r)
    def move(self):
        self.x+=Ball.speed*self.x_dir
        self.y+=Ball.speed*self.y_dir
        if self.x+10>Game.width or self.x-10<0:
            self.x_dir*=-1
        if self.y-10<0:
            self.y_dir=1

    @staticmethod
    def new():
        ball.x=Game.width/2
        ball.y=Rocket.y-Rocket.h
        ball.dir=random.choice(['ru','lu'])
        if ball.dir=='ru':
            ball.x_dir=1
            ball.y_dir=-1
        elif ball.dir=='lu':
            ball.x_dir=-1
            ball.y_dir=-1
        

if __name__=='__main__':
    ball=Ball()
    Game.play()
