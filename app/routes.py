from flask import render_template, flash, redirect, request
from app import app

from app.forms import LocationForm
import api.weather as weather


@app.route("/")
@app.route("/index")
def index():
    form = LocationForm()
    if form.validate_on_submit():
        flash("Location")
        return redirect("/dashboard")

    return render_template("index.html", form=form)


@app.route("/dashboard")
def dashboard():
    # Check if we have valid GET information
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    if not lat or not lon:
        return redirect("/index")

    # Validate latitude and longitude
    if not weather.validate_latlon(float(lat), float(lon)):
        return redirect("/index")

    forecasts = weather.get_forecast(app.config["USER_AGENT"], lat, lon)

    return render_template("dashboard.html", forecasts=forecasts)
