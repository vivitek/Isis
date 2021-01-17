# Xana

# Présentation de l'outil

---

Xana est un outil qui a pour but de catégoriser les sites internet visités par les utilisateurs. Cella permettra au utilisateur de pouvoir mieux visualisé quel site sont visité et de pouvoir bloqué des catégorie entière. Par exemple, si un utilisateur se rend sur le site YouTube, l'administrateur du réseau aura la capacité de voir qu'un site de Streaming est consulté dans son réseau, il pourra donc soir bloqué le site en question, soit bloqué tous les sites de la catégorie Streaming. Nous avons donc développé l'outil Xana qui serra une intelligence artificielle qui aura la capacité de reconnaître les catégories de site en fonction de leur Metadata.

# Scraper

---

Pour développer cet outil nous voulons entraîner une intelligence artificielle a catégoriser des sites, pour que notre intelligence artificielle fonctionne, il lui faut de la data brut. Nous avons développé un scraper, c'est un outil qui permet d'ouvrir une page internet et de récupérer tout le html de cette page, ensuite nous avons parser ce code afin de ne garder que les balise méta.

# Utilisation de l'outil Scraper

---

Prérequis d'installation

```python
pip install bs4
pip install beautifulsoup4
pip install request
```

Pour récupérer des URL, le scraper va lire le fichier site.txt

```python
file = open('site.txt', "r")
##scraper.py
```

Voici quelque exemple d'URL contenu dans site.txt

```
https://Google.fr
https://Facebook.com
https://Youtube.com
https://Amazon.fr
https://Wikipedia.org
https://Orange.fr
https://Live.com
https://Yahoo.com
https://Leboncoin.fr
https://Free.fr
https://Twitter.com
https://Linkedin.com
https://Cdiscount.com
https://Instagram.com
https://Livejasmin.com
https://Ebay.fr
https://Lemonde.fr
https://Allocine.fr
https://Buzzfil.net
https://Lefigaro.fr
```

Pour exécuter le code 

```
python3 scraper.py
```

Une fois exécuté, le scraper va ouvrir toute les URL contenu dans le fichier site.txt, et va écrire toute les Metadata dans un fichier data.txt

```
https:

Facebook.com
Créez un compte ou connectez-vous à Facebook. Connectez-vous avec vos amis, la famille et d’autres connaissances. Partagez des photos et des vidéos,...
https:

Youtube.com
Profitez des vidÃ©os et de la musique que vous aimez, mettez en ligne des contenus originaux, et partagez-les avec vos amis, vos proches et le monde entier.
https:

Amazon.fr
Achat et vente en ligne parmi des millions de produits en stock. Livraison gratuite à partir de 25€. Vos articles à petits prix : culture, high-tech, mode, jouets, sport, maison et bien plus !
https:
```
