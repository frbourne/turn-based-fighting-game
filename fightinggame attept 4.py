from math import *
from random import *
from time import *
from tkinter import *
root = Tk()
s = Canvas( root, width=800, height=800, background="limegreen" )
s.pack()

#values need before code
dead = True
enemys = False
#mouse stuff
xMouse=0
yMouse =0
on = 0
#commands
def setstats (x):
    global q, h, xh, hp, xhp, d, xd, a, xa, ac, xac, ed, dead, asdf, asdfg,stats
    #base stats
    #hit points
    hp = 10
    #max health
    h = 10
    #defense
    d = 50
    #attack
    a = 10
    #accuracy/crit chance
    ac=80
    #enemies defeated
    ed=0
    #dead or not checker
    dead=False
    #random stuff to stop bugs
    q = 0
    asdf = 0
    asdfg = 0
    stats=1
#making background for the fight
def fighting (x, y, s):
    global grasse, grass, grassep, player, playerp, skeleton, skeletonp, xMouse, yMouse, textwindow, texts, button1, button1texts, button2, button2texts, h, xh, hp, xhp, d, xd, a, xa, ac, xac, ed
    grass = PhotoImage(file="fight grass.gif")
    grasse = PhotoImage(file="your fight grass.gif")
    grassp = s.create_image(x+600, y+150, image = grass, anchor=N)
    grassep = s.create_image(x+200, y+550, image = grasse, anchor=N)    
    s.update()
#spawns player model  
def mplayer(x, y, s):
    global grasse, grass, grassep, player, playerp, skeleton, skeletonp, xMouse, yMouse, textwindow, texts, button1, button1texts, button2, button2texts, h, xh, hp, xhp, d, xd, a, xa, ac, xac, ed
    player = PhotoImage(file="player.gif")
    playerp = s.create_image(x+250, y+280, image = player, anchor=N)
#deletes player model
def delplayer(s):
    global grasse, grass, grassep, player, playerp, skeleton, skeletonp, xMouse, yMouse, textwindow, texts, button1, button1texts, button2, button2texts, h, xh, hp, xhp, d, xd, a, xa, ac, xac, ed
    s.delete(playerp)
#spawns enemy model    
def enemyskeleton(x, y, s):
    global grasse, grass, grassep, player, playerp, skeleton, skeletonp, xMouse, yMouse, textwindow, texts, button1, button1texts, button2, button2texts, h, xh, hp, xhp, d, xd, a, xa, ac, xac, ed
    skeleton = PhotoImage(file="skeleton warrior.gif")
    skeletonp = s.create_image(x+600, y+75, image = skeleton, anchor=N)
    s.update()
#deletes enemy model
def delenemyskeleton(s):
    global grasse, grass, grassep, player, playerp, skeleton, skeletonp, xMouse, yMouse, textwindow, texts, button1, button1texts, button2, button2texts, h, xh, hp, xhp, d, xd, a, xa, ac, xac, ed
    s.delete(skeletonp)
#commend made for createing text on screen (saves me lots of time (x, y control cordanits, s is just there form older model of game, and would be big pain to remove, and t is text)    
def text(x, y, s, t):
    global grasse, grass, grassep, player, playerp, skeleton, skeletonp, xMouse, yMouse, textwindow, texts, button1, button1texts, button2, button2texts, h, xh, hp, xhp, d, xd, a, xa, ac, xac, ed
    textwindow = s.create_rectangle(6,700, 798, 800, fill ="white", outline = "black", width = 8)
    texts = s.create_text(350, 720, fill="black", font="Comic 10", text=y)
#deletes text commands text
def deltext(s):
    s.delete(textwindow, texts)
