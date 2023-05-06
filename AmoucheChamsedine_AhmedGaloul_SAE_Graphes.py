def pref(u):
    """
    Cette fonction prend une chaîne de caractère en paramètre et renvoie une liste contenant tous les préfixes de la chaîne.
    Si le paramètre n'est pas une chaîne de caractère, la fonction affiche un message d'erreur.

    Args:
        u (str): une chaîne de caractère

    Returns:
        list: une liste contenant tous les préfixes de la chaîne
    """
    if type(u) == str:
        longueur = len(u)
        lst_pref = [u[:i] for i in range(longueur + 1)]
        return lst_pref
    else:
        print("Erreur, le paramètre n'est pas une chaîne de caractère.")


def suf(u):
    """
    Cette fonction prend une chaîne de caractère en paramètre et renvoie une liste contenant tous les suffixes de la chaîne.
    Si le paramètre n'est pas une chaîne de caractère, la fonction affiche un message d'erreur.

    Args:
        u (str): une chaîne de caractère

    Returns:
        list: une liste contenant tous les suffixes de la chaîne
    """
    if type(u) == str:
        lst = []
        for i in range(len(u)+1):
            lst.append(u[i:len(u)])
        return lst
    else:
        print("Erreur, le paramètre n'est pas une chaîne de caractère.")


def fact(u):
    """
    Cette fonction prend une chaîne de caractère en paramètre et renvoie une liste contenant tous les facteurs de la chaîne.
    Si le paramètre n'est pas une chaîne de caractère, la fonction affiche un message d'erreur.

    Args:
        u (str): une chaîne de caractère

    Returns:
        list: une liste contenant tous les facteurs de la chaîne, triée par ordre alphabétique
    """
    if type(u) == str:
        facteurs = set()
        for i in range(len(u)):
            for j in range(i, len(u)+1):
                facteurs.add(u[i:j])
        return sorted(list(facteurs))
    else:
        print("Erreur, le paramètre n'est pas une chaîne de caractère.")


def miroir(u):
    """
    Cette fonction prend une chaîne de caractère en paramètre et renvoie la chaîne renversée.
    Si le paramètre n'est pas une chaîne de caractère, la fonction affiche un message d'erreur.

    Args:
        u (str): une chaîne de caractère

    Returns:
        str: la chaîne renversée
    """
    if type(u) == str:
        return u[::-1]
    else:
        print("Erreur, le paramètre n'est pas une chaîne de caractère.")

        
def concatene(L1, L2):
    """
    Cette fonction prend en entrée deux listes de chaînes de caractères et renvoie toutes les
    concaténations possibles entre les éléments de ces deux listes. Si les deux listes ne sont pas
    valides, un message d'erreur sera affiché.
    
    Args:
    - L1 (list): La première liste de chaînes de caractères
    - L2 (list): La deuxième liste de chaînes de caractères
    
    Returns:
    - lst_concatene (list): La liste de toutes les concaténations possibles entre les deux listes.
    """
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
    """
    Cette fonction prend en entrée une liste de chaînes de caractères et un entier n et renvoie
    toutes les chaînes de caractères obtenues en concaténant des éléments de la liste L n fois. Si
    les arguments ne sont pas valides, un message d'erreur sera affiché.
    
    Args:
    - L (list): La liste de chaînes de caractères à élever à la puissance n
    - n (int): La puissance à laquelle élever la liste L
    
    Returns:
    - L_puis (list): La liste de toutes les chaînes de caractères obtenues en concaténant des
    éléments de la liste L n fois.
    """
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
    """
    Cette fonction prend en entrée une liste de chaînes de caractères et un entier n et renvoie
    toutes les chaînes de caractères qui peuvent être obtenues en concaténant des éléments de la
    liste L entre 1 et n fois. Si les arguments ne sont pas valides, un message d'erreur sera
    affiché.

    Args:
    - L (list): La liste de chaînes de caractères à utiliser pour former les mots.
    - n (int): Le nombre maximal de fois que l'on peut concaténer les chaînes de caractères de la liste L.

    Returns:
    - lst (list): La liste de toutes les chaînes de caractères obtenues en concaténant des éléments
    de la liste L entre 1 et n fois.
    """
    if type(L) == list and type(n) == int: #Vérifie si les paramètres sont bien une liste et un entier
        lst = ['']
        for i in range(n):
            lst += puis(L, i+1)
        return lst

    else: #Si les paramètres ne sont pas valides.
        print("Erreur, vos paramètres ne sont pas une liste et un entier.")

