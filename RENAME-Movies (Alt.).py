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
    print("           |___/                         \n\n")


# Primitive FileName Formatting
def FormatStr(temp):
    rest = replace_URL(temp)
    rest = re.sub(r'^([^\w]+)', '', rest)
    # remove all extra info in filename
    rest = re.sub(
        r'1080p.+|720p.+|\.mkv|\.mp4|\.avi|\.wmv|\[.+', '', rest, flags=re.IGNORECASE)
    # remove all unwanted characters
    rest = re.sub(r'[\.\(\)]', ' ', rest).strip()
    # remove all double spaces
    rest = re.sub(r'\s\s+', ' ', rest).strip()
    return rest


# Find any URLs present in FileName
def replace_URL(string):
    return re.sub('(www.(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\)]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)', '', string, flags=re.IGNORECASE)


def main(path=None):
    # Driver Code
    os.system("cls")
    Title()
    input_folder = path or "./Input"
    if not os.path.exists(input_folder):
        os.mkdir(input_folder)
    if not os.path.exists("./Output"):
        os.mkdir("Output")
    input_folder = './Input'
    i = 0
    ErrorFlag = 0
    FileFlag = 0
    files = [file for file in os.listdir(
        input_folder) if file[-4:] in ['.mp4', '.mkv']]
    for file in files:
        extn = file[-4:]
        ###############################################################################
        # MOVIE TITLE RETRIEVE
        rest = FormatStr(file)

        '''
        Puts parenthesis around the year
        Input -> '12 Years a Slave 2013'
        Output -> '12 Years a Slave (2013)'
        '''
        rest = re.sub(r'\(?([1][7-9]\d\d|[2][0]\d\d)\)?', r"(\1)", rest)
        Final = f"{rest}{extn}"
        ###############################################################################
        # RENAME HAPPENS HERE
        path_new = os.getcwd() + "\\Output\\" + rest
        if not os.path.exists(path_new):
            os.makedirs(path_new)
        if not os.path.exists(os.path.join(path_new, Final)):
            shutil.move(os.path.join(path, file),
                        os.path.join(path_new, Final))
        else:
            print(f"Error - File Already Exist: {rest}")
            FileFlag = 1
            ErrorFlag = 1
            i -= 1
        i += 1

    ###############################################################################
    # RESULT GENERATION
    if(FileFlag == 1):
        print("Solution: Try again after removing the above file(s) from Output folder")
    if(i > 0 or ErrorFlag == 1):
        print(f"{i} File(s) Renamed and Organised Successfully")
        if(i > 0):
            os.system("start " + os.getcwd() + "\\Output\\")
    else:
        print("No Media File Found in Input Folder")
    print("\n\n\nEnter any key to exit...\n")
    msvcrt.getch()


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
    main(path)
