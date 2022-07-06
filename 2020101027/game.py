import copy
import pickle
from src.input import Get, input_to
from src.village import codepos,n,m,buildingclass,building,town_hall,wall,colorpos,hut
import numpy as np
from src.barbarians import barbarian, personclass
from src.archers import archer
from src.balloon import balloon, balloonclass
from colorama import Fore, Back, Style, init
from src.spells import healspell,ragespell
import os

direction = 0


init(autoreset=True)

class codenm():
    def define(self, code, color, x):
        if x == -1:
            if code == 0:
                if color == 0:
                    print(Fore.BLACK + Back.GREEN + Style.BRIGHT + 'T',end='')
                if color == 1:
                    print(Fore.BLACK + Back.YELLOW + Style.BRIGHT + 'T',end='')
                if color == 2:
                    print(Fore.BLACK + Back.RED + Style.BRIGHT + 'T',end='')
            else:
                if code == 1:
                    if color == 0:
                        print(Fore.BLACK + Back.GREEN + Style.BRIGHT + 'H',end='')
                    if color == 1:
                        print(Fore.BLACK + Back.YELLOW + Style.BRIGHT + 'H',end='')
                    if color == 2:
                        print(Fore.BLACK + Back.RED + Style.BRIGHT + 'H',end='')
        
                else:
                    if code == 2:
                        if color == 0:
                            print(Fore.BLACK + Back.GREEN + Style.BRIGHT + 'W',end='')
                        if color == 1:
                            print(Fore.BLACK + Back.YELLOW + Style.BRIGHT + 'W',end='')
                        if color == 2:
                            print(Fore.BLACK + Back.RED + Style.BRIGHT + 'W',end='')
            if code == -1:
                print(Back.BLUE + ' ',end='')

            if code == 14:
                print(Back.BLACK + Fore.MAGENTA + Style.NORMAL + 'K', end = '')

            if code == 7:
                if color == 0:
                    print(Fore.GREEN + Back.WHITE + Style.BRIGHT + 'B',end='')
                if color == 1:
                    print(Fore.YELLOW + Back.WHITE + Style.BRIGHT + 'B',end='')
                if color == 2:
                    print(Fore.RED + Back.WHITE + Style.BRIGHT + 'B',end='')

            if code == 3:
                if color == 0:
                    print(Fore.BLACK + Back.GREEN + Style.BRIGHT + 'C',end='')
                if color == 1:
                    print(Fore.BLACK + Back.YELLOW + Style.BRIGHT + 'C',end='')
                if color == 2:
                    print(Fore.BLACK + Back.RED + Style.BRIGHT + 'C',end='')

            if code == 13:
                if color == 0:
                    print(Fore.WHITE + Back.GREEN + Style.BRIGHT + 'M',end='')
                if color == 1:
                    print(Fore.WHITE + Back.YELLOW + Style.BRIGHT + 'M',end='')
                if color == 2:
                    print(Fore.WHITE + Back.RED + Style.BRIGHT + 'M',end='')

        
            if code == 11:
                if color == 0:
                    print(Fore.GREEN + Back.WHITE + Style.BRIGHT + 'A',end='')
                if color == 1:
                    print(Fore.YELLOW + Back.WHITE + Style.BRIGHT + 'A',end='')
                if color == 2:
                    print(Fore.RED + Back.WHITE + Style.BRIGHT + 'A',end='')


        if x != -1:
            if code == 0:
                if color == 0:
                    print(Fore.BLACK + Back.GREEN + Style.BRIGHT + '1',end='')
                if color == 1:
                    print(Fore.BLACK + Back.YELLOW + Style.BRIGHT + '1',end='')
                if color == 2:
                    print(Fore.BLACK + Back.RED + Style.BRIGHT + '1',end='')
            else:
                if code == 1:
                    if color == 0:
                        print(Fore.BLACK + Back.GREEN + Style.BRIGHT + '9',end='')
                    if color == 1:
                        print(Fore.BLACK + Back.YELLOW + Style.BRIGHT + '9',end='')
                    if color == 2:
                        print(Fore.BLACK + Back.RED + Style.BRIGHT + '9',end='')
        
                else:
                    if code == 2:
                        if color == 0:
                            print(Fore.BLACK + Back.GREEN + Style.BRIGHT + '6',end='')
                        if color == 1:
                            print(Fore.BLACK + Back.YELLOW + Style.BRIGHT + '6',end='')
                        if color == 2:
                            print(Fore.BLACK + Back.RED + Style.BRIGHT + '6',end='')
            if code == -1:
                print(Back.BLUE + 'B',end='')

            if code == 14:
                print(Back.BLACK + Fore.MAGENTA + Style.NORMAL + '7', end = '')

            if code == 7:
                if color == 0:
                    print(Fore.GREEN + Back.WHITE + Style.BRIGHT + '8',end='')
                if color == 1:
                    print(Fore.YELLOW + Back.WHITE + Style.BRIGHT + '8',end='')
                if color == 2:
                    print(Fore.RED + Back.WHITE + Style.BRIGHT + '8',end='')

            if code == 3:
                if color == 0:
                    print(Fore.BLACK + Back.GREEN + Style.BRIGHT + '4',end='')
                if color == 1:
                    print(Fore.BLACK + Back.YELLOW + Style.BRIGHT + '4',end='')
                if color == 2:
                    print(Fore.BLACK + Back.RED + Style.BRIGHT + '4',end='')

            if code == 13:
                if color == 0:
                    print(Fore.WHITE + Back.GREEN + Style.BRIGHT + '0',end='')
                if color == 1:
                    print(Fore.WHITE + Back.YELLOW + Style.BRIGHT + '0',end='')
                if color == 2:
                    print(Fore.WHITE + Back.RED + Style.BRIGHT + '0',end='')


            if code == 11:
                if color == 0:
                    print(Fore.GREEN + Back.WHITE + Style.BRIGHT + '5',end='')
                if color == 1:
                    print(Fore.YELLOW + Back.WHITE + Style.BRIGHT + '5',end='')
                if color == 2:
                    print(Fore.RED + Back.WHITE + Style.BRIGHT + '5',end='')


