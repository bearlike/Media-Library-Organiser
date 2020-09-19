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
from imdb import IMDb
from similarity.damerau import Damerau

# Returns most closest Movie name
def find_most_apt(name, movies):
    damerau = Damerau()
    deg = []
    for movie in movies:
        if(name.upper() == movie.upper()):
            return movie
        else:
            deg.append(damerau.distance(name.upper(), movie.upper()))
    if not deg:
        return name
    indd = int(deg.index(min(deg)))
    mostapt = movies[indd]
    return mostapt if mostapt else name

# Find any URLs present in FileName
def replace_URL(string):
    return re.sub('(www.(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\)]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)', '', string, flags=re.IGNORECASE)

# what about str.rindex()?
# https://docs.python.org/3/library/stdtypes.html#str.rindex
def lastIndexOf(str1, toFind):
    index = len(str1)-1
    i = 0
    for ch in str1:
        if(ch == toFind):
            index = i
        i += 1
    return(index)

# Returns a List Movie name and release year using imDB from Old_FileName
# https://www.w3schools.com/python/ref_dictionary_get.asp
def main_imdb(movie_query):
    ia = IMDb()
    s_result = ia.search_movie(movie_query)
    movies = []
    for movie in s_result:
        if(movie.get('kind') == 'movie'):
            movie_title = movie.get('title')
            movie_year = movie.get('year')
            if not movie_year:
                movie_year = "----"
            movies.append(f"{movie_title} ({movie_year})")
    return movies

# Remove illegal characters from file name
def removeIllegal(str):
    return re.sub(r'[\<\>\:\"\/\\\|\?\*]', '', str)

# Print Program Title
def Title():
    os.system("cls")
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
    rest = re.sub(r'1080p.+|720p.+|\.mkv|\.mp4|\.avi|\.wmv|\[.+', '', rest, flags=re.IGNORECASE)
    # remove all unwanted characters
    rest = re.sub(r'[\.\(\)]', ' ', rest).strip()
    # remove all double spaces
    rest = re.sub(r'\s\s+', ' ', rest).strip()
    return rest

# Driver Code
def main(path=None):
    Title()
    input_folder = path or "./Input/Movies"
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
    if not os.path.exists("./Output/Movies"):
        os.makedirs("./Output/Movies")
    ErrorFlag = FileFlag = i = 0
    files = [file for file in os.listdir(input_folder) if file[-4:] in ['.mp4', '.mkv', '.srt']]
    for file in files:
        temp = file
        extn = file[-4:]
        # Title()
        print(f"{i} File(s) Processed....")
        rest = FormatStr(temp)
        rest = re.sub(r'\(?([1][7-9]\d\d|[2][0]\d\d)\)?', r"(\1)", rest)
        Final = rest
        print(f"Derived: {Final}")
        movies = main_imdb(rest)
        rest = find_most_apt(Final, movies) # Sometimes causes error
        rest = removeIllegal(Final)
        Final = rest + extn
        print(f"Most Apt: {Final}\n")
        # Rename from old -> new happens below
        movie_output_path = f"{os.getcwd()}\\Output\\Movies\\{rest}"
        if not os.path.exists(movie_output_path):
            os.makedirs(movie_output_path)
        if not os.path.exists(os.path.join(movie_output_path, Final)):
            shutil.move(os.path.join(input_folder, file),
                        os.path.join(movie_output_path, Final))
        else:
            print(f"Error - File Already Exist: {rest}")
            FileFlag = 1
            ErrorFlag = 1
            i -= 1
        i += 1
    ### Result Generation ###
    # Title()
    print("All Files Processed...")
    if(FileFlag == 1):
        print("Solution: Try again after removing the above file(s) from Output folder")
    if(i > 0 or ErrorFlag == 1):
        print(f"{i} File(s) Renamed and Organised Successfully")
        # if(i>0): os.system("start " + str(os.getcwd() + "\\Output\\"))
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
    main(path)
    print("Moving files..")
    print("Enter any key to exit...\n")
    msvcrt.getch()
