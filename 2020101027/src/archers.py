from turtle import color
import numpy as np
from src.village import codepos,n,m,buildingclass,building,town_hall,wall,colorpos
from src.barbarians import personclass

class archer():
    def __init__(self,x,y):
        self.strength = 5
        self.health = 50
        self.damage = 50
        self.deleted = 0

        self.x = x
        self.y = y
        i = x
        j = y
        codepos[i][j] = 11
        colorpos[i][j] = 0
        personclass[i][j] = self

    def __sub__(self, other):
        return self.damage - other

    def __mul__(self, other):
        return self * other

    def multiply(self, x):
        self.damage = self.damage*x
        if self.damage > 100:
            self.damage = 100
        self.color()

    def find_nearest(self, x, y):
        list1 = []
        list2 = []
        c = 0
        for i in range(n):
            for j in range(m):
                if buildingclass[i][j] != -1 and codepos[i][j] != 2:
                    list1.append(pow(i-x,2)+pow(j-y,2))
                    list2.append((i,j))
                    c = 1
        if c == 0:
            return -1,-1
        result = np.where(list1 == np.amin(list1))
        i,j = list2[int(result[0][0])][0],list2[int(result[0][0])][1]
        a  = 1
        l = []
        mp = []
        mp.append((x+1,y))
        mp.append((x-1,y))
        mp.append((x+1,y+1))
        mp.append((x-1,y-1))
        mp.append((x,y+1))
        mp.append((x,y-1))
        mp.append((x+1,y-1))
        mp.append((x-1,y+1))
        l.append(pow(i-a-x,2) + pow(j-y,2))
        l.append(pow(i+a-x,2)+pow(j-y,2))
        l.append(pow(i-a-x,2)+pow(j-a-y,2))
        l.append(pow(i+a-x,2)+pow(j+a-y,2))
        l.append(pow(i-x,2)+pow(j-a-y,2))
        l.append(pow(i-x,2)+pow(j+a-y,2))
        l.append(pow(i-a-x,2)+pow(j+a-y,2))
        l.append(pow(i+a-x,2)+pow(j-a-y,2))

        result2 = np.where(l == np.amin(l))
        x,y = mp[int(result2[0])][0],mp[int(result2[0])][1]

        return x,y
    
    def change_strength(self,power):
        self.strength = power

    def ret_damage(self):
        return self.damage

    def change_destroy(self):
        self.strength = self.strength*2

    def move(self):
        if self.x == -1 and self.y == -1:
            return
        i,j = self.find_nearest(self.x,self.y)
        if i == -1 and j == -1:
            return
        list1 = []
        list2 = []
        for p in range(n):
            for q in range(m):
                if buildingclass[p][q] != -1 and codepos[p][q] != 2:
                    list1.append(pow(p-self.x,2)+pow(q-self.y,2))
                    list2.append((p,q))

        result = np.where(list1 == np.amin(list1))
        p,q = list2[int(result[0][0])][0],list2[int(result[0][0])][1]
        if pow(self.x - p,2)+pow(self.y - q, 2) <= 64 :
            buildingclass[p][q].damage(self.strength)
            return
        if codepos[i][j] == -1:
            codepos[self.x][self.y] = -1
            personclass[self.x][self.y] = -1
            y = colorpos[self.x][self.y]
            colorpos[self.x][self.y] = 0
            self.x = i
            self.y = j
            codepos[self.x][self.y] = 11
            colorpos[self.x][self.y] = y
            personclass[self.x][self.y] = self
        if codepos[i][j] != -1 and buildingclass[i][j] != -1:
            buildingclass[i][j].damage(self.strength)
        if codepos[i][j] != -1 and buildingclass[i][j] == -1:
            return

    def delete(self):
        codepos[self.x][self.y] = -1
        colorpos[self.x][self.y] = 0
        personclass[self.x][self.y] = -1
        self.x = -1
        self.y = -1

    def hurt(self, damage):
        self.damage = self.damage - damage
        self.color()
    
    def color(self):
        i = self.x
        j = self.y
        if self.damage < self.health*0.5 and self.damage >= self.health*0.2:         
            colorpos[i][j] = 1
        if self.damage < self.health*0.2 and self.damage > 0:
            colorpos[i][j] = 2
        if self.damage <= 0 and self.deleted == 0:
            self.deleted = 1
            self.delete()

    def change_damage(self, num):
        self.damage = num