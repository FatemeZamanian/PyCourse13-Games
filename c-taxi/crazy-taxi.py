import pygame
import random
pygame.init()
class Game:
    width=220
    height=500
    screen=pygame.display.set_mode((width,height))
    pygame.display.set_caption('CrazyTaxi')
    clock=pygame.time.Clock()
    fps=30
    @staticmethod
    def play():
        global c
        c=0
        obj_car=BlueCar()
        while True:
            if Taxi.accident(obj_car)==False:
                c+=1
                Car.speed+=0.005
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        exit()
                    if event.type==pygame.MOUSEMOTION:
                        Taxi.move()
                Taxi.rect.update(Taxi.x,Taxi.y,60,120)
                if c%100==0:
                    txi=random.choice(['red','blue','black'])
                    if txi=='red':
                        obj_car=RedCar()
                    elif txi=='blue':
                        obj_car=BlueCar()
                    elif txi=='black':
                        obj_car=BlackCar()
                obj_car.move()
                Game.screen.fill((143,188,143))
                pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
                obj_car.show()
                Taxi.show()
            if Taxi.accident(obj_car)==True:
                Game.screen.fill((0,0,0))
                font=pygame.font.SysFont('comicsansms',35)
                txt_lose=font.render('Game Over',True,(255,0,0))
                Game.screen.blit(txt_lose,(10,Game.height/2))
                
            pygame.display.update()
            Game.clock.tick(Game.fps)

class Car:
    speed=5
    def __init__(self):
        self.y=0
        self.line=random.choice(['1','2','3'])
        if self.line=='1':
            self.x=20
        elif self.line=='2':
            self.x=80
        elif self.line=='3':
            self.x=140

    def show(self):
        Game.screen.blit(self.img,(self.x,self.y))
    
    def move(self):
        self.y+=Car.speed

class BlueCar(Car):
    def __init__(self):
        super().__init__()
        self.img='c-taxi/images/blue.png'
        self.img=pygame.image.load(self.img)
        self.rect=self.img.get_rect()
        
class RedCar(Car):
    def __init__(self):
        super().__init__()
        self.img='c-taxi/images/red.png'
        self.img=pygame.image.load(self.img)
        self.rect=self.img.get_rect()

class BlackCar(Car):
    def __init__(self):
        super().__init__()
        self.img='c-taxi/images/black.png'
        self.img=pygame.image.load(self.img)
        self.rect=self.img.get_rect()
class Taxi:
    x=Game.width/2
    y=Game.height-120
    w=60
    image=pygame.image.load('c-taxi/images/tx.png')
    rect=image.get_rect()
    @staticmethod
    def show():
        Game.screen.blit(Taxi.image,(Taxi.x,Taxi.y))
    @staticmethod
    def move():
        Taxi.x=pygame.mouse.get_pos()[0]
        if Taxi.x>Game.width-60:
            Taxi.x=Game.width-60
    
    def accident(car):
        if pygame.Rect(car.x,car.y,60,110).colliderect(pygame.Rect(Taxi.x,Taxi.y,60,110)):
            return True
        else:
            return False
        


if __name__=='__main__':
    Game.play()