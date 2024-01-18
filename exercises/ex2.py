students = {
    'Alice': {
        'Mathematiques': 90,
        'Francais': 80,
        'Histoire': 95
    },
    'Bob': {
        'Mathematiques': 75,
        'Francais': 85,
        'Histoire': 70
    },
    'Charlie': {
        'Mathematiques': 88,
        'Francais': 92,
        'Histoire': 78
    }
}

notes = []

nom = input("Entrez le nom de l'étudiant:")

if nom in students:
    print(f"\nNotes de {nom}:\n")
    for matiere in students[nom]:
        print(f"{matiere} : {students[nom][matiere]}")
        notes.append(int(students[nom][matiere]))
        moyenne = sum(notes) / len(notes)
    print(f"\nMoyenne de {nom} : {moyenne}\n")
else:
    print(f"L'étudiant {nom} n'existe pas dans la liste.")
