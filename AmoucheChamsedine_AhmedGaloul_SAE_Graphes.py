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
    L2=['a', 'b', '']
    print(concatene(L1,L2))
    L1=['aa','ab','ba','bb']
    print(puis(L1,2))
    
