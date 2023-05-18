"C major"

import winsound


def Fis4(time):
    """ファ#"""
    winsound.Beep(740,time)

def D4(time):
    """レ"""
    winsound.Beep(587,time)

def A4(time):
    """ラ"""
    winsound.Beep(880,time)

def E4(time):
    """ミ"""
    winsound.Beep(659,time)

def A3(time):
    """ラ、オクターブ下"""
    winsound.Beep(440,time)

def famima():
    Fis4(500)
    D4(500)
    A3(500)
    D4(500)
    E4(500)
    A4(500)
    A4(500)
    E4(500)
    Fis4(500)
    E4(500)
    A3(500)
    D4(500)

famima()