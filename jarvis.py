import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
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



def commend():

    listener = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print('I am Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
    except:
        engine.say('Say that again...')
        engine.runAndWait()
        commend()
# def takeCommand():
#     r = sr.Recognizer
#     with sr.Microphone as source:
#         speak("Listening...")
#         audio = r.listen(source)
#
#     try:
#         speak("Recognizing...")
#         query = r.recognize_google(audio, language="en-US")
#         print(f"User said: {query} \n")
#
#     except Exception as e:
#         speak("Say that again")
#         return "None"
#     return query

# listener = sr.Recognizer()
# try:
#     with sr.Microphone() as source:
#         print('listening')
#         voice = listener.listen(source)
#         command = listener.recognize_google(voice)
#         print(command)
# except:
#     pass



if __name__ == '__main__':
    wishMe()
    commend()



    # takeCommand()
