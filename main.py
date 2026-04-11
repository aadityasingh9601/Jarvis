import tkinter as tk
from tkinter import scrolledtext
import threading
import speech_recognition as sr
import pyttsx3
import requests
import webbrowser
import pyautogui
import os
from dotenv import load_dotenv
import musicLibrary
from llmHandler import callLLM

load_dotenv()

recognizer = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def searchBrowser(query):
    command = query.split("search ")[1]
    pyautogui.typewrite(command)
    pyautogui.hotkey("enter")

def fetchNews():
    api_key = os.environ.get("NEWS_API_KEY")
    r = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=us&pageSize=5&apiKey={api_key}"
    )
    if r.status_code == 200:
        data = r.json()
        articles = data.get("articles", [])
        headlines = []
        for article in articles:
            headlines.append(article["title"])
        return "\n".join(headlines)
    return "Could not fetch news."

def followCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        return "Opening Google..."
    elif "open the browser" in c.lower():
        webbrowser.open("https://")
        return "Opening browser..."
    elif "open new tab" in c.lower():
        pyautogui.hotkey("ctrl", "t")
        return "Opening new tab..."
    elif "close the tab" in c.lower():
        pyautogui.hotkey("ctrl", "w")
        return "Closing tab..."
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube..."
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
        return "Opening LinkedIn..."
    elif "search" in c.lower():
        searchBrowser(c.lower())
        return f"Searching for {c.split('search')[1].strip()}..."
    elif "scroll the page" in c.lower():
         pyautogui.scroll(10, x=100, y=100)
    elif "play" in c.lower():
        song = c.lower().split(" ")[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
            return f"Playing {song}..."
        return f"Song '{song}' not found in library."
    elif "pause" in c.lower():
        pyautogui.click(672, 552)
        return "Paused."
    elif "resume" in c.lower():
        pyautogui.click(672, 552)
        return "Resumed."
    elif "news" in c.lower():
        return fetchNews()
    else:
        speak("Thinking! Just a moment, Sir!")
        response = callLLM(c)
        return response


class JarvisUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jarvis Voice Assistant")
        self.root.geometry("900x750")
        self.root.configure(bg="#1a1a2e")
        self.root.resizable(False, False)

        self.is_running = False
        self.setup_ui()

    def setup_ui(self):
        tk.Label(
            self.root,
            text="🤖 JARVIS",
            font=("Helvetica", 28, "bold"),
            fg="#00d4ff",
            bg="#1a1a2e"
        ).pack(pady=(30, 5))

        tk.Label(
            self.root,
            text="Voice Assistant",
            font=("Helvetica", 12),
            fg="#888888",
            bg="#1a1a2e"
        ).pack(pady=(0, 20))

        # Status
        self.status_label = tk.Label(
            self.root,
            text="● Ready",
            font=("Helvetica", 13),
            fg="#00ff88",
            bg="#1a1a2e"
        )
        self.status_label.pack(pady=(0, 20))

        # Start/Stop button
        self.listen_btn = tk.Button(
            self.root,
            text='Click to start "Jarvis',
            font=("Helvetica", 13, "bold"),
            fg="white",
            bg="#0077ff",
            activebackground="#0055cc",
            activeforeground="white",
            relief="flat",
            padx=25,
            pady=14,
            cursor="hand2",
            command=self.toggle_jarvis
        )
        self.listen_btn.pack(pady=(0, 30))

        # Transcript
        tk.Label(
            self.root,
            text="Conversation",
            font=("Helvetica", 11, "bold"),
            fg="#aaaaaa",
            bg="#1a1a2e"
        ).pack(anchor="w", padx=40)

        self.transcript = scrolledtext.ScrolledText(
            self.root,
            font=("Helvetica", 11),
            fg="white",
            bg="#16213e",
            relief="flat",
            padx=15,
            pady=15,
            height=16,
            wrap=tk.WORD,
            state="disabled"
        )
        self.transcript.pack(padx=40, pady=(5, 20), fill="both", expand=True)

        
        tk.Button(
            self.root,
            text="Clear",
            font=("Helvetica", 10),
            fg="#aaaaaa",
            bg="#1a1a2e",
            activebackground="#1a1a2e",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.clear_transcript
        ).pack(pady=(0, 20))

    def set_status(self, text, color="#00ff88"):
        self.status_label.config(text=text, fg=color)

    def append(self, text):
        self.transcript.config(state="normal")
        self.transcript.insert(tk.END, text + "\n")
        self.transcript.see(tk.END)
        self.transcript.config(state="disabled")

    def clear_transcript(self):
        self.transcript.config(state="normal")
        self.transcript.delete(1.0, tk.END)
        self.transcript.config(state="disabled")
        self.set_status("● Ready", "#00ff88")

    def toggle_jarvis(self):
        if not self.is_running:
            self.is_running = True
            self.listen_btn.config(
                text="⏹ Stop Jarvis",
                bg="#ff4444"
            )
            thread = threading.Thread(target=self.run_jarvis)
            thread.daemon = True
            thread.start()
        else:
            self.is_running = False
            self.listen_btn.config(
                text='Say "Jarvis" to activate',
                bg="#0077ff"
            )
            self.set_status("● Ready", "#00ff88")


    def run_jarvis(self):
        self.set_status("Calibrating microphone...", "#ffaa00")
        self.append("Jarvis: Initializing...\n")
        speak("Initializing Jarvis!")

        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)

        self.append('Jarvis: Say "Jarvis" to activate me.\n')
        self.set_status('Waiting for "Jarvis"...', "#00d4ff")

        while self.is_running:
            try:
                with sr.Microphone() as source:
                    # Listen for wake word
                    audio = recognizer.listen(
                        source, timeout=4, phrase_time_limit=3
                    )
                    command = recognizer.recognize_google(audio).lower()
                    self.append(f"You: {command}")

                    if command == "jarvis":
                        speak("Yes sir!")
                        self.append("Jarvis: Yes sir!\n")
                        self.set_status("🎤 Listening for command...", "#00d4ff")

                        # Listen for command
                        audio = recognizer.listen(
                            source, timeout=5, phrase_time_limit=8
                        )
                        command = recognizer.recognize_google(audio).lower()
                        self.append(f"You: {command}")

                        if "good bye" in command:
                            speak("Good bye! Sir.")
                            self.append("Jarvis: Good bye Sir!\n")
                            self.is_running = False
                            self.listen_btn.config(
                                text='🎤  Say "Jarvis" to activate',
                                bg="#0077ff"
                            )
                            self.set_status("● Ready", "#00ff88")
                            break

                        # Execute command
                        self.set_status("⚙️ Processing...", "#ffaa00")
                        response = followCommand(command)
                        speak(response)
                        self.append(f"Jarvis: {response}\n")
                        self.set_status('👂 Waiting for "Jarvis"...', "#00d4ff")

            except sr.WaitTimeoutError:
                continue

            except sr.UnknownValueError:
                self.set_status('👂 Waiting for "Jarvis"...', "#00d4ff")
                continue

            except Exception as e:
                self.append(f"Error: {e}\n")
                self.set_status("Error occurred", "#ff4444")



if __name__ == "__main__":
    root = tk.Tk()
    app = JarvisUI(root)
    root.mainloop()