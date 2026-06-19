# Модуль материалов и склада
class Material:
    def __init__(self, id, name, cost, quantity):
        self.id = id
        self.name = name
        self.cost = cost
        self.quantity = quantity

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def update_cost(self, new_cost):
        self.cost = new_cost

class Warehouse:
    def __init__(self, id, address):
        self.id = id
        self.address = address
        self.materials = []

    def add_material(self, material):
        self.materials.append(material)

    def remove_material(self, material_id):
        self.materials = [m for m in self.materials if m.id != material_id]

    def check_stock(self):
        for m in self.materials:
            print(f"{m.name}: {m.quantity} шт.")

class Supply:
    def __init__(self, id, material_id, quantity):
        self.id = id
        self.material_id = material_id
        self.quantity = quantity
