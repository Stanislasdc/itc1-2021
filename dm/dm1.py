## DM 1 d'informatique Stanislas de Chezekkes

## 1. Écrire une fonction somme telle que somme(n) renvoie la somme des entiers de 1 à n.
## Par exemple, somme(4) renvoie 10 (= 1 + 2 + 3 + 4).
def somme (n):
    for i in range (n):
        n=n+i
    return n

## 2. Écrire une fonction puissance2 telle que puissance2(n) renvoie la liste
## contenant les puissances de 2 jusqu'à 2**n.
## Par exemple, puissance2(4) renvoie [1, 2, 4, 8] (car 2**0 = 1, 2**1 = 2, 2**2 = 4, 2**3 = 8).
def puissance2(n):
    L=[]
    for i in range (n):
        u=2**i
        L.append(u)
    return L
## 3. Écrire une fonction produit telle que, si L est une liste de nombre,
## produit(L) renvoie la multiplication de tous les éléments de L
## Par exemple, produit([2, 1, 5, 4]) doit renvoyer 40 (= 2*1*5*4)
def produit(L):
    u=1
    for i in range (len[L]):
        u=u*L[i]
    return u
## 4. Écrire une fonction egal telle que egal(L) renvoie True si tous les éléments de L sont égaux, False sinon.
## Par exemple, egal([1, 1, 1, 1]) doit renvoyer True, egal([1, 2]) doit renvoyer False.
def egal(L):
    for i in L:
        if L[i]!=L[0]:
            return False
    else: return True
