from flask import *
import random
import chinchilla

app = Flask(__name__)
chinchilla_list = chinchilla.Chinchilla.get_chinchillas()

@app.route("/")
def index():
    print(chinchilla_list)
    return jsonify(
        url=random.choice(chinchilla_list)
    )



