import winsound
import time
from model.sound_base import Sound


class HinoSound(Sound):
    """
    Representa um excerto aproximado do Hino Nacional de Portugal
    usando winsound.Beep (frequência + duração).
    """

    def __init__(self):
        # Melodia simples e aproximada do início de "A Portuguesa"
        # Cada tuplo é: (frequência em Hz, duração em ms)
        self.__melodia = [
            (440, 400),  # Lá
            (440, 400),
            (523, 600),  # Dó
            (494, 400),  # Si
            (440, 400),
            (392, 600),  # Sol
            (440, 800),
        ]

    def play(self) -> None:
        for freq, dur in self.__melodia:
            winsound.Beep(freq, dur)
            time.sleep(0.05)
