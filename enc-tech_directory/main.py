from flask import Flask, render_template, abort
from gunicorn import app
from formatter import formatter

app = Flask(__name__)

@app.route("/curso/<int:actual_text>")
def hub_introduction(actual_text):
    with open(f"templates/TEXTOS/TEXTO{actual_text}.txt", "r") as file:
        content = file.read()
        actual_text = formatter(content)

    return render_template('index.html', text=actual_text)

@app.route("/")
def home():
    return render_template('intro.html')

if __name__ == '__main__':
    app.run()
