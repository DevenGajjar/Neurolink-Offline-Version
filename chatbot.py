import requests

def chat_with_ollama(prompt, model="llama3"):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": f"""
        You are a supportive chatbot.  
        - Keep answers short: 1–1.5 sentences only.  
        - Sound like a close friend who motivates and listens.  
        - Be casual, warm, and positive.  
        - Encourage the user in a natural, human way.  
        - If they feel low, lift them up gently.  
        - If they ask study doubts, explain briefly and clearly.  

         {prompt}
        """,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        data = response.json()

        if "response" in data:
            return data["response"].strip()
        else:
            return f"⚠️ Ollama Error: {data}"

    except Exception as e:
        return f"⚠️ Connection Error: {e}"


print("🤖 Offline Chat-Bot bu NEUROLINK (type 'exit' to quit)\n")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Catch you later, buddy 👋 Stay strong!")
        break

    reply = chat_with_ollama(user_input)
    print("Bot:", reply, "\n")
