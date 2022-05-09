from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def cloth_consumption(self):
        pass


class Coat(Clothes):

    def __init__(self, measure):
        self.v = measure

    @property
    def cloth_consumption(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, measure):
        self.h = measure

    @property
    def cloth_consumption(self):
        return 2 * self.h + 0.3


coat = Coat(560)
print(f'Cloth consumption for coat is {coat.cloth_consumption:.2f}')
suit = Suit(180)
print(f'Cloth consumption for suit is {suit.cloth_consumption:.2f}')
