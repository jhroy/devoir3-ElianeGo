# coding: utf-8

import csv, requests
from bs4 import BeautifulSoup 

fichier = "articleS.csv"
articleS = []
#je vais tenter d'en faire une liste car mon fichier csv que ca imprime est en désordre...

# url = "https://www.lemonde.fr/archives-du-monde/01-01-2020/"

entetes = {
    "User-Agent":"Eliane Gosselin, étudiante en journalisme au QC"
}

dates = (range(1,32))
n = 0
for jour in dates:
    if jour < 10:
        jour = "0"+ str(jour)
    url = "https://www.lemonde.fr/archives-du-monde/{}-01-2020/".format(jour)
    # urlDuJour = url + str(jour)
    # print(urlDuJour)
    print(jour)

    site = requests.get(url, headers=entetes)

    print(site.status_code)
    

    page = BeautifulSoup(site.text, "html.parser")
    
#     # url = "https://www.lemonde.fr/archives-du-monde/{}-01-2020/"

# # print()
# # print(page.find("title"))
# # print()
    articles = page.find_all("section", class_="teaser")
    for article in articles:
        # print(article.find("a")["href"])
        n += 1
        urlArticle = article.find("a")["href"]
        print(n, urlArticle)
        print("."*10)

        siteArticle = requests.get(urlArticle, headers=entetes)
        pageArticle = BeautifulSoup(siteArticle.text, "html.parser")
        
        titreArticle = article.find("h3", class_="teaser__title").text.strip()
        print(titreArticle)
        articleS.append(titreArticle)
        
        #je suis vraiment proche de trouver le titre, et de les isoler pour chaque article, mais tout ce que j'essaie ne fonctionne pas même si je le vois dans mon code html!!! arghhh

        # nomAuteur = article.find("a", class_="article__author-link").text.strip()
        # print(nomAuteur)
        # ca m'imprime juste le premier nom et JE SAIS PAS POURQUOI CA IMPRIME PAS LES AUTRES
        
        # dateArticle = <meta property="og:article:published_time" content="2020-01-01T20:36:14+00:00">
        
        dateArticle = article.find("span", class_="meta__date").text.strip()
        print(dateArticle)
        articleS.append(dateArticle)
        # nomAuteur = pageArticle.find("section", class_="article_author-link")text.strip()
        # print(nomAuteur)

        
        try:
            nomAuteur = pageArticle.find("span", class_="meta__author").text.strip()
        except:
            nomAuteur = "aucun"
        print(nomAuteur)
        articleS.append(nomAuteur)

#toutes les infos que je veux s'imprime, reste à voir si le fichier créer sera en ordre

    dead = open(fichier,"a")
    obies = csv.writer(dead)
    obies.writerow(article)

        # j'ai eu de la difficulté à trouver quoi mettre comme variable après mon writerow... 
#Ma liste dans mon terminal imprime super bien mais pas mon fichier csv et je ne sais pas pourquoi
        
