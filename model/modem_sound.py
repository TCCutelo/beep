import winsound
import time
from model.sound_base import Sound


class ModemSound(Sound):
    """
    Simulação prolongada e mais contínua do som de ligação
    à internet por modem (anos 90).
    """

    def play(self) -> None:
        # ASE 1 — Tom inicial (chamada)
        winsound.Beep(1100, 700)
        winsound.Beep(1300, 700)
        time.sleep(0.03)

        # FASE 2 — Handshake caótico prolongado
        for _ in range(4):
            for freq in [
                1800, 2000, 1700, 2100,
                1600, 2200, 1500, 2300,
                1400, 2000
            ]:
                winsound.Beep(freq, 120)

        time.sleep(0.04)

        # FASE 3 — Treino de linha (alternância metálica longa)
        for _ in range(8):
            winsound.Beep(2400, 100)
            winsound.Beep(900, 100)

        time.sleep(0.05)
        
        # FASE 4 — Estabilização final antes de ligar
        for freq in [1500, 1700, 1600, 1800]:
            winsound.Beep(freq, 300)

        # FASE 5 — Tom final (ligação estabelecida)
        winsound.Beep(1200, 1200)
