from os import environ
from flask import Flask
import bot

app = Flask(__name__)

@app.route("/")
def home():
    bot.main()
    return "Commenting..."

app.run(host= '0.0.0.0', port=environ.get('PORT'))
