from flask_wtf import FlaskForm
from wtforms import DecimalField
from wtforms.validators import NumberRange


# Get method form for grabbing latlon
class LocationForm(FlaskForm):
    class Meta:
        csrf = False

    lat = DecimalField("Latitude", places=4, validators=[NumberRange(min=-90, max=90)])
    lon = DecimalField(
        "Longitude", places=4, validators=[NumberRange(min=-180, max=180)]
    )
