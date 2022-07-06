from colorama import Fore, Back, Style, init
import numpy as np

n = 40
m = 80
codepos =  [[-1 for y in range(m)] for x in range(n)]
colorpos =  [[-1 for y in range(m)] for x in range(n)]
buildingclass = [[-1 for y in range(m)] for x in range(n)]
init(autoreset=True)
varaiable = 0

class building:
    def __init__(self, hitpoint):
        self.init_hitpoints = hitpoint
        self.hitpoints = hitpoint
        self.deleted = 0

    def return_hitpoints(self):
        return self.hitpoints

    def change_hitpoints(self, hitpoints):
        self.hitpoints = hitpoints

    def code(self, code):
        self.code = code

    def size(self,x,y):
        self.xsize = x
        self.ysize = y
        i = 0
        j = 0
        self.x = np.random.randint(0,n - x)
        self.y = np.random.randint(0,m - y)
        while i >= self.x and i <= self.x+self.xsize:
            while j >= self.y and j <= self.y+self.ysize:
                if codepos[i][j] != -1 or (i == 0 and j == 0) or (j == 0 and i == n-1) or (i == 0 and j == m-1):
                    self.x = np.random.randint(0,n - x)
                    self.y = np.random.randint(0,m - y)
                    i = -1
                    j = -1
                j = j + 1
            
            i = i + 1

        for i in range(self.x, self.x+self.xsize):
            for j in range(self.y, self.y+self.ysize):  
                codepos[i][j] = self.code
                colorpos[i][j] = 0
                buildingclass[i][j] = self

    def delete(self):
        for i in range(self.x, self.x+self.xsize):
            for j in range(self.y, self.y+self.ysize):
                codepos[i][j] = -1
                colorpos[i][j] = -1
                buildingclass[i][j] = -1
        
    def __sub__(self, other):
        return self.hitpoints - other

    def __mul__(self, other):
        return self.init_hitpoints * other

    def damage(self, damage):
        self.hitpoints = self.hitpoints - damage
        if self.hitpoints < self.init_hitpoints*0.5 and self.hitpoints >= self.init_hitpoints*0.2:
            for i in range(self.x, self.x+self.xsize):
                for j in range(self.y, self.y+self.ysize):   
                    colorpos[i][j] = 1
        if self.hitpoints < self.init_hitpoints*0.2 and self.hitpoints > 0:
            for i in range(self.x, self.x+self.xsize):
                for j in range(self.y, self.y+self.ysize):   
                    colorpos[i][j] = 2
        if self.hitpoints <= 0 and self.deleted == 0:
            self.deleted = 1
            self.delete()

class wall(building):
    pass


class town_hall(building):
    pass


class hut(building):
    pass





# for i in range(n):
#     for j in range(m):
#         code().define(codepos[i][j], colorpos[i][j])
#     print('')

# ton.damage(12)
# print("Hi")

# for i in range(n):
#     for j in range(m):
#         code().define(codepos[i][j], colorpos[i][j])
#     print('')


# i = int(input(i))
# j = int(input(j))
# buildingclass[i][j].damage(50)

# for i in range(n):
#     for j in range(m):
#         code().define(codepos[i][j], colorpos[i][j])
#     print('')
