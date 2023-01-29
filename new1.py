import pygame
import random
pygame.init()

#designing of display
window=pygame.display.set_mode((800,700))
caption=pygame.display.set_caption("Collect The Flower")
icon=pygame.image.load("icon1.png")
icondisplay=pygame.display.set_icon(icon)
basket=pygame.image.load("wicker-basket.png")
sky=pygame.image.load("sky.png")
sky5=pygame.image.load("sky5.jpg")
basket2=pygame.image.load("wicker-basket2.png")

# flowers images
flower1=pygame.image.load("rose.png")
flower2=pygame.image.load("flower.png")
flower3=pygame.image.load("sunflower.png")

# game sound
# Sound
background=pygame.mixer.Sound("Intro Theme.mp3")
background.play(-1)
# collecting sound
def sound():
    sound1=pygame.mixer.Sound("gamesound.mp3")
    sound1.play()

# lossing sound
def lossSound():
    lossSound=pygame.mixer.Sound("lossingsound.mp3")
    lossSound.play()

# game oversound
def overSound():
    overSound=pygame.mixer.Sound("oversound.mp3")
    overSound.play()
#____________SOUND END______________

#basket axes and change
basketX=360
basketY=600
change=0
extrachange=1.5
var="on"
# basket 2


#func of basket
def moveBasket(x,y):
    window.blit(basket,(x,y))

#flower
flowerX=random.randint(5,650)
flowerY=2
changeFlower=1

# score
score=0
flowerNo=0

# indexs of flower
def rand(flowerNo,x,y):
    flower=[flower1,flower2,flower3]
    window.blit(flower[flowerNo],(x,y))

# chances
miss=3
missfont=pygame.font.Font('freesansbold.ttf',16)

# game over
over=pygame.font.Font('freesansbold.ttf',100)

#function  display the score on the screen
def displayScore(size,x,y,text,score):
    font=pygame.font.Font('freesansbold.ttf', size)
    text=font.render(text+str(score),True,(0,0,0))
    window.blit(text,(x,y))

# +2 or +1 and +3
def n2orn1orn3(size,x,y,text):
    numfont=pygame.font.Font('freesansbold.ttf', size)
    numtext=numfont.render(text,True,(0,0,0))
    window.blit(numtext,(x,y))

# highscore I dentifiyer
f=open("highscore.txt")
highscore=f.read()

# highscore font
def displayhighscore(size,x,y,text,highscore):
    highscorefont=pygame.font.Font("freesansbold.ttf",size)
    highscoretext=highscorefont.render(text+str(highscore),True,(0,0,0))
    window.blit(highscoretext,(x,y))

    # ------------------buttons-------------
# color of button before effects
blue = (0, 160, 255)
green=(0,230,0)
black = (0, 0, 0)#outine color
# after effects
lightblue = (135, 206, 235)
lightgreen=(57,255,7)
# button positions
# play button
xx, yy, xx1, yy1 = 150, 540, 150, 100
X = (xx, yy, xx1, yy1)
Xl = (xx+2, yy+2, xx1, yy1)
X14 = (xx-1, yy-1, xx1+1, yy1+1)
X11 = (xx-2, yy-1, xx1+1, yy1+1)
X13 = (xx+5, yy+1, xx1+7, yy1+5)
X12 = (xx+3, yy+1, xx1+6, yy1+4)
# effect after click
Xl4 = (xx-1, yy-1, xx1+2, yy1+1)
Xl1 = (xx-2, yy-1, xx1+2, yy1+1)
Xl3 = (xx+6, yy+1, xx1+8, yy1+5)
Xl2 = (xx+6, yy+1, xx1+7, yy1+4)
# quit button position
x11,y11,x22,y22=450,540,150,100
Xa=(x11,y11,x22,y22)
X24=(x11-1,y11-1,x22,y22+1)
X21=(x11-2,y11-1,x22+1,y22+1)
X23=(x11+5,y11+1,x22+7,y22+5)
X22=(x11+3,y11+1,x22+6,y22+4)
# after click
Xm4=(x11-1,y11-2,x22+1,y22+2)
Xm1=(x11-2,y11-1,x22+1,y22+2)
Xm3=(x11+6,y11+1,x22+8,y22+5)
Xm2=(x11+6,y11+1,x22+7,y22+4)
# font position
b = (xx+30, yy+25)
bc = (xx+37, yy+26)
d=(x11+30 ,y11+25)
dc=(x11+37 ,y11+26)

size = 40#font size of btton
click=pygame.mouse.get_pressed()


mp=pygame.mouse.get_pos()

def button(window, color, X, size, string, textColor, blitPosition,a=0):
    pygame.draw.ellipse(window, color, X,width=a)
    font = pygame.font.SysFont("times", size, 0,1)
    text = font.render(string, 1, textColor)
    window.blit(text, blitPosition)
def Xseries(X,X11,X12,X13,X14,blue,black,b,p="Play"):
    button(window, blue, X, size, p, black, b)
    button(window, blue, X11, size, p, black, b,11)
    button(window, blue, X12, size, p, black, b,14)
    button(window, black, X13, size, p, black, b,4)
    button(window, black, X14, size, p, black, b,2)