class king():
    def __init__(self):
        self.damage = 100
        self.dead = 0
        i = np.random.randint(0, n)
        j = np.random.randint(0, m)

        while codepos[i][j] != -1:
            i = np.random.randint(0, n)
            j = np.random.randint(0, m)
        
        self.x = i
        self.y = j
        codepos[i][j] = 14
        colorpos[i][j] = -1
        personclass[i][j] = self

    def change_damage(self, num):
        self.damage = num
    
    def destroy(self):
        self.destroy = 20

    def change_destroy(self):
        self.destroy = self.destroy*2

    def code(self):
        self.code = 14

    def die(self):
        codepos[self.x][self.y] = -1
        colorpos[self.x][self.y] = -1
        personclass[self.x][self.y] = -1
        self.x = -1
        self.y = -1

    def __sub__(self, other):
        return self.damage - other

    def __mul__(self, other):
        return self * other

    def ret_damage(self):
        return self.damage
    
    def multiply(self, x):
        self.damage = self.damage*x
        if self.damage > 100:
            self.damage = 100
        
    def hurt(self, damage):
        self.damage = self.damage - damage
        if self.damage <= 0 and self.dead == 0:
            self.dead = 1
            self.die()

    def move(self, ch):
        global direction
        if self.x == -1 and self.y == -1:
            return
        i = self.x
        j = self.y
        self.p = 0
        personclass[i][j] = -1
        if ch == 'w' or ch == 'W':
            self.p = 1
            if i - 1 >= 0 and codepos[i-1][j] == -1:
                codepos[i][j] = -1
                codepos[i-1][j] = 14
                i = i - 1
                self.x = i
                direction = 1
            else:
                direction = 1
        if ch == 'a' or ch == 'A':
            self.p = 1
            if j-1 >=0 and codepos[i][j-1] == -1:
                codepos[i][j] = -1
                codepos[i][j-1] = 14
                j = j - 1
                self.y = j
                direction = 0
            else:
                direction = 0
        if ch == 's' or ch == 'S':
            self.p = 1
            if i+1 < n and codepos[i+1][j] == -1:
                codepos[i][j] = -1
                codepos[i+1][j] = 14
                i = i + 1
                self.x = i
                direction = 2
            else:
                direction = 2        
        if ch == 'd' or ch == 'D':
            self.p = 1
            if j+1 < m and codepos[i][j+1] == -1:
                codepos[i][j] = -1
                codepos[i][j+1] = 14
                j = j + 1
                self.y = j
                direction = 3
            else:
                direction = 3
        personclass[self.x][self.y] = self
        if self.p == 0:
            return

    def attack(self): 
        global direction
        i = self.x
        j = self.y
        if direction == 0:
            if j - 1 >= 0 and buildingclass[i][j - 1] != -1:
                buildingclass[i][j - 1].damage(self.destroy)
        if direction == 1:
            if i - 1 >= 0 and buildingclass[i - 1][j] != -1:
                buildingclass[i - 1][j].damage(self.destroy)
        if direction == 2:
            if i + 1 < n and buildingclass[i + 1][j] != -1:
                buildingclass[i + 1][j].damage(self.destroy)
        if direction == 3:
            if j + 1 < m and buildingclass[i][j + 1] != -1:
                buildingclass[i][j + 1].damage(self.destroy)  


