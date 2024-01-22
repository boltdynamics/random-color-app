from flask import Flask, render_template
import random

app = Flask(__name__)

# random choice of colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

@app.route("/")
def run_color_app():
    """
    This function returns a html template with a random color
    """
    color = random.choice(colors)
    return render_template("index.html", color=color)