#bacially a text that also creates 2 buttons, with can be named with a1, and a2
def textquestion(x, y, a1, a2, s):
    global grasse, grass, grassep, player, playerp, skeleton, skeletonp, xMouse, yMouse, textwindow, texts, button1, button1texts, button2, button2texts, h, xh, hp, xhp, d, xd, a, xa, ac, xac, ed
    textwindow = s.create_rectangle(6,700, 798, 800, fill ="white", outline = "black", width = 8)
    texts = s.create_text(350, 720, fill="black", font="Comic 10", text=y)
    button1 = s.create_rectangle(700, 700, 800, 750, fill = "red", outline="black", width = 8)
    button1texts = s.create_text(750, 725, fill="black", font="Comic 10", text=a1)
    button2 = s.create_rectangle(700, 750, 800, 800, fill = "cyan", outline="black", width = 8)
    button2texts = s.create_text(750, 775, fill="black", font="Comic 10", text=a2)
    s.update()
#deletes text question   
def deltextquestion(x):
    global grasse, grass, grassep, player, playerp, skeleton, skeletonp, xMouse, yMouse, textwindow, texts, button1, button1texts, button2, button2texts, h, xh, hp, xhp, d, xd, a, xa, ac, xac, ed
    s.delete( textwindow, texts, button1, button1texts, button2, button2texts)

def mouseClickDetector( event ):
    global gamestart, on, enemys, q, grasse, grass, grassep, player, playerp, skeleton, skeletonp, xMouse, yMouse, textwindow, texts, button1, button1texts, button2, button2texts, h, xh, hp, xhp, d, xd, a, xa, ac, xac, ed
    xMouse = event.x
    yMouse = event.y
    #checks if ytou have acually started the game or not
    if gamestart == True:
        #checking to see if new enemy needs to be spawned
        if xhp < 0 or xhp == 0:
            enemys = False
        #checks if you are dead or not be for allowing you to fight more
        if xhp > 0 and xhp != 0:
            fight(0)
        #the elif was bugging out so I needed to seperated it
        if True:
            #q is checking if a question is on screen,  and if soo it will not spawn another one
            if q == 0 and enemys == True and xhp != 0:
                q=1
                textquestion(0, "would you like to attack or block", "attack", "block", s)
                fight(0)
            #making sure enemys are dead before allowing you to contuine
            elif enemys == False or xhp <= 0:
                if on == 0:
                    xMouse = 0
                    yMouse = 0
                    on = 1
                #starts the imporve stats thing
                elif on == 1:
                    battleend(s)
    #all for the intro screen
    else:
        startscreenclick(s)
    #if you die this will restart the game, provied you click 
    if hp <= 0:
        hp = 1
        s.delete()
        startscreenstart(s)
                
#it orgilay had more in it but this is whats left, and I just left it
def intro(x):
    global grasse, grass, grassep, player, playerp, skeleton, skeletonp, xMouse, yMouse, textwindow, texts, button1, button1texts, button2, button2texts, h, xh, hp, xhp, d, xd, a, xa, ac, xac, ed
    fighting(0,0,s)
    mplayer(0,0,s)
#spawns enemy, and gives text
def enemy(x, y):
    global estats, enemys, asdf, grasse, grass, grassep, player, playerp, skeleton, skeletonp, xMouse, yMouse, textwindow, texts, button1, button1texts, button2, button2texts, h, xh, hp, xhp, d, xd, a, xa, ac, xac, ed
    enemys = True
    text(0,("your stats are curret health = "+ str(hp)+ "   max health = "+ str(h)+"   defense = "+ str(d)+ "   attack = "+  str(a)+ "   accuracy = "+ str(ac)), s, 5)
    s.update()
    sleep(5)
    deltext(s)
    print(asdf)
    if asdf == 1:
        deltextquestionbe(s)
        s.delete(button3, button3texts, button4, button4texts)
    else:
        asdf = 1
    xh = randint((7+int(estats*ed)), (10+int(estats*ed)))
    xhp = xh
    xd = randint((40+int(estats*ed)), (50+int(estats*ed)))
    xa =  randint((4+int(estats*ed)), (5+int(estats*ed)))
    xac = randint((70+int(estats*ed)), (80+int(estats*ed)))
    #makes sure his stats don't go over the limet (other wise he would be unkillable)
    if xd >= 80:
        xd = 80
    if xac >= 160:
        xac = 160
    enemyskeleton(x,y,s)
    healthbars(s)
    text(0,("an enemy has appeared!!!. his stats are "+ str(xhp)+ " health "+ str(xd)+ " defense "+ str(xa)+ " attack "+ str(xac)+ " accuracy"), s, 5)
    s.update()
    sleep(5)
    deltext(s)
    text(0,(" you have slain "+ str(ed)+ " enemies"), s, 5)
    s.update()
    sleep(2)
    deltext(s)
    enemys = True
    q=0
    textquestion(0, "would you like to attack or block", "attack", "block", s)
