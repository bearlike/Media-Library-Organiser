"""  Code Written by ~KK~
  To Automate the boring process of renaming files for your TV Shows library
  Useful for organising bulk media files or frequent updation of
  your XBMC library (Like Kodi, Plex and OSMC)
"""

def downloadsub(keyword,location,chance):
    import os
    from bs4 import BeautifulSoup
    import googlesearch as gs
    import requests
    LANGUAGE_CODES = {
        "Arabic": "ar",
        "Chinese": "zh",
        "Danish": "da",
        "Dutch": "nl",
        "English": "en",
        "Esperanto": "eo",
        "Finnish": "fi",
        "French": "fr",
        "German": "de",
        "Greek": "el",
        "Hebrew": "he",
        "Hindi": "hi",
        "Irish": "ga",
        "Italian": "it",
        "Japanese": "ja",
        "Korean": "ko",
        "Mongolian": "mn",
        "Norwegian": "no",
        "Persian": "fa",
        "Polish": "pl",
        "Portuguese": "pt",
        "Russian": "ru",
        "Spanish": "es",
        "Swedish": "sv",
        "Thai": "th",
        "Urdu": "ur",
        "Vietnamese": "vi",
        "Welsh": "cy",
        "Yiddish": "yi",
        "Zulu": "zu"
    }

    q = keyword
    temp = q
    x = location
    q = q + " English Subtitle SubScene"
    tdisp = "Googling - "+q+" "
    print(tdisp)
    possible = []
    for j in gs.search(q, tld="com", num=10, stop=1, pause=3):
        sp = "https://subscene.com/subtitles/"
        n = len(sp)
        if j[:n] == sp:
            possible.append(j)
    fin = ""
    eng_flag = 0

    for p in possible:
        c = 0
        ind_count = 0
        for i in p:
            if i == '/':
                c += 1
                if c==5:
                    eng = "english/"
                    print("Being Checked - ",p[(ind_count+1):(ind_count+9)]," ")
                    if(p[(ind_count+1):(ind_count+9)] == eng):
                        eng_flag = 1
            ind_count += 1
        if (c == 6) and (eng_flag == 1):
            fin = p
            break

    url = fin
    tdisp = "Found URL for this movie as - " + url + " "
    print(tdisp)
    if not bool(url):
        tdisp = "Couldn't find movie from the filename - " + temp + "\n\n"
        print(tdisp)
        nnn = len(temp)
        nnn = (3 * nnn) / 4
        nnn = int(nnn)
        if nnn >= int(chance / 2):
            tdisp = "Retrying with 75% of file name"
            print(tdisp)
            q = temp[:nnn]
            downloadsub(q, x, chance)
        return

    else:
        r = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')
        ssample = "/subtitles/english-text/"
        ssn = len(ssample)
        final = ""
        n = ssn
        for link in soup.find_all('a'):
            s = link.get('href')
            if s[:n] == ssample:
                final = "https://subscene.com" + s
        urll = final
        if bool(urll):
            tdisp = "Downloading from URL - " + urll + " "
            print(tdisp)
            r = requests.get(urll, allow_redirects=True)
            location = x + "\\" + temp + ".zip"
            tdisp = "Placing at location - " + location + "\n\n"
            print(tdisp)
            open(location, 'wb').write(r.content)
        else:
            tdisp = "Couldn't find movie from this filename - " + temp + "\n\n"
            print(tdisp)
            nnn=len(temp)
            nnn=(3*nnn)/4
            nnn = int(nnn)
            if nnn>=int(chance/2):
                tdisp = "Retrying...(With 75% of file name)\n"
                print(tdisp)
                q = temp[:nnn]
                downloadsub(q,x,chance)
            return(str(location))

def unZip(path_to_zip_file,directory_to_extract_to):
    import zipfile
    zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
    zip_ref.extractall(directory_to_extract_to)
    zip_ref.close()

if __name__ == '__main__':
    import os
    try:os.mkdir(".cache")
    except:pass
    path_ = os.getcwd()+"\\.cache"
    files = os.listdir(path_)
    for file in files:
        if (file.endswith(".mp4") or file.endswith(".mkv")):
            downloadsub(file[:-4],path_,5)
        elif (file.endswith(".zip")):
            unZip(file,path_)
            os.remove(file)
