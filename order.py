# Модуль заказов и этапов работ
class Order:
    def __init__(self, id, client_id, address, order_type, status="Новый"):
        self.id = id
        self.client_id = client_id
        self.address = address
        self.order_type = order_type
        self.status = status
        self.stages = []

    def add_stage(self, stage):
        self.stages.append(stage)

    def calculate_cost(self):
        total = 0
        for stage in self.stages:
            total += stage.cost
        return total

class Stage:
    def __init__(self, id, name, start_date, end_date, status):
        self.id = id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.cost = 0

    def change_deadline(self, new_end_date):
        self.end_date = new_end_date
        print(f"Срок этапа изменен на {new_end_date}")

    def update_status(self, new_status):
        self.status = new_status
