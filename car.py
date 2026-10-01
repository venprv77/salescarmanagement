class Car:

    def __init__(self, brand, model, price, quantity, car_id=None):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.price = price
        self.quantity = quantity