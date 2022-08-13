class Road:

    def __init__(self, length, width):
        self._lenght = length
        self._width = width

    def mas(self, waith = 25, cm = 5):
        print(f'Масса асфальта для покрытия дороги = {(self._width * self._lenght * waith * cm) / 1000} тонн')


road1 = Road(20, 5000)
road1.mas()
road2 = Road(30, 6000)
road2.mas()
