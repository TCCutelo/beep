import winsound
import time
from model.sound_base import Sound


class OdeSound(Sound):
    """
    Excerto da melodia 'Ode à Alegria' (Beethoven),
    adaptada para winsound.Beep (monofónica).
    """

    def __init__(self):
        # Frequências das notas (Hz)
        E = 659
        F = 698
        G = 784
        D = 587
        C = 523

        # Cada tuplo: (frequência, duração em ms)
        self.__melodia = [
            E,
            E,
            F,
            G,
            G,
            F,
            E,
            D,
            C,
            C,
            D,
            E,
            E,
            D,
            D,
            E,
            E,
            F,
            G,
            G,
            F,
            E,
            D,
            C,
            C,
            D,
            E,
            D,
            C,
            C,
        ]

        self.__duracao_curta = 350
        self.__duracao_longa = 700

        # Padrão rítmico simples
        self.__ritmo = [self.__duracao_curta] * len(self.__melodia)

        # Algumas notas finais mais longas
        self.__ritmo[14] = self.__duracao_longa
        self.__ritmo[-1] = self.__duracao_longa

    def play(self) -> None:
        for freq, dur in zip(self.__melodia, self.__ritmo):
            winsound.Beep(freq, dur)
            time.sleep(0.05)
