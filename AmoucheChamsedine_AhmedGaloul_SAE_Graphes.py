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

#1.2.3 Il est possible de définir une fonction qui calcule l'étoile d'un langage en théorie, mais il n'est pas possible de la faire pour tous les langages en pratique. Dans certains cas, il ne sera pas possible de lister explicitement toutes les concaténations possibles.

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

def accepte(auto ,mot):
    # On enregistre la liste des mots pouvant être lu par l'état initial
    lst = liremot(auto["transitions"], auto["I"], mot)
    present = False
    
    # On vérifie si au moins un état final de l'automate est présent dans la liste des mots lu dans lst
    for element in auto["F"]:
        if element in lst :
            present = True
            break
    return present


def langage_accept(auto, n):
    lst_langage_accept = [] #Initialisation de la liste des mots acceptés
    lst_tousmots = tousmots(auto['alphabet'], n) #On stocke tous les mots que l'alphabet permet de crée avec une longueur inférieur à n.
    for mot in lst_tousmots: #On parcourt cette liste.
        if accepte(auto , mot): #Si l'automate accepte le mot
            lst_langage_accept.append(mot) #alors on l'ajoute à notre liste des mots acceptés
    return lst_langage_accept #On retourne cette liste

#1.3.6 On ne peut  pas faire une fonction qui renvoie le langage accepté par un automate car il faudrait donner la liste de tous les mots accepté et cette liste peut être longue voir infinie

def deterministe(auto):
    if len(auto['I']) > 1: #Si l'automate possède plus d'un état initial, alors il n'est pas déterministe.
        return False
    else:
        transitions = auto['transitions']
        for transition in transitions: #On parcourt les transitions
            etat_source, etiquette, etat_arrive = transition
            for transition2 in transitions: #On reparcourt les transitions
                if transition == transition2: #On évite de confondre les même transitions  (vu qu'on les parcourt 2 fois !)
                    continue
                etat_source2, etiquette2, etat_arrive2 = transition2
                if etat_source == etat_source2 and etiquette == etiquette2 and etat_arrive != etat_arrive2: #On vérifie si il existe 2 transitions d'un même état avec la même étiquette mais vers un état d'arrivé différent !
                    return False #Si c'est le cas on return False
    return True #Si on ne tombe jamais sur le cas du dessus, on retourne True

def trouver_etat_determinise(auto):
    etats_determinises = [] #Liste qui stockera les nouveaux états déterminisés
    alphabet = auto['alphabet']
    transitions = auto['transitions']
    etats_initiaux = auto['I']
    
    
    etats_determinises.append(etats_initiaux) #On initialise la liste des états déterminisés avec l'état initial de l'automate
    
    for etat in etats_determinises: #On parcourt la liste des nouveaux états déterminisés
        for a in alphabet:
            ensemble = lirelettre(transitions, etat, a)   #On calcule l'ensemble des états atteignables en lisant la lettre a depuis l'ensemble d'états E
            if ensemble and ensemble not in etats_determinises: #Si l'ensemble n'est pas vide et qu'il n'est pas présent dans la liste des nouveaux états déterminisés
                etats_determinises.append(ensemble)
    
    return etats_determinises #On retourne la liste

def trouver_transitions_determinise(auto, etats):
    nouvelles_transitions = [] #liste contenant les nouvelles transitions
    for e in etats: #On parcourt les nouveaux etats
        for a in auto['alphabet']: #On parcourt chaque lettre
            transitions = auto['transitions'] #Calculer la liste d'états atteignables par la lettre a depuis l'état e
            lst = lirelettre(transitions, e, a) #appel de lirelettre pour lire la lettre a depuis l'etat e
            if lst: #si la liste d'états atteignable est non vide.
                e2_deter = etats.index(lst)  # trouver l'indice de la liste d'états e2 dans la liste des nouveaux états
                nouvelles_transitions.append([e, a, etats[e2_deter]]) # ajouter la transition e-a-e2 à la liste des nouvelles transitions
    return nouvelles_transitions #On retourne la liste contenant les nouvelles transitions
            
def trouver_etats_initiaux_determinise(auto):
    #Initialise la liste des nouveaux etats initiaux
    etats_initiaux_determinise = []
    etats_initiaux_determinise.append(auto['I']) 
    return etats_initiaux_determinise #On retourne la liste des nouveaux etats initiaux
    
def trouver_etats_finaux_determinise(auto, etats):
    etats_finaux = auto['F'] 
    nouveaux_etats_finaux = [] #Initialise la liste des nouveaux etats finaux
    for e in etats: #On parcourt les etats
        if set(e).intersection(set(etats_finaux)): #Si l'ensemble d'etats contient au moins un état final (l'utilisation d'ensemble est obligatoire pour l'utilisaton de la fonction intersection())
            nouveaux_etats_finaux.append(e) #Alors on ajoute cet état a la liste d'états finaux
    return nouveaux_etats_finaux #On retourne la liste des nouveaux etats finaux

