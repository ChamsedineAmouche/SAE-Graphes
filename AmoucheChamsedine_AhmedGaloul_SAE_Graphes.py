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

if __name__ == "__main__":
    print("Préfixe")
    print(pref('coucou'))
    print("\n Suffixe")
    print(suf('coucou'))
    print("\n Facteur")
    print(fact('coucou'))
    print("\n Miroir")
    print(miroir('coucou'))
    