def defauto():
    """
    Fonction permettant à l'utilisateur de définir un automate.
    Cette fonction demande à l'utilisateur de saisir l'alphabet, les états, les transitions, les états initiaux
    et les états finaux de l'automate.
    La fonction renvoie le dictionnaire représentant l'automate ainsi créé, avec les clés "alphabet", "etats",
    "transitions", "I" et "F".
    Args:
    - L (list): La liste de chaînes de caractères à utiliser pour former les mots.
    - n (int): Le nombre maximal de fois que l'on peut concaténer les chaînes de caractères de la liste L.

    Returns:
    - lst (list): La liste de toutes les chaînes de caractères obtenues en concaténant des éléments
    de la liste L entre 1 et n fois.
    """
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
    """
    Fonction qui prend en entrée une liste de transitions T, un ensemble d'états E et une lettre a.
    Elle renvoie l'ensemble des états atteignables depuis E en lisant la lettre a.
    
    Args:
    - T: Une liste de transitions de l'automate. Chaque transition est une liste de trois éléments: l'état de départ, l'étiquette et l'état d'arrivée.
    - E: Une liste contenant les états de départ pour la lecture de la lettre.
    - a: La lettre à lire.

    Returns:
    - Une liste contenant les états d'arrivée possibles en lisant la lettre a depuis les états de départ E.
    """
    lst_etats = []
    for transition in T:
        if transition[1] == a and transition[0] in E: # Si la lettre est a et que l'état de départ est dans E.
            lst_etats.append(transition[2]) # Pour ajouter l'état d'arriver
    return sorted(list(set(lst_etats))) # Pour renvoyer une liste triée et sans doublons

def liremot(T, E, mot):
    """
    Cette fonction renvoie une liste contenant les états d'arrivée possibles en lisant un mot donné depuis un ensemble d'états donné.
    
    Args:
        - T: Une liste de transitions de l'automate. Chaque transition est une liste de trois éléments: l'état de départ, l'étiquette et l'état d'arrivée.
        - E: Une liste contenant les états de départ pour la lecture du mot.
        - mot: Le mot à lire.
        
    Returns:
        - Une liste contenant les états d'arrivée possibles en lisant le mot mot depuis les états de départ E.
    """
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
    """
    Vérifie si l'automate reconnaît le mot donné en entrée.

    Args:
        auto (dict): Dictionnaire représentant l'automate.
        mot (str): Mot dont on veut vérifier la reconnaissance par l'automate.

    Returns:
        bool: True si le mot est reconnu par l'automate, False sinon.
    """
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
    """
    Renvoie la liste des mots de longueur n reconnus par l'automate.
    
    Args:
        auto (dict): Dictionnaire représentant l'automate.
        n (int): Longueur des mots à considérer.
    
    Returns:
        list: Liste des mots de longueur n reconnus par l'automate.
    """
    lst_langage_accept = [] #Initialisation de la liste des mots acceptés
    lst_tousmots = tousmots(auto['alphabet'], n) #On stocke tous les mots que l'alphabet permet de crée avec une longueur inférieur à n.
    for mot in lst_tousmots: #On parcourt cette liste.
        if accepte(auto , mot): #Si l'automate accepte le mot
            lst_langage_accept.append(mot) #alors on l'ajoute à notre liste des mots acceptés
    return lst_langage_accept #On retourne cette liste

#1.3.6 On ne peut  pas faire une fonction qui renvoie le langage accepté par un automate car il faudrait donner la liste de tous les mots accepté et cette liste peut être longue voir infinie

