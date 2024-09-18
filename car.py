class Car:
    def __init__(self, brand, name, color, power, price):
        self.brand = brand
        self.name = name
        self.color = color
        self.power = power
        self.price = price

    def get_name(self):
        print(f"{self.name} from {self.brand}")