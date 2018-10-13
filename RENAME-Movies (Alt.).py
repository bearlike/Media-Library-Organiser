##Under Constructions
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

from imdb import IMDb
import re
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


    movies.append(str2)
print(movies)
