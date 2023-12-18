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
    compteur = {}
    for page in miniWeb.keys():
        compteur[page] = 0
    for i in range(nb_simulations):
        page = simule_marche_aleatoire(miniWeb, nb_deplacements)
        compteur[page] += 1
    return compteur

def plot_stats(compteur):
    pages = list(compteur.keys())
    counts = list(compteur.values())
    plt.bar(pages, counts)
    plt.xlabel('Pages')
    plt.ylabel('Counts')
    plt.title('Page visits over iterations')
    plt.show()

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
compteur = classement_pages(miniWeb, 100, 1000)
plot_stats(compteur)
