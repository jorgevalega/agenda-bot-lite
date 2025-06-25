# app/web/routes.py

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def inicio():
    return "Agenda Bot Lite funcionando"
