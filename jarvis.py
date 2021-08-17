<<<<<<< HEAD
import pyttsx3
import datetime
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good Morning! Let's get some coffee and start grinding")

    elif 12 <= hour < 15:
        speak("Good Afternoon, You are doing great")

    elif 15 <= hour < 20:
        speak("Good Evening. it's time for some tea")

    else:
        speak("Get recharged now. Good Night")

    speak("I am Jarvis at your service")


if __name__ == '__main__':
    wishMe()
    
=======
import pyttsx3
import datetime
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good Morning! Let's get some coffee and start grinding")

    elif 12 <= hour < 15:
        speak("Good Afternoon, You are doing great")

    elif 15 <= hour < 20:
        speak("Good Evening. it's time for some tea")

    else:
        speak("Get recharged now. Good Night")

    speak("I am Jarvis at your service")


if __name__ == '__main__':
    wishMe()
    
>>>>>>> 279a2fbdeff40ebe59b463f8688b29c39f7aad55
