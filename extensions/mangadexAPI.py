import requests

BASE_URL = "https://api.mangadex.org"

def getMangaCoverID(name):
    manga = requests.get(f"{BASE_URL}/manga",params={"title": name}).json()
    for item in manga['data'][0]['relationships']:
        if item['type'] == "cover_art":
            coverID = item['id']
            break
    return coverID

def getCoverArtFile(name):
    mangaCoverID = getMangaCoverID(name)
    mangaInfo = requests.get(f"{BASE_URL}/cover/{mangaCoverID}").json()
    return mangaInfo['data']['attributes']['fileName']

def getMangaID(name):
    mangaCoverID = getMangaCoverID(name)
    mangaInfo = requests.get(f"{BASE_URL}/cover/{mangaCoverID}").json()
    return mangaInfo['data']['relationships'][0]['id']

def getCoverArtLink(name):
    mangaID = getMangaID(name)
    coverartfile = getCoverArtFile(name)
    return f"https://mangadex.org/covers/{mangaID}/{coverartfile}"