#does the health bar things
def healthbars(s):
    global hp, h, xhp, xh, healthbarswindow, ehealthbarswindow, healthbar, ehealthbar
    healthbarswindow = s.create_rectangle(6,450, 298, 400, fill ="red", outline = "black", width = 8)
    ehealthbarswindow = s.create_rectangle(800,5, 502, 50, fill ="red", outline = "black", width = 8)
    hh=hp/h
    print(hh)
    xhh=xhp/xh
    print(xhh)
    healthbar = s.create_rectangle(6,450, int(298*hh), 400, fill ="green", outline = "black", width = 0)
    if int(502+(300*(1-xhh))) >= 800:
        xcyvubh=1
    else:
        ehealthbar = s.create_rectangle(800,5, int(502+(300*(1-xhh))), 50, fill ="green", outline = "black", width = 0)
    s.update()
#delets the health bar things
def delhealthbars(s):
    global healthbarswindow ,ehealthbarswindow, healthbar, ehealthbar
    s.delete(healthbarswindow, ehealthbarswindow, healthbar, ehealthbar)
#this is the long one that does all the calulations for fight
#to sum up the code it checks with button you press
#if attack it checks if you miss or not, then if you crit or not, then does the same for the enemy (if you crit you do double damage
#the way damage is calulated is defese stat divided by 100, then the attack stat is times by that number, and that is the damage you deal
#if you block it checks if you blocked or not, and then if you have a chance a returning an attack
#if you don't block checks if the enemy missed, crit, or just did a normal attack 
def fight(f):
    global stats, enemys, button3, button3texts, button4, button4texts, q, dead, grasse, grass, grassep, player, playerp, skeleton, skeletonp, xMouse, yMouse, textwindow, texts, button1, button1texts, button2, button2texts, h, xh, hp, xhp, d, xd, a, xa, ac, xac, ed, healthbarswindow, ehealthbarswindow, healthbar, ehealthbar
    #attack
    print (xMouse, yMouse)
    try:
        deltextquestionbes(s)
    except:
        x=1
    if xMouse < 800 and xMouse > 700 and yMouse < 750 and yMouse >700:
        xMouse = 0
        yMouse = 0
        deltextquestion(0)
        q = 0
        b3 = randint(0, 60)
        b4 = randint(70, 160)
        b = randint(0, 60)
        b2 = randint(70, 160)
        if b3 <= ac and dead != True:
            if b4 <= ac and dead != True:
                res = a*(xd/100)
                dam = a - res
                xhp = xhp - int(dam*2)
                text(0,("you dealt a crit, dealing "+ str(dam*2)+ " damage, their current health is "+ str (xhp)), s,5)
                att = s.create_polygon(525, 150, 500, 100, 550, 100, 600, 50, 600, 100, 650, 150, 600, 150, 600, 200, 550, 165, 500, 200, 525, 150, fill = "white", width = 0)
                s.update()
                sleep(0.3)
                s.delete(att)
                s.update()
                f=0
                ff = 0
                for x in range (0, 40):
                    enemyskeleton(f*3,0,s)
                    if f < 10 and ff != 1:
                        f=f+1
                    else:
                        ff=1
                        f=f-1
                        if f < -10:
                            ff=0
                    delenemyskeleton(s)
                enemyskeleton(0,0,s)
                
                if hp <=0:
                    dead = True
                if b <= xac and dead != True:
                    if b2 <= xac and xhp >0 and xhp != 0:
                        xres = xa*(d/100)
                        xdam = xa - xres
                        hp = hp - int(xdam*2)
                        text(0,("the enemy dealt a crit, dealing "+ str(xdam*2)+ " damage, your current health is "+ str(hp)), s,5)
                        att = s.create_polygon(350, 525, 300, 500, 300, 550, 250, 600, 300, 600, 350, 650, 350, 600, 400, 600, 365, 550, 400, 500, 350, 525, fill = "white", width = 0)
                        s.update()
                        sleep(0.3)
                        s.delete(att)
                        s.update()
                        f=0
                        ff = 0
                        for x in range (0, 40):
                            mplayer(f*3,0,s)
                            text(0,("the enemy dealt a crit, dealing "+ str(xdam*2)+ " damage, your current health is "+ str(hp)), s,5)
                            s.update()
                            if f < 10 and ff != 1:
                                f=f+1
                            else:
                                ff=1
                                f=f-1
                                if f < -10:
                                    ff=0
                            delplayer(s)
                        mplayer(0,0,s)
                        
                    elif dead != True and xhp != 0 and xhp >0:
                        xres = xa*(d/100)
                        xdam = xa - xres
                        hp = hp - int(xdam)
                        text(0,(" you got hit and where dealt "+ str(xdam)+ " damage, your current health is" + str(hp)), s,5)
                        att = s.create_polygon(350, 525, 300, 500, 300, 550, 250, 600, 300, 600, 350, 650, 350, 600, 400, 600, 365, 550, 400, 500, 350, 525, fill = "white", width = 0)
                        s.update()
                        sleep(0.3)
                        s.delete(att)
                        s.update()
                        f=0
                        ff = 0
                        for x in range (0, 40):
                            mplayer(f*3,0,s)
                            text(0,(" you got hit and where dealt "+ str(xdam)+ " damage, your current health is" + str(hp)), s,5)
                            s.update()
                            if f < 10 and ff != 1:
                                f=f+1
                            else:
                                ff=1
                                f=f-1
                                if f < -10:
                                    ff=0
                            delplayer(s)
                        mplayer(0,0,s)
            elif dead != True:
                res = a*(xd/100)
                dam = a - res
                xhp = xhp - int(dam)
                text(0,("you dealt "+ str(dam)+ " damage ,and he currently has "+ str(xhp)+ " health"), s,5)
                s.update()
                sleep(3)
                att = s.create_polygon(525, 150, 500, 100, 550, 100, 600, 50, 600, 100, 650, 150, 600, 150, 600, 200, 550, 165, 500, 200, 525, 150, fill = "white", width = 0)
                s.update()
                sleep(0.3)
                s.delete(att)
                s.update()
                f=0
                ff = 0
                for x in range (0, 40):
                    enemyskeleton(f*3,0,s)
                    if f < 10 and ff != 1:
                        f=f+1
                    else:
                        ff=1
                        f=f-1
                        if f < -10:
                            ff=0
                    delenemyskeleton(s)
                enemyskeleton(0,0,s)
                deltext(s)
                if b <= xac and dead != True:
                    if b2 <= xac and dead != True and xhp >0 and xhp != 0:
                        xres = xa*(d/100)
                        xdam = xa - xres
                        hp = hp - int(xdam*2)
                        text(0,("the enemy dealt a crit, dealing "+ str(xdam*2)+ " damage, your current health is "+ str(hp)), s,5)
                        att = s.create_polygon(350, 525, 300, 500, 300, 550, 250, 600, 300, 600, 350, 650, 350, 600, 400, 600, 365, 550, 400, 500, 350, 525, fill = "white", width = 0)
                        s.update()
                        sleep(0.3)
                        s.delete(att)
                        s.update()
                        f=0
                        ff = 0
                        for x in range (0, 40):
                            mplayer(f*3,0,s)
                            text(0,("the enemy dealt a crit, dealing "+ str(xdam*2)+ " damage, your current health is "+ str(hp)), s,5)
                            s.update()
                            if f < 10 and ff != 1:
                                f=f+1
                            else:
                                ff=1
                                f=f-1
                                if f < -10:
                                    ff=0
                            delplayer(s)
                        mplayer(0,0,s)
                    elif dead != True and xhp >0 and xhp != 0:
                        xres = xa*(d/100)
                        xdam = xa - xres
                        hp = hp - int(xdam)
                        text(0,("you got hit and where dealt "+ str(xdam)+ " damage, your current health is "+ str(hp)), s,5)
                        att = s.create_polygon(250, 525, 200, 500, 200, 550, 150, 600, 200, 600, 250, 650, 250, 600, 300, 600, 265, 550, 300, 500, 250, 525, fill = "white", width = 0)
                        s.update()
                        sleep(0.3)
                        s.delete(att)
                        s.update()
                        f=0
                        ff = 0
                        for x in range (0, 40):
                            mplayer(f*3,0,s)
                            text(0,("you got hit and where dealt "+ str(xdam)+ " damage, your current health is "+ str(hp)), s,5)
                            s.update()
                            if f < 10 and ff != 1:
                                f=f+1
                            else:
                                ff=1
                                f=f-1
                                if f < -10:
                                    ff=0
                            delplayer(s)
                        mplayer(0,0,s)
                elif dead != True and xhp >0 and xhp != 0:
                    text(0,("the enemy missed"), s,5)
                    s.update()
                    sleep(3)
                    deltext(s)
        elif dead != True:
            text(0,("you missed"), s,5)
            s.update()
            sleep(3)
            deltext(s)
            if b <= xac and dead != True:
                if b2 <= xac and dead != True:
                    xres = xa*(d/100)
                    xdam = xa - xres
                    hp = hp - int(xdam*2)
                    text(0,("the enemy dealt a crit, dealing "+ str(xdam*2)+ " damage, your current health is "+ str(hp)), s,5)
                    att = s.create_polygon(350, 525, 300, 500, 300, 550, 250, 600, 300, 600, 350, 650, 350, 600, 400, 600, 365, 550, 400, 500, 350, 525, fill = "white", width = 0)
                    s.update()
                    sleep(0.3)
                    s.delete(att)
                    s.update()
                    f=0
                    ff = 0
                    for x in range (0, 40):
                        mplayer(f*3,0,s)
                        text(0,("the enemy dealt a crit, dealing "+ str(xdam*2)+ " damage, your current health is "+ str(hp)), s,5)
                        s.update()
                        if f < 10 and ff != 1:
                            f=f+1
                        else:
                            ff=1
                            f=f-1
                            if f < -10:
                                ff=0
                        delplayer(s)
                    mplayer(0,0,s)
                elif dead != True:
                    xres = xa*(d/100)
                    xdam = xa - xres
                    hp = hp - int(xdam)
                    text(0,("you got hit and where dealt "+ str(xdam)+ " damage, your current health is "+ str(hp)), s,5)
                    att = s.create_polygon(350, 525, 300, 500, 300, 550, 250, 600, 300, 600, 350, 650, 350, 600, 400, 600, 365, 550, 400, 500, 350, 525, fill = "white", width = 0)
                    s.update()
                    sleep(0.3)
                    s.delete(att)
                    s.update()
                    f=0
                    ff = 0
                    for x in range (0, 40):
                        mplayer(f*3,0,s)
                        text(0,("you got hit and where dealt "+ str(xdam)+ " damage, your current health is "+ str(hp)), s,5)
                        s.update()
                        if f < 10 and ff != 1:
                            f=f+1
                        else:
                            ff=1
                            f=f-1
                            if f < -10:
                                ff=0
                        delplayer(s)
                    mplayer(0,0,s)
            elif dead != True:
                text(0,("the enemy missed"),5)
                s.update()
                sleep(3)
                deltext(s)
            
    #block
    elif xMouse < 800 and xMouse > 700 and yMouse < 800 and yMouse >750:
        b = randint(0, d)
        if b >=50:
            res = a*(xd/100)
            dam = a - res
            xhp = xhp - int(dam)
            text(0,("you blocked the enemy attack and counter attacked dealing "+ str(dam)+ " and leave his health at "+ str(xhp)), s,5)
            att = s.create_polygon(525, 150, 500, 100, 550, 100, 600, 50, 600, 100, 650, 150, 600, 150, 600, 200, 550, 165, 500, 200, 525, 150, fill = "white", width = 0)
            s.update()
            sleep(0.3)
            s.delete(att)
            s.update()
            f=0
            ff = 0
            for x in range (0, 40):
                enemyskeleton(f*3,0,s)
                if f < 10 and ff != 1:
                    f=f+1
                else:
                    ff=1
                    f=f-1
                    if f < -10:
                         ff=0
                delenemyskeleton(s)
            enemyskeleton(0,0,s)
        elif b >= 35:
            text(0,("you blocked the enemy attack, but you didn't have time to counter attack!"), s,5)
            s.update()
            sleep(3)
            deltext(s)
        else:
            xres = xa*(d/100)
            xdam = xa - xres
            hp = hp - int(xdam)
            text(0,("the enemy attacked and delt "+ str(xdam)+ " your current health is "+ str(hp)), s,5)
            att = s.create_polygon(350, 525, 300, 500, 300, 550, 250, 600, 300, 600, 350, 650, 350, 600, 400, 600, 365, 550, 400, 500, 350, 525, fill = "white", width = 0)
            s.update()
            sleep(0.3)
            s.delete(att)
            s.update()
            f=0
            ff = 0
            for x in range (0, 40):
                mplayer(f*3,0,s)
                text(0,("the enemy attacked and delt "+ str(xdam)+ " your current health is "+ str(hp)), s,5)
                s.update()
                if f < 10 and ff != 1:
                    f=f+1
                else:
                    ff=1
                    f=f-1
                    if f < -10:
                        ff=0
                delplayer(s)
            mplayer(0,0,s)
            text(0,("the enemy attacked and delt "+ str(xdam)+ " your current health is "+ str(hp)), s,5)
    if xhp <= 0:
        enemys = False
        delenemyskeleton(s)
        deltextquestion(s)
        ed = ed +1
        battleend(s)
        q==1
        if stats !=1:
            try:
                deltextquestionbe(s)
            except:
                asdfg = 1
            textquestion(0,"stat improve? (h) health (will restore health) (d) defense (a) attack (ac) accuracy (also crit rate)","attack", "accuracy", s)
            button3 = s.create_rectangle(700, 650, 800, 700, fill = "red", outline="black", width = 8)
            button3texts = s.create_text(750, 675, fill="black", font="Comic 10", text="health")
            button4 = s.create_rectangle(700, 600, 800, 650, fill = "cyan", outline="black", width = 8)
            button4texts = s.create_text(750, 625, fill="black", font="Comic 10", text="defense")
            print("hi")
        else:
            stats = 0
    healthbars(s)
    s.update()
    xMouse = 0
    yMouse = 0
