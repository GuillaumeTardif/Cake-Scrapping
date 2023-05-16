from bs4 import BeautifulSoup

# Lecture des données HTML
f = open("recette.html", "r", encoding="UTF-8") # Ouverture du fichier en read
html_content = f.read() # Lecture du fichier
f.close() # Fermeture du fichier
soup = BeautifulSoup(html_content, "html.parser") # On indique à BS de parcourir du HTML

titre_h1 = soup.find("h1") # On trouve la balise html h1 qui contient le titre
# paragraphe_description = soup.find("p", class_ ="description") # On trouve la balise html "p" avec la classe "description"
list_div_centre = soup.findAll("div", class_ ="centre") # On trouve toutes les occurences de la balise "div" avec la classe "centre"
if list_div_centre and len(list_div_centre) >= 2: # On trouve la balise "p" avec classe "description" si on a trouvé deux balises div.
    paragraphe_description = list_div_centre[1].find("p", class_ ="description")
div_image = soup.find("div", class_ = "info")
source_gateau = div_image.find("img", class_ = "centre info")


print("Titre de la page HTML:", titre_h1.text) # on affiche le texte de la balise h1
if paragraphe_description:
    print("Description de la page:", paragraphe_description.text) # On affiche le texte html "p" avec la classe "description"
print("Source de l'image:", source_gateau["src"]) # on affiche le texte de la balise h1




