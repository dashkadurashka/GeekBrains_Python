from abc import ABC, abstractmethod


class Clothes(ABC):
    result = 0

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def expense(self):
        pass

    def __add__(self, other):
        Clothes.result = self.expense + other.expense
        return Suit(0)

    def __str__(self):
        rslt = Clothes.result
        Clothes.result = 0
        return f'Общий расход ткани {rslt}'


class Coat(Clothes):
    @property
    def expense(self):
        return self.param / 6.5 + 0.5


class Suit(Clothes):
    @property
    def expense(self):
        return round((self.param * 2 + 0.3)/100)


coat1 = Coat(44)
suit1 = Suit(164)
print(coat1 + suit1)

