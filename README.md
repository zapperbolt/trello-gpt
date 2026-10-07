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
