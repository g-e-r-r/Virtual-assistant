import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
from os import system

name = 'juan'
listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, "")
                print(rec)
            else:
                print(rec)
    except:
        pass
    return rec

def run():
    rec = listen()
    if "reproduce" in rec:
        try:
            music = rec.replace("reproduce", "")
            talk("Reproduciendo" + music)
            pywhatkit.playonyt(music)
            exit()
        except:
            talk("Perdona, algo ha fallado")
            exit()

    if "hora" in rec:
        try:
            hora = datetime.datetime.now().strftime('%I:%M %p')
            talk("Son las " + hora)
        except:
            talk("Perdona, algo ha fallado")

    if "día es" in rec:
        dia = datetime.datetime.today().strftime('%A')
        if dia == "Monday":
            dia = "Lunes"
        elif dia == "Tuesday":
            dia = "Martes"
        elif dia == "Wednesday":
            dia = "Miércoles"      
        elif dia == "Thursday":
            dia = "Jueves"        
        elif dia == "Friday":
            dia = "Viernes"
        elif dia == "Saturday":
            dia = "Sábado"
        elif dia == "Sunday":
            dia = "Domingo"                
        talk("Hoy estamos a " + dia)        

    if "busca" in rec:
        try:
            order = rec.replace("busca", "")
            info = wikipedia.summary(order, 2)
            print(info)
            talk(info)
        except:
            talk("Perdona, algo ha fallado")

    if "finaliza" in rec:
        talk("Entendido, saliendo")
        exit()

    system("cls")

while True: 
    run()