class queenie():
    def __init__(self):
        self.damage = 75
        self.dead = 0
        i = np.random.randint(0, n)
        j = np.random.randint(0, m)

        while codepos[i][j] != -1:
            i = np.random.randint(0, n)
            j = np.random.randint(0, m)
        
        self.x = i
        self.y = j
        codepos[i][j] = 14
        colorpos[i][j] = -1
        personclass[i][j] = self

    def change_damage(self, num):
        self.damage = num
    
    def destroy(self):
        self.destroy = 15

    def change_destroy(self):
        self.destroy = self.destroy*2

    def code(self):
        self.code = 14

    def die(self):
        codepos[self.x][self.y] = -1
        colorpos[self.x][self.y] = -1
        personclass[self.x][self.y] = -1
        self.x = -1
        self.y = -1

    def __sub__(self, other):
        return self.damage - other

    def __mul__(self, other):
        return self * other

    def ret_damage(self):
        return self.damage
    
    def multiply(self, x):
        self.damage = self.damage*x
        if self.damage > 75:
            self.damage = 75
        
    def hurt(self, damage):
        self.damage = self.damage - damage
        if self.damage <= 0 and self.dead == 0:
            self.dead = 1
            self.die()

    def move(self, ch):
        global direction
        if self.x == -1 and self.y == -1:
            return
        i = self.x
        j = self.y
        self.p = 0
        personclass[i][j] = -1
        if ch == 'w' or ch == 'W':
            self.p = 1
            if i - 1 >= 0 and codepos[i-1][j] == -1:
                codepos[i][j] = -1
                codepos[i-1][j] = 14
                i = i - 1
                self.x = i
                direction = 1
            else:
                direction = 1
        if ch == 'a' or ch == 'A':
            self.p = 1
            if j-1 >=0 and codepos[i][j-1] == -1:
                codepos[i][j] = -1
                codepos[i][j-1] = 14
                j = j - 1
                self.y = j
                direction = 0
            else:
                direction = 0
        if ch == 's' or ch == 'S':
            self.p = 1
            if i+1 < n and codepos[i+1][j] == -1:
                codepos[i][j] = -1
                codepos[i+1][j] = 14
                i = i + 1
                self.x = i
                direction = 2
            else:
                direction = 2        
        if ch == 'd' or ch == 'D':
            self.p = 1
            if j+1 < m and codepos[i][j+1] == -1:
                codepos[i][j] = -1
                codepos[i][j+1] = 14
                j = j + 1
                self.y = j
                direction = 3
            else:
                direction = 3
        personclass[self.x][self.y] = self
        if self.p == 0:
            return

    def attack(self): 
        global direction
        i = self.x
        j = self.y
        if direction == 0:
            y = j - 10
            x = i - 2
            k = 5
            l = 5
            for p in range(k):
                for q in range(l):
                    if x+p >= 0 and x + p < n and y + q >= 0 and y+q <m and buildingclass[x+p][y+q] != -1:
                        buildingclass[x+p][y+q].damage(self.destroy)
        if direction == 1:
            y = j - 2
            x = i - 10
            k = 5
            l = 5
            for p in range(k):
                for q in range(l):
                    if x+p >= 0 and x + p < n and y + q >= 0 and y+q <m and buildingclass[x+p][y+q] != -1:
                        buildingclass[x+p][y+q].damage(self.destroy)
        if direction == 2:
            y = j - 2
            x = i + 6
            k = 5
            l = 5
            for p in range(k):
                for q in range(l):
                    if x+p >= 0 and x + p < n and y + q >= 0 and y+q <m and buildingclass[x+p][y+q] != -1:
                        buildingclass[x+p][y+q].damage(self.destroy)
        if direction == 3:
            y = j + 6
            x = i - 2
            k = 5
            l = 5
            for p in range(k):
                for q in range(l):
                    if x+p >= 0 and x + p < n and y + q >= 0 and y+q <m and buildingclass[x+p][y+q] != -1:
                        buildingclass[x+p][y+q].damage(self.destroy)
                        

