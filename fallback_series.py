#!/usr/bin/env python3
# =============================================================================
# Code Written by ~KK~
# Runs Both RENAME-MOVIES and RENAME-SERIES
# Useful for organising bulk media files or frequent updation of
# your XBMC library (Like Kodi, Plex and OSMC)
# =============================================================================
import os
import shutil
import re
import argparse


Debug = True


def Title():
    # os.system('mode con: cols=50 lines=30')
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
    return str(inputString).zfill(2)


def main(path=None):
    results_extras = results_video = []
    # If path is specified, it will use that otherwise it will get the current directory
    folder = path or os.getcwd()
    
    sname = input("Enter the name of the TV Show: ")
    season = int(input("Enter the Season Number of the TV Show: "))
    episode_number = int(input("Enter the Episode Number to start from: "))

    output_folder = f"{folder}\\Output\\Series\\{sname}\\Season {season}"
    dir_videos = [file for file in os.listdir(folder) if file[-4:] in ['.mp4', '.mkv', '.avi']]
    dir_videos.sort()
    dir_extras = [file for file in os.listdir(folder) if file[-4:] in ['.srt', '.sub', '.idx']]
    dir_extras.sort()

    def get_new_names(list_of_files, list_to_append_to, episode_number_to_start_at):
        for idx, file in enumerate(list_of_files):
            extn = file[-4:]
            episode = AddZero(idx + episode_number_to_start_at)
            Final = f"S{AddZero(season)}E{episode}{extn}"
            list_to_append_to.append(((f"{folder}\\{file}"), f"{output_folder}\\{Final}"))

    get_new_names(dir_videos, results_video, episode_number)
    get_new_names(dir_extras, results_extras, episode_number)

    if Debug == True:
        for (f, n) in results_video:
            print(f"{f} -> {n}\n")
        for (f, n) in results_extras:
            print(f"{f} -> {n}\n")
    answer = input("\n\nRun the renamer? [yes/no]: ")
    if ("y" in answer.lower()):
        print("Running...\n\n")
        if (os.path.exists(folder+"\\Output\\Series") == False):
            os.makedirs(folder+"\\Output\\Series")
        if (os.path.exists(output_folder) == False):
            os.makedirs(output_folder)
        for (f, n) in results_video:
            if(f != "-") and (n != "-"):
                shutil.move(f, n)
        for (f, n) in results_extras:
            if(f != "-") and (n != "-"):
                shutil.move(f, n)


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

    Title()
    main(path)
    print("Process Complete!")
