"""
Vous allez simuler le parcours aléatoire d'un graphe simulant un mini-Web par un internaute et classer les pages Web avec un score de popularité (à la PageRank) à l'aide d'un programme développé en Python.

Voici la liste des taches à réaliser pour réaliser cette modélisation.

Le mini-Web est modélisé par un ensemble de pages Web qui sont reliées entre elles par des liens hypertextes.

Ce mini-Web est représenté par un graphe orienté, non pondéré dont les sommets sont les noms des pages Web et les arêtes les liens hypertextes.

On modélisera ce graphe par une liste d'adjacence avec comme structure de données en Python un dictionnaire dont les clefs sont les sommets du graphe (les noms des pages Web) et les valeurs la liste des pages Web liées à une page donnée par un lien hypertexte.

    Ecrire une fonction Python nommée genere_mini_web_aleatoire(nb_pages) qui génére aléatoirement un mini-Web composé de nb_pages pages Web reliées entre elles par des liens hypertexte.
    Visualiser le graphe ainsi modélisé à l'aide de la bibliothèque Python Graphviz.
    Ecrire une fonction Python nommée simule_marche_aleatoire(miniWeb, nb_deplacements) qui simule une marche aléatoire d'un internaute parmi le mini-Web représenté par le graphe miniWeb composée de nb__deplacements déplacements sur ce graphe.

Cette fonction devra retourner la liste des pages Web du graphe classées par ordre de popularité en se basant sur le principe que plus une page est visitée et plus elle est populaire.

    Représenter graphiquement le mini-Web avec ses pages classées par ordre de popularité à l'aide de la bibliothèque Python Graphviz.

La taille (ou la couleur) d'un disque représentant une page sera proportionnelle à sa popularité.

"""

import networkx as nx
import random
import matplotlib.pyplot as plt

def genere_mini_web_aleatoire(nb_pages):
    """Génère aléatoirement un mini-Web composé de nb_pages pages Web reliées entre elles par des liens hypertexte.
    """
    miniWeb = {}
    for i in range(nb_pages):
        miniWeb[i] = []
    for i in range(nb_pages):
        for j in range(nb_pages):
            if i != j:
                if random.randint(0,1) == 1:
                    miniWeb[i].append(j)
    return miniWeb

def simule_marche_aleatoire(miniWeb, nb_deplacements):
    """Simule une marche aléatoire d'un internaute parmi le mini-Web représenté par le graphe miniWeb composée de nb__deplacements déplacements sur ce graphe.
    """
    liste_pages = list(miniWeb.keys())
    page = random.choice(liste_pages)
    for i in range(nb_deplacements):
        page = random.choice(miniWeb[page])
    return page

def classement_pages(miniWeb, nb_deplacements, nb_simulations):
    """Retourne la liste des pages Web du graphe classées par ordre de popularité en se basant sur le principe que plus une page est visitée et plus elle est populaire.
    """
    compteur = {}
    for page in miniWeb.keys():
        compteur[page] = 0
    for i in range(nb_simulations):
        page = simule_marche_aleatoire(miniWeb, nb_deplacements)
        compteur[page] += 1
    return sorted(compteur, key=compteur.get, reverse=True)

def affiche_mini_web(miniWeb, classement):
    """Représente graphiquement le mini-Web avec ses pages classées par ordre de popularité et des disques dont la taille est proportionnelle à la popularité de la page.
    """
    G = nx.DiGraph()
    for page in miniWeb.keys():
        G.add_node(page)
    for page in miniWeb.keys():
        for voisin in miniWeb[page]:
            G.add_edge(page, voisin)
    nx.draw(G, with_labels=True, node_size=[1000*classement.index(page) for page in G.nodes()])
    plt.show()

miniWeb = genere_mini_web_aleatoire(10)
print(miniWeb)
classement = classement_pages(miniWeb, 100, 1000)
print(classement)
affiche_mini_web(miniWeb, classement)