#button 3, and 4 are the bain of my existence, this little command gives me great joy in deleting the buttons, and there text
def deltextquestionbe(s):
    global button3texts, button4, button4texts
    s.delete(button3, button3texts, button4, button4texts)
    deltextquestion(s)
#does what the command up does, but doesn't delete the question (it fixed some bug)   
def deltextquestionbes(s):
    global button3texts, button4, button4texts
    s.delete(button3, button3texts, button4, button4texts)
#if you win a battle you can improve a stat. this is the command that does that. 
def battleend(f):
    global stats, on, asdfg, button3, button3texts, button4, button4texts, grasse, grass, grassep, player, playerp, skeleton, skeletonp, xMouse, yMouse, textwindow, texts, button1, button1texts, button2, button2texts, h, xh, hp, xhp, d, xd, a, xa, ac, xac, ed
    if hp <= 0:
        text(0,("you lose"), s,5)
    else:
        try:
            deltextquestionbe(s)
        except:
            asdfg = 1
        textquestion(0,"stat improve? (h) health (will restore health) (d) defense (a) attack (ac) accuracy (also crit rate)","attack", "accuracy", s)
        button3 = s.create_rectangle(700, 650, 800, 700, fill = "red", outline="black", width = 8)
        button3texts = s.create_text(750, 675, fill="black", font="Comic 10", text="health")
        button4 = s.create_rectangle(700, 600, 800, 650, fill = "cyan", outline="black", width = 8)
        button4texts = s.create_text(750, 625, fill="black", font="Comic 10", text="defense")
        textquestion(0,"stat improve? (h) health (will restore health) (d) defense (a) attack (ac) accuracy (also crit rate)","attack", "accuracy", s)

        s.update()
        if xMouse < 800 and xMouse > 700 and yMouse < 650 and yMouse >600:
            #so you can't go over the limmit
            if d <=80:
                d= d + 1
                text(0,("you improved defense"), s,5)
                on = 0
                sleep(1)
                enemy(0,0)
                s.delete(button3, button3texts, button4, button4texts)
                stats = 1
            else:
                textquestion(0,("you are at max defense"), "attack", "accuracy", s)
        elif xMouse < 800 and xMouse > 700 and yMouse < 700 and yMouse >650:
            if d != 80:
                h = h + 1
                hp = h
                text(0,("you improved health"), s,5)
                on = 0
                sleep(1)
                enemy(0,0)
                s.delete(button3, button3texts, button4, button4texts)
                stats = 1
            else:
                textquestion(0,("you are at maxium defense"), "attack", "accuracy", s)

        elif xMouse < 800 and xMouse > 700 and yMouse < 750 and yMouse >700:
            a= a + 1
            text(0,("you improved attack"), s,5)
            on = 0
            sleep(1)
            enemy(0,0)
            s.delete(button3, button3texts, button4, button4texts)
            stats = 1
        elif xMouse < 800 and xMouse > 700 and yMouse < 800 and yMouse >750:
            #so you can't go over the limmit
            if ac <=160:
                ac= ac + 1
                text(0,("you improved accuracy"), s,5)
                on = 0
                sleep(1)
                enemy(0,0)
                s.delete(button3, button3texts, button4, button4texts)
                stats = 1
            else:
                textquestion(0,("you are at max accuracy"), "attack", "accuracy", s)
    xMouse = 0
    yMouse = 0
    deltextquestionbe
