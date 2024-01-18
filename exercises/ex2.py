"""
Find students in a list
"""

STUDENT_DICT = {
    "Alice": {
        "Mathematiques": 90,
        "Francais": 80,
        "Histoire": 95,
    },
    "Bob": {
        "Mathematiques": 75,
        "Francais": 85,
        "Histoire": 70,
    },
    "Charlie": {
        "Mathematiques": 88,
        "Francais": 92,
        "Histoire": 78,
    },
}


def compute_average(
    st_name: str,
    student_dict: dict,
) -> int:
    """main function

    Args:
        st_name (str): student name
        student_dict (dict): student dict
    """

    # manage errors : student not in list
    if st_name not in student_dict.keys():
        print(f"L'étudiant {st_name} n'existe pas dans la liste.")
        return 1

    # placeholder for notes
    notes = [int(student_dict[st_name][m]) for m in student_dict[st_name]]

    # compute average
    average = sum(notes) / len(notes)
    print(f"\nMoyenne de {st_name} : {average}\n")

    return 0


def main():
    """Main function"""

    # input student name
    st_name = input("Entrez le student_name de l'étudiant:")

    # compute average
    compute_average(
        st_name=st_name,
        student_dict=STUDENT_DICT,
    )


if __name__ == "__main__":
    main()
