# TrelloGPT

TrelloGPT is a learning project that lets me ask questions about my Trello board in natural language. It uses a Flask backend, the Trello API, and Qwen running locally through Ollama.

## Current status

The working prototype reads cards from one Trello board and answers questions about them. It cannot create or move cards yet.

## How it works

1. The browser shows the chat interface in `index.html`.
2. The interface sends my question to the Flask backend.
3. Flask fetches cards from Trello using credentials stored in a local `.env` file.
4. Flask sends the question and card details to Qwen through Ollama on my computer.
5. The browser displays Qwen's answer.

## Technology

- Python and Flask: the backend web server
- Trello REST API: retrieves board cards
- Ollama and Qwen 2.5 3B: answer questions locally
- HTML, CSS, and JavaScript: the chat interface

## Run locally

1. Open Terminal and go to the project folder: `cd ~/TrelloGPT`
2. Install the Python packages: `.venv/bin/pip install Flask requests python-dotenv`
3. Keep your Trello credentials and board ID in a local `.env` file. Never upload that file.
4. Start Qwen with `ollama run qwen2.5:3b`.
5. In another Terminal window, run `.venv/bin/python server.py`.
6. Open `http://127.0.0.1:5000/app` in a browser.

## Security

The `.env` file contains credentials that can access Trello. Keep it on your computer and never commit or share it. The exported Trello board file may contain private data, so it should also stay out of the repository. `.gitignore` tells Git to leave these local files out.

## What I’m learning

This project helps me understand how APIs, HTTP requests, JSON, environment variables, backend servers, browser interfaces, and local language models work together.
