import math

print("#########################")
print("Choisissez la forme :")
print("1 - Rectangle")
print("2 - Triangle")
print("3 - Cercle")
print("#########################")

choix = int(input("Votre choix :"))

if choix not in (1, 2, 3):
        print("Marche pas")
        exit()

elif choix == 1: 
        print("####### RECTANGLE ########")
        a = int(input("Longueur de la base :"))
        b = int(input("Longueur de la hauteur :"))
        print("####### RESULTATS ########")
        perimetre = (2*a) + (2*b)
        air = a * b
        print("Le périmetre est de:",perimetre)
        print("L'air est de:",air)

elif choix == 2: 
        print("####### TRIANGLE ########")
        a = int(input("Longueur de la base :"))
        c1 = int(input("Longueur côté gauche :"))
        c2 = int(input("Longueur côté droite :"))
        b = int(input("Longueur de la hauteur :"))
        print("####### RESULTATS ########")
        perimetre = a + c1 + c2
        air = (a*b)/2
        print("Le périmetre est de:",perimetre)
        print("L'air est de:",air)

elif choix == 3: 
        print("####### CERCLE ########")
        r = int(input("Longueur du rayon :"))
        print("####### RESULTATS ########")
        perimetre = 2 * math.pi * r
        air = math.pi * r**2
        print("Le périmetre est de:",perimetre)
        print("L'air est de:",air)
