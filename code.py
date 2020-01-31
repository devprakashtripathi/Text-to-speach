#from gtts import gTTS
#import os

#mytext=input()
#language="en"
#myobj=gTTS(text = mytext, lang=language, slow=False)
#myobj.save("abc.mp3")
#os.system("abc.mp3")

import pyttsx3
#engine=pyttsx3.init()
#voices= engine.getProperty("voices")
#for voice in voices:
#    engine.setProperty("voice",voice.id)
#    engine.say("HELLO Nainish Boss,How are you?")
#engine.runAndWait()

engine = pyttsx3.init()
volume = engine.getProperty('volume')
engine.setProperty('volume', volume-10.25)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
