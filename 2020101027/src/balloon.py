from turtle import color
import numpy as np
from src.village import codepos,n,m,buildingclass,colorpos

balloonclass = [[-1 for y in range(m)] for x in range(n)]

class balloon():
    def __init__(self,x,y):
        self.strength = 20
        self.health = 100
        self.damage = 100
        self.deleted = 0

        self.x = x
        self.y = y
        i = x
        j = y
        balloonclass[i][j] = self

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
                    if codepos[i][j] == 3 or codepos[i][j] == 13:
                        if i-self.x == 0 and j - self.y == 0:
                            return i,j,0
                        l = []
                        a = 1
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

                        return x,y,1

        if c == 0:
            return -1,-1,0
        result = np.where(list1 == np.amin(list1))
        i,j = list2[int(result[0][0])][0],list2[int(result[0][0])][1]
        a  = 1
        l = []
        mp = []
        if i-self.x == 0 and j-self.y == 0:
            return i,j,0
        
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
        return x,y,1
    
    def change_strength(self,power):
        self.strength = power

    def ret_damage(self):
        return self.damage

    def change_destroy(self):
        self.strength = self.strength*2

    def move(self):
        if self.x == -1 and self.y == -1:
            return
        i,j,k = self.find_nearest(self.x,self.y)
        if i == -1 and j == -1:
            return
        if balloonclass[i][j] != -1 and k == 1:
            return
        if codepos[i][j] == -1:
            balloonclass[self.x][self.y] = -1
            self.x = i
            self.y = j
            balloonclass[self.x][self.y] = self
        if codepos[i][j] != -1 and buildingclass[i][j] != -1 and k == 1:
            balloonclass[self.x][self.y] = -1
            self.x = i
            self.y = j
            balloonclass[self.x][self.y] = self
        if codepos[i][j] != -1 and buildingclass[i][j] != -1 and k == 0:
            balloonclass[self.x][self.y] = -1
            self.x = i
            self.y = j
            balloonclass[self.x][self.y] = self
            buildingclass[i][j].damage(self.strength)
        if codepos[i][j] != -1 and buildingclass[i][j] == -1:
            balloonclass[self.x][self.y] = -1
            self.x = i
            self.y = j
            balloonclass[self.x][self.y] = self
            return

    def delete(self):
        balloonclass[self.x][self.y] = -1
        self.x = -1
        self.y = -1

    def hurt(self, damage):
        self.damage = self.damage - damage
        self.color()

    def change_damage(self, num):
        self.damage = num

    def color(self):
        i = self.x
        j = self.y
        if self.damage <= 0 and self.deleted == 0:
            self.deleted = 1
            self.delete()