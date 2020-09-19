# =============================================================================
# Code Written by ~KK~
# To Automate the boring process of renaming files for your movie library
# Useful for organising bulk media files or frequent updation of
# your XBMC library (Like Kodi, Plex and OSMC)
# =============================================================================
import os
import re
import msvcrt
import shutil
import argparse
import sys
# from imdb import IMDb
# from similarity.damerau import Damerau


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


# changes '.' to ' ', and cleans up and double spacing
def cleanup_filename(name):
    name = re.sub(r'[\.]', ' ', name)
    name = re.sub(r'\s\+', ' ', name)
    return name

# Remove illegal characters from file name


def removeIllegal(str):
    return re.sub(r'[\<\>\:\"\/\\\|\?\*]', '', str)

# has Condition #1


def hasX(inputString):
    search = re.search(r'(\d{1,2}\s?x\s?\d{1,2})',
                       inputString, flags=re.IGNORECASE)
    return search.group(1) if search else False

# has Condition #2


def hasSE(inputString):
    search = re.search(r'(S\d{1,3}E\d{1,3})', inputString, flags=re.IGNORECASE)
    return search.group(1) if search else False

# has Condition #3


def hasSEP(inputString):
    search = re.search(r'(S\d{1,3}E\d{0,3}?P\d{1,3})',
                       inputString, flags=re.IGNORECASE)
    return search.group(1) if search else False


def FindName(inputString):
    search = re.search(r'^(.+?)([-\(\[\<\>\/\+\{\}0-9]|(S\d))', inputString)
    return re.sub(r'\.', ' ', search.group(1)).strip() if search else ""


def FindDet(inputString):
    inputString = inputString.replace(' x ', 'x', 1)
    filteredList = filter(None, re.split(r'(\dx\d{1,2})', inputString))
    i = 0
    for element in filteredList:
        Det = re.sub(r'[\.\-]', ' ', element).strip()
        if(i == 1):
            return Det
        i += 1


def FindSeason(inputString):
    return FindDet(inputString).split('x')[0]


def FindEpisode(inputString):
    return FindDet(inputString).split('x')[1]


def AddZero(inputString):
    return str(inputString).zfill(2)


def split_line(text):
    return text.split()


# Before Driver
def init(path=None):
    Title()
    if not os.path.exists(".\\Input\\Series"):
        os.makedirs(".\\Input\\Series")
    main(path)


