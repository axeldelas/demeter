# coding: utf-8
import random

####################################
#### REPRESENTATION DES DONNEES ####
####################################

reperes_ligne = ["A", "B", "C", "D", "E", "F", "G", "H"]
reperes_colonne = ["", "1", "2", "3", "4", "5", "6", "7", "8"]

grille_depart = [[0, 0, 0, 0, 0, 0, 0, 0],
                 ["O", 0, "O", 0, "O", 0, "O", 0],
                 [0, "O", 0, "O", 0, "O", 0, "O"],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 ["X", 0, "X", 0, "X", 0, "X", 0],
                 [0, "X", 0, "X", 0, "X", 0, "X"],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
grille_milieu = [[0, 0, 0, 0, 0, 0, 0, 0],
                 ["O", 0, "O", 0, 0, 0, "O", 0],
                 [0, "O", 0, "O", 0, 0, 0, "O"],
                 [0, 0, 0, "X", 0, "O", 0, 0],
                 [0, 0, "X", 0, "X", 0, "O", 0],
                 ["X", 0, 0, 0, 0, 0, "X", 0],
                 [0, 0, 0, "X", 0, "X", 0, "X"],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
grille_fin = [[0, 0, 0, 0, 0, 0, 0, 0],
              ["O", 0, "O", 0, "X", 0, 0, 0],
              [0, "O", 0, "O", 0, 0, 0, "O"],
              [0, 0, 0, 0, "X", 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              ["X", 0, 0, 0, "X", 0, 0, 0],
              [0, 0, 0, "X", "X", "X", "O", "X"],
              [0, 0, 0, 0, 0, "O", "O", 0]]

###########################################
####   PARTIE REPRESENTATION GRAPHIQUE ####
###########################################

def afficher_grille(grille, joueur):
    for j in range(len(reperes_colonne)):
        print("", reperes_colonne[j], end="")
    print("")
    for i in range(8):
        if i == 4:
            print(" " + "+-" * 8 + "+")
        print(reperes_ligne[i], end="")
        for j in range(8):
            valeur = grille[i][j]
            if valeur == 0:
                print("| ", end="")
            else:
                print("|" + str(valeur), end="")
        print("|")
    print(" " + "+-" * 8 + "+")
    print("Joueur 1 : O     Joueur 2 : X     Joueur courant :", joueur)

def choix_grille_courante(joueur):
    print("\n- Grille début de partie : 1")
    print("- Grille milieu de partie : 2")
    print("- Grille fin de partie : 3")
    grille_choisie = input("Entrez le chiffre correspondant à la grille souhaitée : ")
    while grille_choisie not in ["1", "2", "3"]:
        grille_choisie = input("Incorrect, réessayez : ")
    if grille_choisie == "1":
        grille_choisie = grille_depart
    elif grille_choisie == "2":
        grille_choisie = grille_milieu
    else:
        grille_choisie = grille_fin
    print("\nAffichage grille courante :")
    afficher_grille(grille_choisie,joueur)
    return grille_choisie

###########################
####   PARTIE SAISIE   ####
###########################
    
def est_dans_grille(coordonnees):
    if coordonnees[0] in ["A", "B", "C", "D", "E", "F", "G", "H"] and coordonnees[1] in ["1", "2", "3", "4", "5", "6","7", "8"]:
        return True
    return False

def saisir_coordonnees():
    coordonnees = input("Saisissez une coordonnée par sa ligne suivi de sa colonne : ")
    while not len(coordonnees) == 2 or not est_dans_grille(coordonnees):
        coordonnees = input("Erreur coordonnées, réessayez : ")
    print ("\n")
    return indices_cases_depart(coordonnees[0], coordonnees[1])

##################################################################
####   PARTIE FONCTIONS POUR LES DEUX TYPES DE DEPLACEMENT   ####
##################################################################
    
def indices_cases_depart(indice_ligne_depart, indice_colonne_depart):
    for i in range(len(reperes_ligne)):
        if indice_ligne_depart == reperes_ligne[i]:
            i_ligne_depart = i
    for j in range(len(reperes_colonne)):
        if indice_colonne_depart == reperes_colonne[j]:
            i_colonne_depart = j - 1
    return i_ligne_depart, i_colonne_depart

def a_choisi_pion_correct(grille, joueur, indice_ligne_depart, indice_colonne_depart):
    if joueur == "Joueur 1" and grille[indice_ligne_depart][indice_colonne_depart] == "O":
            return True
    elif joueur == "Joueur 2" or joueur == "Ordinateur" and grille[indice_ligne_depart][indice_colonne_depart] == "X":
            return True
    return False

def est_dans_grille_apres_deplacement(direction, indice_ligne_arrivee, indice_colonne_arrivee,indice_ligne_arrivee_diagonale, indice_colonne_arrivee_diagonale):
    if direction in ["1", "2", "3", "4"]:
        if not indice_ligne_arrivee in [0, 1, 2, 3, 4, 5, 6, 7] or not indice_colonne_arrivee in [0, 1, 2, 3, 4, 5, 6,7]:
            return False
    else:
        if not indice_ligne_arrivee_diagonale in [0, 1, 2, 3, 4, 5, 6, 7] or not indice_colonne_arrivee_diagonale in [0,1,2,3,4,5,6,7]:
            return False
    return True

def indices_case_arrivee(indice_ligne_depart, indice_colonne_depart, distance, direction):
    if direction == "1":
        return indice_ligne_depart - int(distance), indice_colonne_depart
    elif direction == "2":
        return indice_ligne_depart + int(distance), indice_colonne_depart
    elif direction == "3":
        return indice_ligne_depart, indice_colonne_depart + int(distance)
    return indice_ligne_depart, indice_colonne_depart - int(distance)

def est_pas_dans_son_camp(joueur, indice_ligne_arrivee, indice_colonne_arrivee,indice_ligne_arrivee_diagonale, indice_colonne_arrivee_diagonale):
    if joueur == "Joueur 1" and (indice_ligne_arrivee == 0 and indice_colonne_arrivee in [3,4]) or (indice_ligne_arrivee_diagonale == 0 and indice_colonne_arrivee_diagonale in [3,4]):
        return False
    else:
        if (indice_ligne_arrivee == 7 and indice_colonne_arrivee in [3,4]) or (indice_ligne_arrivee_diagonale == 7 and indice_colonne_arrivee_diagonale in [3,4]):
            return False
    return True

#########################################
###   PARTIE DEPLACEMENT A DOMICILE   ###
#########################################

def a_pas_depasse_ligne_mediane(joueur, indice_ligne_arrivee, indice_colonne_arrivee):
    if joueur == "Joueur 1" and indice_ligne_arrivee in [0, 1, 2, 3]:
            return True
    elif joueur == "Joueur 2" or joueur == "Ordinateur" and indice_ligne_arrivee in [4, 5, 6, 7]:
            return True
    return False

def est_dans_la_bonne_zone(joueur, indice_ligne_depart):
    if joueur == "Joueur 1" and indice_ligne_depart in [0, 1, 2, 3]:
        return True
    elif joueur == "Joueur 2" or joueur == "Ordinateur" and indice_ligne_depart in [4, 5, 6, 7]:
        return True
    return False

def a_pas_saute_pion(grille, distance, direction, indice_ligne_depart, indice_colonne_depart):
    if direction == "1":
        for i in range(1, int(distance) + 1):
            if not grille[indice_ligne_depart - i][indice_colonne_depart] == 0:
                return False
    elif direction == "2":
        for i in range(1, int(distance) + 1):
            if not grille[indice_ligne_depart + i][indice_colonne_depart] == 0:
                return False
    elif direction == "3":
        for j in range(1, int(distance) + 1):
            if not grille[indice_ligne_depart][indice_colonne_depart + j] == 0:
                return False
    else:
        for j in range(1, int(distance) + 1):
            if not grille[indice_ligne_depart][indice_colonne_depart - j] == 0:
                return False
    return True

# Fonction validation si toutes les conditions sont respectées pour effectuer un déplacement à domicile
def est_valide_deplacement_a_domicile(grille, joueur, direction, distance, indice_ligne_depart, indice_colonne_depart, indice_ligne_arrivee, indice_colonne_arrivee, indice_ligne_arrivee_diagonale, indice_colonne_arrivee_diagonale):
    return est_dans_la_bonne_zone(joueur, indice_ligne_depart) and a_choisi_pion_correct(grille, joueur, indice_ligne_depart, indice_colonne_depart) and est_dans_grille_apres_deplacement(direction, indice_ligne_arrivee, indice_colonne_arrivee, indice_ligne_arrivee_diagonale,indice_colonne_arrivee_diagonale) and a_pas_saute_pion(grille, distance, direction, indice_ligne_depart, indice_colonne_depart) and a_pas_depasse_ligne_mediane(joueur, indice_ligne_arrivee, indice_colonne_arrivee) and est_pas_dans_son_camp(joueur, indice_ligne_arrivee, indice_colonne_arrivee, indice_ligne_arrivee_diagonale, indice_colonne_arrivee_diagonale)

def choix_direction_deplacement_a_domicile():
    print("\n- Haut : 1")
    print("- Bas : 2")
    print("- Droite : 3")
    print("- Gauche : 4")
    deplacement_souhaite = input("Saisissez le chiffre correspondant à la direction souhaitée : ")
    while not deplacement_souhaite in ["1", "2", "3", "4"]:
        deplacement_souhaite = input("Erreur saisie, réessayez : ")
    return deplacement_souhaite

def choix_distance_deplacement():
    distance_souhaitee = input("Saisissez la distance souhaitée : ")
    while not distance_souhaitee in ["1", "2", "3", "4", "5", "6", "7"]:
        distance_souhaitee = input("Erreur saisie, réessayez : ")
    return distance_souhaitee

# Fonction de saisie des paramètres nécessaire au déplacement à domicile
def saisie_utilisateur_deplacement_a_domicile(grille, joueur):
    direction_deplacement = choix_direction_deplacement_a_domicile()
    distance_deplacement = choix_distance_deplacement()
    i_ligne_depart, i_colonne_depart = saisir_coordonnees()
    i_ligne_arrivee, i_colonne_arrivee = indices_case_arrivee(i_ligne_depart, i_colonne_depart, distance_deplacement, direction_deplacement)
    i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale = indices_case_arrivee_saut_diagonale(i_ligne_depart, i_colonne_depart, direction_deplacement)
    while not est_valide_deplacement_a_domicile(grille, joueur, direction_deplacement, distance_deplacement, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale):
        print("")
        print("Déplacement imposssible, réessayez :")
        direction_deplacement = choix_direction_deplacement_a_domicile()
        distance_deplacement = choix_distance_deplacement()
        i_ligne_depart, i_colonne_depart = saisir_coordonnees()
        i_ligne_arrivee, i_colonne_arrivee = indices_case_arrivee(i_ligne_depart, i_colonne_depart, distance_deplacement, direction_deplacement)
        i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale = indices_case_arrivee_saut_diagonale(i_ligne_depart, i_colonne_depart, direction_deplacement)
    return i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee

# Fonction pour effectuer le déplacement à domicile sur un pion
def deplacement_a_domicile(grille, joueur, indice_ligne_depart, indice_colonne_depart, indice_ligne_arrivee, indice_colonne_arrivee):
    grille[indice_ligne_depart][indice_colonne_depart], grille[indice_ligne_arrivee][indice_colonne_arrivee] = grille[indice_ligne_arrivee][indice_colonne_arrivee], grille[indice_ligne_depart][indice_colonne_depart]
    afficher_grille(grille, joueur)
    
# Fonction du tour de jeu
def choix_deplacement_a_domicile(grille, joueur):
    if joueur == "Joueur 1":
        i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee = saisie_utilisateur_deplacement_a_domicile(grille, joueur)
        deplacement_a_domicile(grille, joueur, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee)
    else:
        i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee = saisie_utilisateur_deplacement_a_domicile(grille, joueur)
        deplacement_a_domicile(grille, joueur, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee)
        
#######################################
###   PARTIE DEPLACEMENT PAR SAUT   ###
#######################################

def est_vide_case_arrivee(grille, direction, indice_ligne_arrivee, indice_colonne_arrivee, indice_ligne_arrivee_diagonale, indice_colonne_arrivee_diagonale):
    if direction in ["1", "2", "3", "4"] and grille[indice_ligne_arrivee][indice_colonne_arrivee] == 0:
        return True
    elif direction in ["5","6","7","8"] and grille[indice_ligne_arrivee_diagonale][indice_colonne_arrivee_diagonale] == 0:
        return True
    return False

def a_voisin_direct_orthogonale_joueur_1(grille, direction, indice_ligne_depart, indice_colonne_depart):
    if direction == "1" and grille[indice_ligne_depart - 1][indice_colonne_depart] == "O":
        return True
    elif direction == "2" and grille[indice_ligne_depart + 1][indice_colonne_depart] == "O":
        return True
    elif direction == "3" and grille[indice_ligne_depart][indice_colonne_depart + 1] == "O":
        return True
    elif direction == "4" and grille[indice_ligne_depart][indice_colonne_depart - 1] == "O":
        return True
    return False

def a_voisin_direct_diagonale_joueur_1(grille, direction, indice_ligne_depart, indice_colonne_depart):
    if direction == "5" and grille[indice_ligne_depart - 1][indice_colonne_depart + 1] == "O":
            return True
    elif direction == "6" and grille[indice_ligne_depart + 1][indice_colonne_depart + 1] == "O":
            return True
    elif direction == "7" and grille[indice_ligne_depart - 1][indice_colonne_depart - 1] == "O":
            return True
    elif direction == "8" and grille[indice_ligne_depart + 1][indice_colonne_depart - 1] == "O":
            return True
    return False

def a_voisin_direct_orthogonale_joueur_2(grille, direction, indice_ligne_depart, indice_colonne_depart):
    if direction == "1" and grille[indice_ligne_depart - 1][indice_colonne_depart] == "X":
        return True
    elif direction == "2" and grille[indice_ligne_depart + 1][indice_colonne_depart] == "X":
        return True
    elif direction == "3" and grille[indice_ligne_depart][indice_colonne_depart + 1] == "X":
        return True
    elif direction == "4" and grille[indice_ligne_depart][indice_colonne_depart - 1] == "X":
        return True
    return False

def a_voisin_direct_diagonale_joueur_2(grille, direction, indice_ligne_depart, indice_colonne_depart):
    if direction == "5" and grille[indice_ligne_depart - 1][indice_colonne_depart + 1] == "X":
            return True
    elif direction == "6" and grille[indice_ligne_depart + 1][indice_colonne_depart + 1] == "X":
            return True
    elif direction == "7" and grille[indice_ligne_depart - 1][indice_colonne_depart - 1] == "X":
            return True
    elif direction == "8" and grille[indice_ligne_depart + 1][indice_colonne_depart - 1] == "X":
            return True
    return False

def indices_case_arrivee_saut_orthogonal(indice_ligne_depart, indice_colonne_depart, direction):
    if direction == "1":
        return indice_ligne_depart - 2, indice_colonne_depart
    elif direction == "2":
        return indice_ligne_depart + 2, indice_colonne_depart
    elif direction == "3":
        return indice_ligne_depart, indice_colonne_depart + 2
    return indice_ligne_depart, indice_colonne_depart - 2

def indices_case_arrivee_saut_diagonale(indice_ligne_depart, indice_colonne_depart, direction):
    if direction == "5":
        return indice_ligne_depart - 2, indice_colonne_depart + 2
    elif direction == "6":
        return indice_ligne_depart + 2, indice_colonne_depart + 2
    elif direction == "7":
        return indice_ligne_depart - 2, indice_colonne_depart - 2
    return indice_ligne_depart + 2, indice_colonne_depart - 2

# Fonction validation si toutes les conditions sont respectées pour effectuer un déplacement par saut
def est_valide_deplacement_par_saut(grille, joueur, direction, indice_ligne_depart, indice_colonne_depart, indice_ligne_arrivee, indice_colonne_arrivee, indice_ligne_arrivee_diagonale, indice_colonne_arrivee_diagonale):
    if joueur == "Joueur 1":
        if direction in ["1","2","3","4"]:
            return a_choisi_pion_correct(grille, joueur, indice_ligne_depart, indice_colonne_depart) and est_dans_grille_apres_deplacement(direction, indice_ligne_arrivee, indice_colonne_arrivee, indice_ligne_arrivee_diagonale, indice_colonne_arrivee_diagonale) and a_voisin_direct_orthogonale_joueur_1(grille, direction, indice_ligne_depart, indice_colonne_depart) and est_vide_case_arrivee(grille, direction, indice_ligne_arrivee, indice_colonne_arrivee, indice_ligne_arrivee_diagonale, indice_colonne_arrivee_diagonale) and est_pas_dans_son_camp(joueur, indice_ligne_arrivee, indice_colonne_arrivee, indice_ligne_arrivee_diagonale, indice_colonne_arrivee_diagonale)
        return a_choisi_pion_correct(grille, joueur, indice_ligne_depart, indice_colonne_depart) and est_dans_grille_apres_deplacement(direction, indice_ligne_arrivee, indice_colonne_arrivee, indice_ligne_arrivee_diagonale, indice_colonne_arrivee_diagonale) and a_voisin_direct_diagonale_joueur_1(grille, direction, indice_ligne_depart, indice_colonne_depart) and est_vide_case_arrivee(grille, direction, indice_ligne_arrivee, indice_colonne_arrivee, indice_ligne_arrivee_diagonale, indice_colonne_arrivee_diagonale) and est_pas_dans_son_camp(joueur, indice_ligne_arrivee, indice_colonne_arrivee, indice_ligne_arrivee_diagonale, indice_colonne_arrivee_diagonale)
    elif direction in ["1","2","3","4"]:
        return a_choisi_pion_correct(grille, joueur, indice_ligne_depart, indice_colonne_depart) and est_dans_grille_apres_deplacement(direction, indice_ligne_arrivee, indice_colonne_arrivee, indice_ligne_arrivee_diagonale, indice_colonne_arrivee_diagonale) and a_voisin_direct_orthogonale_joueur_2(grille, direction, indice_ligne_depart, indice_colonne_depart) and est_vide_case_arrivee(grille, direction, indice_ligne_arrivee, indice_colonne_arrivee, indice_ligne_arrivee_diagonale, indice_colonne_arrivee_diagonale) and est_pas_dans_son_camp(joueur, indice_ligne_arrivee, indice_colonne_arrivee, indice_ligne_arrivee_diagonale, indice_colonne_arrivee_diagonale)
    return a_choisi_pion_correct(grille, joueur, indice_ligne_depart, indice_colonne_depart) and est_dans_grille_apres_deplacement(direction, indice_ligne_arrivee, indice_colonne_arrivee, indice_ligne_arrivee_diagonale, indice_colonne_arrivee_diagonale) and a_voisin_direct_diagonale_joueur_2(grille, direction, indice_ligne_depart, indice_colonne_depart) and est_vide_case_arrivee(grille, direction, indice_ligne_arrivee, indice_colonne_arrivee, indice_ligne_arrivee_diagonale, indice_colonne_arrivee_diagonale) and est_pas_dans_son_camp(joueur, indice_ligne_arrivee, indice_colonne_arrivee, indice_ligne_arrivee_diagonale, indice_colonne_arrivee_diagonale)

def choix_direction_deplacement_par_saut():
    print("\n- Haut : 1")
    print("- Bas : 2")
    print("- Droite : 3")
    print("- Gauche : 4")
    print("- Diagonale haut droite: 5")
    print("- Diagonale bas droite: 6")
    print("- Diagonale haut gauche: 7")
    print("- Diagonale bas gauche: 8")
    deplacement_souhaite = input("Saisissez le chiffre correspondant à la direction souhaitée : ")
    while not deplacement_souhaite in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        deplacement_souhaite = input("Erreur saisie, réessayez : ")
    return deplacement_souhaite

# Fonction de saisie des paramètres nécessaire au déplacement par saut
def saisie_utilisateur_deplacement_par_saut(grille, joueur):
    direction_deplacement = choix_direction_deplacement_par_saut()
    i_ligne_depart, i_colonne_depart = saisir_coordonnees()
    i_ligne_arrivee, i_colonne_arrivee = indices_case_arrivee_saut_orthogonal(i_ligne_depart, i_colonne_depart, direction_deplacement)
    i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale = indices_case_arrivee_saut_diagonale(i_ligne_depart, i_colonne_depart, direction_deplacement)
    while not est_valide_deplacement_par_saut(grille, joueur, direction_deplacement, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale):
        print("")
        print("Déplacement demandé impossible, réessayez :")
        direction_deplacement = choix_direction_deplacement_par_saut()
        i_ligne_depart, i_colonne_depart = saisir_coordonnees()
        i_ligne_arrivee, i_colonne_arrivee = indices_case_arrivee_saut_orthogonal(i_ligne_depart, i_colonne_depart, direction_deplacement)
        i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale = indices_case_arrivee_saut_diagonale(i_ligne_depart, i_colonne_depart, direction_deplacement)
    return direction_deplacement, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale

# Fonction pour effectuer le déplacement par saut à un pion
def deplacement_par_saut(grille, joueur, direction, indice_ligne_depart, indice_colonne_depart, indice_ligne_arrivee, indice_colonne_arrivee, indice_ligne_arrivee_diagonale, indice_colonne_arrivee_diagonale):
    if direction in ["1", "2", "3", "4"]:
        grille[indice_ligne_depart][indice_colonne_depart], grille[indice_ligne_arrivee][indice_colonne_arrivee] = grille[indice_ligne_arrivee][indice_colonne_arrivee], grille[indice_ligne_depart][indice_colonne_depart]
    else:
        grille[indice_ligne_depart][indice_colonne_depart], grille[indice_ligne_arrivee_diagonale][indice_colonne_arrivee_diagonale] = grille[indice_ligne_arrivee_diagonale][indice_colonne_arrivee_diagonale], grille[indice_ligne_depart][indice_colonne_depart]
    afficher_grille(grille, joueur)
    
# Fonction tour de jeu d'un déplacement par saut
def choix_deplacement_par_saut(grille, joueur):
    if joueur == "Joueur 1":
        direction_deplacement, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale = saisie_utilisateur_deplacement_par_saut(grille, joueur)
        deplacement_par_saut(grille, joueur, direction_deplacement, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale)
    else:
        direction_deplacement, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale = saisie_utilisateur_deplacement_par_saut(grille, joueur)
        deplacement_par_saut(grille, joueur, direction_deplacement, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale)
    return direction_deplacement, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale
    
###############################
###   PARTIE ENCHAINEMENT   ###
###############################

def a_enchainement_possible_joueur_1(grille, direction, indice_ligne_depart, indice_colonne_depart):
    if (2 <= indice_ligne_depart <= 5) and (2 <= indice_colonne_depart <= 5):
        if direction == "1":
            return (grille[indice_ligne_depart - 1][indice_colonne_depart] == "O" and grille[indice_ligne_depart - 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart][indice_colonne_depart + 1] == "O" and grille[indice_ligne_depart][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart][indice_colonne_depart - 1] == "O" and grille[indice_ligne_depart][indice_colonne_depart - 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart + 1] == "O" and grille[indice_ligne_depart - 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart + 1] == "O" and grille[indice_ligne_depart + 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart - 1] == "O" and grille[indice_ligne_depart - 2][indice_colonne_depart - 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart - 1] == "O" and grille[indice_ligne_depart + 2][indice_colonne_depart - 2] == 0)
        elif direction == "2":
            return (grille[indice_ligne_depart + 1][indice_colonne_depart] == "O" and grille[indice_ligne_depart + 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart][indice_colonne_depart + 1] == "O" and grille[indice_ligne_depart][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart][indice_colonne_depart - 1] == "O" and grille[indice_ligne_depart][indice_colonne_depart - 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart + 1] == "O" and grille[indice_ligne_depart - 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart + 1] == "O" and grille[indice_ligne_depart + 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart - 1] == "O" and grille[indice_ligne_depart - 2][indice_colonne_depart - 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart - 1] == "O" and grille[indice_ligne_depart + 2][indice_colonne_depart - 2] == 0)
        elif direction == "3":
            return (grille[indice_ligne_depart - 1][indice_colonne_depart] == "O" and grille[indice_ligne_depart - 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart] == "O" and grille[indice_ligne_depart + 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart][indice_colonne_depart + 1] == "O" and grille[indice_ligne_depart][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart + 1] == "O" and grille[indice_ligne_depart - 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart + 1] == "O" and grille[indice_ligne_depart + 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart - 1] == "O" and grille[indice_ligne_depart - 2][indice_colonne_depart - 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart - 1] == "O" and grille[indice_ligne_depart + 2][indice_colonne_depart - 2] == 0)
        elif direction == "4":
            return (grille[indice_ligne_depart - 1][indice_colonne_depart] == "O" and grille[indice_ligne_depart - 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart] == "O" and grille[indice_ligne_depart + 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart][indice_colonne_depart - 1] == "O" and grille[indice_ligne_depart][indice_colonne_depart - 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart + 1] == "O" and grille[indice_ligne_depart - 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart + 1] == "O" and grille[indice_ligne_depart + 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart - 1] == "O" and grille[indice_ligne_depart - 2][indice_colonne_depart - 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart - 1] == "O" and grille[indice_ligne_depart + 2][indice_colonne_depart - 2] == 0)
        elif direction == "5":
            return (grille[indice_ligne_depart - 1][indice_colonne_depart] == "O" and grille[indice_ligne_depart - 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart] == "O" and grille[indice_ligne_depart + 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart][indice_colonne_depart + 1] == "O" and grille[indice_ligne_depart][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart][indice_colonne_depart - 1] == "O" and grille[indice_ligne_depart][indice_colonne_depart - 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart + 1] == "O" and grille[indice_ligne_depart - 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart + 1] == "O" and grille[indice_ligne_depart + 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart - 1] == "O" and grille[indice_ligne_depart - 2][indice_colonne_depart - 2] == 0)
        elif direction == "6":
            return (grille[indice_ligne_depart - 1][indice_colonne_depart] == "O" and grille[indice_ligne_depart - 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart] == "O" and grille[indice_ligne_depart + 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart][indice_colonne_depart + 1] == "O" and grille[indice_ligne_depart][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart][indice_colonne_depart - 1] == "O" and grille[indice_ligne_depart][indice_colonne_depart - 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart + 1] == "O" and grille[indice_ligne_depart - 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart + 1] == "O" and grille[indice_ligne_depart + 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart - 1] == "O" and grille[indice_ligne_depart + 2][indice_colonne_depart - 2] == 0)
        elif direction =="7":
            return (grille[indice_ligne_depart - 1][indice_colonne_depart] == "O" and grille[indice_ligne_depart - 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart] == "O" and grille[indice_ligne_depart + 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart][indice_colonne_depart + 1] == "O" and grille[indice_ligne_depart][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart][indice_colonne_depart - 1] == "O" and grille[indice_ligne_depart][indice_colonne_depart - 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart + 1] == "O" and grille[indice_ligne_depart - 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart - 1] == "O" and grille[indice_ligne_depart - 2][indice_colonne_depart - 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart - 1] == "O" and grille[indice_ligne_depart + 2][indice_colonne_depart - 2] == 0)
        return (grille[indice_ligne_depart - 1][indice_colonne_depart] == "O" and grille[indice_ligne_depart - 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart] == "O" and grille[indice_ligne_depart + 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart][indice_colonne_depart + 1] == "O" and grille[indice_ligne_depart][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart][indice_colonne_depart - 1] == "O" and grille[indice_ligne_depart][indice_colonne_depart - 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart + 1] == "O" and grille[indice_ligne_depart + 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart - 1] == "O" and grille[indice_ligne_depart - 2][indice_colonne_depart - 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart - 1] == "O" and grille[indice_ligne_depart + 2][indice_colonne_depart - 2] == 0)
    return True

def a_enchainement_possible_joueur_2(grille, direction, indice_ligne_depart, indice_colonne_depart):
    if (2 <= indice_ligne_depart <= 5) and (2 <= indice_colonne_depart <= 5):
        if direction == "1":
            return (grille[indice_ligne_depart - 1][indice_colonne_depart] == "X" and grille[indice_ligne_depart - 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart][indice_colonne_depart + 1] == "X" and grille[indice_ligne_depart][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart][indice_colonne_depart - 1] == "X" and grille[indice_ligne_depart][indice_colonne_depart - 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart + 1] == "X" and grille[indice_ligne_depart - 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart + 1] == "X" and grille[indice_ligne_depart + 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart - 1] == "X" and grille[indice_ligne_depart - 2][indice_colonne_depart - 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart - 1] == "X" and grille[indice_ligne_depart + 2][indice_colonne_depart - 2] == 0)
        elif direction == "2":
            return (grille[indice_ligne_depart + 1][indice_colonne_depart] == "X" and grille[indice_ligne_depart + 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart][indice_colonne_depart + 1] == "X" and grille[indice_ligne_depart][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart][indice_colonne_depart - 1] == "X" and grille[indice_ligne_depart][indice_colonne_depart - 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart + 1] == "X" and grille[indice_ligne_depart - 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart + 1] == "X" and grille[indice_ligne_depart + 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart - 1] == "X" and grille[indice_ligne_depart - 2][indice_colonne_depart - 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart - 1] == "X" and grille[indice_ligne_depart + 2][indice_colonne_depart - 2] == 0)
        elif direction == "3":
            return (grille[indice_ligne_depart - 1][indice_colonne_depart] == "X" and grille[indice_ligne_depart - 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart] == "X" and grille[indice_ligne_depart + 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart][indice_colonne_depart + 1] == "X" and grille[indice_ligne_depart][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart + 1] == "X" and grille[indice_ligne_depart - 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart + 1] == "X" and grille[indice_ligne_depart + 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart - 1] == "X" and grille[indice_ligne_depart - 2][indice_colonne_depart - 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart - 1] == "X" and grille[indice_ligne_depart + 2][indice_colonne_depart - 2] == 0)
        elif direction == "4":
            return (grille[indice_ligne_depart - 1][indice_colonne_depart] == "X" and grille[indice_ligne_depart - 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart] == "X" and grille[indice_ligne_depart + 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart][indice_colonne_depart - 1] == "X" and grille[indice_ligne_depart][indice_colonne_depart - 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart + 1] == "X" and grille[indice_ligne_depart - 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart + 1] == "X" and grille[indice_ligne_depart + 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart - 1] == "X" and grille[indice_ligne_depart - 2][indice_colonne_depart - 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart - 1] == "X" and grille[indice_ligne_depart + 2][indice_colonne_depart - 2] == 0)
        elif direction == "5":
            return (grille[indice_ligne_depart - 1][indice_colonne_depart] == "X" and grille[indice_ligne_depart - 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart] == "X" and grille[indice_ligne_depart + 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart][indice_colonne_depart + 1] == "X" and grille[indice_ligne_depart][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart][indice_colonne_depart - 1] == "X" and grille[indice_ligne_depart][indice_colonne_depart - 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart + 1] == "X" and grille[indice_ligne_depart - 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart + 1] == "X" and grille[indice_ligne_depart + 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart - 1] == "X" and grille[indice_ligne_depart - 2][indice_colonne_depart - 2] == 0)
        elif direction == "6":
            return (grille[indice_ligne_depart - 1][indice_colonne_depart] == "X" and grille[indice_ligne_depart - 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart] == "X" and grille[indice_ligne_depart + 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart][indice_colonne_depart + 1] == "X" and grille[indice_ligne_depart][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart][indice_colonne_depart - 1] == "X" and grille[indice_ligne_depart][indice_colonne_depart - 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart + 1] == "X" and grille[indice_ligne_depart - 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart + 1] == "X" and grille[indice_ligne_depart + 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart - 1] == "X" and grille[indice_ligne_depart + 2][indice_colonne_depart - 2] == 0)
        elif direction =="7":
            return (grille[indice_ligne_depart - 1][indice_colonne_depart] == "X" and grille[indice_ligne_depart - 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart] == "X" and grille[indice_ligne_depart + 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart][indice_colonne_depart + 1] == "X" and grille[indice_ligne_depart][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart][indice_colonne_depart - 1] == "X" and grille[indice_ligne_depart][indice_colonne_depart - 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart + 1] == "X" and grille[indice_ligne_depart - 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart - 1] == "X" and grille[indice_ligne_depart - 2][indice_colonne_depart - 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart - 1] == "X" and grille[indice_ligne_depart + 2][indice_colonne_depart - 2] == 0)
        return (grille[indice_ligne_depart - 1][indice_colonne_depart] == "X" and grille[indice_ligne_depart - 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart] == "X" and grille[indice_ligne_depart + 2][indice_colonne_depart] == 0) or (grille[indice_ligne_depart][indice_colonne_depart + 1] == "X" and grille[indice_ligne_depart][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart][indice_colonne_depart - 1] == "X" and grille[indice_ligne_depart][indice_colonne_depart - 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart + 1] == "X" and grille[indice_ligne_depart + 2][indice_colonne_depart + 2] == 0) or (grille[indice_ligne_depart - 1][indice_colonne_depart - 1] == "X" and grille[indice_ligne_depart - 2][indice_colonne_depart - 2] == 0) or (grille[indice_ligne_depart + 1][indice_colonne_depart - 1] == "X" and grille[indice_ligne_depart + 2][indice_colonne_depart - 2] == 0)
    return True

def retourne_pas_en_arriere(direction_du_saut, direction_de_enchainement):
    if direction_du_saut == "1" and direction_de_enchainement == "2":
        return False
    elif direction_du_saut == "2" and direction_de_enchainement == "1":
        return False
    elif direction_du_saut == "3" and direction_de_enchainement == "4":
        return False
    elif direction_du_saut == "4" and direction_de_enchainement == "3":
        return False
    elif direction_du_saut == "5" and direction_de_enchainement == "8":
        return False
    elif direction_du_saut == "6" and direction_de_enchainement == "7":
        return False
    elif direction_du_saut == "7" and direction_de_enchainement == "6":
        return False
    elif direction_du_saut == "8" and direction_de_enchainement == "5":
        return False
    return True

def choix_direction_deplacement_pour_enchainement():
    print("\n- Haut : 1")
    print("- Bas : 2")
    print("- Droite : 3")
    print("- Gauche : 4")
    print("- Diagonale haut droite: 5")
    print("- Diagonale bas droite: 6")
    print("- Diagonale haut gauche: 7")
    print("- Diagonale bas gauche: 8")
    print("- Annuler : 9")
    deplacement_souhaite = input("Saisissez le chiffre correspondant à la direction souhaitée : ")
    while not deplacement_souhaite in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        deplacement_souhaite = input("Erreur saisie, réessayez : ")
    return deplacement_souhaite

# Fonction de saisie des paramètres nécessaire à l'enchainement
def saisie_utilisateur_deplacement_par_saut_enchainement(grille, joueur, direction_saut, indice_ligne_depart, indice_colonne_depart):
    direction_enchainement = choix_direction_deplacement_pour_enchainement()
    if direction_enchainement == "9":
        return direction_enchainement, indice_ligne_depart, indice_colonne_depart, indice_ligne_depart, indice_colonne_depart, indice_ligne_depart, indice_colonne_depart
    i_ligne_arrivee, i_colonne_arrivee = indices_case_arrivee_saut_orthogonal(indice_ligne_depart, indice_colonne_depart, direction_enchainement)
    i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale = indices_case_arrivee_saut_diagonale(indice_ligne_depart, indice_colonne_depart, direction_enchainement)
    while not est_valide_deplacement_par_saut(grille, joueur, direction_enchainement, indice_ligne_depart, indice_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale) or not retourne_pas_en_arriere(direction_saut, direction_enchainement):
        print("")
        print("Enchainement demandé impossible, réessayez")
        direction_enchainement = choix_direction_deplacement_pour_enchainement()
        if direction_enchainement == "9":
            return direction_enchainement, indice_ligne_depart, indice_colonne_depart, indice_ligne_depart, indice_colonne_depart, indice_ligne_depart, indice_colonne_depart
        i_ligne_arrivee, i_colonne_arrivee = indices_case_arrivee_saut_orthogonal(indice_ligne_depart, indice_colonne_depart, direction_enchainement)
        i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale = indices_case_arrivee_saut_diagonale(indice_ligne_depart, indice_colonne_depart, direction_enchainement)
    return direction_enchainement, indice_ligne_depart, indice_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale

# Fonction tour d'enchainement pour le joueur 1
def enchainement_joueur_1(grille, joueur, direction, indice_ligne_depart, indice_colonne_depart, indice_ligne_arrivee, indice_colonne_arrivee, indice_ligne_arrivee_diagonale, indice_colonne_arrivee_diagonale):
    i_ligne_depart, i_colonne_depart = actualisation_indices_depart_apres_saut(direction, indice_ligne_arrivee, indice_colonne_arrivee, indice_ligne_arrivee_diagonale, indice_colonne_arrivee_diagonale)
    reponse = "oui"
    direction_saut = direction
    while a_enchainement_possible_joueur_1(grille, direction_saut, i_ligne_depart, i_colonne_depart) and reponse == "oui":
        reponse = input("Voulez-vous faire un enchainement ? (oui/non) ")
        while not reponse in ["oui", "non"]:
            reponse = input("Erreur réponse, réessayez (oui/non) : ")
        if reponse == "oui":
            direction_enchainement, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale = saisie_utilisateur_deplacement_par_saut_enchainement(grille, joueur, direction_saut, i_ligne_depart, i_colonne_depart)
            if direction_enchainement != "9":
                deplacement_par_saut(grille, joueur, direction_enchainement, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale)
                i_ligne_depart, i_colonne_depart = actualisation_indices_depart_apres_saut(direction_enchainement, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale)
                direction_saut = direction_enchainement
            else:
                reponse = "non"
        else:
            return grille
        if est_terminee_partie(grille):
            reponse = "non"
    return grille

# Fonction tour d'enchainement pour le joueur 2
def enchainement_joueur_2(grille, joueur, direction, indice_ligne_depart, indice_colonne_depart, indice_ligne_arrivee, indice_colonne_arrivee, indice_ligne_arrivee_diagonale, indice_colonne_arrivee_diagonale):
    i_ligne_depart, i_colonne_depart = actualisation_indices_depart_apres_saut(direction, indice_ligne_arrivee, indice_colonne_arrivee, indice_ligne_arrivee_diagonale, indice_colonne_arrivee_diagonale)
    reponse = "oui"
    direction_saut = direction
    while a_enchainement_possible_joueur_2(grille, direction_saut, i_ligne_depart, i_colonne_depart) and reponse == "oui":
        reponse = input("\nVoulez-vous faire un enchainement ? (oui/non) ")
        while not reponse in ["oui", "non"]:
            reponse = input("Erreur réponse, réessayez (oui/non) : ")
        if reponse == "oui":
            direction_enchainement, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale = saisie_utilisateur_deplacement_par_saut_enchainement(grille, joueur, direction_saut, i_ligne_depart, i_colonne_depart)
            if direction_enchainement != "9":
                deplacement_par_saut(grille, joueur, direction_enchainement, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale)
                i_ligne_depart, i_colonne_depart = actualisation_indices_depart_apres_saut(direction_enchainement, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale)
                direction_saut = direction_enchainement
            else:
                reponse = "non"
        else:
            return grille
        if est_terminee_partie(grille):
            reponse = "non"
    return grille

#####################################################
###   PARTIE FONCTIONS UTILITAIRES POUR LES IA   ####
#####################################################
    
def anti_retour_arriere_orthogonal(direction):
    if direction == "1":
        return ["1","3","4","5","6","7","8"]
    elif direction == "2":
        return ["2","3","4","5","6","7","8"]
    elif direction == "3":
        return ["1","2","3","5","6","7","8"]
    return ["1","2","4","5","6","7","8"]

def anti_retour_arriere_diagonale(direction):
    if direction == "5":
        return ["1","2","3","4","5","6","7"]
    elif direction == "6":
        return ["1","2","3","4","5","6","8"]
    elif direction == "7":
        return ["1","2","3","4","5","7","8"]
    return ["1","2","3","4","6","7","8"]

############################
###   PARTIE IA NAIVE   ####
############################

# Fonction qui retourne la liste de tous les déplacements à domicile possible 
def liste_deplacement_a_domicile_ordinateur_possible_IAN(grille, joueur):
    liste_possible = []
    for direction in range(1,5):
        for distance in range(1,8):
            for ligne in range(8):
                for colonne in range(1,9):
                    i_ligne_depart, i_colonne_depart = indices_cases_depart(reperes_ligne[ligne], reperes_colonne[colonne])
                    i_ligne_arrivee, i_colonne_arrivee = indices_case_arrivee(i_ligne_depart, i_colonne_depart, str(distance), str(direction))
                    i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale = indices_case_arrivee_saut_diagonale(i_ligne_depart, i_colonne_depart, str(direction))
                    if est_valide_deplacement_a_domicile(grille, joueur, str(direction), str(distance), i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale):
                        liste_possible.append([i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee])
    return liste_possible

# Fonction qui retourne la liste de tous les déplacements par saut possible
def liste_deplacement_par_saut_ordinateur_possible_IAN(grille, joueur):
    liste_possible = []
    for direction in range(1,9):
        for ligne in range(8):
            for colonne in range(1,9):
                i_ligne_depart, i_colonne_depart = indices_cases_depart(reperes_ligne[ligne], reperes_colonne[colonne])
                i_ligne_arrivee, i_colonne_arrivee = indices_case_arrivee_saut_orthogonal(i_ligne_depart, i_colonne_depart, str(direction))
                i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale = indices_case_arrivee_saut_diagonale(i_ligne_depart, i_colonne_depart, str(direction))
                if est_valide_deplacement_par_saut(grille, joueur, str(direction), i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale):
                    liste_possible.append([str(direction), i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale])
    return liste_possible

# Fonction qui retourne la liste de tous les enchainements possible
def liste_deplacement_par_saut_enchainement_ordinateur_possible_IAN(grille, joueur, direction, i_ligne_ordinateur, i_colonne_ordinateur):
    liste_possible = []
    if direction in ["1","2","3","4"]:
        directions_possibles_enchainement = anti_retour_arriere_orthogonal(direction)
    else:
        directions_possibles_enchainement = anti_retour_arriere_diagonale(direction)
    for direction in directions_possibles_enchainement:
        i_ligne_arrivee, i_colonne_arrivee = indices_case_arrivee_saut_orthogonal(i_ligne_ordinateur, i_colonne_ordinateur, str(direction))
        i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale = indices_case_arrivee_saut_diagonale(i_ligne_ordinateur, i_colonne_ordinateur, str(direction))
        if est_valide_deplacement_par_saut(grille, joueur, direction, i_ligne_ordinateur, i_colonne_ordinateur, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale):
            liste_possible.append([direction, i_ligne_ordinateur, i_colonne_ordinateur, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale])
    return liste_possible

# Fonction tour de jeu d'un déplacement à domicile pour l'ordinateur IA Naïve
def deplacement_a_domicile_IAN_etapes(grille, joueur):
    deplacements_possibles = liste_deplacement_a_domicile_ordinateur_possible_IAN(grille, joueur)
    i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee = random.choice(deplacements_possibles)
    deplacement_a_domicile(grille, joueur, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee)

# Fonction tour de jeu d'un déplacement par saut puis d'un potentiel enchainement pour l'ordinateur IA Naïve
def deplacement_par_saut_IAN_etapes(grille, joueur):
    deplacement_possible = liste_deplacement_par_saut_ordinateur_possible_IAN(grille, joueur)
    direction, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale = random.choice(deplacement_possible)
    deplacement_par_saut(grille, joueur, direction, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale)
    enchainement = "oui"
    while not est_terminee_partie(grille) and not enchainement == "non":
        i_ligne_ordinateur, i_colonne_ordinateur = actualisation_indices_depart_apres_saut(direction, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale)
        deplacement_possible = liste_deplacement_par_saut_enchainement_ordinateur_possible_IAN(grille, joueur, direction, i_ligne_ordinateur, i_colonne_ordinateur)
        if not deplacement_possible == []:
            direction, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale = random.choice(deplacement_possible)
            deplacement_par_saut(grille, joueur, direction, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale)
            enchainement = random.choice(["oui"])
        else:
            enchainement = "non"
    
# Fonction tour de jeu de l'ordinateur IA Naïve
def deplacement_ordinateur_IAN(grille, joueur):
    deplacement_a_effectuer = random.choice(["Déplacement à domicile", "Déplacement par saut"])
        
    if deplacement_a_effectuer == "Déplacement à domicile":
        deplacement_a_domicile_IAN_etapes(grille, joueur)
    else:
        deplacement_par_saut_IAN_etapes(grille, joueur)
        
    return "non"

##############################
###   PARTIE IA AVANCEE   ####
##############################

# Fonction qui retourne la distance de déplacement la plus grande possible pour une liste contenant des déplacements à domicile possible
def plus_grande_distance(liste_deplacements_vers_camp_adverse):
    plus_grande_distance = liste_deplacements_vers_camp_adverse[0][4]
    for i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, distance in liste_deplacements_vers_camp_adverse:
        if distance > plus_grande_distance:
            plus_grande_distance = distance
    return plus_grande_distance

# Fonction qui retourne les deux listes de déplacement à domicile : les déplacements vers le camp adverse et tous les autres
def listes_deplacement_a_domicile_ordinateur_possible_IAA_etapes(grille, joueur):
    liste_possible_normal = []
    liste_possible_vers_camp_adverse = []
    for direction in range(1,5):
        for distance in range(1,8):
            for ligne in range(8):
                for colonne in range(1,9):
                    i_ligne_depart, i_colonne_depart = indices_cases_depart(reperes_ligne[ligne], reperes_colonne[colonne])
                    i_ligne_arrivee, i_colonne_arrivee = indices_case_arrivee(i_ligne_depart, i_colonne_depart, str(distance), str(direction))
                    i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale = indices_case_arrivee_saut_diagonale(i_ligne_depart, i_colonne_depart, str(direction))
                    if est_valide_deplacement_a_domicile(grille, joueur, str(direction), str(distance), i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale) and direction == 1:
                        liste_possible_vers_camp_adverse.append([i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, distance])
                    elif est_valide_deplacement_a_domicile(grille, joueur, str(direction), str(distance), i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale):
                        liste_possible_normal.append([i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee])
    return liste_possible_normal, liste_possible_vers_camp_adverse

# Fonction qui retourne la liste des déplacements à domicile avec la plus grande distance possible
def liste_deplacement_avec_plus_grande_distance(liste_deplacements_vers_camp_adverse, distance_max):
    liste_deplacement_plus_grande_distance = []
    for i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, distance in liste_deplacements_vers_camp_adverse:
        if distance == distance_max:
            liste_deplacement_plus_grande_distance.append([i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee])
    return liste_deplacement_plus_grande_distance

# Fonction qui choisit l'une des deux listes de déplacements à domicile possible : la liste avec tous les déplacements qui ont la plus grande distance vers le camp adverse. Si aucun, alors tous les autres
def liste_deplacement_a_domicile_ordinateur_possible_IAA(grille, joueur):
    liste_possible_normal, liste_possible_vers_camp_adverse = listes_deplacement_a_domicile_ordinateur_possible_IAA_etapes(grille, joueur)
    if liste_possible_vers_camp_adverse != []:
        distance_max = plus_grande_distance(liste_possible_vers_camp_adverse)
        return liste_deplacement_avec_plus_grande_distance(liste_possible_vers_camp_adverse, distance_max)
    return liste_possible_normal

# Fonction qui retourne la liste des sauts possibles vers le camp adverse
def liste_deplacement_par_saut_ordinateur_possible_IAA_etapes(grille, joueur):
    liste_possible_vers_camp_adverse = []
    for direction in range(1,9):
        for ligne in range(8):
            for colonne in range(1,9):
                i_ligne_depart, i_colonne_depart = indices_cases_depart(reperes_ligne[ligne], reperes_colonne[colonne])
                i_ligne_arrivee, i_colonne_arrivee = indices_case_arrivee_saut_orthogonal(i_ligne_depart, i_colonne_depart, str(direction))
                i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale = indices_case_arrivee_saut_diagonale(i_ligne_depart, i_colonne_depart, str(direction))
                if est_valide_deplacement_par_saut(grille, joueur, str(direction), i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale) and direction == 1:
                    liste_possible_vers_camp_adverse.append([str(direction), i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale])
    return liste_possible_vers_camp_adverse

# Fonction qui retourne la liste des enchainements possibles vers le camp adverse
def liste_deplacement_par_saut_enchainement_ordinateur_possible_IAA_etapes(grille, joueur, direction, i_ligne_ordinateur, i_colonne_ordinateur):
    liste_possible_vers_camp_adverse = []
    if direction in ["1","2","3","4"]:
        directions_possibles_enchainement = anti_retour_arriere_orthogonal(direction)
    else:
        directions_possibles_enchainement = anti_retour_arriere_diagonale(direction)
    for direction in directions_possibles_enchainement:
        i_ligne_arrivee, i_colonne_arrivee = indices_case_arrivee_saut_orthogonal(i_ligne_ordinateur, i_colonne_ordinateur, str(direction))
        i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale = indices_case_arrivee_saut_diagonale(i_ligne_ordinateur, i_colonne_ordinateur, str(direction))
        if est_valide_deplacement_par_saut(grille, joueur, direction, i_ligne_ordinateur, i_colonne_ordinateur, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale) and direction == "1":
            liste_possible_vers_camp_adverse.append([direction, i_ligne_ordinateur, i_colonne_ordinateur, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale])
    return liste_possible_vers_camp_adverse

# Fonction qui effectue le déplacement à domicile en choisissant une possibilité au hasard de déplacement dans une liste donnée
def deplacement_a_domicile_IAA_etapes(grille, joueur):
    deplacements_possibles = liste_deplacement_a_domicile_ordinateur_possible_IAA(grille, joueur)
    i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee = random.choice(deplacements_possibles)
    deplacement_a_domicile(grille, joueur, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee)

# Fonction qui effectue le déplacement par saut et un/des potentiel(s) enchainement(s) vers le camp adverse. Si aucun, alors déplacement à domicile
def deplacement_par_saut_IAA_etapes(grille, joueur):
    liste_deplacement_possible = liste_deplacement_par_saut_ordinateur_possible_IAA_etapes(grille, joueur)
    if liste_deplacement_possible != []:
        direction, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale = random.choice(liste_deplacement_possible)
        deplacement_par_saut(grille, joueur, direction, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale)
        while a_enchainement_possible_joueur_2(grille, direction, i_ligne_depart, i_colonne_depart) or not est_terminee_partie(grille):
            i_ligne_ordinateur, i_colonne_ordinateur = actualisation_indices_depart_apres_saut(direction, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale)
            liste_deplacement_possible = liste_deplacement_par_saut_enchainement_ordinateur_possible_IAA_etapes(grille, joueur, direction, i_ligne_ordinateur, i_colonne_ordinateur)
            if not liste_deplacement_possible == []:
                direction, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale = random.choice(liste_deplacement_possible)
                deplacement_par_saut(grille, joueur, direction, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale)
            else:
                return False
    return liste_deplacement_possible
    
# Fonction tour de jeu de l'ordinateur IA Avancée
def deplacement_ordinateur_IAA(grille, joueur):
    deplacement_possible_saut = deplacement_par_saut_IAA_etapes(grille, joueur)
    
    # Si la liste des déplacements par saut vers le camp adverse est vide, alors l'IA Avancée effectue un déplacement à domicile vers le camp adverse
    # Si la liste n'est pas vide, c'est que l'IA Avancée a déjà effectué un déplacement par saut et potentiellement un/des enchainement(s)
    if deplacement_possible_saut == []:
        deplacement_a_domicile_IAA_etapes(grille, joueur)
    
    return "non"

#############################################################
###   PARTIE FONCTIONS UTILITAIRES POUR LES TOUR DE JEU   ###
#############################################################
    
def choix_type_deplacement():
    print("\n- Déplacement à domicile : 1")
    print("- Déplacement par saut : 2")
    type_deplacement_choisi = input("Saisissez le chiffre correspondant au déplacement souhaité : ")
    while not type_deplacement_choisi in ["1", "2"]:
        type_deplacement_choisi = input("Erreur saisie, réessayez : ")
    return type_deplacement_choisi

def actualisation_indices_depart_apres_saut(direction, indice_ligne_arrivee, indice_colonne_arrivee, indice_ligne_arrivee_diagonale, indice_colonne_arrivee_diagonale):
    if direction in ["1", "2", "3", "4"]:
        i_ligne_depart, i_colonne_depart = indice_ligne_arrivee, indice_colonne_arrivee
    else:
        i_ligne_depart, i_colonne_depart = indice_ligne_arrivee_diagonale, indice_colonne_arrivee_diagonale
    return i_ligne_depart, i_colonne_depart

def actualisation_joueur_courant_JcJ(grille, joueur):
    if not est_terminee_partie(grille):
        print ("\nActualisation du joueur suivant")
        if joueur == "Joueur 1":
            joueur = "Joueur 2"
        else:
            joueur = "Joueur 1"
        afficher_grille(grille, joueur)
    return joueur

def actualisation_joueur_courant_JcO(grille, joueur):
    if not est_terminee_partie(grille):
        print ("\nActualisation du joueur suivant")
        if joueur == "Joueur 1":
            joueur = "Ordinateur"
        else:
            joueur = "Joueur 1"
        afficher_grille(grille, joueur)
    return joueur

def actualisation_statut_partie(grille, reponse):
    if not est_terminee_partie(grille):
        reponse = input("\nVoulez-vous arrêter ? (oui/non) ")
        while not reponse in ["oui", "non"]:
            reponse = input("Erreur réponse, réessayez (oui/non) : ")
    return reponse

##############################
###   PARTIE TOUR DE JEU   ###
##############################

# Fonction tour de jeu Joueur contre Joueur
def tour_de_jeu_JcJ():
    # Choix random du joueur courant pour le premier tour
    joueur_courant = random.choice(["Joueur 1", "Joueur 2"])
    print ("Le",joueur_courant,"commence la partie !")
    # Choix d'une grille par l'utilisateur qui commence la partie
    grille_choisie = choix_grille_courante(joueur_courant)
    
    reponse_statut_partie = "non"
    while not est_terminee_partie(grille_choisie) and not reponse_statut_partie == "oui":
        type_deplacement_choisi = choix_type_deplacement()
        
        # Déplacement à domicile
        if type_deplacement_choisi == "1":
            choix_deplacement_a_domicile(grille_choisie, joueur_courant)
            
        # Déplacement par saut
        else:
            direction_deplacement, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale = choix_deplacement_par_saut(grille_choisie, joueur_courant)
            # Enchainement joueur 1
            if joueur_courant == "Joueur 1" and not est_terminee_partie(grille_choisie):
                grille_choisie = enchainement_joueur_1(grille_choisie, joueur_courant, direction_deplacement, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale)
            # Enchainement joueur 2
            elif joueur_courant == "Joueur 2" and not est_terminee_partie(grille_choisie):
                grille_choisie = enchainement_joueur_2(grille_choisie, joueur_courant, direction_deplacement, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale)
                        
        # Actualisation de la grille avec mise à jour du joueur courant
        joueur_courant = actualisation_joueur_courant_JcJ(grille_choisie, joueur_courant)
    
        # Actualisation de poursuivre le tour de jeu pour l'utilisateur si la partie n'est pas terminée
        reponse_statut_partie = actualisation_statut_partie(grille_choisie, reponse_statut_partie)
    
    if not est_terminee_partie(grille_choisie):
        print ("\nPartie terminée !")
    else:
        print ("\n",joueur_courant,"a gagné !")

# Fonction tour de jeu pour la configuration JcO IA Naive
def tour_de_jeu_JcO_IANaive():
    # Choix random du joueur courant pour le premier tour
    joueur_courant = random.choice(["Joueur 1","Ordinateur"])
    print ("Le",joueur_courant,"commence la partie !")
    # Choix d'une grille par le joueur
    grille_choisie = choix_grille_courante(joueur_courant)
    
    reponse_statut_partie = "non"
    while not est_terminee_partie(grille_choisie) and not reponse_statut_partie == "oui":
        if joueur_courant == "Joueur 1":
            type_deplacement_choisi = choix_type_deplacement()
        
            # Déplacement à domicile
            if type_deplacement_choisi == "1":
                choix_deplacement_a_domicile(grille_choisie, joueur_courant)
            
            # Déplacement par saut
            else:
                direction_deplacement, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale = choix_deplacement_par_saut(grille_choisie, joueur_courant)
                reponse_enchainement = "oui"
                # Enchainement
                if not est_terminee_partie(grille_choisie):
                    grille_choisie = enchainement_joueur_1(grille_choisie, joueur_courant, direction_deplacement, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale, reponse_enchainement)
        
        else:
            deplacement_ordinateur_IAN(grille_choisie, joueur_courant)
        
        # Actualisation de la grille avec mise à jour du joueur courant
        joueur_courant = actualisation_joueur_courant_JcO(grille_choisie, joueur_courant)
    
        # Actualisation de poursuivre le tour de jeu pour l'utilisateur si la partie n'est pas terminée
        reponse_statut_partie = actualisation_statut_partie(grille_choisie, reponse_statut_partie)

    if not est_terminee_partie(grille_choisie):
        print ("\nPartie terminée !")
    else:
        print ("\n",joueur_courant,"a gagné !")
        
# Fonction tour de jeu pour la configuration JcO IA Avancée
def tour_de_jeu_JcO_IAAvancee():
    # Choix random du joueur courant pour le premier tour
    joueur_courant = random.choice(["Joueur 1","Ordinateur"])
    print ("Le",joueur_courant,"commence la partie !")
    # Choix d'une grille par le joueur
    grille_choisie = choix_grille_courante(joueur_courant)
    
    reponse_statut_partie = "non"
    while not est_terminee_partie(grille_choisie) and not reponse_statut_partie == "oui":
        if joueur_courant == "Joueur 1":
            type_deplacement_choisi = choix_type_deplacement()
        
            # Déplacement à domicile
            if type_deplacement_choisi == "1":
                choix_deplacement_a_domicile(grille_choisie, joueur_courant)
            
            # Déplacement par saut
            else:
                direction_deplacement, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale = choix_deplacement_par_saut(grille_choisie, joueur_courant)
                reponse_enchainement = "oui"
                # Enchainement
                if not est_terminee_partie(grille_choisie):
                    grille_choisie = enchainement_joueur_1(grille_choisie, joueur_courant, direction_deplacement, i_ligne_depart, i_colonne_depart, i_ligne_arrivee, i_colonne_arrivee, i_ligne_arrivee_diagonale, i_colonne_arrivee_diagonale, reponse_enchainement)
        
        else:
            deplacement_ordinateur_IAA(grille_choisie, joueur_courant)
        
        # Actualisation de la grille avec mise à jour du joueur courant
        joueur_courant = actualisation_joueur_courant_JcO(grille_choisie, joueur_courant)
    
        # Actualisation de poursuivre le tour de jeu pour l'utilisateur si la partie n'est pas terminée
        reponse_statut_partie = actualisation_statut_partie(grille_choisie, reponse_statut_partie)

    if not est_terminee_partie(grille_choisie):
        print ("\nPartie terminée !")
    else:
        print ("\n",joueur_courant,"a gagné !")
        
#############################
###   PARTIE MENU CHOIX   ###
#############################
        
def choix_configuration_jeu():
    print ("--------------------------------------------------------")
    print ("                      Menu :\n")
    print ("- Joueur contre Joueur : 1")
    print ("- Joueur contre Ordinateur IA Naïve: 2")
    print ("- Joueur contre Ordinateur IA Avancée : 3")
    print ("- Lancer programme de test : 4\n")
    choix_adversaire = input("Saisissez le chiffre correspondant au choix souhaité : ")
    while not choix_adversaire in ["1", "2", "3", "4"]:
        choix_adversaire = input("Erreur saisie, réessayez : ")
    print ("--------------------------------------------------------")
    if choix_adversaire == "1":
        tour_de_jeu_JcJ()
    elif choix_adversaire == "2":
        tour_de_jeu_JcO_IANaive()
    elif choix_adversaire == "3":
        tour_de_jeu_JcO_IAAvancee()
    elif choix_adversaire == "4":
        run_tests()
    
##################################
####   PARTIE FIN DE PARTIE   ####
##################################
    
def est_terminee_partie(grille):
    if not grille[0][3] == "X" and not grille[0][4] == "X" and not grille[7][3] == "O" and not grille[7][4] == "O":
        return False
    return True

##################################################################
####    PARTIE FONCTIONS TEST DES FONCTIONS DE VERIFICATION   ####
##################################################################

def test_est_pas_dans_son_camp():
    assert est_pas_dans_son_camp("Joueur 1", 2, 3, 0, 0), "erreur n'est pas dans son camp déplacement orthogonal"
    assert not est_pas_dans_son_camp("Joueur 2", 7, 4, 0, 0), "erreur dans son camp déplacement orthogonal"
    assert est_pas_dans_son_camp("Joueur 2", 0, 0, 4, 2), "erreur n'est pas dans son camp déplacement diagonale"
    assert not est_pas_dans_son_camp("Joueur 1", 0, 0, 0, 3), "erreur dans son camp déplacement diagonale"
    print ("\ntest_est_pas_dans_son_camp                  ✓")
    
def test_est_dans_grille():
    assert est_dans_grille("F4"), "erreur cas dans la grille"
    assert not est_dans_grille("g8"), "erreur hors ligne inferieure"
    assert not est_dans_grille("A9"), "erreur hors ligne superieure"
    assert not est_dans_grille("H-1"), "erreur hors colonne inferieure"
    assert not est_dans_grille("R9"), "erreur hors colonne superieure"
    print ("test_est_dans_grille                        ✓")

def test_a_choisi_pion_correct():
    grille_test = [[0, 0, 0, 0, 0, 0, 0, 0],
                   ["O", 0, "O", 0, "X", 0, 0, 0],
                   [0, "O", 0, "O", 0, 0, 0, "O"],
                   [0, 0, 0, 0, "X", 0, 0, 0],
                   [0, 0, 0, 0, 0, "X", 0, 0],
                   ["X", 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, "X", "X", "X", "O", "X"],
                   [0, 0, 0, 0, 0, "O", "O", 0]]
    assert a_choisi_pion_correct(grille_test, "Joueur 1", 1, 2), "erreur pion choisi correct"
    assert not a_choisi_pion_correct(grille_test, "Joueur 1", 3, 4), "erreur pion choisi incorrect"
    print ("test_a_choisi_pion_correct                  ✓")

def test_est_dans_grille_apres_deplacement():
    assert est_dans_grille_apres_deplacement(1, 2, 3, 0, 0), "erreur dans la grille après déplacement"
    assert not est_dans_grille_apres_deplacement(6, 0, 0, 11, -1), "erreur n'est pas dans grille après déplacement"
    print ("test_est_dans_grille_apres_deplacement      ✓")

def test_a_pas_depasse_ligne_mediane():
    assert a_pas_depasse_ligne_mediane("Joueur 1", 2, 5), "erreur joueur 1 n'a pas depassé la ligne médiane"
    assert not a_pas_depasse_ligne_mediane("Joueur 1", 5, 3), "erreur joueur 1 a dépassé ligne médiane"
    print ("test_a_pas_depasse_ligne_mediane            ✓")

def test_est_dans_la_bonne_zone():
    assert est_dans_la_bonne_zone("Joueur 1", 3), "erreur dans la bonne zone"
    assert not est_dans_la_bonne_zone("Joueur 1", 6), "erreur n'est pas dans la bonne zone"
    print ("test_est_dans_la_bonne_zone                 ✓")

def test_est_vide_case_arrivee():
    grille_test = [[0, 0, 0, 0, 0, 0, 0, 0],
                   ["O", 0, "O", 0, "X", 0, 0, 0],
                   [0, "O", 0, "O", 0, 0, 0, "O"],
                   [0, 0, 0, 0, "X", 0, 0, 0],
                   [0, 0, 0, 0, 0, "X", 0, 0],
                   ["X", 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, "X", "X", "X", "O", "X"],
                   [0, 0, 0, 0, 0, "O", "O", 0]]
    assert est_vide_case_arrivee(grille_test, "4", 6, 2, 0, 0), "erreur case arrivee vide"
    assert not est_vide_case_arrivee(grille_test, "3", 6, 5, 6, 5), "erreur case arrivee non vide"
    print ("test_est_vide_case_arrivee                  ✓")

def test_a_voisin_direct_orthogonale_joueur_1():
    grille_test = [[0, 0, 0, 0, 0, 0, 0, 0],
                   [0, "O", "O", 0, "X", 0, 0, 0],
                   [0, "O", 0, "O", 0, 0, 0, "O"],
                   [0, 0, 0, 0, "X", 0, 0, 0],
                   [0, 0, 0, 0, 0, "X", 0, 0],
                   ["X", 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, "X", "X", "X", "O", "X"],
                   [0, 0, 0, 0, 0, "O", "O", 0]]
    assert a_voisin_direct_orthogonale_joueur_1(grille_test, "2", 1, 1), "erreur a voisin direct orthogonale joueur 1"
    assert not a_voisin_direct_orthogonale_joueur_1(grille_test, "4", 2, 7), "erreur non voisin direct orthogonale joueur 1"
    print ("test_a_voisin_direct_orthogonale_joueur_1   ✓")

def test_a_voisin_direct_diagonale_joueur_1():
    grille_test = [[0, 0, 0, 0, 0, 0, 0, 0],
                     ["O", 0, "O", 0, "O", 0, "O", 0],
                     [0, "O", 0, "O", 0, "O", 0, "O"],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     ["X", 0, "X", 0, "X", 0, "X", 0],
                     [0, "X", 0, "X", 0, "X", 0, "X"],
                     [0, 0, 0, 0, 0, 0, 0, 0]]
    assert a_voisin_direct_diagonale_joueur_1(grille_test, "6", 1, 0),"erreur voisin diagonale joueur 1"
    assert not a_voisin_direct_diagonale_joueur_1(grille_test, "8", 2, 3),"erreur non voisin diagonale joueur 1"
    print ("test_a_voisin_direct_diagonale_joueur_1     ✓")

def test_a_voisin_direct_orthogonale_joueur_2():
    grille_test = [[0, 0, 0, 0, 0, 0, 0, 0],
                   [0, "O", "O", 0, "X", 0, 0, 0],
                   [0, "O", 0, "O", 0, 0, 0, "O"],
                   [0, 0, 0, 0, "X", 0, 0, 0],
                   [0, 0, 0, 0, 0, "X", 0, 0],
                   ["X", 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, "X", "X", "X", "O", "X"],
                   [0, 0, 0, 0, 0, "O", "O", 0]]
    assert a_voisin_direct_orthogonale_joueur_2(grille_test, "4", 6, 4), "erreur a voisin direct orthogonale joueur 2"
    assert not a_voisin_direct_orthogonale_joueur_2(grille_test, "1", 6, 3), "erreur non voisin direct orthogonale joueur 2"
    print ("test_a_voisin_direct_orthogonale_joueur_2   ✓")

def test_a_voisin_direct_diagonale_joueur_2():
    grille_test = [[0, 0, 0, 0, 0, 0, 0, 0],
                   ["O", 0, "O", 0, "X", 0, 0, 0],
                   [0, "O", 0, "O", 0, 0, 0, "O"],
                   [0, 0, 0, 0, "X", 0, 0, 0],
                   [0, 0, 0, 0, 0, "X", 0, 0],
                   ["X", 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, "X", "X", "X", "O", "X"],
                   [0, 0, 0, 0, 0, "O", "O", 0]]
    assert a_voisin_direct_diagonale_joueur_2(grille_test, "6", 3, 4), "erreur voisin direct diagonale joueur 2"
    assert not a_voisin_direct_diagonale_joueur_2(grille_test, "5", 5, 0), "erreur non voisin direct diagonale joueur 2"
    print ("test_a_voisin_direct_diagonale_joueur_2     ✓")

def test_est_terminee_partie():
    grille_1 = [[0, 0, 0, 0, 0, 0, 0, 0],
                ["O", 0, "O", 0, "X", 0, 0, 0],
                [0, "O", 0, "O", 0, 0, 0, "O"],
                [0, 0, 0, 0, "X", 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                ["X", 0, 0, 0, "X", 0, 0, 0],
                [0, 0, 0, "X", "X", "X", "O", "X"],
                [0, 0, 0, 0, 0, "O", "O", 0]]
    assert not est_terminee_partie(grille_1), "erreur partie non terminée"
    grille_2 = [[0, 0, 0, 0, 0, 0, 0, 0],
                ["O", 0, "O", 0, "X", 0, 0, 0],
                [0, "O", 0, "O", 0, 0, 0, "O"],
                [0, 0, 0, 0, "X", 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                ["X", 0, 0, 0, "X", 0, 0, 0],
                [0, 0, 0, "X", 0, "X", "O", "X"],
                [0, 0, 0, 0, "O", "O", 0, 0]]
    assert est_terminee_partie(grille_2), "erreur partie terminée"
    print ("test_est_terminee_partie                    ✓")

def test_a_enchainement_possible_joueur_1():
    grille_test = [[0, 0, 0, 0, 0, "X", 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, "O", 0, "O", 0, "O", 0, 0],
                   [0, 0, "O", 0, "X", "O", 0, 0],
                   [0, 0, 0, 0, 0, "X", 0, 0],
                   ["X", 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, "X", "X", "X", "O", "X"],
                   [0, 0, 0, 0, 0, "O", "O", 0]]
    assert a_enchainement_possible_joueur_1(grille_test, "6", 3, 2), "erreur a enchainement possible joueur 1"
    assert not a_enchainement_possible_joueur_1(grille_test, "2", 3, 5), "erreur n'a pas d'enchainement possible joueur 1"
    print ("test_a_enchainement_possible_joueur_1       ✓")
    
def test_a_enchainement_possible_joueur_2():
    grille_test = [[0, 0, 0, 0, 0, "X", 0, 0],
                   [0, 0, "O", 0, 0, 0, 0, 0],
                   [0, "O", 0, "O", 0, 0, 0, "O"],
                   [0, 0, "O", 0, 0, "X", 0, 0],
                   ["X", 0, 0, "X", 0, "X", 0, 0],
                   [0, 0, 0, "X", 0, "X", 0, 0],
                   [0, 0, 0, 0, 0, 0, "O", "X"],
                   [0, 0, 0, 0, 0, "O", "O", 0]]
    assert a_enchainement_possible_joueur_2(grille_test, "1", 4, 5), "erreur a enchainement possible joueur 2"
    assert not a_enchainement_possible_joueur_2(grille_test, "1", 4, 3), "erreur n'a pas d'enchainement possible joueur 2"
    print ("test_a_enchainement_possible_joueur_2       ✓")
    
def test_retourne_pas_en_arriere():
    assert retourne_pas_en_arriere("1", "3"), "erreur retourne pas en arrière"
    assert not retourne_pas_en_arriere("3", "4"), "erreur retourne en arrière"
    assert retourne_pas_en_arriere("6", "12")
    print ("test_retourne_pas_en_arriere                ✓")
    
def run_tests():
    #fonctions utilitaires pour les deux déplacements
    test_est_pas_dans_son_camp()
    test_est_dans_grille_apres_deplacement()
    test_a_choisi_pion_correct()
    test_est_dans_grille()
    #fonctions test pour le déplacement à domicile
    test_est_dans_la_bonne_zone()
    test_a_pas_depasse_ligne_mediane()
    #fonctions test pour le déplacement par saut
    test_est_vide_case_arrivee()
    test_est_terminee_partie()
    test_a_voisin_direct_orthogonale_joueur_1()
    test_a_voisin_direct_diagonale_joueur_1()
    test_a_voisin_direct_orthogonale_joueur_2()
    test_a_voisin_direct_diagonale_joueur_2()
    #fonctions test pour l'enchainement
    test_a_enchainement_possible_joueur_1()
    test_a_enchainement_possible_joueur_2()
    test_retourne_pas_en_arriere()
    print ("\nToutes les fonctions de vérification sont ok\n")

###################################
####   PARTIE CODE PRINCIPAL   ####
###################################
    
choix_configuration_jeu()