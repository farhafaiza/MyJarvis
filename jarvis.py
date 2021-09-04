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
    try:
        with sr.Microphone() as source:
            print('I am Listening...')

            listener = sr.Recognizer()
            listener.pause_threshold = 0.8  # Represents the minimum length of silence (in seconds)
            listener.energy_threshold = 50  # Values below this threshold are considered silence
            listener.adjust_for_ambient_noise(source, duration=1)
            listener.operation_timeout = None  # Represents the timeout (seconds) for internal operations
            listener.dynamic_energy_threshold = True   # energy level for sounds should be auto adjusted
            listener.dynamic_energy_adjustment_damping = 0.15

            voice = listener.listen(source)
            query = listener.recognize_google(voice)
            query = query.lower()
            print("User said:" + query)
            if 'jarvis tell me' in query:   # Say "Jarvis tell me" to get info from wikipedia
                what = query.replace('jarvis tell me', ' ')
                print("Searching" + what)
                searchWiki(what)
            elif 'open youtube' in query:  # Say "open youtube." to open youtube
                webbrowser.open("youtube.com")
            elif 'open google' in query:  # Say "open google." to open google
                webbrowser.open("google.com")
            elif 'the time' in query:     # Say "the time" to tell you time
                say_time = datetime.datetime.now().strftime("%#I %#M %p")
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
        print(results)
        speak("According to wikipedia..." + results)
    except:
        sorry = "I am Sorry, I don't know"
        print(sorry)
        speak(sorry)


if __name__ == '__main__':
    wishMe()
    command()
