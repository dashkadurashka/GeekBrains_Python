class Stationery:
    def __init__(self, title):
         self.tiile = title

    def draw(self):
        print(f"Мы пишем {self.tiile}")


class Pen(Stationery):
    def draw(self):
        print(f"Мы пишем {self.tiile} ручкой")


class Pencil(Stationery):
    def draw(self):
        print(f"Мы пишем {self.tiile} карандашом")


class Handle(Stationery):
    def draw(self):
        print(f"Мы пишем {self.tiile} маркером")


pen1 = Pen("Синей")
pen1.draw()

pensil1 = Pencil("Красным")
pensil1.draw()

handle1 = Handle("Зеленым")
handle1.draw()
