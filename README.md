# Media Library Organiser
###### `v1.1-a1` `No-GUI`  
A program that'll automatically bulk rename and organise your **Movie and TV-Shows Library** (ideal for maintaining your *xbmc* library). Movies and TV Shows are easily organized by your xbmc if they're given the right name.

#### What's New !
* `[UPDATE]` Uses **imDB** to retrieve the most relevent movie names.
* **To view the entire Update log** - [log-update.md](https://github.com/KrishnaAlagiri/Media-Library-Organiser/blob/master/log-update.md)
* **To view the features that are to added on the next version** - [current-working.md](https://github.com/KrishnaAlagiri/Media-Library-Organiser/blob/master/current-working.md)


## Getting Started
### Prerequisites
What things you need to run the program:
- Python Compiler (3.7 Recommmended)
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
- ```bash
<Movie_name> (<year>)
```

- Offline TV_Series files are renamed and organized in format:
```bash
<TV_Series_name>
```

- All episodes of series are renamed in the format:
```bash
 S<Season_number>E<Episode_Number>
```

- All episodes of a series are moved inside a folder with their corresponding Season number in it:
```bash
//<TV_Series_name>//S<Season_number>//
```

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
