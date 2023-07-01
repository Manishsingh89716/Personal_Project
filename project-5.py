import pyttsx3
import datetime

#for taking voices command
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[1].id)


#speak the taken voice command
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good Morning")

    elif hour >= 12 and hour <18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("Hey Manish! A very very happy birthday to you"
          "God bless you and Enjoy your day.")



if __name__ == '__main__':
    wishMe()
