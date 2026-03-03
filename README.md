
# 🎬 MovieMate – AI Movie Recommender

MovieMate is a simple AI-based movie recommendation system that suggests movies based on the user's **mood, preferred genre, and language**.  
It focuses on **emotion-aware recommendations** and **user experience**, rather than complex UI or heavy ML models.

---

## 💡 Problem Statement
Users often spend a lot of time deciding *what movie to watch*, especially when they are emotionally tired or confused.  
MovieMate solves this by:
- Understanding the user’s **mood**
- Matching it intelligently with suitable **movie genres**
- Recommending **high-rated movies** available on popular OTT platforms

---

## 🤖 AI Concept Used
- **Natural Language Processing (NLP)** for mood detection (text-based)
- **Emotion-aware decision logic**
- **Rule-based recommendation system**
- **Fallback intelligence** (recommends comedy when user feels sad, etc.)

> This project demonstrates **AI thinking and decision-making**, not just filtering.

---

## ✨ Features
- 🎭 Mood-based movie recommendations  
- 🧠 AI mood detection from user input text  
- 🎤 Simulated voice mood input (real voice planned)  
- ⭐ Top 3 movies sorted by rating  
- 📺 OTT platform availability  
- ⏱ Movie duration & short description  
- 😊 Emoji-based friendly output  

---

## 🛠️ Tech Stack
- **Python**
- **Pandas**
- **CSV Dataset**
- **Basic NLP logic**

---

## 📂 Project Structure

Moviemate/
│
├── app.py # Main application file
├── functions.py # Movie loading & recommendation logic
├── mood_ai.py # Mood detection logic
├── data/
│ └── movies.csv # Movie dataset
└── README.md


---

## ▶️ How to Run
1. Install required library:
```bash
pip install pandas

Run the application:

python app.py

Enter:

Your mood (or simulate voice input)

Preferred genre

Preferred language

 🐦‍🔥 Get instant movie recommendations!

🎤 Voice Input (Current Status)

Voice input is simulated using text NLP

Real-time microphone input is planned for future versions

Planned APIs:

OpenAI Whisper

Google Speech-to-Text

🚀 Future Enhancements

🎤 Real-time voice-based mood detection

🤖 ML-based recommendation engine

🌐 Direct OTT links

📱 Web / Mobile interface

🧠 Deep emotion classification

👩‍💻 Team

Team size: 2 members

Role: AI logic, dataset design, Python development

🙌 Conclusion

MovieMate demonstrates how AI can improve user experience by understanding emotions and making intelligent recommendations.
The project focuses on clarity, simplicity, and practical AI usage, making it ideal for academic showcases.