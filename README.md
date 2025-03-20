# Amadeus Chatbot

Amadeus is a locally hosted AI chatbot powered by LLaMA 2, designed to provide an interactive conversational experience. This chatbot runs offline on your machine, ensuring privacy and control over your AI interactions. It is built using Python, Streamlit for the UI, and Pyttsx3 for text-to-speech (TTS) capabilities.

---

## Features
✅ **Offline Chatbot** – No internet required, runs on your local system.
✅ **Streamlit Web Interface** – Easy-to-use UI for chatting.
✅ **Text-to-Speech (TTS)** – Amadeus can speak responses using Pyttsx3.
✅ **Secure & Private** – Your data never leaves your machine.

---

## Installation

### 1. **Install Python & Dependencies**
Make sure you have Python installed (preferably Python 3.10+). If not, download it from [Python.org](https://www.python.org/).

Then, install the required libraries:
```sh
pip install streamlit pyttsx3
```

### 2. **Clone the Repository**
```sh
git clone https://github.com/your-username/AmadeusChatbot.git
cd AmadeusChatbot
```

### 3. **Run the Chatbot**
```sh
streamlit run webchat.py
```

This will open the chatbot in your browser.

---

## Usage
- Open the **Streamlit UI** in your browser.
- Type your message in the chatbox and press "Send".
- Amadeus will respond, and you can also hear the response using the built-in TTS feature.

---

## How It Works
1. **User Input:** You type a message in the Streamlit chat UI.
2. **Processing:** The chatbot (powered by LLaMA 2) generates a response.
3. **Response Output:** The response is displayed and spoken using Pyttsx3.

---

## Troubleshooting
❌ **Streamlit Not Found?**

```sh
pip install streamlit
```

❌ **Pyttsx3 Not Working?**

```sh
pip install pyttsx3
```

❌ **Python Not Recognized?**

Make sure Python is installed and added to your system’s PATH.

---

## Future Improvements 🚀
- Add **voice input support**.
- Implement **better UI design**.
- Improve **response accuracy** using fine-tuning.

---

## Contributions 🤝
Feel free to **fork** this repository, create a **new branch**, and submit a **pull request** with improvements!

---

## License
This project is open-source under the **MIT License**.

---


