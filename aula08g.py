'''DESAFIO
FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA O AUDIO DE UM ARQUIVO MP3.
Nao funcionou
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex08.mp3')
pygame.mixer.music.play()
pygame.event.wait()


from pydub import AudioSegment
from pydub.playback import play
song = AudioSegment.from_mp3("ex08.mp3")
play(song)
'''


#ESSE FUNCIONOU importando o modulo de som playsound e colocando o arquivo para tocar
from playsound import playsound
playsound('ex08.mp3')
