from flask import Flask, render_template
from gunicorn import app
from formatter import formatter

app = Flask(__name__)

@app.route("/")
def hub_introduction():
    converted_content = []

    for i in range(1, 6):
        with open(f"templates/TEXTO{i}.txt", "r") as file:
            content = file.read()
            formatter_var = formatter(content)
            converted_content.append(formatter_var)

    return render_template('index.html', texts=converted_content)

if __name__ == '__main__':
    app.run()
