from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, TextAreaField, SubmitField

from wtforms.validators import InputRequired, Optional, NumberRange, URL, Length


class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField(
        "Pet name", render_kw={'class': 'form-control'}, validators=[InputRequired(message="Name cannot be blank")]
    )
    species = StringField(
        "Species", render_kw={'class': 'form-control'}, validators=[InputRequired(message="Species cannot be blank")]
    )
    photo_url = StringField(
        "Photo URL", render_kw={'class': 'form-control'},
        validators=[URL(message="Please enter a valid URL")],
    )
    age = IntegerField("Age", render_kw={'class': 'form-control'}, validators=[NumberRange(min=0, max=30)])

    available = BooleanField("Is available", render_kw={'class': 'form-check-input'}, default="checked")

    notes = TextAreaField("Notes", render_kw={'class': 'form-control'}, validators=[Optional(), Length(min=10)])

    submit = SubmitField('Add Pet', render_kw={'class': 'btn btn-success'})


class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    name = StringField(
        "Pet name", render_kw={'class': 'form-control'}, validators=[InputRequired(message="Name cannot be blank")]
    )

    photo_url = StringField(
        "Photo URL", render_kw={'class': 'form-control'},
        validators=[URL(message="Please enter a valid URL")],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )

    available = BooleanField("Is available", render_kw={'class': 'form-check-input'}, default="checked")

    submit = SubmitField('Edit Pet', render_kw={'class': 'btn btn-success'})
