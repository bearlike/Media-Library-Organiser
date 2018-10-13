##Under Constructions
from imdb import IMDb
import re
def FindYear(Str):
    yr = re.findall('([(]+[0-9]+[0-9]+[0-9]+[0-9]+[)])', str2)
    yr = str(yr)
    yr = yr.replace("[","")
    yr = yr.replace("]","")
    yr = yr.replace("'","")
    yr = yr.replace(",","")
    yr = yr.replace(" ","")
    if(yr == ""):
        yr = "(----)"
    return(yr)

def lastIndexOf(str1,toFind):
    index = len(str1)-1
    i = 0
    for ch in str1:
        if(ch == toFind):
            index = i
        i+=1
    return(index)

def main_imdb(str2):
    ia = IMDb()
    s_result = ia.search_movie('The Untouchables')
    movies = []
    str1="Movie\n=====\nTitle: "
    for movie in s_result:
        str2 = (movie.summary())
        str2=str2.replace(str1,"")
        str2=str2.replace("\n","")
        str2=str2.replace("\"","")
        str2=str2.replace("\"","")
        year_str=FindYear(str2)
        str2 = str2[:lastIndexOf(str2,",")]
        str2 = str2.split("(",1)[0]
        str2 = str2.strip()
        movies.append(str2+" "+year_str)
    return(movies)

main_imdb(str2)
