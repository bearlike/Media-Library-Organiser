"""
  Code Written by ~KK~
  To Automate the boring process of renaming files for your TV Shows library
  Useful for organising bulk media files or frequent updation of
  your XBMC library (Like Kodi, Plex and OSMC)
"""
import os
import re
import msvcrt
import shutil
import getopt
import sys
from imdb import IMDb
from similarity.damerau import Damerau

# Title
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


# Find most apt name in Series List
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


# Retrieves name from imDB
def main_imdb(str21):
    ia = IMDb()
    s_result = ia.search_movie(str21)
    series = []
    for ss in s_result:
        if(ss['kind'] == "tv series"):
            str2 = ss['title']
            series.append(str2)
    return(series)


# Remove illegal characters from file name
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

# has Condition #1
def hasX(inputString):
    return bool(re.search(r'\dx\d', inputString) or re.search(r'\d x \d', inputString))

# has Condition #2
def hasSE(inputString):
    return bool(re.search(r'S\d\dE\d\d', inputString) or re.search(r'S\dE\d\d', inputString) or re.search(r's\d\de\d\d', inputString) or re.search(r's\de\d\d', inputString))

# has Condition #3
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


# Before Driver
def init(path="NULL"):
    Title()
    try:
        os.mkdir(str(os.getcwd())+"\\Input")
    except:
        pass
    try:
        os.mkdir(str(os.getcwd())+"\\Input\\Series")
    except:
        pass
    main(path)


# Driver Code
def main(path="NULL"):
    if path == "NULL":
        cwd = str(os.getcwd())
        path = cwd+"\\Input\\Series\\"
        case = 1
    else:
        cwd = path
        print(path)
        case = 2
    path_new = path_new_1 = rest = Final = "NULL"
    NAME=""
    Copy=""
    i=0
    ErrorFlag=0
    FileFlag=0
    print("Reading Files....")
    # main loop
    for (dirpath, dirnames, filenames) in os.walk(path):
        files = os.listdir(dirpath)
        for file in files:
            CheckFlag=0
            temp = file
            extn = file[(len(file)-4) : len(file)]
            """Logic Starts here"""
            # All possible media extensions go here
            media_extensions = [
                    ".mp4",
                    ".mkv",
                    ".srt",
                    ".avi",
                    ".wmv"
            ]
            if (file.endswith(ex1) for ex1 in media_extensions):
                Title()
                print(str(i)+" File(s) Processed....")
                rest = temp.split(extn,1)[0]
                unwanted_stuff = [
                    ".1080p",
                    ".720p",
                    "HDTV",
                    "x264",
                    "AAC",
                    "E-Subs",
                    "ESubs",
                    "WEBRip",
                    "WEB",
                    "BluRay",
                ]
                for stuff in unwanted_stuff:
                    rest = rest.replace(stuff,"")
                rest = rest.replace(".", " ")
                # Specifically written for'x' type Files
                if hasX(file):
                    CheckFlag=1
                    NAME = FindName(rest)
                    SEASON = FindSeason(rest)
                    EPISODE = AddZero(FindEpisode(rest))
                    Final = "S"+AddZero(FindSeason(rest))+"E"+EPISODE+extn

                # Specifically written for 'S__E__' type Files
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
                    # print(brackets_)
                    for yy in brackets_:
                        try:
                            NAME = NAME.replace(yy,"")
                        except:
                            pass
                    if(NAME != Copy):
                        Copy = NAME
                        series = main_imdb(NAME)
                        NAME = find_most_apt(NAME, series)
                        NAME = removeIllegal(NAME)
                        NAME = NAME.strip()
                        Restore = NAME
                    else:
                        NAME = Restore
                    TEMP=Final=Final.strip()
                    TEMP=TEMP.replace('S',"")
                    SEASON = TEMP.split('E',1)[0]
                    EPISODE = TEMP.split('E',1)[1]
                    Final = Final + extn
                    CheckFlag=1

            if CheckFlag == 1:
                if case == 1:
                    path_new = cwd + "\\Output\\Series\\" + NAME
                    path_new_1 = cwd + "\\Output\\Series\\" + NAME +"\\Season "+ str(int(SEASON))
                elif case == 2:
                    path_new = cwd + "\\" + NAME
                    path_new_1 = cwd + "\\" + NAME +"\\Season "+ str(int(SEASON))


            """Naming Logic Ends here"""
            # For Testing
            def TEST():
                print ("\n\n")
                print("NAME: " + NAME)
                print("SEASON: " + SEASON)
                print("EPISODE: " + EPISODE)
                print("EXTN: " + extn)
                # print("TEMP: " + temp)
                print("REST: " + rest)
                print("Final: " + Final)
                print("PATH: "+ path_new)
                print ("\n\n")
            # TEST()    # Test Call
            if CheckFlag == 1:
                if case == 1:
                    try:
                        os.mkdir(cwd+"\\Output")
                    except FileExistsError:
                        pass
                    try:
                        os.mkdir(cwd+"\\Output\\Series")
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
                    os.rename(os.path.join(dirpath, file), os.path.join(path_new_1, Final ))
                except FileExistsError:
                    print("Error - File Already Exist: \\"+ NAME +"\\Season "+ str(int(SEASON)) + "\\" + Final)
                    FileFlag=1
                    ErrorFlag=1
                    i=i-1;
                i=i+1
        """Result Generation"""
        Title()
        print ("All Files Processed...")
        if(FileFlag==1):
            print("Solution: Try again after removing the above file(s) from Output folder")
        if(i>0 or ErrorFlag==1):
            print(str(i)+" File(s) Renamed and Organised Successfully")
            # os.system("explorer.exe " + str(os.getcwd() + "\Output\\"))
        else:
            print("No Media File Found in Input Folder")


# Prints usage/help
def usageHelp():
    print('\nUsage:\n  RENAME-Series.py [options] <commands (or) path>')
    print("\nGeneral Options:")
    print("  -h \tShow help.")
    print("  -p \tTo orgainise TV Shows in the specified directory\n")
    sys.exit(2)


if __name__ == '__main__':
    path = "NULL"
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'p:h', ["path="])
    except getopt.GetoptError:
        usageHelp()
    for opt, arg in opts:
        if opt in ("-p", "--path"):
            path = arg
        elif opt == '-h':
            usageHelp()
    init(path)
    print("Moving files..")
    print("Enter any key to exit...")
    print()
    msvcrt.getch()
