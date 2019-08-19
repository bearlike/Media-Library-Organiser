<h1 align="center">
  <br>
  <img src="http://cdn.thekrishna.in/img/common/mlo.png" alt="Media Library Organiser" width="650">
  <br>
</h1>

<h4 align="center">Automatically bulk renames and organises your Movie and TV-Shows Library.<br>Ideal for maintaining your xbmc library.</h4>

<p align="center">
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/language-python-blue.svg?style=flat"></a>
  <a href="https://github.com/KrishnaAlagiri/Media-Library-Organiser/releases/tag/v1.3-a1"><img src="https://img.shields.io/badge/release-v1.3.0--a1-orange.svg?style=flat"></a>
  <a href="#"><img src="https://img.shields.io/github/last-commit/KrishnaAlagiri/Media-Library-Organiser.svg"></a>
  <a href="/LICENSE.md"><img src="https://img.shields.io/github/license/KrishnaAlagiri/Media-Library-Organiser.svg?color=blue"></a>
</p>


### Why do I do it?
This boosts my frequently updated massive media library organised almost instantly.


### What's New !
- `[ADDED]` Fallback mode if unable to detect a TV Show.
- `[ADDED]` Automatic Subtitle Downloader.
- `[UPDATE]` Uses **imDB** to retrieve the most relevent movie and series names.
- **To view the entire Update log** - [log-update.md](https://github.com/KrishnaAlagiri/Media-Library-Organiser/blob/master/log-update.md)
- **To view the features that are to be added on the next version** - [current-working.md](https://github.com/KrishnaAlagiri/Media-Library-Organiser/blob/master/current-working.md)


## Getting Started

### Prerequisites
What things you need to run the program:
- Python Compiler (3.7 Recommended)
- Install the following Packages from pypi by using the following commands:
  - **strsim** and **imdbpy**
    ```bash
    pip install strsim
    pip install imdbpy
    ```

### Features
-  Offline Movie files are renamed and organized in format:
```
<Movie_name> (<year>)
```

- All episodes of series are renamed in the format:
```
S<Season_number>E<Episode_Number>
```

- Allmovies are moved inside a folder with their corresponding name and release year in it:
```
*/Output/Movies/<Movie_name> (<year>)/
```


- All episodes of a series are moved inside a folder with their corresponding Season number in it:
```
*/Output/Series/<TV_Series_name>/S<Season_number>/
```

### Usage
* Step 1: Move all the media files that are to be renamed and organised into "/Input/Movies" or "/Input/Series" folder according to the requirement.
* Step 2: Run the appropirate .py file **RENAME-Movies.py** or **RENAME-Series.py**
* Step 3: If no error occurs, the organized files would be inside "/Output/Movies" or "/Output/Series" folder accordingly.

### Screenshot

#### RENAME-Movies.py
<img src="https://github.com/KrishnaAlagiri/Media-Library-Organiser/raw/master/Screenshots/Movies%20-%20Before%20and%20After.PNG" width="500"/>

#### RENAME-Series.py
<img src="https://github.com/KrishnaAlagiri/Media-Library-Organiser/raw/master/Screenshots/TV%20Shows%20-%20Before%20and%20After.PNG" width="500"/>

## Authors
* **Krishna Alagiri** - [K-Kraken](https://github.com/K-Kraken/)

## Acknowledgments
* Hat tip to anyone whose code was used.
* Myself :P


<p align="center">
  Made with ❤️ by <a href="https://github.com/KrishnaAlagiri">Krishna Alagiri</a>
</p>

![wave](http://cdn.thekrishna.in/img/common/border.png)