def mouse(mp):
    click=pygame.mouse.get_pressed()
    if mp[0] > xx and mp[0] < xx1+xx and mp[1] > yy and mp[1] < yy1+ yy:
        button(window, lightblue, X, size, 'Play', black, b)
        button(window, black, X, size, 'Play', black, b,1)
        Xseries(X,X11,X12,X13,X14,lightblue,black,b)
        if click==(1,0,0):
          Xseries(Xl,Xl1,Xl2,Xl3,Xl4,blue,black,bc)
          pygame.time.delay(500)
          start()
      


def mouse1(mp,xx,xx1,yy,yy1):
    click=pygame.mouse.get_pressed()
    if mp[0] > xx and mp[0] < xx1+xx and mp[1] > yy and mp[1] < yy1+yy:
        button(window, lightgreen, Xa, size, 'Quit', black, d)
        button(window, lightgreen, Xa, size, 'Quit', black, d,1)
        Xseries(Xa,X21,X22,X23,X24,lightgreen,black,d,"Quit")
        if click==(1,0,0):
          Xseries(Xa,Xm1,Xm2,Xm3,Xm4,green,black,dc,"Quit")
          pygame.time.delay(400)
          pygame.quit()
          quit()
# menu function



def start():
    # basket position and its change
    basketX=360
    basketY=600
    change=0
    extrachange=1.5
    var="on"
    # flower positon
    flowerX=random.randint(5,650)
    flowerY=2
    changeFlower=1
    # score and miss limit
    score=0
    flowerNo=0  
    miss=3
    run=True
    while run:
        # text label and sky and chances
        window.blit(sky,(0,0))
        # buttons
        # score  text
        displayScore(32,5,5,"score :",score)
    # miss text
        misstext=missfont.render("Miss: "+str(miss),True,(0,0,0)) 
        overText=over.render("Game Over!!! ",True,(0,0,0))
        window.blit(misstext,(720,5))

        # high score text
        if int(highscore)>score: 
            displayhighscore(32,280,5,"highscore: ",highscore)
        else:
            displayhighscore(32,280,5,"highscore: ",score)   
        
        # keybord track
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    change=+extrachange
                elif event.key==pygame.K_LEFT:
                    change=-extrachange
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:
                    change=0
    # moving the objects   
        basketX+=change
        flowerY+=changeFlower
    # preventing touching boundries
        if basketX<=0:
            basketX=0
        elif basketX>=736:
            basketX = 736
    # movement of basket 
        moveBasket(basketX,basketY)
        window.blit(basket,(basketX,basketY))
    # flower position
        rand(flowerNo,flowerX,flowerY)
        
        # collecting distance
        distance=((flowerX-basketX)**2 +(flowerY-basketY)**2)**0.5

        # checking boundories
        if flowerY>=680:
            lossSound()
            miss-=1
            flowerY=10
            flowerX=random.randint(5,650)
            flowerNo=random.randint(0,2)
            rand(flowerNo,flowerX,flowerY)

    
            
    # effects after collecting
        elif distance<40 and basketY>=flowerY and flowerX>=basketX-30:
            basket2X=basketX
            window.blit(basket2,(basket2X,basketY))
            if flowerNo==0:
                n2orn1orn3(20,basketX,basketY-20,"+1")
                score+=1
                pygame.display.update()
                pygame.time.delay(1)
            elif flowerNo==1:
                n2orn1orn3(20,basketX,basketY-20,"+2")
                score+=2
                pygame.display.update()
                pygame.time.delay(1)
            else:
                n2orn1orn3(20,basketX,basketY-20,"+3")
                score+=3
                pygame.display.update()
                pygame.time.delay(1)

            #picking flower
            flowerY=10
            flowerX=random.randint(5,650)
            flowerNo=random.randint(0,2)
            rand(flowerNo,flowerX,flowerY)
            pygame.display.update()
            sound()
            changeFlower+=0.05

           
        # increasing speed of flower
        # if score>=40:
        #     changeFlower=2      
        # elif score>=20:
        #     changeFlower=1.8
        # elif score>=10:
        #     changeFlower=1.5
        # elif score>=5:
        #     changeFlower=1.3

        pygame.display.update()
    # checking missess
        if miss <=0: 
            window.blit(overText,(80,220))
            background.stop()
            pygame.time.delay(500)
            if score<=int(highscore):
                displayScore(32,(overText.get_width()//2-60),320,"Your Score:",score)
            else:
                displayScore(32,(overText.get_width()//2-50),320,"New Highscore:",score)
            overSound()
            pygame.display.update()
            pygame.time.delay(1000)
            run=False
            background.play(-1)
    # file to store hiscore
    f=open("highscore.txt","w")
    if score>int(highscore):
        f.write(str(score))
    else:
        f.write(str(highscore))
    f.close()
def menu():
    mp=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    global run
    run = True
    while run:
        window.blit(sky5,(0,0))
        Xseries(X,X11,X12,X13,X14,blue,black,b)
        Xseries(Xa,X21,X22,X23,X24,green,black,d,"Quit")

        mouse(mp)
        mouse1(mp,Xa[0],Xa[2],Xa[1],Xa[3])
    
        for event in pygame.event.get():
            mp = pygame.mouse.get_pos()
            click=pygame.mouse.get_pressed()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        pygame.display.update()

menu()