# Media Library Organiser
[![Language](https://img.shields.io/badge/language-python-blue.svg?style=flat)](https://www.python.org)
[![Release](https://img.shields.io/badge/release-v1.3.0--a1-orange.svg?style=flat)](https://github.com/KrishnaAlagiri/Media-Library-Organiser/releases/tag/v1.3-a1)
[![No-GUI](https://img.shields.io/badge/No--GUI-yellowgreen.svg)](#media-library-organiser)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/KrishnaAlagiri/Media-Library-Organiser/blob/master/LICENSE.md)


## About
A (simple) program that'll automatically bulk rename and organise your **Movie and TV-Shows Library** (ideal for maintaining your *xbmc* library). Movies and TV Shows are easily organized by your xbmc if they're given the right name.
#### Why do I do it?
This boosts my frequently updated massive media library organised almost instantly.
#### What's New !
* `[UPDATE]` Uses **imDB** to retrieve the most relevent movie and series names.
######
* **To view the entire Update log** - [log-update.md](https://github.com/KrishnaAlagiri/Media-Library-Organiser/blob/master/log-update.md)
* **To view the features that are to be added on the next version** - [current-working.md](https://github.com/KrishnaAlagiri/Media-Library-Organiser/blob/master/current-working.md)


## Getting Started
### Prerequisites
What things you need to run the program:
- Python Compiler (3.7 Recommended)
- Install the following Packages from pypi by using the following commands:
  - **strsim**
    ```bash
    pip install strsim
    ```
  - **imdbpy**
    ```bash
    pip install imdbpy
    ```

### Features
-  Offline Movie files are renamed and organized in format:
```
<Movie_name> (<year>)
```

- Offline TV_Series files are renamed and organized in the format:
```
<TV_Series_name>
```

- All episodes of series are renamed in the format:
```
S<Season_number>E<Episode_Number>
```

- All episodes of a series are moved inside a folder with their corresponding Season number in it:
```
//<TV_Series_name>//S<Season_number>//
```

### Usage
* Step 1: Move all the media files that are to be renamed and organised into "/Input/Movies" or "/Input/Series" folder according to the requirement.
* Step 2: Run the appropirate .py file **RENAME-Movies.py** or **RENAME-Series.py**
* Step 3: If no error occurs, the organized files would be inside "/Output/Movies" or "/Output/Series" folder accordingly.
### Screenshot
#### RENAME-Movies.py
![Screenshots_Movies](https://github.com/KrishnaAlagiri/Media-Library-Organiser/raw/master/Screenshots/Movies%20-%20Before%20and%20After.PNG)
#### RENAME-Series.py
![Screenshots_TVShows](https://github.com/KrishnaAlagiri/Media-Library-Organiser/raw/master/Screenshots/TV%20Shows%20-%20Before%20and%20After.PNG)

## Authors
* **Krishna Alagiri** - *Initial work* - [KrishnaAlagiri](https://github.com/KrishnaAlagiri/)

## Acknowledgments
* Hat tip to anyone whose code was used.
* Myself :P
