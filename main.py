import webbrowser
import speech_recognition as sr
import pyttsx3
import musicLibrary
from llmHandler import callLLM
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def fetchNews():
    api_key = os.environ.get("NEWS_API_KEY")
    r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&pageSize=5&apiKey={api_key}")
    
    if r.status_code == 200:
        data = r.json()

        articles = data.get("articles", [])

        for article in articles:
            print(article["title"])
            print()
            speak(article["title"])
        
def followCommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "play" in c.lower():
        # Currently you music library is visile on github repo, either change the songs there, or remove it (maybe)
        song = c.lower().split(" ")[1]
        print(song)
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        fetchNews()
    else:
        speak("Thinking! Just a moment, Sir!")
        print("AI handling the response")
        speak(callLLM(c))
        # Write logic to handle calling OpenAI API or any other LLM API that is free if possible & speaking the response.

# Tune the settings & properties of audio listener & recognizer etc here so that it hears accurately, more easily & in a better
# way overall, so that it's smooth & more effective.

# Initialize recognizer
recognizer = sr.Recognizer()
# recognizer.energy_threshold = 300
# recognizer.dynamic_energy_threshold = True

if __name__ == "__main__":
    speak("Initializing Jarvis!")
    print("Calibrating microphone...")
    
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)

    while True:
        try:
            print("Listening for Wake Word!")
            # listen for the wake word "Jarvis"
            with sr.Microphone() as source:
                audio = recognizer.listen( source,timeout=4,phrase_time_limit=3)
                
                command = recognizer.recognize_google(audio).lower()
                print("Heard:", command)
                
                if(command == "jarvis"):
                    speak("Yes sir!")
                    print("Listening for command!")

                    audio = recognizer.listen(source,timeout=5,phrase_time_limit=5)
                    
                    command = recognizer.recognize_google(audio).lower()
                    print("Command",command)
                    if "good bye" in command:
                        speak("Good bye! Sir.")
                        break
                    followCommand(command)
    
        except sr.WaitTimeoutError:
                continue
        
        except sr.UnknownValueError:
            print("Could not understand audio")

        except Exception as e:
            print("Error:",e)