def determinise(auto):
    if deterministe(auto):
        return auto
    else:
        auto_determinise =  {} #On initialise le nouvel automate déterminisé
        auto_determinise['alphabet'] = auto['alphabet']
        
        nouveaux_etats = trouver_etat_determinise(auto) #Créer les nouveaux états déterminisés
        
        nouvelles_transitions = trouver_transitions_determinise(auto, nouveaux_etats) #Créer les nouvelles transitions
        
        #Créer les nouveaux états initiaux et finaux
        nouveaux_etats_initiaux = trouver_etats_initiaux_determinise(auto)
        nouveaux_etats_finaux = trouver_etats_finaux_determinise(auto, nouveaux_etats)
        
        auto_determinise['etats'] = nouveaux_etats
        auto_determinise['transitions'] = nouvelles_transitions
        auto_determinise['I'] = nouveaux_etats_initiaux
        auto_determinise['F'] = nouveaux_etats_finaux
        
        return auto_determinise #On retourne l'automate déterminisé

def renommage(auto):
    com = 0
    chaine = str(auto) # On remet l'automate sous forme de chaine
    for i in range(len(auto['etats'])):
        chaine = chaine.replace(str(auto['etats'][i]), str(com)) # On remplace chaque état par le plus petit entier positif disponible
        com += 1
    return eval(chaine) # On retourne l'automate

def complet(auto):
    etats = auto['etats']
    alphabet = auto['alphabet']
    transitions = auto['transitions']
    
    for etat in etats: #On parcourt les etats
        for etiquette in alphabet: #On parcourt les lettres
            complet = False 
            for transition in transitions: #On parcourt les transitions
                if transition[0] == etat and transition[1] == etiquette: #Si une transition contenant l'etat et l'étiquette existe
                    complet=True #Alors pour l'instant l'automate est complet
                    break
            
            if not complet: #Si on n'a pas trouvé de transition
                return False    #Alors l'automate n'est pas complet

    return True #Si toutes les transitions ont été trouvés, alors l'automate est complet

def complete(auto):
    if complet(auto): #Si l'automate est déjà complet
        return auto
    else: 
        auto_complete = {} #On intialise le nouvel automate complété
        auto_complete['alphabet'] = auto['alphabet']
        auto_complete['etats'] = auto['etats']
        auto_complete['transitions'] = auto['transitions']
        auto_complete['I'] = auto['I']
        auto_complete['F'] = auto['F']
        
        #Rajout d'un état puits
        compteur_etats = 0
        for etats in auto_complete['etats']: #On parcourt les etats
            compteur_etats+=1
        auto_complete['etats'].append(compteur_etats) #On attribue l'entier suivant le dernier etat à l'état puit.
        
        #Rajout des nouvelles transitions
        for etat in auto_complete['etats']: #On parcourt les etats
            for etiquette in auto_complete['alphabet']: #On parcourt les lettres
                for transition in auto_complete['transitions']: #On parcourt les transitions
                    trouver = False
                    if transition[0] == etat and etiquette == transition[1]: #Si il existe au moins une transition contenant l'etat et l'étiquette
                        trouver = True
                        break
                if not trouver: #Si il n'existe pas de transition avec cet état et cette étiquette
                    auto_complete['transitions'].append([etat, etiquette, compteur_etats]) #Alors on ajoute une transition etat, etiquette, etat_puit
        return auto_complete #On retourne le nouvel automate complété
    
def complement(auto):
    auto_complement = auto.copy() #On créer un copie de l'automate pour pas modifier celui de base.
    auto_complement = determinise(auto_complement) #On déterminise
    auto_complement = renommage(auto_complement)
    auto_complement = complete(auto_complement) #On complète
    
    #On inverse les états terminaux
    auto_complement['F'].clear() #On vide la liste d'états terminaux
    for etat in auto_complement['etats']: #On parcourt tous les états
        if etat not in auto['F']: #Si l'état n'est pas dans les états terminaux de base
            auto_complement['F'].append(etat) #Alors l'état est un état terminal du complément
    return auto_complement #On retourne l'état complément.

def inter(auto1, auto2):
    if not deterministe(auto1) or not deterministe(auto2):
        print("Erreur, au moins l'un des deux automates n'est pas déterministe.")
    else:
        auto_produit = {}
        auto_produit['alphabet'] = auto1['alphabet']
        auto_produit['I'] = [(auto1['I'][0], auto2['I'][0])]
        
        auto_produit['etats'] = [auto_produit['I'][0]]
        auto_produit['transitions'] = []

        # Parcours de tous les états accessibles
        for etat in auto_produit['etats']:
            for lettre in auto_produit['alphabet']:
                # Recherche de la transition possible
                trans1 = [(s, a, e) for s, a, e in auto1['transitions'] if s == etat[0] and a == lettre]
                trans2 = [(s, a, e) for s, a, e in auto2['transitions'] if s == etat[1] and a == lettre]
                if trans1 and trans2:
                    # Ajout de l'état et de la transition
                    etat_arrivee = (trans1[0][2], trans2[0][2])
                    if etat_arrivee not in auto_produit['etats']:
                        auto_produit['etats'].append(etat_arrivee)
                    auto_produit['transitions'].append([etat, lettre, etat_arrivee])
        
        auto_produit['F'] = []
        for etat1 in auto1['F']:
            for etat2 in auto2['F']:
                auto_produit['F'].append((etat1, etat2))


        return auto_produit