class cannon(building):
    def range(self, damage):
        self.damage_value = damage
    def attack(self):
        if self.deleted == 1:
            return
        for i in range(n):
            for j in range(m):
                if personclass[i][j] != -1 and pow(self.x - i,2)+pow(self.y - j, 2) <= 49 :
                    personclass[i][j].hurt(self.damage_value)
                    return

class wizard_tower(building):
    def range(self, damage):
        self.damage_value = damage
    def attack(self):
        if self.deleted == 1:
            return
        for i in range(n):
            for j in range(m):
                if (personclass[i][j] != -1 or balloonclass[i][j] != -1) and pow(self.x - i,2)+pow(self.y - j, 2) <= 49 :
                    for a in range(-1,2):
                        for b in range(-1,2):
                            if i+a < n and  j+b<m and i+a>=0 and j+b>=0 and balloonclass[i+a][j+b] != -1:
                                balloonclass[i+a][j+b].hurt(self.damage_value)
                            else:
                                if i+a < n and  j+b<m and i+a>=0 and j+b>=0 and personclass[i+a][j+b] != -1:
                                    personclass[i+a][j+b].hurt(self.damage_value)
                    return


def printboard():
    os.system('clear')
    for i in range(n):
        for j in range(m):
            codenm().define(codepos[i][j], colorpos[i][j], balloonclass[i][j])
        print('')



ch1 = int(input("Do you want the murderous king or the evil queen, choose 0 or 1 for them respectively:"))



direction = 0
level = 0

