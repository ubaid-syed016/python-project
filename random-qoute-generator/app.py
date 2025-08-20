import random
from flask import Flask, jsonify

app = Flask(__name__)

quotes = [
    "Life is what happens when you're busy making other plans.",
    "The purpose of our lives is to be happy.",
    "Get busy living or get busy dying.",
    "You only live once, but if you do it right, once is enough."
]

@app.route('/quote')
def random_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
