from flask import Flask, request
from perpclone import perplexity_clone
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    query = request.json["query"]
    if os.getenv("PROXY"):
        return {"result": perplexity_clone(
            query,
            proxies={
                "http": os.getenv("PROXY"),
                "https": os.getenv("PROXY")
            }
        )}
    else:
        return {"result": perplexity_clone(query)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)