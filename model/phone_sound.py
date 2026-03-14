import winsound
import time
from model.sound_base import Sound


# Simula o toque de um telefone clássico
class PhoneSound(Sound):
    def play(self) -> None:
        for _ in range(3):  # número de toques
            winsound.Beep(1000, 800)
            time.sleep(0.2)
            winsound.Beep(1000, 800)
            time.sleep(1.2)  # pausa entre ciclos
