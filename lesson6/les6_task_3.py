class Worker:

    def __init__(self, n, s, p, wage, bonus):
        self.name = n
        self.surname = s
        self.position = p
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(f"Сотрудник - {self.name} {self.surname}")

    def get_total_income(self):
        print(f"Его доход с учетом премии - {sum(self._income.values())} рублей")


worker1 = Position("Dasha", "Domanskaya", "Pharmacy", 2000, 500)
worker1.get_full_name()
print(f"Работает на должности - {worker1.position}")
worker1.get_total_income()
