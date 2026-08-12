class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(f"\nYour {self.color} {self.year} {self.make} {self.model} is now driving! 🚗")


print("=== Create Your Car ===")

make = input("Enter the make of your car: ")
model = input("Enter the model of your car: ")
year = input("Enter the year of your car: ")
color = input("Enter the color of your car: ")

print("\nCreating your car...\n")

my_car = Car(make, model, year, color)

print("Your car has been created!")
print(f"Make: {my_car.make}")
print(f"Model: {my_car.model}")
print(f"Year: {my_car.year}")
print(f"Color: {my_car.color}")

print()

my_car.drive()

