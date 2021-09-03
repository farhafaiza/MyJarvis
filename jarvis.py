import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

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
            if 'jarvis tell me' in query:   # Say "Jarvis tell me" to get info from wikipedia
                what = query.replace('jarvis tell me', '')
                searchWiki(what)

            elif 'open youtube' in query:  # Say "open youtube." to open youtube
                webbrowser.open("youtube.com")
            elif 'open google' in query: # Say "open google." to open google
                webbrowser.open("google.com")
            elif 'the time' in query:     # Say "the time" to tell you time
                say_time = datetime.datetime.now().strftime("%H:%M:%S")
                speak("the time is" + say_time)
            elif 'open github' in query:    # Say "open github" to open github in your desktop
                git_path = "C:\\Users\\Unique\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"
                os.startfile(git_path)
    except:
        engine.say('Say that again...')
        engine.runAndWait()
        command()


def searchWiki(searchQuery):
    try:
        speak("Searching wikipedia...")
        cmd = searchQuery.replace("wikipedia", "")
        results = wikipedia.summary(cmd, 2)
        speak("According to wikipedia...")
        print(results)
        speak(results)
    except:
        sorry = 'Hey, I am Unable to find, I am really Sorry :('
        print(sorry)
        speak(sorry)


if __name__ == '__main__':
    wishMe()
    command()
