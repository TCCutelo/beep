import winsound
from model.sound_base import Sound

class BeepSound(Sound):

    def __init__(self, freq: int, dur: int):
        self.__freq = freq
        self.__dur = dur

    def play(self) -> None:
        winsound.Beep(self.__freq, self.__dur)