import random

def tri_insertion(tab):
    for i in range(1, len(tab)):
        valeur_a_inserer = tab[i]
        position = i

        # Déplacement des éléments plus grands que la valeur à insérer vers la droite
        while position > 0 and tab[position - 1] > valeur_a_inserer:
            tab[position] = tab[position - 1]
            position -= 1

        # Insérer la valeur à sa position correcte
        tab[position] = valeur_a_inserer


def generer_tableau_aleatoire(taille):
    return [random.randint(1, 100) for _ in range(taille)]


tableau = generer_tableau_aleatoire(20)

print("Tableau initial :", tableau)


tri_insertion(tableau)

print("Tableau trié :", tableau)