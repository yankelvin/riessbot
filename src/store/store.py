from .distribuction import Distribuction


class Product:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

    def __repr__(self):
        return f"Name: {self.name}, Weight: {self.weight}, Value: {self.value}"


class Store:
    def __init__(self):
        self.truck = {
            "products": []
        }

    def AddProduct(self, name, weight, value):
        product = Product(name, weight, value)
        self.truck["products"].append(product)

    def GetDistribuction(self, limit):
        dist = Distribuction(self.truck["products"], limit)
        betters = dist.GetBetters()

        return betters
