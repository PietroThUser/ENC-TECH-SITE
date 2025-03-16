from flask import Flask, render_template, abort
from gunicorn import app
from formatter import formatter

app = Flask(__name__)

@app.route("/curso/<int:actual_text>")
def hub_introduction(actual_text):
    with open(f"templates/TEXTOS/TEXTO{actual_text}.txt", "r") as file:
        content = file.read()
        actual_text = formatter(content)

    return render_template('text.html', text=actual_text)

@app.route("/")
def home():
    with open("templates/roadmap.txt", "r") as roadmap_archive:
        roadmap_content = roadmap_archive.read()
        roadmap_text = formatter(roadmap_content)

    return render_template('index.html', roadmap=roadmap_text)

if __name__ == '__main__':
    app.run()
