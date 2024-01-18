words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

comprehension = []

voyelles = ["a", "e", "i", "o", "u", "y"]

number = 0

for word in words:
    for v in word:
        if v in voyelles:
            number += 1
    comprehension.append((word, number))
    number = 0
print(comprehension)
