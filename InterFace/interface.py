import time
import json
import pygame
from pygame.locals import *
import urllib.request
from pygame.color import THECOLORS
pygame.init()
Brack=[0,0,0]
White=[255,255,255]
Green=[0,255,0]
Red=[255,0,0]
Gray=[169,169,169]
button_text=["开 始","开 始","开 始","开 始","开 始"]
line=['http://localhost:5050/mixer/000','http://localhost:5050/mixer/100','http://localhost:5050/mixer/200','http://localhost:5050/mixer/300','http://localhost:5050/mixer/400']
color=[Green,Green,Green,Green,Green]
button_text0="手动状态:"
screen = pygame.display.set_mode((1240,768),FULLSCREEN,32)
screen.fill(Brack)
pygame.draw.rect(screen,White,[470,184,300,400],0)
text=["工  序  甲:","工  序  乙:","工  序  丙:","工  序  丁:","工  序  戊:"]
text_0=pygame.font.Font("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",22)
text_1=pygame.font.Font("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",18)
text_2=pygame.font.Font("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",15)
text_fmt0=text_0.render("操   作   界   面",2,Brack)
screen.blit(text_fmt0,(545,200))
pygame.display.update()
def Process(num,x,y,button_text,color):
    text_fmt1=text_1.render(text[num],1,Brack)
    screen.blit(text_fmt1,(x-127,y))
    pygame.display.update()
    pygame.draw.rect(screen,Brack,[x,y,60,25],2)
    pygame.draw.rect(screen,color,[x+2,y+2,57,22],0)
    button=text_2.render(button_text,1,Brack)
    screen.blit(button,(x+13,y+3))
    pygame.display.update()
if __name__ == '__main__':
    while True:
        time.sleep(1)
        pygame.draw.rect(screen,White,[506,520,85,28],0)
        pygame.draw.rect(screen,Brack,[597,520,65,28],2)
        pygame.draw.rect(screen,Green,[599,522,62,25],0)
        button=text_1.render(button_text0,1,Brack)
        screen.blit(button,(506,524))
        B=[[0,647,260,button_text[0],color[0]],[1,647,310,button_text[1],color[1]],[2,647,360,button_text[2],color[2]],[3,647,410,button_text[3],color[3]],[4,647,460,button_text[4],color[4]]]
        if button_text0=="手动状态:":
            for t in range(5):
                if button_text[t]=="结 束":
                    button_text[t]="开 始"
                    color[t]=Green
        elif button_text0=="自动状态:":
            if button_text[0]=="结 束":
                response0=urllib.request.urlopen(line[0])
                html0=response0.read()
                text0=json.loads(html0)
                print(text0)
                button_text[0]="开 始"
                button_text[1]="结 束"
            elif button_text[1]=="结 束":
                response0=urllib.request.urlopen(line[1])
                html0=response0.read()
                text0=json.loads(html0)
                print(text0)
                button_text[1]="开 始"
                button_text[2]="结 束"
            elif button_text[2]=="结 束":
                response0=urllib.request.urlopen(line[2])
                html0=response0.read()
                text0=json.loads(html0)
                print(text0)
                button_text[2]="开 始"
                button_text[3]="结 束"
            elif button_text[3]=="结 束":
                response0=urllib.request.urlopen(line[3])
                html0=response0.read()
                text0=json.loads(html0)
                print(text0)
                button_text[3]="开 始"
                button_text[4]="结 束"
            elif button_text[4]=="结 束":
                response0=urllib.request.urlopen(line[4])
                html0=response0.read()
                text0=json.loads(html0)
                print(text0)
                button_text[4]="开 始"
        for i in B:
            Process(i[0],i[1],i[2],i[3],i[4])
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
                        if index==0:
                            if 597<=pos[0]<=662 and 520<=pos[1]<=548:
                                if button_text0=="自动状态:" and button_text==["开 始","开 始","开 始","开 始","开 始"]:
                                    button_text0="手动状态:"
                                    color=[Green,Green,Green,Green,Green]
                                elif button_text0=="手动状态:" and button_text==["开 始","开 始","开 始","开 始","开 始"]:
                                    button_text0="自动状态:"
                                    button_text[0]="结 束"
                                    color=[Gray,Gray,Gray,Gray,Gray]
                            for i in B:
                                if i[1]<=pos[0]<=i[1]+60 and i[2]<=pos[1]<=i[2]+25:
                                    if button_text==["开 始","开 始","开 始","开 始","开 始"] and button_text0=="手动状态:":
                                        color[i[0]]=Red
                                        button_text[i[0]]="结 束"
                                        response1=urllib.request.urlopen(line[i[0]])
                                        html1=response1.read()
                                        text1=json.loads(html1)
                                        print(text1)
