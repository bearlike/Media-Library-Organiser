##=============================================================================
##  Code Written by ~KK~
##  Runs Both RENAME-MOVIES and RENAME-SERIES
##  Useful for organising bulk media files or frequent updation of
##  your XBMC library (Like Kodi, Plex and OSMC)
##=============================================================================
import os
import msvcrt
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


while(1==1):
    os.system("cls")
    Title()
    print("")
    print(" Menu")
    print("=======")
    print("1. Rename and Organise Movies")
    print("2. Rename and Organise TV Shows")
    print("3. Exit Program")
    print("")
    print("Enter you Choice: ",end='')
    ch=int(input())
    if ch==1:
        os.system("py RENAME-Movies.py")
    elif ch==2:
        os.system("py RENAME-Series.py")
    elif ch==3:
        print("Press any key to exit... ")
        msvcrt.getch()
        exit()
    else:
        print("Invalid Choice ")
        print("Press any key to continue... ")
        msvcrt.getch()
