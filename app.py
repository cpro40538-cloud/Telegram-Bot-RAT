import os
import requests
from flask import Flask, request, jsonify

BOT_TOKEN = "8954948878:AAFGDdv7tAomWcqXNWZnM-FVzQVTOcLiKWU"
ADMIN_CHAT_ID = "8140401592"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return "OK", 200

    data = request.get_json(force=True)
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        if str(chat_id) == ADMIN_CHAT_ID:
            if text == "/Alldevice":
                reply = "Danh sách thiết bị: chưa có dữ liệu"
                requests.post(f"{BASE_URL}/sendMessage", json={"chat_id": chat_id, "text": reply})
    return jsonify({"ok": True}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
