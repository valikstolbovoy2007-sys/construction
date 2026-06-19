# Модуль отчетов по складу
class WarehouseReport:
    def __init__(self, warehouse):
        self.warehouse = warehouse

    def generate_report(self):
        print("=== ОТЧЕТ ПО СКЛАДУ ===")
        print(f"Склад: {self.warehouse.address}")
        print("Материалы:")
        for m in self.warehouse.materials:
            print(f"  - {m.name}: {m.quantity} шт. (цена: {m.cost})")
        print("========================")
EOF 
