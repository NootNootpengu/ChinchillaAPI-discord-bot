from flask import *
import mysql.connector
import random
import capybara

app = Flask(__name__)
capybara_list = capybara.Capybara.get_capybaras()

@app.route("/")
def index():
    print(capybara_list)
    return jsonify(
        url=random.choice(capybara_list)
    )