#makes the back ground, and the buttons at the start of the game
def startscreenstart(s):
    global mainscreen, mainscreenp, buttonstart, buttonstarttext, buttondiff, buttondifftext, gamestart, firstclick
    firstclick=True
    mainscreen = PhotoImage(file="mainscreen.gif")
    mainscreenp = s.create_image(400, 0, image = mainscreen, anchor=N)
    buttonstart = s.create_rectangle(300, 300, 500, 400, fill = "red", width = 6, outline = "black")
    buttonstarttext = s.create_text(400, 350, fill="black", font="Comic 30", text="start")
    buttondiff = s.create_rectangle(300, 400, 500, 500, fill = "blue", width = 6, outline = "black")
    buttondifftext = s.create_text(400, 450, fill="black", font="Comic 30", text="difficulty")
    gamestart = False
#allows you to change difficulty, and start the game                                
def startscreenclick(s):
    global mainscreen, mainscreenp, buttonstart, buttonstarttext, buttondiff, buttondifftext, xMouse, yMouse, firstclick, gamestart, buttonhard, buttonhardtext, estats
    if xMouse < 500 and xMouse > 300 and yMouse < 500 and yMouse >400:
        if firstclick == True:
            firstclick = False
            s.delete(buttonstarttext, buttondifftext)
            buttonhard = s.create_rectangle(300, 500, 500, 600, fill = "green", width = 6, outline ="black")
            buttonhardtext = s.create_text(400, 550, fill="black", font="Comic 30", text="Hard")
            buttonstarttext = s.create_text(400, 350, fill="black", font="Comic 30", text="Easy")
            buttondifftext = s.create_text(400, 450, fill="black", font="Comic 30", text="Medium")
        else:
            estats= 0.3334
            firstclick = True
            s.delete(buttonstarttext, buttondifftext,buttonhard, buttonhardtext)
            buttondifftext = s.create_text(400, 450, fill="black", font="Comic 30", text="difficulty")
            buttonstarttext = s.create_text(400, 350, fill="black", font="Comic 30", text="start")
            
    if xMouse < 500 and xMouse > 300 and yMouse < 400 and yMouse >300:
        if firstclick == True:
            rungame(1)
        else:
            estats= 0.25
            firstclick = True
            s.delete(buttonstarttext, buttondifftext,buttonhard, buttonhardtext)
            buttondifftext = s.create_text(400, 450, fill="black", font="Comic 30", text="difficulty")
            buttonstarttext = s.create_text(400, 350, fill="black", font="Comic 30", text="start")
    
    if xMouse < 500 and xMouse > 300 and yMouse < 600 and yMouse > 500:
        if firstclick == True:
            asdqfghj=1
        else:
            estats= 0.5
            firstclick = True
            s.delete(buttonstarttext, buttondifftext,buttonhard, buttonhardtext)
            buttondifftext = s.create_text(400, 450, fill="black", font="Comic 30", text="difficulty")
            buttonstarttext = s.create_text(400, 350, fill="black", font="Comic 30", text="start")
