# Offline AI Chatbot using LLaMA 3 & Ollama

An **offline AI chatbot** powered by **LLaMA 3** using **Ollama**. This chatbot runs locally on your machine, works without an internet connection, and can act as a friendly assistant, motivator, or conversational partner.

---

## Features

* Runs **completely offline** using Ollama.
* Uses **LLaMA 3** model for AI responses.
* Short, interactive, and context-aware answers.
* Easy to customize for personal use.

---

## Requirements

* **Operating System**: Windows / Mac / Linux
* **Python**: 3.10+
* **Ollama**: Installed and working
* **Git** (optional, for cloning the repo)

---

## Installation

1. **Install Ollama**:
   Follow instructions for your OS from [Ollama official site](https://ollama.com/).

   Example for Mac:

   ```bash
   brew install ollama
   ```

   For Windows:

   ```powershell
   winget install Ollama
   ```

2. **Install Python dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   *(Make sure your Python is added to PATH.)*

3. **Clone this repo (optional)**:

   ```bash
   git clone https://github.com/yourusername/offline-chatbot.git
   cd offline-chatbot
   ```

---

## Setting up the Model

Download or run LLaMA 3 model via Ollama:

```bash
ollama pull llama3
```

This will download the model locally so you can use it offline.

---

## Running the Chatbot

1. Open your terminal (or VS Code terminal).
2. Navigate to the project directory.
3. Run the chatbot Python script:

```bash
python chatbot.py
```

The chatbot will start in your terminal, and you can type messages directly.
Example:

```
You: Hello!
Bot: Hey! How’s your day going?
```

---

## Ollama Commands Overview

Ollama provides a command-line interface for interacting with LLaMA models. Here are the main commands:

| Command               | Description                       |
| --------------------- | --------------------------------- |
| `ollama pull <model>` | Download a model locally          |
| `ollama list`         | List all available local models   |
| `ollama run <model>`  | Run a model interactively         |
| `ollama chat <model>` | Start a chat session with a model |
| `ollama stop <model>` | Stop a running model              |
| `ollama --help`       | Show full command options         |

Example to start a chat directly without Python:

```bash
ollama chat llama3
```

---

## Python Script Usage

`chatbot.py` (example structure):

```python
from ollama import Ollama

# Initialize Ollama with LLaMA 3
model = Ollama(model="llama3")

print("Offline Chatbot is ready! Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    response = model.chat(user_input)
    print("Bot:", response)
```

* **Customization**: You can adjust the response length, temperature, and style inside the Python script for a more casual or motivating tone.

---

## Tips for Users

* Make sure your model is downloaded (`ollama pull llama3`) before running the script.
* The chatbot works offline—no internet required once the model is downloaded.
* Use short messages for faster responses.
* Experiment with different prompts for varied conversational styles.

---

## Troubleshooting

* **Command not found**: Make sure Ollama is installed and added to your system PATH.
* **Python errors**: Ensure Python 3.10+ is installed and dependencies are installed (`pip install -r requirements.txt`).
* **Model not found**: Run `ollama list` to check downloaded models.

---

## License

This project is licensed under the MIT License.

---

✅ **You’re ready to chat offline with LLaMA 3 using Ollama!**
