# 🟪 Sierpinski Carpet (Python)

Programme Python qui génère un **tapis de Sierpinski** en utilisant la **récursivité** et la bibliothèque **Turtle**, avec des couleurs aléatoires à chaque exécution.

> 📚 **Projet scolaire** : réalisé en Terminale dans le cadre de la spécialité NSI (Numérique et Sciences Informatiques). Je le partage simplement pour transmettre ce que j'ai appris. Il n'a pas vocation à être un projet professionnel.

---

## 🧩 Qu'est-ce que le tapis de Sierpinski ?

Le tapis de Sierpinski est une **fractale** décrite par le mathématicien polonais Wacław Sierpiński en 1916. On l'obtient ainsi :

1. On part d'un carré.
2. On le découpe en une grille de 3 × 3 carrés identiques.
3. On met en évidence le carré central.
4. On recommence le processus sur les 8 carrés restants, puis sur leurs sous-carrés, et ainsi de suite.

À chaque niveau, le motif se répète à une échelle plus petite : c'est le principe d'**autosimilarité** des fractales.

---

## ✨ Fonctionnalités

- Génération récursive du tapis de Sierpinski
- Profondeur de récursion paramétrable
- Couleurs aléatoires (RVB) différentes pour chaque niveau de récursion
- Approche orientée objet avec une classe `Carre`
- Dessin rapide grâce à la vitesse maximale de Turtle

---

## 🛠️ Prérequis

- **Python 3.x**
- La bibliothèque **Turtle**, incluse par défaut avec Python (aucune installation nécessaire)

> Sous certaines distributions Linux, il peut être nécessaire d'installer Tkinter :
> `sudo apt install python3-tk`

---

## 🚀 Utilisation

1. Clone le dépôt :
   ```bash
   git clone https://github.com/<ton-pseudo>/sierpinski-carpet.git
   cd sierpinski-carpet
   ```
2. Lance le programme :
   ```bash
   python sierpinski_carpet.py
   ```
3. Une fenêtre Turtle s'ouvre et dessine le tapis. 🎨

---

## ⚙️ Personnalisation

En bas du fichier, tu peux modifier ces paramètres :

| Paramètre | Ligne concernée | Effet |
|-----------|-----------------|-------|
| Profondeur | `tapis(3, 300, -200, -200)` | Le premier argument (`3`) définit le nombre de niveaux de récursion |
| Taille | `Carre(300, -200, -200)` et `tapis(3, 300, ...)` | Longueur du côté du carré de départ (en pixels) |
| Position | `-200, -200` | Coordonnées du coin inférieur gauche |
| Couleurs | `nb_couleur = 5` | Nombre de couleurs aléatoires générées |

> ⚠️ La profondeur ne doit pas dépasser `nb_couleur` (5 par défaut), car chaque niveau utilise sa propre couleur. Au-delà de 4 niveaux, le dessin devient aussi très long avec Turtle.

---

## 🧠 Fonctionnement du code

### La classe `Carre`
Elle modélise un carré grâce à trois attributs privés : la longueur du côté et les coordonnées de son coin inférieur gauche. Sa méthode `afficher()` déplace la tortue et dessine un carré rempli avec la couleur choisie.

### La fonction récursive `tapis(n, longueur, a, o)`
- **Cas de base** (`n == 0`) : on dessine le carré central de la zone.
- **Cas récursif** :
  1. on dessine le carré central (1/3 de la longueur) ;
  2. on rappelle `tapis` sur les **8 sous-carrés** qui l'entourent, avec `n - 1`.

```python
for i in range(3):
    for j in range(3):
        if i != 1 or j != 1:   # on ignore le carré central
            tapis(n - 1, c, a + i * c, o + j * c)
```

Le nombre de carrés dessinés augmente très vite : à chaque niveau, il est multiplié par 8.

---

## 🎓 Notions abordées

- Récursivité (cas de base / appel récursif)
- Programmation orientée objet (classe, constructeur, attributs privés, accesseurs)
- Fractales et autosimilarité
- Dessin avec le module Turtle
- Génération de nombres aléatoires (`random`)

---

## 👤 Auteur

**Nicola Miralles** : projet réalisé en Terminale (spécialité NSI), octobre 2024.
