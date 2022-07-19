##=============================================================================
##  Code Written by ~KK~
##  To Automate the boring process of renaming files for your movie library
##  Useful for organising bulk media files or frequent updation of
##  your XBMC library (Like Kodi, Plex and OSMC)
##=============================================================================
import os
import re
import msvcrt

def Title():
    os.system('mode con: cols=75 lines=30')
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

def FormatStr(temp):
            if ".1080p" in temp:
                sep = ".1080p"
            elif ".720p" in temp:
                sep = ".720p"
            elif "[" in temp:
                sep = "["
            elif "1080p" in temp:
                sep = "1080p"
            elif "720p" in temp:
                sep = "720p"
            if "TamilRockers" in temp:
                temp = temp.split(' - ',1)[1]
            try:
                rest = temp.split(sep,1)[0]
            except:
                pass
            rest = rest.replace("."," ")
            rest = rest.replace("(","")
            rest = rest.replace(")","")
            return(rest)

def Find(string):
    # findall() has been used
    # with valid conditions for urls in string
    url = re.findall('www.(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
    return url

#Driver Code
os.system("cls")
Title()
try:
    os.mkdir("Input")
    os.mkdir("Output")
except FileExistsError:
    pass
path = 'Input'
i=0
ErrorFlag=0
FileFlag=0
files = os.listdir(path)
for file in files:
    temp = file
    extn = file[(len(file)-4) : len(file)]

    if(file.endswith(".mp4") or file.endswith(".mkv")) :
###############################################################################
##MOVIE TITLE RETRIEVE
        rest = FormatStr(temp)
        year_str =  '('+ rest[len(rest)-4 : len(rest)] +')'
        rest = rest[0:len(rest)-4]
        Final = rest + year_str + extn
###############################################################################
##RENAME HAPPENS HERE
        path_new = os.getcwd() + "\Output\\" + rest + year_str
        try:
            os.mkdir("Output")
        except FileExistsError:
            pass
        try:
            os.mkdir(path_new)
        except FileExistsError:
            pass
        try:
            os.rename(os.path.join(path, file), os.path.join(path_new, Final ))
        except:
            print("Error - File Already Exist: "+rest + year_str)
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
    if(i>0): os.system("explorer.exe " + str(os.getcwd() + "\Output\\"))
else:
    print("No Media File Found in Input Folder")
print("Enter any key to exit...")
print()
msvcrt.getch()
