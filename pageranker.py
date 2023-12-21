import networkx as nx
import random
import matplotlib.pyplot as plt
import random

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
    fig = plt.figure()
    nx.draw(G, with_labels=True, node_size=[1000*classement.index(page) for page in G.nodes()])
    return fig

def affiche_visites_pages(miniWeb, nb_deplacements, nb_simulations):
    """Représente graphiquement le nombre de visites de chaque page du mini-Web.
    """
    compteur = {}
    for page in miniWeb.keys():
        compteur[page] = 0
    for i in range(nb_simulations):
        page = simule_marche_aleatoire(miniWeb, nb_deplacements)
        compteur[page] += 1

    pages = list(compteur.keys())
    visites = list(compteur.values())

    fig, ax = plt.subplots()
    ax.bar(pages, visites)
    ax.set_xlabel('Pages')
    ax.set_ylabel('Nombre de visites')
    ax.set_title('Nombre de visites de chaque page du mini-Web')
    return fig
