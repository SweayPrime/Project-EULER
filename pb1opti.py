
import math

# Résume : Compte le nombre de multiple dans chaque ensemble,
# puis multiplie ce nombre par la valeur moyenne du multiple.
# Finalement, effectue l'union entre les ensembles et retire
# l'ensemble des multiples de 3 et de 5 (donc de 15) qui sont comptés deux fois.
if __name__ == '__main__':
    fin = 1000

    # diviseurs
    div = [3, 5, 15]
    # calcul le nombre de multiple
    taille = [math.floor(fin / div[0]), math.floor(fin / div[1]), math.floor(fin / div[2])]
    # dernier multiple
    fin = [taille[0] * div[0], taille[1] * div[1], taille[2] * div[2]]
    # somme par moyenne
    somme = [taille[0] * (fin[0] + div[0]) / 2, taille[1] * (fin[1] + div[1]) / 2, taille[2] * (fin[2] + div[2]) / 2]

    # l'ensemble des multiples des deux est compté deux fois
    reponse = int(somme[0] + somme[1] - somme[2])
    print("Réponse :", reponse)
