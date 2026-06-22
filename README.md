# 🐱 TALKING TOM - Voice Mimic Simulator

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Pygame](https://img.shields.io/badge/Pygame-GUI-green?style=for-the-badge)
![Speech Recognition](https://img.shields.io/badge/Speech-Recognition-orange?style=for-the-badge)
![pyttsx3](https://img.shields.io/badge/Text-To-Speech-pyttsx3-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

### A Python-Based Interactive Talking Tom Simulator

</div>

---

## 📖 Overview

**TALKING TOM** is a simple and interactive desktop application developed using **Python**, **Pygame**, **SpeechRecognition**, and **pyttsx3**.

The application listens to the user's voice through the microphone, converts the speech into text, and makes the animated cat repeat the recognized words using text-to-speech technology.

The project demonstrates concepts such as:

* Graphical User Interface Development
* Real-Time Speech Recognition
* Text-To-Speech Synthesis
* Character Animation
* Multithreading
* Event-Driven Programming
* Audio Processing

---

# ✨ Key Features

### 🎤 Real-Time Voice Recognition

* Captures user speech through the microphone.
* Converts speech into text using Google's Speech Recognition API.

### 🗣️ Text-To-Speech Output

* The cat repeats whatever the user says.

### 🐱 Animated Character

* Displays different images while idle and while speaking.

### ⌨️ Keyboard Interaction

* Press the **SPACEBAR** to activate voice recording.

### ⚡ Multithreaded Processing

* Uses Python threads to ensure smooth application execution.

### 🖥️ Interactive Graphical Interface

* Built using Pygame for real-time rendering and interaction.

### 🎭 Dynamic Character Animation

* Automatically switches between idle and talking states.

---

# 🏗️ System Architecture

```text
Application Starts
        |
        ↓
Display Idle Cat
        |
        ↓
User Presses SPACEBAR
        |
        ↓
Activate Microphone
        |
        ↓
Capture User Voice
        |
        ↓
Convert Speech To Text
        |
        ↓
Generate Speech Output
        |
        ↓
Display Talking Animation
        |
        ↓
Return To Idle State
```

---

# 🛠️ Technologies Used

| Technology        | Purpose                       |
| ----------------- | ----------------------------- |
| Python            | Programming Language          |
| Pygame            | GUI and Animation             |
| SpeechRecognition | Speech Recognition Processing |
| pyttsx3           | Text-To-Speech Engine         |
| Threading         | Background Task Handling      |

---

# 📂 Project Structure

```text
TalkingTom/
│
├── main.py
├── cat_idle.png
├── cat_talking.png
├── requirements.txt
│
└── README.md
```

---

# 🧠 Application Workflow

## User Flow

1. Launch the application.
2. The idle cat image is displayed.
3. Press the **SPACEBAR**.
4. The microphone starts listening.
5. Speak into the microphone.
6. Speech is converted into text.
7. The cat repeats the recognized speech.
8. The talking animation is displayed.
9. The application returns to the idle state.

---

# 🎤 Speech Recognition Workflow

```text
Microphone Input
        |
        ↓
Capture Audio
        |
        ↓
Recognize Speech
        |
        ↓
Convert To Text
        |
        ↓
Generate Voice Output
        |
        ↓
Play Through Speakers
```

---

# ⚙️ Installation and Setup

## Step 1: Install Python

Download and install Python from the official website.

---

## Step 2: Clone the Repository

```bash
git clone https://github.com/your-username/TalkingTom.git
```

Move into the project directory:

```bash
cd TalkingTom
```

---

## Step 3: Install Dependencies

Execute:

```bash
pip install pygame
pip install SpeechRecognition
pip install pyttsx3
pip install pyaudio
```

---

## Step 4: Run the Application

Execute:

```bash
python main.py
```

---

# 🚀 Application Screens

## 🐱 Idle State

* Displays the normal cat image.
* Waits for user interaction.

---

## 🎤 Listening State

* Activated when the user presses the **SPACEBAR**.
* The microphone starts recording.

---

## 🗣️ Talking State

* Displays the talking cat image.
* Repeats the recognized speech.

---

# 🌟 Future Enhancements

* [ ] Multiple Character Skins
* [ ] Background Music
* [ ] Sound Effects
* [ ] AI-Based Conversations
* [ ] Emotion Detection
* [ ] Offline Speech Recognition
* [ ] Facial Expression Animation

---

# 🧪 Testing

| Test Case             | Expected Result                |
| --------------------- | ------------------------------ |
| Press SPACEBAR        | Microphone Activates           |
| Speak Into Microphone | Speech Is Captured             |
| Speech Recognition    | Correct Text Is Generated      |
| Text-To-Speech        | Cat Repeats User Speech        |
| Talking Animation     | Talking Image Is Displayed     |
| Close Window          | Application Exits Successfully |

---

# 🤝 Contribution

Contributions are welcome.

### Steps:

1. Fork the repository.

2. Create a new feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Added new feature"
```

4. Push the changes.

```bash
git push origin feature-name
```

5. Create a Pull Request.

---

# 👨‍💻 Developed For Learning Purpose

This project demonstrates:

* Pygame Window Management
* Speech Recognition
* Text-To-Speech
* Multithreading
* Event Handling
* Audio Processing
* Character Animation

---

# 👨‍💻 Author

**Ajith P A**

---

# 📄 License

This project is developed for educational and learning purposes.

---

<div align="center">

## ⭐ If you found this project useful, consider giving it a star!

### 🐱 TALKING TOM

**Listen • Repeat • Have Fun**

*Built with ❤️ using Python and Pygame*

</div>
