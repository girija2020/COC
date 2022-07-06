from src.barbarians import personclass
from src.village import n,m

class healspell():
    def heal():
        for i in range(n):
            for j in range(m):
                if personclass[i][j] != -1:
                    personclass[i][j].multiply(1.5)

class ragespell():
    def rage():
        for i in range(n):
            for j in range(m):
                if personclass[i][j] != -1:
                    personclass[i][j].change_destroy()
                