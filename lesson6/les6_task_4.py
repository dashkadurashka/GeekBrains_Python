from random import choice
class Car:
    direction = ["Запад", "Север", "Юг", "Восток"]

    def __init__(self, speed, color, name, police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.police = police

    def go(self):
        print(f"Машина {self.name} - Vruuuuuuum!")

    def stop(self):
        print(f"Машина {self.name} - You shall not pass!")

    def turn(self):
        print(f"Машина {self.name} повернула на {choice(self.direction)}")

    def show_speed(self):
        return f"Машина {self.name}: скорость - {self.speed}"


class TownCar(Car):
    def show_speed(self):
        return f"Car {self.name}: скорость - {self.speed}. Alarm!" if self.speed > 60 else super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        return f"Car {self.name}: скорость - {self.speed}. Alarm!" if self.speed > 40 else super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, police=True)

town_car = TownCar(48, "бирюзовая", "Купер")
sport_car = SportCar(90, "красная", "Феррари")
work_car = WorkCar(45, "желтая", "Экскаватор")
police_car = PoliceCar(24, "синяя", "Мусоровоз")

cars_list = [town_car, sport_car, work_car, police_car]

for car in cars_list:
    car.go()
    print(car.show_speed())
    car.turn()
    car.stop()
    print()

