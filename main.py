from bs4 import BeautifulSoup

# Made with Python 3.11.0b4

# Reading data from the HTML file
f = open("recette.html", "r", encoding="UTF-8")
html_content = f.read()
f.close()
soup = BeautifulSoup(html_content, "html.parser") # Telling BS to parse data data

# Find and store data
title_h1 = soup.find("h1") # Finding the html h1 tag

list_div_centre = soup.findAll("div", class_ ="centre") # Finding all the "div" tag occurencies with the "centre" class
if list_div_centre and len(list_div_centre) >= 2: # Finding the "p" tag with the "description class" should we find more than one.
    paragraphe_description = list_div_centre[1].find("p", class_ ="description")

div_image = soup.find("div", class_ = "info")
source_gateau = div_image.find("img", class_ = "centre info")

# Printing out the data
print("Titre de la page HTML:", title_h1.text) # on affiche le texte de la balise h1
if paragraphe_description:
    print("Description de la page:", paragraphe_description.text) # On affiche le texte html "p" avec la classe "description"
print("Source de l'image:", source_gateau["src"]) # on affiche le texte de la balise h1