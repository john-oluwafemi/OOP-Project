import CarClass as cc

car1 = cc.Car(2024, "Tesla")

print("Car in motion")

for i in range(5):
    car1.set_accelerate()
    print(f"Car Speed:\t{car1.get_speed()}")

print()
print("Braking")

for i in range(5):
    car1.set_brake()
    print(f"Car Speed:\t{car1.get_speed()}")




