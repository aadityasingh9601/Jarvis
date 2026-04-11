# 🤖 Jarvis — AI Voice Assistant

A Python-based personal voice assistant powered by Google Gemini AI. Jarvis listens for a wake word, understands natural language commands, and performs real-world actions on your machine — all through voice.

---

## ✨ Features

- 🎤 **Wake word detection** — Say "Jarvis" to activate
- 🌐 **Browser control** — Open Google, YouTube, LinkedIn, new tabs, close tabs
- 🔍 **Voice search** — Search the web hands-free
- 🎵 **Music playback** — Play songs from your personal music library
- 📰 **Live news** — Fetches and reads top headlines via NewsAPI
- ⏯️ **Playback control** — Pause and resume media
- 🤖 **AI fallback** — Powered by Google Gemini for anything not covered by built-in commands
- 🖥️ **Desktop UI** — Clean Tkinter interface with live conversation transcript and status indicator

---

## 🖼️ Demo

> _Add a screenshot or screen recording of the UI here_

---

## 🛠️ Tech Stack

| Technology        | Purpose                           |
| ----------------- | --------------------------------- |
| Python            | Core language                     |
| SpeechRecognition | Voice input & transcription       |
| pyttsx3           | Text-to-speech output             |
| Google Gemini API | AI responses for unknown commands |
| NewsAPI           | Fetching live news headlines      |
| PyAutoGUI         | Browser automation (tabs, search) |
| Tkinter           | Desktop UI                        |

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.9+
- A working microphone
- Google Gemini API key → [Get one here](https://aistudio.google.com/app/apikey)
- NewsAPI key → [Get one here](https://newsapi.org/)

---

### 1. Clone the repository

```bash
git clone https://github.com/aadityasingh9601/Jarvis.git
cd Jarvis
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not present, install manually:
>
> ```bash
> pip install speechrecognition pyttsx3 google-genai pyautogui requests python-dotenv
> ```

### 3. Set up environment variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
NEWS_API_KEY=your_newsapi_key_here
```

### 4. Add your music library (optional)

Open `musicLibrary.py` and add your songs in this format:

```python
music = {
    "song name": "https://youtube-link-here",
}
```

### 5. Run Jarvis

```bash
# With UI
python ui.py

# Without UI (CLI only)
python main.py
```

---

## 🗣️ Voice Commands

| Command            | Action                          |
| ------------------ | ------------------------------- |
| `Jarvis`           | Wake word — activates Jarvis    |
| `open google`      | Opens Google in browser         |
| `open youtube`     | Opens YouTube in browser        |
| `open linkedin`    | Opens LinkedIn in browser       |
| `open the browser` | Opens a new browser window      |
| `open new tab`     | Opens a new tab (Ctrl+T)        |
| `close the tab`    | Closes current tab (Ctrl+W)     |
| `search <query>`   | Types and searches your query   |
| `play <song>`      | Plays a song from music library |
| `pause`            | Pauses media                    |
| `resume`           | Resumes media                   |
| `news`             | Reads top 5 news headlines      |
| `good bye`         | Shuts down Jarvis               |
| _anything else_    | Handled by Gemini AI            |

---

## 📁 Project Structure

```
Jarvis/
├── main.py            # Core logic — commands, speech, Jarvis loop
├── ui.py              # Tkinter UI — visual interface
├── llmHandler.py      # Google Gemini AI integration
├── musicLibrary.py    # Personal music library (song → URL map)
├── cursorPosition.py  # Utility to find screen coordinates
├── .env               # API keys (not committed)
├── .gitignore
└── README.md
```

---

## 🔑 Environment Variables

| Variable         | Description                            |
| ---------------- | -------------------------------------- |
| `GEMINI_API_KEY` | Google Gemini API key for AI responses |
| `NEWS_API_KEY`   | NewsAPI key for fetching headlines     |

---

## ⚠️ Known Limitations

- Requires a physical microphone — does not work in cloud environments
- `search` command uses PyAutoGUI to type — browser must be open and focused
- `pause`/`resume` use hardcoded screen coordinates — may need adjustment based on your screen resolution (use `cursorPosition.py` to find the correct coordinates)
- Music library requires manual setup in `musicLibrary.py`

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

MIT
