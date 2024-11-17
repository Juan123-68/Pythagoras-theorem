
first_number = input("Inserte el primer número: ")
second_number = input("Inserte el segundo número: ")


from math import sqrt


def pythagoras_theorem(number_one, number_two):
    result = number_one ** 2 + number_two ** 2
    print(sqrt(result))
    
pythagoras_theorem(int(first_number), int(second_number))
