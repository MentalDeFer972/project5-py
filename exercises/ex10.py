# Write your code here
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Name : {self.name}, \nAge : {self.age}")


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        super().display_details()
        print(f"Salary : {self.salary}")


employee = Employee("Joffrey", 25, 2500)
employee.display_details()
