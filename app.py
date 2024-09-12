from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Azure! This is a Flask app."

if __name__ == "__main__":
    app.run(debug=True)
