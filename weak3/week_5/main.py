from utils import calculate_total, print_receipt

name = input("Customer name: ")

coffee = int(input("Coffee quantity: "))
tea = int(input("Tea quantity: "))
sandwich = int(input("Sandwich quantity: "))

total = calculate_total(coffee, tea, sandwich)

print_receipt(name, coffee, tea, sandwich, total)