while level < 3:
    for i in range(n):
        for j in range(m):
            codepos[i][j] = -1
            colorpos[i][j] = -1
            buildingclass[i][j] = -1
            personclass[i][j] = -1
            balloonclass[i][j] = -1
    if ch1 == 0:
        queen = king()
        queen.code()
        queen.destroy()
    if ch1 == 1:
        queen = queenie()
        queen.code()
        queen.destroy()
    str = building(50)
    ton = town_hall(str)
    ton.code(0)
    ton.size(4,3)

    for i in range(30):
        wl = wall(str)
        wl.code(2)
        wl.size(1,1)
        
    for i in range(25):
        wl = hut(str)
        wl.code(1)
        wl.size(1,1)
        
    ca1 = cannon(str)
    ca2 = cannon(str)
    ca1.code(3)
    ca2.code(3)
    ca1.size(1,1)
    ca2.size(1,1)
    ca1.range(10)
    ca2.range(15)

    wt1 = wizard_tower(str)
    wt2 = wizard_tower(str)
    wt1.code(13)
    wt2.code(13)
    wt1.size(1,1)
    wt2.size(1,1)
    wt1.range(10)
    wt2.range(15)
    if level >= 1:
        wt3 = wizard_tower(str)
        wt3.code(13)
        wt3.size(1,1)
        ca3 = cannon(str)
        ca3.code(3)
        ca3.size(1,1)

    if level == 2:
        wt4 = wizard_tower(str)
        wt4.code(13)
        wt4.size(1,1)
        ca4 = cannon(str)
        ca4.code(3)
        ca4.size(1,1)

    time  = []
    whatever = []
    something = []
    another = []
    whatever.append(copy.deepcopy(codepos))
    something.append(copy.deepcopy(colorpos))
    another.append(copy.deepcopy(balloonclass))
    time.append(0)
    print("READY TO START")
    printboard()
    get = Get()
    t = 1
    archerlist = []
    balloonlist = []
    barblist = []
    k = 0
    while(1):
        time.append(copy.deepcopy(t))
        for i in archerlist:
            i.move()
        for i in balloonlist:
            i.move()
        print("King's health : ")
        if queen.ret_damage() > 0:
            q = int(queen.ret_damage()/10)
            for i in range(q):
                print(Back.GREEN + " ", end ='')
            
        print()
        ch = input_to(get, timeout=t)
        a = ch
        if a != " " and a != "x" and a != "y" and a != "z" and a != "X" and a != "Y" and a != "Z" and a != "h" and a != "H" and a != "r" and a != "R" and a != "j" and a != "k" and a != "l" and a != "b" and a != "J" and a != "K" and a != "L" and a != "B" and a != "n" and a != "N" and a != "m" and a != "M":
            queen.move(a)

        elif a == " ":
            queen.attack()

        for i in barblist:
            i.move()
        for i in archerlist:
            i.move()
        for i in balloonlist:
            i.move()


        if(a == "x" or a == "X"):
            if len(barblist) < 6:
                barb = barbarian(0,0)
                barblist.append(barb)

        if(a == "j" or a == "J"):
            if len(archerlist) < 6:
                arch = archer(0,0)
                archerlist.append(arch)

        if(a == "k" or a == "K"):
            if len(archerlist) < 6:
                arch = archer(0,m-1)
                archerlist.append(arch)

        if(a == "l" or a == "L"):
            if len(archerlist) < 6:
                arch = archer(n-1,0)
                archerlist.append(arch)
        
        if(a == "y" or a == "Y"):
            if len(barblist) < 6:
                barb = barbarian(0,m-1)
                barblist.append(barb)

        if(a == "z" or a == "Z"):
            if len(barblist) < 6:
                barb = barbarian(n-1,0)
                barblist.append(barb)
    
        if(a == "h" or a == "H"):
            healspell.heal()
        
        if(a == "r" or a == "R"):
            ragespell.rage()
            t = t/2

        if(a == "b" or a == "B"):
            if len(balloonlist) < 3:
                ball = balloon(0,0)
                balloonlist.append(ball)

        if(a == "N" or a == "n"):
            if len(balloonlist) < 3:
                ball = balloon(0,m-1)
                balloonlist.append(ball)

        if(a == "m" or a == "M"):
            if len(balloonlist) < 3:
                ball = balloon(n-1,0)
                balloonlist.append(ball)

        ca1.attack()
        ca2.attack()
        wt1.attack()
        wt2.attack()
        c = 0
        d = 0
        whatever.append(copy.deepcopy(codepos))
        something.append(copy.deepcopy(colorpos))
        another.append(copy.deepcopy(balloonclass))
        printboard()

        for i in range(n):
            for j in range(m):
                if buildingclass[i][j] != -1 and codepos[i][j] != 2:
                    c = 1

        for i in range(n):
            for j in range(m):
                if personclass[i][j] != -1:
                    d = 1
                if balloonclass[i][j] != -1:
                    d = 1

        if c == 0:
            print("YOU WIN")
            k = 1
            print("Name the file in which you want to save the replay of this level : ")
            x = input()
            f = open("replays/" + x + ".txt", "wb")
            pickle.dump(whatever, f)
            pickle.dump(something, f)
            pickle.dump(another, f)
            pickle.dump(time, f)
            f.close()
            level = level + 1
            break

        if d == 0:
            print("YOU LOSE")
            print("Name the file in which you want to save the replay this level : ")
            x = input()
            f = open("replays/" + x + ".txt", "wb")
            pickle.dump(whatever, f)
            pickle.dump(something, f)
            pickle.dump(another, f)
            pickle.dump(time, f)
            f.close()
            level = level + 1
            break

