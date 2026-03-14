# Controller - responsável por coordenar a aplicação. sound_controller.p = liga a view ao model
from model.sound_base import Sound
from console_view import ConsoleView


class SoundController:
    def __init__(self, view: ConsoleView):
        self.__view = view

    def play(self, sound: Sound) -> None:
        self.__view.show("A tocar som...")
        sound.play()
