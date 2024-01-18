# Créez votre classe ici
class Rectangle:
  def __init__(self,length,width):
    self.length = length
    self.width = width
  def calculate_area(self):
    return self.length * self.width
  def calculate_perimeter(self):
    return 2*(self.length + self.width)

# Test de la classe Rectangle
rectangle = Rectangle(5, 3) # 5:width & 3:length
print("Largeur:", rectangle.width)
print("Longueur:", rectangle.length)
print("Aire:", rectangle.calculate_area())
print("Périmètre:", rectangle.calculate_perimeter())


