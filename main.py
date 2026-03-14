# main - ponto de entrada da aplicação/ficheiro que se executa
from typing import Annotated

from sound_controller import SoundController
from console_view import ConsoleView
from model.beep_sound import BeepSound
from model.hino_sound import HinoSound
from model.ode_sound import OdeSound
from model.modem_sound import ModemSound
from model.phone_sound import PhoneSound
import typer


def main(
    sound_name: Annotated[str, typer.Argument()] = "beep",
):
    print(f"Hello {sound_name}")
    view = ConsoleView()
    controller = SoundController(view)

    if sound_name == "beep":
        sound = BeepSound(freq=1000, dur=2000)
    elif sound_name == "hino":
        sound = HinoSound()
    elif sound_name == "ode":
        sound = OdeSound()
    elif sound_name == "modem":
        sound = ModemSound()
    elif sound_name == "phone":
        sound = PhoneSound()
    else:
        raise typer.BadParameter("Som inválido. Usa: beep | hino | ode | modem | phone")

    controller.play(sound)


if __name__ == "__main__":
    typer.run(main)
