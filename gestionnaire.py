def ajouterTache(tache):
    nouvelle_tache = input("Ajouter la tache: ")
    tache.append(nouvelle_tache) #append est une fonction qui permet d'ajouter un élément à la fin d'une liste 
    print("Tache ajouté avec succès")

def afficherTache(tache):
    for element in tache:
        print(element)

def supprimerTache(tache):
    afficherTache(tache)
    indice_tache = int(input("Entrez le numéro de la tâche à supprimer : "))
    if indice_tache < len(tache):
        del tache[indice_tache]
        print("Tache supprimé avec succès")
    else:
        print("cette tache n'existe pas")

def marquerTacheTerminee(tache):
    # Demander à l'utilisateur de saisir l'ID de la tâche
    id_tache = input("Entrez l'ID de la tâche à marquer comme terminée : ")

    # Vérifier si la tâche existe
    if id_tache not in range(len(tache)):
        print("La tâche n'existe pas.")
        return tache

    # Marquer la tâche comme terminée
    tache[id_tache] = f"{tache[id_tache]} (terminée)"

    return tache

tache=[]

while True:
    print("\nMENU:")
    print("1. Ajouter une tache")
    print("2. Afficher taches")
    print("3. Supprimer tache")
    print("4. Marquer une tache terminée")
    print("5. Quitter")

    choix = input("Choisissez une option: ")
    if(choix == "1"):
        ajouterTache(tache)
    elif(choix == "2"):
        afficherTache(tache)
    elif(choix == "3"):
        supprimerTache(tache)
    elif(choix == "4"): 
        marquerTacheTerminee(tache)
    elif(choix == "5"):
        print("Au revoir")
        break
    else:
        print("Option invalide")