# Driver Code
def main(path=None):
    if path == None:
        cwd = os.getcwd()
        path = cwd + "\\Input\\Series\\"
        case = 1
    else:
        cwd = re.sub(r'\\$', '', path)
        # print(path)
        case = 2
    path_new = path_new_1 = rest = Final = None
    NAME = Copy = ""
    ErrorFlag = FileFlag = i = 0
    print("Reading Files....")
    # main loop
    for (dirpath, dirnames, filenames) in os.walk(path):
        files = os.listdir(dirpath)
        for file in files:
            CheckFlag = 0
            temp = file
            extn = file[-4:]
            """Logic Starts here"""
            # All possible media extensions go here
            media_extensions = [
                ".mp4",
                ".mkv",
                ".srt",
                ".avi",
                ".wmv"
            ]
            if (extn in media_extensions):
                # Title()
                print(f"{i} File(s) Processed....")
                # rest = temp.split(extn, 1)[0]

                '''
                re.sub() that finds the first bit of extra crap and removes everything after it, because usually more crap follows it
                input -> 'Ratched.S1E1.720p.NF.WEBRip.x264-GalaxyTV.mkv'
                output -> 'Ratched.S1E1'
                '''
                rest = re.sub(
                    r'1080p.+|720p.+|HDTV.+|x264.+|x265.+|AAC.+|E-Subs.+|WEBrip.+|WEB.+|BluRay.+|\.mp4|\.mkv|\.srt|\.avi|\.wmv', '', rest, flags=re.IGNORECASE)
                rest = cleanup_filename(rest)
                # Specifically written for'x' type Files
                if hasX(file):
                    CheckFlag = 1
                    NAME = FindName(rest)
                    print(f"rest: {rest} -> NAME: {NAME}")
                    search = re.search(
                        r'(\d{1,2})\s?x\s?(\d{1,2})', file, flags=re.IGNORECASE)
                    SEASON = AddZero(search.group(1))
                    SEASON_NUM = AddZero(search.group(1)) if search else ""
                    EPISODE = AddZero(search.group(2))
                    Final = f"S{SEASON}E{EPISODE}{extn}"

                # Specifically written for 'S__E__' type Files
                elif hasSE(file):
                    Restore = NAME = ""
                    # words = split_line(rest)
                    # for word in words:
                    #     if(hasSE(word)):
                    #         Final = word
                    #         break
                    #     if(hasSEP(word)):
                    #         Final = word
                    #         break
                    #     else:
                    #         NAME = NAME + word + " "
                    # brackets_ = re.findall('[(]+(.*?)[)]', NAME)
                    # # print(brackets_)
                    # for yy in brackets_:
                    #     try:
                    #         NAME = NAME.replace(yy, "")
                    #     except:
                    #         pass
                    # if(NAME != Copy):
                    #     Copy = NAME
                    #     # series = main_imdb(NAME)
                    #     series = ''
                    #     # NAME = find_most_apt(NAME, series)
                    #     NAME = removeIllegal(NAME)
                    #     NAME = NAME.strip()
                    #     Restore = NAME
                    # else:
                    #     NAME = Restore
                    NAME = FindName(file)
                    SEASON = hasSEP(file) or hasSE(file)
                    search = re.search(
                        r'S(\d{1,2})E\d{1,2}', SEASON, re.IGNORECASE)
                    SEASON_NUM = AddZero(search.group(1)) if search else "??"
                    Final = SEASON + extn
                    CheckFlag = 1

            if CheckFlag == 1:
                if case == 1:
                    print(NAME)
                    path_new = f'{cwd}\\Output\\Series\\{NAME}'
                    path_new_1 = f'{cwd}\\Output\\Series\\{NAME}\\Season {SEASON_NUM}'
                elif case == 2:
                    path_new = f'{cwd}\\{NAME}'
                    path_new_1 = f'{cwd}\\{NAME}\\Season {SEASON_NUM}'

            """Naming Logic Ends here"""
            # For Testing
            def TEST():
                print("\n\n")
                print("NAME: " + NAME)
                print("SEASON: " + SEASON)
                print("EPISODE: " + EPISODE)
                print("EXTN: " + extn)
                # print("TEMP: " + temp)
                print("REST: " + rest)
                print("Final: " + Final)
                print("PATH: " + path_new)
                print("\n\n")
            # TEST()    # Test Call
            if CheckFlag == 1:
                if case == 1:
                    if not os.path.exists(cwd+"\\Output\\Series"):
                        os.makedirs(cwd+"\\Output\\Series")
                if not os.path.exists(path_new_1):
                    os.makedirs(path_new_1)
                if not os.path.exists(os.path.join(path_new_1, Final)):
                    # https://www.codespeedy.com/difference-between-os-rename-and-shutil-move-in-python/
                    print("src: ", os.path.join(dirpath, file))
                    print("wtf: ", path_new_1)
                    print("dst: ", os.path.join(path_new_1, Final))
                    shutil.move(os.path.join(dirpath, file),
                                os.path.join(path_new_1, Final))
                else:
                    print(
                        f"Error - File Already Exist: \\{NAME}\\Season {SEASON}\\{Final}")
                    FileFlag = 1
                    ErrorFlag = 1
                    i -= 1
                i += 1
        """Result Generation"""
        Title()
        print("All Files Processed...")
        if(FileFlag == 1):
            print(
                "Solution: Try again after removing the above file(s) from Output folder")
        if(i > 0 or ErrorFlag == 1):
            print(f"{i} File(s) Renamed and Organised Successfully")
            # os.system(f"start {os.getcwd() + '\Output\\'}')
        else:
            print("No Media File Found in Input Folder")


if __name__ == '__main__':
    path = None

    parser = argparse.ArgumentParser(description='''To Automate the boring process of renaming files for your TV Shows library
    Useful for organising bulk media files or frequent updation of
    your XBMC library (Like Kodi, Plex and OSMC)''')

    # default=os.getcwd()
    # Add in if you want
    parser.add_argument('-p', '--path', type=str,
                        help='To orgainise TV Shows in the specified directory')

    args = parser.parse_args()
    if (args.path):
        if (os.path.exists(args.path)):
            path = args.path
        else:
            print(
                f"\n\nERROR: '{args.path}' is not a valid path\n\n\nPlease try again!\n")
            exit()
    init(path)
    print("Moving files...")
    print("Enter any key to exit...\n")
    msvcrt.getch()
