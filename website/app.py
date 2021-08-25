import tensorflow as tf
import numpy as np
from tensorflow.keras.layers.experimental import preprocessing
from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='templates/static')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./archive.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Archive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    generated_text = db.Column(db.String(600))
    art_branch = db.Column(db.String(10))
    genre = db.Column(db.String(30))
    seed_input = db.Column(db.String(35))
    length_input = db.Column(db.String(3))

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_and_surname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone_number = db.Column(db.String(20))
    topic = db.Column(db.String(100))
    message = db.Column(db.String())

def generate_text(model_choice, seed, length):

    model_dict = {
        "pop":"pop_generator",
        "rap":"rap_generator",
        "rock":"rock_generator",
        "cumhuriyet":"cumhuriyet_donemi_saf_siir_generator",
        "garip":"garip_siiri_generator",
        "milliedebiyat":"milli_edebiyat_generator",
        "kadın":"kadin_tirad_generator",
        "erkek":"erkek_tirad_generator"
    }

    art_form_dict = {
        "pop":"song_generators",
        "rap":"song_generators",
        "rock":"song_generators",
        "cumhuriyet":"poem_generators",
        "garip":"poem_generators",
        "milliedebiyat":"poem_generators",
        "kadın":"tirade_generators",
        "erkek":"tirade_generators"
    }

    used_model = model_dict[model_choice]
    art_form_of_model = art_form_dict[model_choice]
    model = tf.saved_model.load("models/"+art_form_of_model+"/"+used_model)

    states = None

    next_char = tf.constant([seed])
    result = [next_char]

    for n in range(int(length)):
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

    id = archived_generation.id
    generated_text = archived_generation.generated_text
    art_branch = archived_generation.art_branch
    genre = archived_generation.genre
    seed_input = archived_generation.seed_input
    length_input = archived_generation.length_input

    output = str(generated_text).replace("_", "").replace(")", "").replace("(", "").replace("'", "").replace('"',"").split("\\n")
    output = list(filter(None, output))[:-1]

    return render_template("generator_output.html", id = id, output=output, art_branch=art_branch, genre=genre, seed_input=seed_input, length_input=length_input)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contact", methods=["POST"])
def contact_post():
    name_and_surname = request.form["name_and_surname"]
    email = request.form["email"]
    phone_number = request.form["phone_number"]
    topic = request.form["topic"]
    message = request.form["message"]

    new_contact = Contact(name_and_surname=name_and_surname, email=email, phone_number=phone_number, topic=topic, message=message)
    db.session.add(new_contact)
    db.session.commit()

    return render_template("contact.html", contact_status="Success")

@app.route("/generator")
def generate_text_page():
    return render_template("generator.html")

@app.route("/generator", methods=["POST"])
def generate_text_page_post():
    art_form = request.form["mainartform"]
    
    art_form_dict = {
        "sarki":"songartform",
        "siir":"poetartform",
        "tirad":"tiradartform"
    }
    
    sub_art_form = art_form_dict[art_form]

    generator_type = request.form[sub_art_form]
    seed_input = request.form["startinginput"]
    length_input = request.form["outputlimit"]

    output = str(generate_text(generator_type, seed_input, length_input))

    art_branch_corrector = {
        "sarki":"Şarkı",
        "siir":"Şiir",
        "tirad":"Tirad"
    }

    genre_corrector = {
        "pop":"Pop",
        "rap":"Rap",
        "rock":"Rock",
        "cumhuriyet":"Cumhuriyet Dönemi Saf Şiir",
        "garip":"Garip Şiiri",
        "milliedebiyat":"Milli Edebiyat",
        "kadın":"Kadın Karakter",
        "erkek":"Erkek Karakter"
    }

    art_branch = art_branch_corrector[art_form]
    genre = genre_corrector[generator_type]

    new_archive = Archive(generated_text = output, art_branch = art_branch, genre = genre, seed_input = seed_input, length_input = length_input)
    db.session.add(new_archive)
    db.session.commit()

    return redirect(url_for("particular_archive_element", id=new_archive.id))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)