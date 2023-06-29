from flask import *
import mysql.connector
import random

capybara_list=[]

app = Flask(__name__)

urls = open("urls.txt", "r")

for i in urls:
    capybara_list.append(i.replace("\n", ""))

@app.route("/")
def index():
    print(capybara_list)
    return jsonify(
        url=random.choice(capybara_list)
    )



