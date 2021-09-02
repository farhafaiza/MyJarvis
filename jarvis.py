import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
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
    speak("I am Jarvis at your service. how can i help you?")


def command():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('I am Listening...')
            voice = listener.listen(source)
            query = listener.recognize_google(voice)
            query = query.lower()
            print("User said:" + query)
            if "wikipedia" in query:
                searchWiki(query)
    except:
        engine.say('Say that again...')
        engine.runAndWait()
        command()


def searchWiki(searchQuery):
    speak("Searching wikipedia...")
    cmd = searchQuery.replace("wikipedia", "")
    results = wikipedia.summary(cmd, sentences=2)
    speak("According to wikipedia...")
    print(results)
    speak(results)


if __name__ == '__main__':
    wishMe()
    command()
