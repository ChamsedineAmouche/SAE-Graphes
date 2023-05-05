def pref(u):
    if type(u) == str: # Vérifie si le paramètre est une chaîne de caractère.
        longueur = len(u)
        lst_pref = [u[:i] for i in range(longueur + 1)]
        return lst_pref
    else: # Si u n'est pas une chaine alors on affiche une erreur
        print("Erreur, le paramètre n'est pas une chaîne de caractère.")

def suf(u):
    if type(u) == str: # Vérifie si le paramètre est une chaîne de caractère.
        lst = []
        for i in range(len(u)+1):
            lst.append(u[i:len(u)]) # slice qui permet d'ajouter les suffixe en enlenvant une lettre a chaque fois
        return lst
    else: # Si u n'est pas une chaine alors on affiche une erreur
        print("Erreur, le paramètre n'est pas une chaîne de caractère.")

def fact(u):
    if type(u) == str: # Vérifie si le paramètre est une chaîne de caractère.
        facteurs = set() # Set pour éviter les doublons
        for i in range(len(u)):
            for j in range(i, len(u)+1):
                facteurs.add(u[i:j]) # ajoute la sous-chaîne de u allant de i à j inclus dans facteurs
        return sorted(list(facteurs))
    else :# Si u n'est pas une chaine alors on affiche une erreur
        print("Erreur, le paramètre n'est pas une chaîne de caractère.")

def miroir(u):
    if type(u) == str : #Vérifie si le paramètre est une chaîne de cractère.
        return u[::-1] #Renverse l'ordre des caractères
    else: #Si le paramètre n'est pas uen chaîne de caractère.
        print("Erreur, le paramètre n'est pas une chaîne de cractère.")
        
def concatene(L1, L2):
    if type(L1) == list and type(L2) == list: #Vérifie si les paramètres sont bien des listes.
        lst_concatene = [] #Initialisation de la liste contenant la concaténation.
        for element1 in L1: #On parcourt les élements de L1.
            for element2 in L2: #On parcourt les élements de L2.
                chaine_auxiliaire = element1 + element2 #On concatène.
                if chaine_auxiliaire not in lst_concatene: #Si la concaténation n'est pas déjà présente (Pour éviter les doublons !)
                    lst_concatene.append(chaine_auxiliaire) #On ajoute la concaténation à la liste.
        return lst_concatene
    else: #Si au moins un des paramètres n'est pas une liste.
        print("Erreur, vos paramètres ne sont pas des listes.")

def puis(L, n):
    if type(L) == list and type(n) == int: #Vérifie si les paramètres sont bien une liste et un entier
        L_puis = []
        if n == 0: #Puissance 0 donc on renvoit ''
            L_puis.append('')
            return L_puis
        else:
            for element in L: #On parcourt tous les mots de L
                for element2 in puis(L, n-1): #Récursivité, On parcourt tous les mots de L élevés à la puissance n-1
                    chaine_auxiliaire = element + element2 #On concatène
                    if chaine_auxiliaire not in L_puis: #Si la concaténation n'est pas déjà présente (Pour éviter les doublons !)
                        L_puis.append(chaine_auxiliaire)
            return L_puis
    else: #Si les paramètres ne sont pas valides.
        print("Erreur, vos paramètres ne sont pas une liste et un entier.")

def tousmots(L, n):
    if type(L) == list and type(n) == int: #Vérifie si les paramètres sont bien une liste et un entier
        lst = ['']
        for i in range(n):
            lst += puis(L, i+1)
        return lst

    else: #Si les paramètres ne sont pas valides.
        print("Erreur, vos paramètres ne sont pas une liste et un entier.")

def defauto():
    auto = {} #Initialisation du dictionnaire qui forme l'automate.
    alphabet = set(input("Entrez l'alphabet de l'automate, chaque lettres étant séparé par des espaces : ").split())
    auto['alphabet'] = sorted(list(alphabet))
    etats = set(input("Entrez les états de l'automate, chaque états étant séparés par des espaces : ").split())
    auto["etats"] = sorted(list(etats))
    auto["transitions"] = [] #Initialisation de la liste contenant les transitions.
    
    while True: #Pour pouvoir entrer autant de transitions que l'on souhaite
        transition = input("Entrez une transition sous la forme 'etat_depart étiquette etat_arrivee', ou appuyez sur Entrée pour terminer : ")
        if not transition:
            break #Pour sortir de la boucle une fois que l'utilisateur appuie sur Entrée sans avoir rien écrit
        transition = transition.split() 
        if len(transition) != 3: #Si la transition ne contient par 3 élements
            print("Erreur, la transition doit être de la forme 'etat_depart étiquette etat_arrivee'")
            continue
        etat_depart, etiquette, etat_arrivee = transition
        if etat_depart not in auto["etats"] or etat_arrivee not in auto["etats"]: #Si au moins l'un des états n'est pas dans les états de l'automate.
            print("Erreur, les états de la transition doivent appartenir à l'ensemble des états de l'automate")
            continue
        if etiquette not in auto["alphabet"]: #Si l'étiquette n'est pas dans l'alphabet de l'automate.
            print("Erreur, l'étiquette de la transition doit appartenir à l'alphabet de l'automate !")
            continue
        auto["transitions"].append([etat_depart, etiquette, etat_arrivee])
    
    I = input("Entrez l'ensemble des états initiaux, séparés par des espaces : ").split()
    auto["I"] = I
    F = input("Entrez l'ensemble des états finaux, séparés par des espaces : ").split()
    auto["F"] = F
    return auto

def lirelettre(T, E, a):
    lst_etats = []
    for transition in T:
        if transition[1] == a and transition[0] in E: # Si la lettre est a et que l'état de départ est dans E.
            lst_etats.append(transition[2]) # Pour ajouter l'état d'arriver
    return sorted(list(set(lst_etats))) # Pour renvoyer une liste triée et sans doublons

def liremot(T, E, mot):
    if mot == "":
        return E
    
    # On prend les états pouvant être atteint en lisant la premiere lettre
    etats_suivants = lirelettre(T, E, mot[0])
    
    # Si on a parcouru tout le mot, on renvoie les états atteints
    if len(mot) == 1:
        return etats_suivants
    
    # Sinon, on appelle récursivement la fonction en partant des états atteignables et en lisant le reste du mot
    return liremot(T, etats_suivants, mot[1:])


if __name__ == "__main__":
    print("Préfixe")
    print(pref('coucou'))
    print("\n Suffixe")
    print(suf('coucou'))
    print("\n Facteur")
    print(fact('coucou'))
    print("\n Miroir")
    print(miroir('coucou'))
    L1=['aa','ab','ba','bb']
    L2=['a', 'b']
    print(concatene(L1,L2))
    L1=['aa','ab','ba','bb']
    print(puis(L1,2))
    print("\n Tous Mots")
    print(tousmots(L2, 3))

    auto ={"alphabet":['a','b'],"etats": [1,2,3,4],
    "transitions":[[1,'a',2],[2,'a',2],[2,'b',3],[3,'a',4]],
    "I":[1],"F":[4]}

    print(lirelettre(auto["transitions"],auto["etats"],'a'))
    print(liremot(auto["transitions"],auto["etats"],'aba'))
    
    
