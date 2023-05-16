from flask import Flask, request, render_template, redirect, flash, url_for
from flask_debugtoolbar import DebugToolbarExtension

#import os
from forms import AddPetForm, EditPetForm
from models import db, connect_db, Pet

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pet_adoption"
# app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
#     "DATABASE_URL", "postgresql:///pet_adoption"
# )
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "mysecretkey"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)

connect_db(app)
app.app_context().push()

@app.route("/")
def show_pets():
    """Shows list of all pets up for adoption"""
    pets = Pet.query.all()
    return render_template("index.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add a pet."""

    form = AddPetForm()

    if form.validate_on_submit():

        name = form.name.data
        species = form.species.data
        age = form.age.data
        available = form.available.data
        notes = form.notes.data
        
        new_pet = Pet(name=name, species=species, age=age, available=available, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        #flash(f"{new_pet.name} added.")
        return redirect("/")

    else:
        # re-present form for editing
        return render_template("add_pet_form.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        #flash(f"{pet.name} updated.")
        return redirect('/')

    else:
        # failed; re-present form for editing
        return render_template("edit_pet_form.html", form=form, pet=pet)

if __name__ == "__main__":
    app.run(debug=True)