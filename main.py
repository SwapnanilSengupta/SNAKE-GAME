import pygame
import random
import math
from pygame import mixer
pygame.init() # black screen creation
icon=pygame.image.load("dice.png") # game icon image
pygame.display.set_icon(icon)
font=pygame.font.Font("freesansbold.ttf",32) #font type
button=pygame.image.load("record.png")
playery=1
player1score=0
player2score=0
winnerx=100
winnery=100
buttonx=30
buttony=100
buttonx1=15
buttony1=170
screen=pygame.display.set_mode((800,600)) #screen width and hieght

def show_winner(x,y): # func for show winner
 playerx = font.render("PLAYER1:  " + str(player1score)+"  STEPS", True, (0,0, 0))
 playery = font.render("PLAYER2:  " + str(player2score)+"  STEPS", True, (0, 0, 0))
 screen.blit(playerx, (x, y))
 screen.blit(playery, (x, y+100))
 if(player1score>player2score):
  winner1=font.render("WINNER IS PLAYER 2", True, (0, 0, 0))
  screen.blit(winner1,(x, y+300))
 else:
  winner2 = font.render("WINNER IS PLAYER 1", True, (0, 0, 0))
  screen.blit(winner2, (x, y + 300))

running1=True

for i in range (2): # loop for two player

 mixer.music.load("roll.wav") #music load

 def butt(x,y):
  screen.blit(button,(x,y))
  scorex=font.render("PRESS",True,(0, 0, 0))
  screen.blit(scorex,(buttonx1,buttony1))

 def musicplay(): # func for playing music
  mixer.music.play()

 x=random.randint(1,6)
 scorey=1
 count=0
 posx=30
 posy=30
 flyx=300
 flyy=300
 textx=520
 texty=0
 playerxc=200
 playeryc=0

 def player(x,y): #func to show player count
  playerx = font.render("PLAYER:  "+str(playery), True, (0, 0, 0))
  screen.blit(playerx,(x, y))


 def score(x,y): # func to show times dice rolled
  scorex=font.render("DICE ROLLED: "+str(scorey),True,(0, 0, 0))
  screen.blit(scorex,(x,y))

 background=pygame.image.load("background.png") #background image

 pygame.display.set_caption("DICE GAME") #game name

 fly=pygame.image.load("fly.png")#fly image

 snake=pygame.image.load("snake.png") # snake image


 snakex=0
 snakey=536
 snakexchange=20
 snakexchangereplica=20
 snakeychange=64
 snakexchangeminus=-20
 pygame.display.set_icon(icon)
 d1=pygame.image.load("1.png") # dice 1 image load
 d2=pygame.image.load("2.png")
 d3=pygame.image.load("3.png")
 d4=pygame.image.load("4.png")
 d5=pygame.image.load("5.png")
 d6=pygame.image.load("6.png")

 def flypos(flyx,flyy):
  screen.blit(fly,(flyx,flyy))

 def d1x(posx,posy):
  screen.blit(d1,(posx,posy))

 def d2x(posx, posy):
  screen.blit(d2, (posx, posy))

 def d3x(posx, posy):
  screen.blit(d3, (posx, posy))

 def d4x(posx,posy):
  screen.blit(d4,(posx,posy))

 def d5x(posx, posy):
  screen.blit(d5, (posx, posy))

 def d6x(posx, posy):
  screen.blit(d6, (posx, posy))

 def snakemovement(snakex,snakey):
  screen.blit(snake,(snakex,snakey))

 def check(x,y,x1,y1):
  d=math.sqrt((math.pow(x-x1,2))+(math.pow(y-y1,2)))
  return d

 running = True
 while running:
  screen.fill((255,255,255))
  screen.blit(background,(-200,-100))
  butt(buttonx,buttony)
  player(playerxc,playeryc)
  for event in pygame.event.get():
   if event.type==pygame.QUIT:
    running=False
   if event.type==pygame.MOUSEBUTTONDOWN: # mouse sensation
    mx,my=pygame.mouse.get_pos()
    if(mx>0)and(mx<200) and (my>0)and(my<200):
     posx+=0
     posy+=0
     musicplay()
   if event.type==pygame.MOUSEBUTTONUP:
    posx+= 0
    posy+= 0
    count=0
    x=random.randint(1,6)
    scorey+=1

  if x==1:
   d1x(posx,posy)
  if (x == 2):
   d2x(posx,posy)
  if (x == 3):
   d3x(posx, posy)
  if (x == 4):
   d4x(posx, posy)
  if (x == 5):
   d5x(posx, posy)
  if (x == 6):
   d6x(posx, posy)

  if(count==0):
   snakex+=snakexchange*x
   count+=1

  if(snakex>730):
   snakex=730
   snakexchange=snakexchangeminus
   snakey-=snakeychange

  if(snakex<0)and(snakey<536):
   snakex=0
   snakexchange=snakexchangereplica
   snakey-=snakeychange

  snakemovement(snakex,snakey)
  t=check(snakex,snakey,flyx,flyy)
  score(textx,texty)
  if(snakex<64)and(snakey<64):
   running=False
  if(t>50):
   flypos(flyx,flyy)
  else:
   playery+=1
   running=False
   if i==0:
    player1score=scorey
   else:
    player2score=scorey

  pygame.display.update()
 pygame.time.wait(2000) # time pause 2000 msec
while running1: # another loop for showing winner at last
 screen.fill((255, 255, 255))
 for event in pygame.event.get():
   if event.type == pygame.QUIT:
    running1 = False
 show_winner(winnerx,winnery)
 pygame.display.update()
