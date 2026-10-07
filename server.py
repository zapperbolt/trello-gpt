from flask import Flask, jsonify, request, send_file
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

KEY = os.getenv("TRELLO_KEY")
TOKEN = os.getenv("TRELLO_TOKEN")
BOARD_ID = os.getenv("BOARD_ID")

TRELLO_URL = "https://api.trello.com/1"
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:3b"

@app.route("/app")
def app_page():
    return send_file("index.html")

@app.route("/")
def home():
    return "TrelloGPT is running!"


@app.route("/cards")
def cards():
    response = requests.get(
        f"{TRELLO_URL}/boards/{BOARD_ID}/cards",
        params={
            "key": KEY,
            "token": TOKEN,
            "fields": "all",
            "members": "true",
            "labels": "true",
        },
        timeout=30,
    )

    response.raise_for_status()
    return jsonify(response.json())


@app.route("/chat", methods=["POST"])
def chat():
    question = request.json.get("question", "")

    trello_response = requests.get(
        f"{TRELLO_URL}/boards/{BOARD_ID}/cards",
        params={
            "key": KEY,
            "token": TOKEN,
            "fields": "all",
        },
        timeout=30,
    )

    trello_response.raise_for_status()
    trello_cards = trello_response.json()

    card_text = "\n".join(
        f"- {card['name']} | {card.get('desc', '')} | "
        f"Due: {card.get('due', 'No due date')}"
        for card in trello_cards
    )

    prompt = f"""
You are TrelloGPT, an AI assistant that helps the user manage their Trello tasks.

Here are the user's Trello cards:

{card_text}

The user's question is:

{question}

Answer the user's question using the Trello information above.
If the information is not available, say so clearly.
"""

    ai_response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
        },
        timeout=120,
    )

    ai_response.raise_for_status()

    answer = ai_response.json()["response"]

    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)