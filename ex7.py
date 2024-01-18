# Write your code here

def square(number):
    try:
        result = number ** 2
        return result
    except TypeError:
        print("Le paramètre doit être un nombre!")
        return None


print(square(2))
print(square("2"))

