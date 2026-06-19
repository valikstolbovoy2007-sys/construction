# Модуль пользователей и аутентификации
class User:
    def __init__(self, id, name, phone, email, password):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password

    def login(self):
        print(f"Пользователь {self.name} выполнил вход")

    def logout(self):
        print(f"Пользователь {self.name} выполнил выход")

class Client(User):
    def __init__(self, id, name, phone, email, password, address):
        super().__init__(id, name, phone, email, password)
        self.address = address

    def make_order(self):
        print("Клиент оформил заказ")

class Manager(User):
    def calculate_salary(self):
        print("Расчет заработной платы")

class Foreman(User):
    def control_stage(self):
        print("Контроль этапа работ")

class Storekeeper(User):
    def receive_materials(self):
        print("Прием материалов на склад")
