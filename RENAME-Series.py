##=============================================================================
##  Code Written by ~KK~
##  To Automate the boring process of renaming files for your TV Shows library
##  Useful for organising bulk media files or frequent updation of
##  your XBMC library (Like Kodi, Plex and OSMC)
##=============================================================================
import os
import msvcrt
import re
def Title():
    os.system('mode con: cols=90 lines=30')
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


def hasX(inputString):
    return bool(re.search(r'\dx\d', inputString) or re.search(r'\d x \d', inputString))

def hasSE(inputString):
    return bool(re.search(r'S\d\dE\d\d', inputString) or re.search(r'S\dE\d\d', inputString))

def FindName(inputString):
    inputString = inputString.replace(' x ', 'x', 1)
    filteredList = filter(None, re.split(r'(\dx\d)', inputString))
    for element in filteredList:
        Name = element
        Name = Name.replace('-',' ')
        Name = Name.replace('.',' ')
        Name = Name.strip()
        return str(Name)

def FindDet(inputString):
    inputString = inputString.replace(' x ', 'x', 1)
    filteredList = filter(None, re.split(r'(\dx\d\d)', inputString))
    i=0
    for element in filteredList:
        Det = element
        Det = Det.replace('.',' ')
        Det = Det.replace('-',' ')
        Det = Det.strip()
        if(i==1):
            return str(Det)
        i=i+1

def FindSeason(inputString):
    Det = FindDet(inputString)
    Season = Det.split('x')[0]
    return str(Season)

def FindEpisode(inputString):
    Det = FindDet(inputString)
    Episode = Det.split('x')[1]
    return str(Episode)

def AddZero(inputString):
    if(int(inputString) <10):
        return str('0' + str(int(inputString)))
    return(inputString)

def split_line(text):
    words = text.split()
    return words
###############################################################################
##MAIN
os.system("cls")
Title()
try:
    os.mkdir(str(os.getcwd())+"\Input")
except:
    pass
path = str(os.getcwd())+"\Input"
path_new = path_new_1 = rest = Final = "NULL"
NAME=""
i=0
ErrorFlag=0
FileFlag=0
files = os.listdir(path)
for file in files:
    CheckFlag=0
    temp = file
    extn = file[(len(file)-4) : len(file)]
###############################################################################
    if (file.endswith(".mp4") or file.endswith(".mkv")):
        rest = temp.split(extn,1)[0]
        if ".1080p" in temp:
            sep = ".1080p"
        elif ".720p" in temp:
            sep = ".720p"
        ##SAFE CASES
        elif "HDTV" in temp:
            sep ="HDTV"
        elif "x264" in temp:
            sep = "x264"
        elif "AAC" in temp:
            sep = "AAC"
        elif "E-Subs" in temp:
            sep = "E-Subs"
        elif "ESubs" in temp:
            sep = "ESubs"
        elif "WEBRip" in temp:
            sep = "WEBRip"
        elif "WEB" in temp:
            sep = "WEB"

        rest = rest.split(sep,1)[0]
        rest = rest.replace("."," ")
    ##Specifically written for'x' type Files
        if hasX(file):
            CheckFlag=1
            NAME = FindName(rest)
            SEASON = FindSeason(rest)
            EPISODE = AddZero(FindEpisode(rest))
            Final = "S"+AddZero(FindSeason(rest))+"E"+EPISODE+extn

    ##Specifically written for 'S__E__' type Files
        elif hasSE(file):
            NAME=""
            words = split_line(rest)
            for word in words:
                if(hasSE(word)):
                    Final = word
                    break
                else:
                    NAME = NAME + word + " "
            NAME=NAME.strip()
            TEMP=Final=Final.strip()
            TEMP=TEMP.replace('S',"")
            SEASON = TEMP.split('E',1)[0]
            EPISODE = TEMP.split('E',1)[1]
            Final = Final + extn
            CheckFlag=1

    if CheckFlag==1:
        path_new = os.getcwd() + "\Output\\" + NAME
        path_new_1 = os.getcwd() + "\Output\\" + NAME +"\\Season "+ str(int(SEASON))

        ###############################################################################
    """
    ##   TESTING
    ## =============
    print (" ")
    print (" ")
    print("NAME: " + NAME)
    print("SEASON: " + SEASON)
    print("EPISODE: " + EPISODE)
    print("EXTN: " + extn)
    ##print("TEMP: " + temp)
    print("REST: " + rest)
    print("Final: " + Final)
    print("PATH: "+ path_new)
    print (" ")
    print (" ")
    ###"""
    if CheckFlag==1:
        try:
            os.mkdir(str(os.getcwd())+"\Output")
        except FileExistsError:
            pass
        try:
            os.mkdir(path_new)
        except FileExistsError:
            pass
        try:
            os.mkdir(path_new_1)
        except FileExistsError:
            pass
        try:
            os.rename(os.path.join(path, file), os.path.join(path_new_1, Final ))
        except FileExistsError:
            print("Error - File Already Exist: \\"+ NAME +"\\Season "+ str(int(SEASON)) + "\\" + Final)
            FileFlag=1
            ErrorFlag=1
            i=i-1;
        i=i+1

###############################################################################
##RESULT GENERATION
print (" ")
if(FileFlag==1):
    print("Solution: Try again after removing the above file(s) from Output folder")
if(i>0 or ErrorFlag==1):
    print(str(i)+" File(s) Renamed and Organised Successfully")
    os.system("explorer.exe " + str(os.getcwd() + "\Output\\"))
else:
    print("No Media File Found in Input Folder")
print("Enter any key to exit...")
print(" ")
msvcrt.getch()
