# Ajoutez votre décorateur ici
def log_decorator(function):
    def wrapper():
        print("Début de la fonction")
        result = function()
        print("Fin de la fonction")
        return result

    return wrapper


@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")


function_test()