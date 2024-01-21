"""
Random Color App
"""
import random

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# random choice of colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


@app.get("/")
def run_color_app(request: Request):
    """
    This function returns a html template with a random color
    """
    return templates.TemplateResponse(
        "index.html", {"request": request, "color": random.choice(colors)}
    )
