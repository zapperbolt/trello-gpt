import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("TRELLO_KEY")
TOKEN = os.getenv("TRELLO_TOKEN")
BOARD_ID = os.getenv("BOARD_ID")

if not KEY or not TOKEN or not BOARD_ID:
    raise ValueError("Missing TRELLO_KEY, TRELLO_TOKEN, or BOARD_ID in .env")

BASE_URL = "https://api.trello.com/1"

AUTH = {
    "key": KEY,
    "token": TOKEN,
}


def get(endpoint, params=None):
    if params is None:
        params = {}

    response = requests.get(
        f"{BASE_URL}{endpoint}",
        params={**AUTH, **params},
        timeout=30,
    )

    response.raise_for_status()
    return response.json()


print("Getting board information...")
board = get(f"/boards/{BOARD_ID}", {
    "fields": "all"
})

print(f"Board: {board['name']}")

print("Getting lists...")
lists = get(f"/boards/{BOARD_ID}/lists", {
    "fields": "all"
})

print("Getting cards...")
cards = get(f"/boards/{BOARD_ID}/cards", {
    "fields": "all",
    "members": "true",
    "member_fields": "fullName,username",
    "labels": "true",
    "checklists": "all",
})

print(f"Found {len(lists)} lists and {len(cards)} cards.")

export = {
    "board": board,
    "lists": lists,
    "cards": cards,
}

output_file = "trello_export.json"

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(export, f, indent=2, ensure_ascii=False)

print()
print("✅ Export complete!")
print(f"Saved to: {os.path.abspath(output_file)}")