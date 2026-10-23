import json
from pathlib import Path
from flask import Flask, render_template

app = Flask(__name__)
CONTENT_FILE = Path(__file__).resolve().parent / "content.json"

def get_content():
    """Reads the latest content from the JSON file."""
    try:
        with CONTENT_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "recipient": "My Love",
            "message": "I love you!",
            "bg_image_url": "",
            "song_url": ""
        }

@app.route("/")
def home():
    content = get_content()
    return render_template("index.html", content=content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)