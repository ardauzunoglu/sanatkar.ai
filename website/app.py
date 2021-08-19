import tensorflow as tf
import numpy as np
import time
from tensorflow.keras.layers.experimental import preprocessing
from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = ""
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Archive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    generated_text = db.Column(db.String(500))
    runtime = db.Column(db.Float())
    art_branch = db.Column(db.String(10))
    genre = db.Column(db.String(30))

def generate_text(model_choice, seed, length):

    model_dict = {
        "pop":"pop_generator",
        "rap":"rap_generator",
        "rock":"rock_generator",
        "cumhuriyet_donemi_saf_siir":"cumhuriyet_donemi_saf_siir_generator",
        "garip_siiri":"garip_siiri_generator",
        "milli_edebiyat":"milli_edebiyat_generator",
        "kadin_tirad":"kadin_tirad_generator",
        "erkek_tirad":"erkek_tirad_generator"
    }

    used_model = model_dict[model_choice]
    model = tf.saved_model.load(used_model)

    start = time.time()
    states = None

    next_char = tf.constant([seed])
    result = [next_char]

    for n in range(length):
        next_char, states = model.generate_one_step(next_char, states=states)
        result.append(next_char)

    result = tf.strings.join(result)
    end = time.time()

    output = result[0].numpy().decode('utf-8'), '\n\n' + '_'*80
    runtime = end - start

    return output, runtime

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/metin_uret")
def generate_text_page():
    return render_template("metin_uretimi.html")

@app.route("/metin_uret/<string:generator_type>", methods=["POST"])
def generate_text_page_post(generator_type):
    output, runtime = generate_text(generator_type, seed_input, length_input)

    return render_template("metin_uretimi.html", output=output, runtime=runtime, is_text_generated=True)

@app.route("/arsiv")
def archive():
    archive = Archive.query.all()

    return render_template("arsiv.html", archive=archive)

@app.route("/arsiv/<int:id>")
def particular_archive_element(id):
    archived_generation = Archive.query.filter_by(id = id).first()
    generated_text = archived_generation.generated_text
    runtime = archived_generation.runtime
    art_branch = archived_generation.art_branch
    genre = archived_generation.genre

    return render_template("spesifik_arsiv.html", generated_text=generated_text, runtime=runtime, art_branch=art_branch, genre=genre)

@app.route("/hakkimizda")
def about_us():
    return render_template("hakkimizda.html")

if __name__ == "__main__":
    app.run(debug=True)