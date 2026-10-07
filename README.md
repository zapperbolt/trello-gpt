1. In the README editor, click in the text and press **⌘A**. Replace it with this description:

```markdown
# TrelloGPT

TrelloGPT is a local-first learning project that lets me ask questions about my Trello board in natural language. It connects Trello’s API to a Flask backend and uses Qwen through Ollama to generate answers.

## Current status

The working prototype can read cards from one configured Trello board and answer questions about them. It does not create or move cards yet.

## How it works

1. The browser displays the chat interface from `index.html`.
2. The interface sends a question to the Flask backend at `/chat`.
3. Flask uses the Trello API credentials and board ID from a local `.env` file to fetch board cards.
4. Flask sends the question and card details to Qwen through Ollama running on the same computer.
5. Flask returns Qwen’s answer to the browser.

```text
Browser UI → Flask backend → Trello REST API
                         ↘ Ollama → Qwen
```

## Technology

- Python and Flask for the local web server
- Trello REST API for board data
- Ollama running the `qwen2.5:3b` model locally
- HTML, CSS, and JavaScript for the chat interface

## Run locally

1. Install Python and Ollama.
2. In Terminal, go to the project folder and install the Python packages:

   ```bash
   cd ~/TrelloGPT
   .venv/bin/pip install Flask requests python-dotenv
   ```

3. Create a local `.env` file containing your own Trello credentials and board ID:

   ```text
   TRELLO_KEY=your_key
   TRELLO_TOKEN=your_token
   BOARD_ID=your_board_id
   ```

4. Start the model in Ollama, then start the app:

   ```bash
   ollama run qwen2.5:3b
   ```

   In another Terminal window:

   ```bash
   cd ~/TrelloGPT
   .venv/bin/python server.py
   ```

5. Open [http://127.0.0.1:5000/app](http://127.0.0.1:5000/app).

## Security

The `.env` file contains credentials that can access Trello. Keep it on your computer and never commit or share it. The local Trello export may contain private board data, so it should stay out of the repository too. The `.gitignore` file excludes these local files.

## Learning goals

This project is helping me learn how APIs, HTTP requests, JSON data, environment variables, backend servers, browser interfaces, and local language models work together.
```

2. Review that the README says **read-only** for the current version; that accurately describes what works today.
3. Click **Commit changes**, keep the default options, and tell me when it’s saved. Then I’ll walk through the project’s technical flow with you.
