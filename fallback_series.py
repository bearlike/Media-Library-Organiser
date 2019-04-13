#!/usr/bin/env python3
##=============================================================================
##  Code Written by ~KK~
##  Runs Both RENAME-MOVIES and RENAME-SERIES
##  Useful for organising bulk media files or frequent updation of
##  your XBMC library (Like Kodi, Plex and OSMC)
##=============================================================================
import os
import re
Debug = False

def Title():
    os.system('mode con: cols=50 lines=30')
    print("    _       _                  _          _  ")
    print("   /_\ _  _| |_ ___ _ __  __ _| |_ ___ __| | ")
    print("  / _ \ || |  _/ _ \ '  \/ _` |  _/ -_) _` | ")
    print(" /_/ \_\_,_|\__\___/_|_|_\__,_|\__\___\__,_| ")
    print("                                             ")
    print("  _    _ _                       ")
    print(" | |  (_) |__ _ _ __ _ _ _ _  _  ")
    print(" | |__| | '_ \ '_/ _` | '_| || | ")
    print(" |____|_|_.__/_| \__,_|_|  \_, | ")
    print("                           |__/  ")
    print("   ___                     _             ")
    print("  / _ \ _ _ __ _ __ _ _ _ (_)___ ___ _ _ ")
    print(" | (_) | '_/ _` / _` | ' \| (_-</ -_) '_|")
    print("  \___/|_| \__, \__,_|_||_|_/__/\___|_|  ")
    print("           |___/                         ")
    print("")

def AddZero(inputString):
    if(int(inputString) <10):
        return str('0' + str(int(inputString)))
    return(inputString)

def main():
    resultv = [[("-")]*2]
    results = [[("-")]*2]
    folder = os.getcwd()
    sname = str(input("Enter the name of the TV Show: "))
    season = int(input("Enter the Season Number of the TV Show: "))
    i = int(input("Enter the Episode Number to start from: "))
    i1 = i
    cwd = os.getcwd() + "\\"
    mainp = str(cwd + "Output\\Series\\" + sname)
    mainp1 = str(cwd + "Output\\Series\\" + sname +"\\Season "+ str(int(season)))
    dirall = os.listdir(folder)
    dirall.sort()

    for f in dirall:
        if (f.endswith(".mp4") or f.endswith(".mkv")):
            extn = f[(len(f)-4) : len(f)]
            episode = AddZero(str(i))
            i = i + 1
            Final = "S"+AddZero(season)+"E"+episode+extn
            resultv.append(((cwd + str(f)) , str(mainp1 + '\\' + Final)))

        elif(f.endswith(".srt") or f.endswith(".sub") or f.endswith(".idx")):
            extn = f[(len(f)-4) : len(f)]
            episode = AddZero(str(i1))
            i1 = i1 + 1
            Final = "S"+AddZero(season)+"E"+episode+extn
            results.append(((cwd + str(f)) , str(mainp1 + '\\' + Final)))

    if Debug==True:
        for (f, n) in resultv:
            if(f!="-") and (n!="-"):
                print(f," -> ",n)
                print()
        for (f, n) in results:
            if(f!="-") and (n!="-"):
                print(f," -> ",n)
                print()
    else:
        try:
            os.mkdir(str(os.getcwd())+"\\Output")
        except FileExistsError:
            pass
        try:
            os.mkdir(str(os.getcwd())+"\\Output\\Series")
        except FileExistsError:
            pass
        try:
            os.mkdir(mainp)
        except FileExistsError:
            pass
        try:
            os.mkdir(mainp1)
        except FileExistsError:
            pass
        for (f, n) in resultv:
            if(f!="-") and (n!="-"):
                os.rename(f,n)
        for (f, n) in results:
            if(f!="-") and (n!="-"):
                os.rename(f,n)


if __name__ == '__main__':
    Title()
    main()
    print("Process Complete!")
