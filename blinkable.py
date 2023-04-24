from abc import ABC, abstractmethod


class Blinkable(ABC):
    """
    We can use an Abstract Base Class (ABC) to create an interface.
    The interface is an abstract method. It has not real implementation,
    it can simply contain pass. It must, however, by imlemented
    by subclasses that promise to implement it.
    """
    @abstractmethod
    def blink(self):
        pass