def deterministe(auto):
    """
       Vérifie si l'automate est déterministe.
    
       Args:
           auto (dict): Dictionnaire représentant l'automate.
    
       Returns:
           bool: True si l'automate est déterministe, False sinon.
   """
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
    """
    Fonction qui prend en entrée un automate non-déterministe et retourne la liste des états de l'automate déterminisé.

    Args:
        auto (dict): automate non-déterministe sous forme d'un dictionnaire contenant:
            - "alphabet": l'alphabet de l'automate (liste de caractères).
            - "transitions": les transitions de l'automate (liste de tuples (e1, a, e2) où e1 et e2 sont des ensembles d'états et a est un caractère).
            - "I": l'ensemble des états initiaux (liste d'états).
            - "F": l'ensemble des états finaux (liste d'états).

    Returns:
        list: la liste des états de l'automate déterminisé.
    """
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
    """
    Trouve les nouvelles transitions pour un automate déterminisé.
    
    Args:
    - auto (dict): un automate non-déterminisé sous forme d'un dictionnaire.
    - etats (list): une liste d'états pour l'automate déterminisé.
    
    Returns:
    - nouvelles_transitions (list): une liste contenant les nouvelles transitions sous forme de listes d'états et de lettre.
    """
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
    """
    Cette fonction prend en entrée un automate non déterministe et retourne une liste contenant les nouveaux états initiaux
    de l'automate déterminisé.
    
    Args:
        auto (dict): l'automate non déterministe
        
    Returns:
        list: une liste contenant les nouveaux états initiaux de l'automate déterminisé.
    """
    #Initialise la liste des nouveaux etats initiaux
    etats_initiaux_determinise = []
    etats_initiaux_determinise.append(auto['I']) 
    return etats_initiaux_determinise #On retourne la liste des nouveaux etats initiaux
    
def trouver_etats_finaux_determinise(auto, etats):
    """
    Cette fonction prend en entrée un automate non déterministe et une liste d'états de l'automate déterminisé,
    et retourne une liste contenant les nouveaux états finaux de l'automate déterminisé.
    
    Args:
        auto (dict): l'automate non déterministe
        etats (list): une liste d'états de l'automate déterminisé
        
    Returns:
        list: une liste contenant les nouveaux états finaux de l'automate déterminisé.
    """
    etats_finaux = auto['F'] 
    nouveaux_etats_finaux = [] #Initialise la liste des nouveaux etats finaux
    for e in etats: #On parcourt les etats
        if set(e).intersection(set(etats_finaux)): #Si l'ensemble d'etats contient au moins un état final (l'utilisation d'ensemble est obligatoire pour l'utilisaton de la fonction intersection())
            nouveaux_etats_finaux.append(e) #Alors on ajoute cet état a la liste d'états finaux
    return nouveaux_etats_finaux #On retourne la liste des nouveaux etats finaux

def determinise(auto):
    """
    Cette fonction prend en entrée un automate non déterministe et retourne l'automate déterminisé.
    
    Args:
        auto (dict): l'automate non déterministe
        
    Returns:
        dict: l'automate déterminisé.
    """
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
    """
    Renomme les états d'un automate en les remplaçant par les plus petits entiers positifs disponibles.
    
    Args:
    - auto (dict): un automate sous forme d'un dictionnaire.
    
    Returns:
    - auto (dict): l'automate avec les états renommés.
    """
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
    
def est_emonde(auto):
    """
    Vérifie si un automate fini déterministe est un automate émondé.
    
    Un automate est émondé s'il satisfait les conditions suivantes:

    Args:
        auto (dict): Un dictionnaire représentant l'automate fini déterministe.

    Returns:
        bool: True si l'automate est émondé, False sinon.
    """
    # Vérifier que tous les états ont au plus une transition pour chaque symbole de l'alphabet.
    for etat in auto["etats"]:
        transitions_etat = [t for t in auto["transitions"] if t[0] == etat]
        symboles_transitions = set([t[1] for t in transitions_etat])
        if len(symboles_transitions) != len(auto["alphabet"]):
            return False
    return True



