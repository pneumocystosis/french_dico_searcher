fichier = open(r"dico.txt")
long = int(input("Quelle longueur de mot? "))
lettres = list(input("Quelles sont les lettres nécessaires?(séparées par un espace): ").split())
listemots = []
listLignes = list(fichier.readlines())

def longu(long, ligne):
    if int(len(ligne)) == long+1:
        return True

def chars(lettres):
    status = True
    for j in range (len(lettres)):
            if ligne.count(lettres[j]) == 0:
                status = False
    if status:
        return True
            
for ligne in listLignes:
    if longu(long, ligne) and chars(lettres):
        listemots.append(ligne)
    
print("".join(listemots))
input("Appuyez sur entrée pour continuer...")


