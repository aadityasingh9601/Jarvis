import webbrowser
import speech_recognition as sr
import pyttsx3
import musicLibrary
import os
import requests

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def fetchNews():
    api_key = os.environ.get("NEWS_API_KEY","e920378ec5744ddeb3f9d4038d91894f")
    r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}")

    if r.status_code == 200:
        data = r.json()
        # Extract the articles.
        articles = data.get("articles",[])
        print(articles)

        for article in articles:
            speak(articles["title"])
        
    speak("news")

def followCommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "play" in c.lower():
        song = c.lower().split(" ")[1]
        print(song)
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        fetchNews()
    else:
        print("Let open AI handle it!")
        # Write logic to handle calling OpenAI API or any other LLM API that is free if possible & speaking the response.

# Tune the settings & properties of audio listener & recognizer etc here so that it hears accurately, more easily & in a better
# way overall, so that it's smooth & more effective.

# if __name__ == "__main__":
#     speak("Initializing Jarvis!")
#     while True:
#         try:
#             # Initialize recognizer
#             recognizer = sr.Recognizer()
#             print("recognizing!")
#             # listen for the wake word "Jarvis"
#             with sr.Microphone() as source:
#                 print("Say something!")
#                 # Adjust for ambient noise and record audio
#                 recognizer.adjust_for_ambient_noise(source)
#                 audio = recognizer.listen(source,timeout=2,phrase_time_limit=1)
#                 command = recognizer.recognize_google(audio)
#                 if(command.lower() == "hello"):
#                     speak("Yes sir!")
#                     # Listen for command
#                     with sr.Microphone() as source:
#                         print("Jarvis is active!")
#                         audio = recognizer.listen(source,phrase_time_limit=1)
#                         command = recognizer.recognize_google(audio)
#                         if "goodbye" in command.lower():
#                             speak("Good bye! Sir.")
#                             break
#                         followCommand(command)
    
#         except Exception as e:
#             print("Error -> ", e)


fetchNews()
