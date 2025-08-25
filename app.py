from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.getenv("bot_api_key")  # replace with your bot token
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    # extract chat id and message
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        # Simple reply logic
        if text.lower() == "hello":
            send_message(chat_id, "Hi, I’m Orbit 🚀")
        else:
            send_message(chat_id, f"You said: {text}")

    return {"ok": True}


def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)


if __name__ == "__main__":
    app.run(port=5000, debug=True)