# Fonction calculate_average
def calculate_average(numbers_list):
    number_final = 0
    for number in numbers_list:
        number_final = number_final + number
    return number_final / len(numbers_list)


# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", average)
