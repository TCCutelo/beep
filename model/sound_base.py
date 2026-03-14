#Classe abstracta
from abc import ABC, abstractmethod

class Sound(ABC):

    @abstractmethod
    def play(self) -> None:
        pass