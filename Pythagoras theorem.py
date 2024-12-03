from math import sqrt

first_number = input("Inserte el primer número: ")
second_number = input("Inserte el segundo número: ")

def pythagoras_theorem(number_one, number_two):
    return (number_one ** 2 + number_two ** 2) / 3
    
print(pythagoras_theorem(int(first_number), int(second_number)))
