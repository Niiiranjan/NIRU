from abc import ABC, abstractmethod
class car(ABC):
    @abstractmethod
    def mileage(self):
        pass
class Defender(car):
    def mileage(self):
        print("The milleage is 7km/l")
class Diago(car):
    def mileage(self):
        print("The milleage is 13km/l")
class pajero(car):
    def mileage(self):
        print("The milleage is 13km/l")

d=Defender()
d.mileage()
i=Diago()
i.mileage()
p=pajero()
p.mileage()

