from turtle import title
import requests

class Manga:
    __BASE_URL = "https://api.mangadex.org"
    titles = {}
    manga_id = "" 
    __manga_cover_id = ""
    __manga_cover_file = "" 
    manga_cover_link = ""
    descriptions = {}
    publication_demographic = "" 
    status = "" 
    publication_year = "" 
    def __init__(self,name: str) -> None:
        #json of the information about the manga
        info = requests.get(f"{self.__BASE_URL}/manga",params={"title": name}).json()

        #list of the data requested, find the first matching manga base on name
        manga_list = []
        for item in info['data']:
            manga_list.append(item)
        for item in manga_list:
            titles = []
            titles.append(item['attributes']['title'])
            for lang in item['attributes']['altTitles']:
                titles.append(lang)
            has_found = False
            for lang in titles:
                for key, val in lang.items():
                    if name.title() in val.title():
                        info = item
                        has_found = True
                        break
            if has_found:
                break
            
            
        #id of the manga
        self.manga_id = info['id']

        #all titles in every language available
        self.titles.update(info['attributes']['title'])
        for item in info['attributes']['altTitles']:
            self.titles.update(item)

        #all descriptions in every language available
        lang = []
        for item in info['attributes']['description']:
            lang.append(item)
        for item in lang:
            desc = info['attributes']['description'][str(item)]
            desc = desc[:desc.find("---"):]
            desc = " ".join(desc.split())
            self.descriptions.update({str(item): desc})

        #the target demographic
        self.publication_demographic = info['attributes']['publicationDemographic']

        #year of release
        self.publication_year = info['attributes']['year']

        #status: if is ongoing or has ended or something else
        self.status = info['attributes']['status']

        #make a link to the manga cover art
        for item in info['relationships']:
            if item['type'] == "cover_art":
                self.__manga_cover_id = item['id']
                break
        json_of_cover = requests.get(f"{self.__BASE_URL}/cover/{self.__manga_cover_id}").json()
        self.__manga_cover_file = json_of_cover['data']['attributes']['fileName']
        self.manga_cover_link = f"https://mangadex.org/covers/{self.manga_id}/{self.__manga_cover_file}"