def difference(auto1, auto2):
    if not deterministe(auto1) or not deterministe(auto2):
        print("Erreur, au moins l'un des deux automates n'est pas déterministe.")
    else:
        # Compléter les deux automates
        if not complete(auto1):
            auto1_complete = complete(auto1)
        else:
            auto1_complete = auto1
        
        if not complete(auto2):
            auto2_complete = complete(auto2)
        else:
            auto2_complete = auto2
        
        # Calculer l'intersection des deux automates complets
        auto_difference = inter(auto1_complete, auto2_complete)
        
        # Inverser les états finaux de l'automate produit
        auto_difference['F'].clear()
        for etat in auto_difference['etats']:
            if etat[0] in auto1_complete['F'] and etat[1] not in auto2_complete['F']:
                auto_difference['F'].append(etat)
                
        # Trier les états de l'automate différence
        auto_difference['etats'] = sorted(auto_difference['etats'], key=lambda x: (x[1], x[0]))
        
        return auto_difference

if __name__ == "__main__":
    print("Préfixe :")
    print(pref('coucou'))
    print("\nSuffixe :")
    print(suf('coucou'))
    print("\nFacteur :")
    print(fact('coucou'))
    print("\nMiroir :")
    print(miroir('coucou'))
    print("\nConcatène :")
    L1=['aa','ab','ba','bb']
    L2=['a', 'b']
    print(concatene(L1,L2))
    L1=['aa','ab','ba','bb']
    print("\nPuis :")
    print(puis(L1,2))
    print("\nTous Mots")
    print(tousmots(L2, 3))

    auto = {"alphabet":['a','b'],"etats": [1,2,3,4],
    "transitions":[[1,'a',2],[1,'a',1],[2,'a',2],[2,'b',3],[3,'a',4]],
    "I":[1],"F":[4]}

    print("\nlire lettre :")
    print(lirelettre(auto["transitions"],auto["etats"],'a'))
    
    print("\nliremot :")
    print(liremot(auto["transitions"],auto["etats"],'aba'))
    
    print("\naccepte :")
    print(accepte(auto, 'a'))
    
    print("\nlangage_accept :")
    print(langage_accept(auto, 3))
    
    auto0 ={"alphabet":['a','b'],"etats": [0,1,2,3],
    "transitions":[[0,'a',1],[1,'a',1],[1,'b',2],[2,'a',3]], "I":[0],"F":[3]}
    auto1 ={"alphabet":['a','b'],"etats": [0,1],
    "transitions":[[0,'a',0],[0,'b',1],[1,'b',1],[1,'a',1]], "I":[0],"F":[1]}
    auto2={"alphabet":['a','b'],"etats": [0,1],
    "transitions":[[0,'a',0],[0,'a',1],[1,'b',1],[1,'a',1]], "I":[0],"F":[1]}
    
    print("\ndéterministe :")
    print(deterministe(auto0))
    print(deterministe(auto1))
    print(deterministe(auto2))

    print("\ndéterminise :")
    print(determinise(auto2))
    
    print("\nrenommage :")
    print(renommage(determinise(auto2)))
    
    auto3 ={"alphabet":['a','b'],"etats": [0,1,2,],
    "transitions":[[0,'a',1],[0,'a',0],[1,'b',2],[1,'b',1]], "I":[0],"F":[2]}

    print("\ncomplet :")
    print(complet(auto0))
    print(complet(auto1))
    
    print("\ncomplete :")
    print(complete(auto0))
    
    print("\ncomplement :")
    print(complement(auto3))
    
    auto4 ={"alphabet":['a','b'],"etats": [0,1,2],
    "transitions":[[0,'a',1],[1,'b',2],[2,'b',2],[2,'a',2]], "I":[0],"F":[2]}
    auto5 ={"alphabet":['a','b'],"etats": [0,1,2],
    "transitions":[[0,'a',0],[0,'b',1],[1,'a',1],[1,'b',2],[2,'a',2],[2,'b',0]],
    "I":[0],"F":[0,1]}
    
    print("\ninter :")
    print(inter(auto4,auto5))
    print("\ninter & renommage:")
    print(renommage(inter(auto4,auto5)))
    
    print("\ndifference :")
    print(difference(auto4,auto5))
    print("\nrenommage & différence :")
    print(renommage(difference(auto4,auto5)))
