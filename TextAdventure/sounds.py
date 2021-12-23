import os.path
import winsound


def horror_night():
    winsound.PlaySound(os.path.abspath("KillerSound.wav"), winsound.SND_FILENAME)


def invalidCode():
    winsound.PlaySound(os.path.abspath("Wrong-answer-sound-effect.wav"), winsound.SND_FILENAME)


def zombie():
    winsound.PlaySound(os.path.abspath("zoombie.wav"), winsound.SND_FILENAME)


def monsterSound():
    winsound.PlaySound(os.path.abspath("monster.wav"), winsound.SND_FILENAME)


def spiderSound():
    winsound.PlaySound(os.path.abspath("spider.wav"), winsound.SND_FILENAME)


def wolfSound():
    winsound.PlaySound(os.path.abspath("wolf-kill-moan.wav"), winsound.SND_FILENAME)


def startSound():
    winsound.PlaySound(os.path.abspath("start.wav"), winsound.SND_FILENAME)


def penguinSound():
    winsound.PlaySound(os.path.abspath("penguin.wav"), winsound.SND_FILENAME)
