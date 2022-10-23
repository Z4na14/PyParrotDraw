# encoding=utf-8
import os, platform, sys
from glob import glob
from time import sleep

try:
    arg = str(sys.argv[1])
except:
    arg = None

frames = []
colores = ['0;31;40', '0;32;40', '0;33;40', '0;34;40', '0;35;40', '0;36;40', '0;37;40', ]
color = 0


def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


for b in glob('./frames/*.txt'):
    frames.append(b)

while True:
    for a in range(len(frames)):
        clear()
        frame = open("{frame}".format(frame=frames[a]), 'r')
        if arg == 'color':
            if color >= 7:
                color = 0

            print(f'\x1b[{colores[color]}m' + frame.read() + '\x1b[0m')

        elif arg == None:
            print(frame.read())

        frame.close()
        color += 1
        sleep(0.07)
