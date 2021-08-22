import tensorflow as tf
import numpy as np
from tensorflow.keras.layers.experimental import preprocessing
from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='templates/static')
app.config["SQLALCHEMY_DATABASE_URI"] = ""
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Archive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    generated_text = db.Column(db.String(500))
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

    states = None

    next_char = tf.constant([seed])
    result = [next_char]

    for n in range(length):
        next_char, states = model.generate_one_step(next_char, states=states)
        result.append(next_char)

    result = tf.strings.join(result)

    output = result[0].numpy().decode('utf-8'), '\n\n' + '_'*80
    
    return output

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/archive")
def archive():
    archive = Archive.query.all()

    return render_template("archive.html", archive=archive)

@app.route("/archive/<int:id>")
def particular_archive_element(id):
    archived_generation = Archive.query.filter_by(id = id).first()
    generated_text = archived_generation.generated_text
    art_branch = archived_generation.art_branch
    genre = archived_generation.genre

    return render_template("generator_output.html", generated_text=generated_text, art_branch=art_branch, genre=genre)

@app.route("/contact")
def about_us():
    return render_template("contact.html")

@app.route("/generator")
def generate_text_page():
    return render_template("generator.html")

@app.route("/generator_output/<string:generator_type>", methods=["POST"])
def generate_text_page_post(generator_type):
    output = generate_text(generator_type, seed_input, length_input)

    return render_template("metin_uretimi.html", output=output, is_text_generated=True)

if __name__ == "__main__":
    app.run(debug=True)