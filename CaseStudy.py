class Vehicle:
def __init__(self, vehicle_type):
self.vehicle_type = vehicle_type

class Automobile(Vehicle):
def __init__(self, vehicle_type, year, make, model, doors, roof):
super().__init__(vehicle_type)
self.year = year
self.make = make
self.model = model
self.doors = doors
self.roof = roof

def main():
vehicle_type = "car" # Hardcoding vehicle_type as "car" as specified in the question
year = input("Enter the year: 2024")
make = input("Enter the make: Subaru")
model = input("Enter the model: Impreza]")
doors = input("Enter the number of doors: 4")
roof = input("Enter the type of roof: sun roof")



print("Vehicle type:", automobile.vehicle_type)
print("Year:", automobile.year)
print("Make:", automobile.make)
print("Model:", automobile.model)
print("Number of doors:", automobile.doors)
print("Type of roof:", automobile.roof)

if __name__ == "__main__":
main()
