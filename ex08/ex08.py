def print_pyramid(n):
    # Vérifier si n est un entier positif
    if not isinstance(n, int) or n <= 0:
        print("Veuillez entrer un entier positif.")
        return
    
    # Boucle pour chaque ligne de la pyramide
    for i in range(1, n + 1):
        # Calculer le nombre d'étoiles pour la ligne i
        num_stars = 2 * i - 1
        # Calculer le nombre d'espaces à gauche pour centrer la ligne
        num_spaces = n - i
        # Construire la ligne avec les espaces et les étoiles
        line = " " * num_spaces + "*" * num_stars
        # Afficher la ligne
        print(line)

# Demander à l'utilisateur le nombre de lignes pour la pyramide
try:
    num_lines = int(input("Entrez le nombre de lignes pour la pyramide d'étoiles : "))
    # Appeler la fonction pour imprimer la pyramide
    print_pyramid(num_lines)
except ValueError:
    print("Veuillez entrer un entier.")