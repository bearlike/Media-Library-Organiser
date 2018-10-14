# Media Library Organiser
###### `v1.1-a1` `No-GUI`  
A program that'll automatically rename and organise all your offline media files.

#### What's New !
* `[UPDATE]` Uses **imDB** to retrieve the most relevent movie names.
* **To view the entire Update log** - [log-update.md](https://github.com/KrishnaAlagiri/Media-Library-Organiser/blob/master/log-update.md)

## Getting Started
### Prerequisites
What things you need to run the program:
- Python Compiler (3.7 Recommmended)
- Install the following Packages:
  - **strsim**
    - From pypi:
    ```bash
    pip install strsim
    ```
  - **imdbpy**
    - From pypi:
    ```bash
    pip install imdbpy
    ```
### Features
*  Offline Movie files are renamed and organised in format:
```
<Movie_name> (<year>)
```
* Offline TV_Series files are renamed and organised in format:
```
<TV_Series_name>
```
* All episodes of series are renamed in the format:
```
 S<Season_number>E<Episode_Number>
```
* All episodes of a series are moved inside a folder with their corresponding Season number in it:
```
//<TV_Series_name>'//S<Season_number>//
```
End with an example of getting some data out of the system or using it for a little demo


## Authors

* **Krishna Alagiri** - *Initial work* - [KrishnaAlagiri](https://github.com/KrishnaAlagiri/)

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
