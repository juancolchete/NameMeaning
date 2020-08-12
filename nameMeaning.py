from bs4 import BeautifulSoup as bs
import requests
def getName(text):
    if(text.lower().index('significado de ') != -1):
        stringtSize = len(text)
        name = text[15:stringtSize]
        return name
def getMeaning(nome):
    request = requests.get("https://www.dicionariodenomesproprios.com.br/"+nome)
    html = bs(request.text, "html.parser")

    divMeaning = html.find(id="significado")
    meanigP = divMeaning.find_all("p")
    Meaning  = ""
    for x in meanigP:
        Meaning  += x.text+"\n\n"
    return Meaning

print(getMeaning(getName('Significado de juan')))