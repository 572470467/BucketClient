import time
import json
import pygame
from pygame.locals import *
import urllib.request
from pygame.color import THECOLORS
pygame.init()
Brack=[0,0,0]
White=[255,255,255]
number_a=["A0","A1","A2","A3","A4"]
number_b=["B0","B1","B2","B3"]
icon={'00':'img/kz.jpg','10':'img/bz.jpg','11':'img/mz.jpg','01':'img/gz.jpg'}
screen = pygame.display.set_mode((1240,768),FULLSCREEN,32)
screen.fill(Brack)
class Bottles(object):
    def Icon_a(num,x,y,a):
        img0=pygame.image.load(icon[a])
        screen.blit(img0,(x,y))
        text=pygame.font.Font("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",46)
        text_fmt0=text.render(number_a[num],3,White)
        screen.blit(text_fmt0,(x-70,y+50))
        pygame.display.update()
    def Icon_b(num,x,y,b):
        img0=pygame.image.load(icon[b])
        screen.blit(img0,(x,y))
        text=pygame.font.Font("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",46)
        text_fmt0=text.render(number_b[num],3,White)
        screen.blit(text_fmt0,(x-70,y+50))
        pygame.display.update()
    def WeightIcon(x,y,a):
        img0=pygame.image.load('img/cz.jpg')
        screen.blit(img0,(x,y))
        text=pygame.font.Font("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",16)
        text_fmt0=text.render(a,3,White)
        screen.blit(text_fmt0,(x+90,y+30))
        pygame.display.update()
    def VibratoryFeeder(x,y):
        img0=pygame.image.load('img/zd.jpg')
        screen.blit(img0,(x,y))
        pygame.display.update()
if __name__ == '__main__':
    while True:
        time.sleep(1/3)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
                elif event.type == QUIT:
                    exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                pos = pygame.mouse.get_pos()
                for index in range(len(pressed_array)):
                    if pressed_array[index]:
                        if 70<=pos[0]<=235 and 600<=pos[1]<=765:
                            if index == 0:
                                response4=urllib.request.urlopen("http://localhost:5000/feederon/a")
                                html4=response4.read()
                                text4=json.loads(html4)
                                print(text4['status'])
                            elif index==2:
                                response5=urllib.request.urlopen("http://localhost:5000/feederoff/a")
                                html5=response5.read()
                                text5=json.loads(html5)
                                print(text5['status'])
                        elif 790<=pos[0]<=955 and 600<=pos[1]<=765:
                            if index == 0:
                                response6=urllib.request.urlopen("http://localhost:5000/feederon/b")
                                html6=response6.read()
                                text6=json.loads(html6)
                                print(text6['status'])
                            elif index==2:
                                response7=urllib.request.urlopen("http://localhost:5000/feederoff/b")
                                html7=response7.read()
                                text7=json.loads(html7)
                                print(text7['status'])                       
        response0=urllib.request.urlopen("http://localhost:5000/bucketgroup/a")
        html0=response0.read().decode()
        response1=urllib.request.urlopen("http://localhost:5000/bucketgroup/b")
        html1=response1.read().decode()
        response2=urllib.request.urlopen("http://localhost:5000/scale/a")
        html2=response2.read()
        response3=urllib.request.urlopen("http://localhost:5000/scale/b")
        html3=response3.read()
        text0=json.loads(html0)
        text1=json.loads(html1)
        text2=json.loads(html2)
        text3=json.loads(html3)
        Bottles.Icon_a(1,70,50,text0['1'])
        Bottles.Icon_a(0,70,350,text0['0'])
        Bottles.Icon_a(4,340,0,text0['4'])
        Bottles.Icon_a(3,340,200,text0['3'])
        Bottles.Icon_a(2,340,400,text0['2'])
        Bottles.Icon_b(1,790,50,text1['1'])
        Bottles.Icon_b(3,1050,50,text1['3'])
        Bottles.Icon_b(0,790,350,text1['0'])
        Bottles.Icon_b(2,1050,350,text1['2'])
        Bottles.VibratoryFeeder(70,600)
        Bottles. WeightIcon(340,600,b'%0.2f' % text2['reading'])
        Bottles.VibratoryFeeder(790,600)
        Bottles. WeightIcon(1050,600,b'%0.2f' % text3['reading'])
        
        #pygame.draw.rect(screen,Brack,[0,0,1240,768],0)