def prefixe(auto):
    """
    Modifie l'automate pour qu'il accepte les préfixes de tous les mots du langage qu'il acceptait initialement.
    Marque tous les états de l'automate comme états finaux.

    Args:
        auto (dict): l'automate à modifier.

    Returns:
        dict: l'automate modifié.
    """
    if not est_emonde(auto):
        print("L'automate n'est pas émondé.")
        return None

    auto["F"] = auto["etats"]
    return auto


def suffixe(auto):
    """
    Modifie l'automate pour qu'il accepte les suffixes de tous les mots du langage qu'il acceptait initialement.
    Marque tous les états de l'automate comme états initiaux.

    Args:
        auto (dict): l'automate à modifier.

    Returns:
        dict: l'automate modifié.
    """
    if not est_emonde(auto):
        print("L'automate n'est pas émondé.")
        return None

    auto["I"] = auto["etats"]
    return auto


def facteur(auto):
    """
    Modifie l'automate pour qu'il accepte les facteurs de tous les mots du langage qu'il acceptait initialement.
    Marque tous les états de l'automate comme états initiaux et finaux.

    Args:
        auto (dict): l'automate à modifier.

    Returns:
        dict: l'automate modifié.
    """
    if not est_emonde(auto):
        print("L'automate n'est pas émondé.")
        return None

    auto["I"] = auto["etats"]
    auto["F"] = auto["etats"]
    return auto


def miroir_auto(auto):
    """
    Modifie l'automate pour obtenir son automate miroir, c'est-à-dire un automate qui accepte le langage miroir du langage
    qu'il acceptait initialement. Inverse les flèches de l'automate et inverse les états finaux et initiaux.

    Args:
        auto (dict): l'automate à modifier.

    Returns:
        dict: l'automate miroir.
    """
    if not est_emonde(auto):
        print("L'automate n'est pas émondé.")
        return None

    transitions = [[t[2], t[1], t[0]] for t in auto["transitions"]]
    auto["transitions"] = transitions
    auto["I"], auto["F"] = auto["F"], auto["I"]
    return auto

def etats_equivalents(auto, etat1, etat2):
    """Détermine si deux états sont équivalents dans un automate donné.

    Args:
        auto (dict): un automate représenté par un dictionnaire.
        etat1 (str): le nom du premier état.
        etat2 (str): le nom du deuxième état.

    Returns:
        bool: True si les deux états sont équivalents, False sinon.
    """
    pile = [(etat1, etat2)]
    visite = set()
    while pile:
        e1, e2 = pile.pop()
        if (e1 in auto["F"]) != (e2 in auto["F"]):
            # Si les deux états n'ont pas le même statut final, ils ne sont pas équivalents
            return False
        if (e1 in auto["I"]) != (e2 in auto["I"]):
            # Si les deux états n'ont pas le même statut initial, ils ne sont pas équivalents
            return False
        if (e1, e2) in visite:
            # Si on a déjà visité ces deux états, on passe au prochain couple
            continue
        visite.add((e1, e2))
        for symbole in auto["alphabet"]:
            transitions1 = lirelettre(auto["transitions"], [e1], symbole)
            transitions2 = lirelettre(auto["transitions"], [e2], symbole)
            if len(transitions1) != len(transitions2):
                # Si les deux états n'ont pas le même nombre de transitions sortantes pour un symbole donné,
                # ils ne sont pas équivalents
                return False
            pile += [(nouvel_etat1, nouvel_etat2) for nouvel_etat1, nouvel_etat2 in zip(transitions1, transitions2)]
    # Si on a parcouru tous les chemins possibles sans trouver de différence, les deux états sont équivalents
    return True


def regrouper_etats_equivalents(auto):
    """Regroupe les états équivalents dans un automate donné.

    Args:
        auto (dict): un automate représenté par un dictionnaire.

    Returns:
        list: une liste de groupes d'états équivalents.
    """
    groupes = []
    
    # Parcours de chaque état de l'automate
    for etat in auto["etats"]:
        # On recherche un groupe d'états déjà existant
        groupe_exist = False
        for groupe in groupes:
            if etats_equivalents(auto, etat, groupe[0]):
                groupe.append(etat)
                groupe_exist = True
                break
        
        # Si on ne trouve aucun groupe d'états déja existant alors on créer un nouveau groupe
        if not groupe_exist:
            groupes.append([etat])
    
    return groupes

