from src.walker.walker import Walker
from src.store.store import Store


class Program:
    def __init__(self):
        self.walker = Walker()
        self.store = Store()

    def GetBestWay(self, origin, destiny):
        result = self.walker.Generate_Way(origin, destiny, _type=1)
        return result

    def AddProduct(self, name, weight, value):
        self.store.AddProduct(name, weight, value)

    def GetDistribuction(self, limit):
        result = self.store.GetDistribuction(limit)
        return result


program = Program()
result = program.GetBestWay("A", "Q")
print(result)

print()

program.AddProduct("Prod1", weight=5, value=5)
program.AddProduct("Prod2", weight=2, value=1)
program.AddProduct("Prod3", weight=2, value=3)
result = program.GetDistribuction(7)
print(result)
