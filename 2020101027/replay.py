import pickle
from src.village import n,m
import os
import time
from colorama import Fore, Back, Style, init

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


x = input("Enter the file name you want to replay : ")
f = open("replays/" + x + ".txt", "rb")
codepos = pickle.load(f)
colorpos = pickle.load(f)
balloonclass = pickle.load(f)
times = pickle.load(f)
f.close()

for i in range(len(codepos)):
    time.sleep(times[i])
    os.system('clear')
    for x in range(n):
        for y in range(m):
            codenm().define(codepos[i][x][y], colorpos[i][x][y], balloonclass[i][x][y])
        print('')
