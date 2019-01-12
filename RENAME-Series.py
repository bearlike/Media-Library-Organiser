##=============================================================================
##  Code Written by ~KK~
##  To Automate the boring process of renaming files for your TV Shows library
##  Useful for organising bulk media files or frequent updation of
##  your XBMC library (Like Kodi, Plex and OSMC)
##=============================================================================
import os
import re
import msvcrt
from imdb import IMDb
from similarity.damerau import Damerau

def Title():
    os.system('mode con: cols=90 lines=30')
    os.system("cls")
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

def find_most_apt(name, series):
    damerau = Damerau()
    deg = []
    for ss in series:
        if(name.upper() == ss.upper()):
            return(ss)
        else:
            deg.append(damerau.distance(name.upper(), ss.upper()))
    indd = int(deg.index(min(deg)))
    mostapt = series[indd]
    return(mostapt)

def main_imdb(str21):
    ia = IMDb()
    s_result = ia.search_movie(str21)
    series = []
    for ss in s_result:
        if(ss['kind'] == "tv series"):
            str2 = ss['title']
            series.append(str2)
    return(series)

def removeIllegal(str):
    str=str.replace('<',"")
    str=str.replace('>',"")
    str=str.replace(':',"")
    str=str.replace('"',"")
    str=str.replace('/',"")
    str=str.replace('\\',"")
    str=str.replace('|',"")
    str=str.replace('?',"")
    str=str.replace('*',"")
    str=str.strip()
    return(str)

def hasX(inputString):
    return bool(re.search(r'\dx\d', inputString) or re.search(r'\d x \d', inputString))

def hasSE(inputString):
    return bool(re.search(r'S\d\dE\d\d', inputString) or re.search(r'S\dE\d\d', inputString) or re.search(r's\d\de\d\d', inputString) or re.search(r's\de\d\d', inputString))

def hasSEP(inputString):
    return bool(re.search(r'S\d\dEP\d\d', inputString) or re.search(r'S\dEP\d\d', inputString) or re.search(r's\d\dep\d\d', inputString) or re.search(r's\dep\d\d', inputString))

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
Title()
try:
    os.mkdir(str(os.getcwd())+"\Input")
except:
    pass
try:
    os.mkdir(str(os.getcwd())+"\\Input\\Series")
except:
    pass
path = str(os.getcwd())+"\\Input\\Series\\"
path_new = path_new_1 = rest = Final = "NULL"
NAME=""
Copy=""
i=0
ErrorFlag=0
FileFlag=0
files = os.listdir(path)
print("Reading Files....")
for file in files:
    CheckFlag=0
    temp = file
    extn = file[(len(file)-4) : len(file)]
###############################################################################
    if (file.endswith(".mp4") or file.endswith(".mkv") or file.endswith(".srt")):
        Title()
        print(str(i)+" File(s) Processed....")
        rest = temp.split(extn,1)[0]
        rest = rest.replace(".1080p","")
        rest = rest.replace(".720p","")
        rest = rest.replace("HDTV","")
        rest = rest.replace("x264","")
        rest = rest.replace("AAC","")
        rest = rest.replace("E-Subs","")
        rest = rest.replace("ESubs","")
        rest = rest.replace("WEBRip","")
        rest = rest.replace("WEB","")
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
                if(hasSEP(word)):
                    Final = word
                    break
                else:
                    NAME = NAME + word + " "
            brackets_ = re.findall('[(]+(.*?)[)]', NAME)
            for yy in brackets_:
                try:
                    NAME=NAME.replace(yy,"")
                except:
                    pass
            if(NAME != Copy):
                Copy = NAME
                series = main_imdb(NAME)
                NAME = find_most_apt(NAME, series)
                NAME = removeIllegal(NAME)
                NAME=NAME.strip()
                Restore = NAME
            else:
                NAME = Restore
            TEMP=Final=Final.strip()
            TEMP=TEMP.replace('S',"")
            SEASON = TEMP.split('E',1)[0]
            EPISODE = TEMP.split('E',1)[1]
            Final = Final + extn
            CheckFlag=1

    if CheckFlag==1:
        path_new = os.getcwd() + "\\Output\\Series\\" + NAME
        path_new_1 = os.getcwd() + "\\Output\\Series\\" + NAME +"\\Season "+ str(int(SEASON))

###############################################################################
    def TEST():
        ##   TESTING
        ## =============
        print ("\n\n")
        print("NAME: " + NAME)
        print("SEASON: " + SEASON)
        print("EPISODE: " + EPISODE)
        print("EXTN: " + extn)
        ##print("TEMP: " + temp)
        print("REST: " + rest)
        print("Final: " + Final)
        print("PATH: "+ path_new)
        print ("\n\n")
    #TEST()
    if CheckFlag==1:
        try:
            os.mkdir(str(os.getcwd())+"\\Output")
        except FileExistsError:
            pass
        try:
            os.mkdir(str(os.getcwd())+"\\Output\\Series")
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
Title()
print ("All Files Processed...")
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