def determiner_transitions(auto):
    """
    Détermine les transitions possibles pour un automate donné.

    args: 
        auto : dict

    returns: 
        list
            La liste des transitions possibles pour l'automate donné. Chaque transition est représentée par un tuple
            (état de départ, lettre, état d'arrivée).

    """
    # On commence par regrouper les états équivalents
    groupes = regrouper_etats_equivalents(auto)
    
    # On parcourt chaque groupe d'états
    transitions = []
    for groupe in groupes:
        
        # Pour chaque lettre de l'alphabet, on détermine les états d'arrivée possibles
        for a in auto["alphabet"]:
            etats_arrivee = lirelettre(auto["transitions"], groupe, a)
            
            # Pour chaque groupe d'états, on vérifie si les états d'arrivée possibles sont inclus dans ce groupe
            for groupe_dest in groupes:
                if set(etats_arrivee) <= set(groupe_dest):
                    # Si c'est le cas, on ajoute la transition correspondante à la liste des transitions possibles
                    transitions.append((groupe, a, groupe_dest))
                    break
    
    # On renvoie la liste des transitions possibles
    return transitions



def minimise(auto):
    """Minimise un automate donné en regroupant les états équivalents.

    Args:
        auto (dict): un automate représenté par un dictionnaire.

    Returns:
        dict: un automate minimisé représenté par un dictionnaire.
    """
    if not deterministe(auto) :
        auto = renommage( determinise(auto))
    # Regroupement des états équivalents
    if not complet(auto) :
        auto = complete(auto)
    groupes = regrouper_etats_equivalents(auto)
    
    # On détermine les transitions de l'atomate équivalent
    transitions = determiner_transitions(auto)
    
    # On initialise l'automate minimisé
    auto_min = {
        "alphabet": auto["alphabet"],
        "etats": groupes,
        "transitions": [],
        "I": [],
        "F": [],
    }
    
    # On parcour les transitions pour les ajouter à l'automate minimisé
    for groupe_dep, a, groupe_dest in transitions:
        auto_min["transitions"].append([groupe_dep, a, groupe_dest])
    
    # On recherche les etats initiaux et finaux de l'automate minimisé
    for groupe in groupes:
        if auto["I"][0] in groupe:
            auto_min["I"].append(groupe)
        if set(groupe) & set(auto["F"]):
            auto_min["F"].append(groupe)
    
    return auto_min


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
    
    auto_emonde = {"alphabet": ['0', '1'],
               "etats": [0, 3],
               "transitions": [[0, '0', 0], [0, '1', 3], [3, '0', 3], [3, '1', 3]],
               "I": [0],
               "F": [3]}
    
    print("\nPréfixe (émondé):")
    print(prefixe(auto_emonde))
    print("\nSuffixe (émondé):")
    print(suffixe(auto_emonde))
    print("\nFacteur (émondé):")
    print(facteur(auto_emonde))
    print("\nMiroir (émondé):")
    print(miroir_auto(auto_emonde))
    
    print("\ndifference :")
    print(difference(auto4,auto5))
    print("\nrenommage & différence :")
    print(renommage(difference(auto4,auto5)))
    
    auto6 ={"alphabet":['a','b'],"etats": [0,1,2,3,4,5,6,7],
    "transitions":[[0,'a',2],[0,'b',1],[1,'a',2],[1,'b',1],[2,'a',3],[2,'b',2],[3,'a',5],[3,'b',4],
    [4,'a',5],[4,'b',4],[5,'a',6],[5,'b',5], [6, 'a', 5], [6, 'b', 7], [7, 'a', 5], [7, 'b', 7]],
    "I":[0],"F":[0,3,4,6,7]}

    print("\n Minimisé Normal")
    print( minimise(auto6))
    
    print("\n Minimisé Renomé")
    print( renommage(minimise(auto6)))