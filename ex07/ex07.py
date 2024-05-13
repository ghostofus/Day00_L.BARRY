def est_nombre_armstrong(num):
    # Convertir le nombre en une chaîne de caractères pour itérer à travers chaque chiffre
    str_num = str(num)
    # Calculer la somme des cubes des chiffres
    somme_cubes = sum(int(chiffre)**3 for chiffre in str_num)
    # Vérifier si la somme des cubes est égale au nombre lui-même
    if somme_cubes == num:
        return True
    else:
        return False


num = int(input("Entrez un numéro : "))


if est_nombre_armstrong(num):
    print(f"{num} est un nombre Armstrong")
else:
    print(f"{num} n'est pas un nombre Armstrong")