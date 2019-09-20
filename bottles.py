import time
import json
import pygame
from pygame.locals import *
import urllib.request
from pygame.color import THECOLORS
pygame.init()
state='close'
state_a=['close','close','close','close','close']
state_b=['close','close','close','close']
line_a0=['192.168.10.200:5000/feeder/0/0','192.168.10.200:5000/feeder/1/0','192.168.10.200:5000/feeder/2/0','192.168.10.200:5000/feeder/3/0','192.168.10.200:5000/feeder/4/0']
line_a1=['192.168.10.200:5000/feeder/0/1','192.168.10.200:5000/feeder/1/1','192.168.10.200:5000/feeder/2/1','192.168.10.200:5000/feeder/3/1','192.168.10.200:5000/feeder/4/1']
line_b0=['192.168.10.201:5000/feeder/0/0','192.168.10.201:5000/feeder/1/0','192.168.10.201:5000/feeder/2/0','192.168.10.201:5000/feeder/3/0']
line_b1=['192.168.10.201:5000/feeder/0/1','192.168.10.201:5000/feeder/1/1','192.168.10.201:5000/feeder/2/1','192.168.10.201:5000/feeder/3/1']
Brack=[0,0,0]
White=[255,255,255]
number_a=["A0","A1","A2","A3","A4"]
number_b=["B0","B1","B2","B3"]
icon={'00':'img/kz.jpg','10':'img/bz.jpg','11':'img/mz.jpg','01':'img/gz.jpg'}
screen = pygame.display.set_mode((1240,768),FULLSCREEN,32)
screen.fill(Brack)
class Bottles(object):
    def Icon_a(num,x,y,a):
        img=pygame.image.load(icon[a])
        img=pygame.transform.smoothscale(img,(100,100))
        screen.blit(img,(x,y))
        text=pygame.font.Font("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",36)
        text_fmt0=text.render(number_a[num],3,White)
        screen.blit(text_fmt0,(x-70,y+20))
        pygame.display.update()
    def Icon_b(num,x,y,a):
        img=pygame.image.load(icon[a])
        img=pygame.transform.smoothscale(img,(100,100))
        screen.blit(img,(x,y))
        text=pygame.font.Font("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",36)
        text_fmt0=text.render(number_b[num],3,White)
        screen.blit(text_fmt0,(x-70,y+20))
        pygame.display.update()
    def WeightIcon(x,y,a):
        img=pygame.image.load('img/cz.jpg')
        img=pygame.transform.smoothscale(img,(100,100))
        screen.blit(img,(x,y))
        pygame.draw.rect(screen,Brack,[x+130,y,150,100],0)
        text=pygame.font.Font("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",26)
        text_fmt0=text.render(a,3,White)
        screen.blit(text_fmt0,(x+130,y+30))
        pygame.display.update()
    def VibratoryFeeder(x,y):
        img=pygame.image.load('img/zd.jpg')
        img=pygame.transform.smoothscale(img,(100,100))
        screen.blit(img,(x,y))
        pygame.display.update()
if __name__ == '__main__':
    while True:
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
                        for i in B0:
                            if i[1]<=pos[0]<=i[1]+100 and i[2]<=pos[1]<=i[2]+100:
                                if state_a==['close','close','close','close','close']:
                                    if index ==0:
                                        state_a[i[0]]='open'
                                        #response0=urllib.request.urlopen(line_a1[i[0]])
                                        #html0=response0.read()
                                        #text0=json.loads(html0)
                                        print(line_a1[i[0]])
                                elif state_a[i[0]]=='open':
                                    if index ==2:
                                        state_a[i[0]]='close'
                                        #response1=urllib.request.urlopen(line_a0[i[0]])
                                        #html1=response1.read()
                                        #text1=json.loads(html1)
                                        print(line_a0[i[0]])
                        for v in B1:
                            if v[1]<=pos[0]<=v[1]+100 and v[2]<=pos[1]<=v[2]+100:
                                if state_b==['close','close','close','close']:
                                    if index ==0:
                                        state_b[v[0]]='open'
                                        #response2=urllib.request.urlopen(line_b1[v[0]])
                                        #html2=response2.read()
                                        #text2=json.loads(html2)
                                        print(line_b1[v[0]])
                                elif state_b[v[0]]=='open':
                                    if index ==2:
                                        state_b[v[0]]='close'
                                        #response3=urllib.request.urlopen(line_b0[v[0]])
                                        #html3=response3.read()
                                        #text3=json.loads(html3)
                                        print(line_b0[v[0]])
                        if 70<=pos[0]<=170 and 600<=pos[1]<=700:
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
                        elif 790<=pos[0]<=890 and 600<=pos[1]<=700:
                            if index == 0:
                                response6=urllib.request.urlopen("http://localhost:5000/feederon/b")
                                html6=response6.read()
                                text6=json.loads(html6)
                                print(text6['status'])
                            elif index==2:
                                response7=urllib.request.urlopen("http://localhost:5000/feederoff/b")
                                html7=response3.read()
                                text7=json.loads(html7)
                                print(text7['status'])
        response8=urllib.request.urlopen("http://localhost:5000/bucketgroup/a")
        html8=response8.read().decode()
        response9=urllib.request.urlopen("http://localhost:5000/bucketgroup/b")
        html9=response9.read().decode()
        response10=urllib.request.urlopen("http://localhost:5000/scale/a")
        html10=response10.read()
        response11=urllib.request.urlopen("http://localhost:5000/scale/b")
        html11=response11.read()
        text8=json.loads(html8)
        text9=json.loads(html9)
        text10=json.loads(html10)
        text11=json.loads(html11)
        B0=[[0,70,250,text8['0']],[1,70,45,text8['1']],[2,340,300,text8['2']],[3,340,150,text8['3']],[4,340,0,text8['4']]]
        B1=[[0,790,250,text9['0']],[1,790,45,text9['1']],[2,1050,250,text9['2']],[3,1050,45,text9['3']]]
        for i in B0:
            Bottles.Icon_a(i[0],i[1],i[2],i[3])
        for v in B1:
            Bottles.Icon_b(v[0],v[1],v[2],v[3])
        Bottles.VibratoryFeeder(190,450)
        Bottles. WeightIcon(190,620,b'%0.2f' % text10['reading'])
        Bottles.VibratoryFeeder(930,450)
        Bottles. WeightIcon(930,620,b'%0.2f' % text11['reading'])
        time.sleep(1/3)