#start the fighting, and summons an enemy, and sets the stats (all he if statments fix one or so bugs)                                   
def rungame(x):
    global gamestart, q, healthbarswindow, ehealthbarswindow, healthbar, ehealthbar , enemys, grasse, grass, grassep, player, playerp, skeleton, skeletonp, xMouse, yMouse, textwindow, texts, button1, button1texts, button2, button2texts, h, xh, hp, xhp, d, xd, a, xa, ac, xac, ed, dead
    s.delete(mainscreenp, buttonstart, buttonstarttext, buttondiff, buttondifftext)
    gamestart = True
    if dead == True:
        setstats(0)
        fighting(0,0,s)
        mplayer(0,0,s)
        intro(0)
    if dead == False:
        if enemys == False:
            enemy(0,0)
            if q == 0:
                q=1
                textquestion(0, "would you like to attack or block", "attack", "block", s)
            fight(0)
            s.update()
            enemys = True
        if enemys == True:
            print("hi")
            print(q)
            if q == 0:
                q=1
                textquestion(0, "would you like to attack or block", "attack", "block", s)
            fight(0)
            s.update()
    healthbars(s)
spacing = 50
for x in range(0, 1000, spacing): 
    s.create_line(x, 25, x, 1000, fill="blue")
    s.create_text(x, 5, text=str(x), font="Times 9", anchor = N)

for y in range(0, 1000, spacing):
    s.create_line(25, y, 1000, y, fill="blue")
    s.create_text(5, y, text=str(y), font="Times 9", anchor = W)

root.after(0, startscreenstart(s))
s.bind( "<Button-1>", mouseClickDetector )
s.bind( "<Motion>", getMousePosition) 
s.focus_set()
s.pack()
root.mainloop()
        
        
        
        
    
                


