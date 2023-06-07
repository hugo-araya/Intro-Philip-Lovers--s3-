from gtts import gTTS
import os
from playsound import playsound

texto = input("Cual es tu nombre: ")
texto = "Buenos Dias "+ texto+ " que tengas un buen pasar durante este dia"
tts = gTTS(text = texto, lang='es', tld='com.mx')
tts.save('tecsify.mp3')
playsound('tecsify.mp3')

