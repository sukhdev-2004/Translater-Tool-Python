import speech_recognition as sr
from gtts import gTTS
import pygame
from io import BytesIO
from deep_translator import GoogleTranslator

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something In English...")
    recognizer.adjust_for_ambient_noise(source) 
    audio = recognizer.listen(source)  

    try:
        text = recognizer.recognize_google(audio).lower() 
        print("You said:", text)
    except sr.UnknownValueError:
        print("Could not understand the audio")
        text = None
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")
        text = None

if text:
    text = recognizer.recognize_google(audio, language="en")
    translated_text = GoogleTranslator(source='en', target='hi').translate(text)
    mp3_fp = BytesIO()
    speech = gTTS(text=translated_text, lang='hi')
    speech.write_to_fp(mp3_fp)
    mp3_fp.seek(0)

    pygame.mixer.init()
    pygame.mixer.music.load(mp3_fp, "mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():  
        continue  
else:
    print("Speech not recognized!")
