from flask import Flask, render_template, redirect, request
from pathlib import Path
from Units import *
from Converters import *

BASE_DIR = Path(__file__).resolve().parent

TEMPLATES_DIR = BASE_DIR / 'templates'
STATIC_DIR = BASE_DIR / 'static'


app = Flask(
    "Unit converter",
    template_folder=TEMPLATES_DIR,
    static_folder=STATIC_DIR,
)

@app.route('/')
def main():
    return redirect("/length")

@app.route("/length")
def main_length():
    return render_template("main_page_length.html", result="", unit_type="length")

@app.route("/weight")
def main_weight():
    return render_template("main_page_weight.html", result="", unit_type="weight")

@app.route("/temperature")
def main_temperature():
    return render_template("main_page_temperature.html", result="", unit_type="temperature")

@app.route("/convert", methods=["POST"])
def convert():
    user_value = float(request.form.get("userValue"))
    from_unit = request.form.get("fromUnit")
    to_unit = request.form.get("toUnit")
    unit_type = request.form.get("unitType")

    

    if from_unit == to_unit:
        match unit_type:
            case UnitTypes.length:
                return render_template("main_page_length.html", result=f"{user_value:.3f}", unit_type="length")
            case UnitTypes.weight:
                return render_template("main_page_weight.html", result=f"{user_value:.4f}", unit_type="weight")
            case UnitTypes.temperature:
                return render_template("main_page_temperature.html", result=f"{user_value:.3f}", unit_type="temperature")

    match unit_type:
        case UnitTypes.length:
            return render_template("main_page_length.html", result=f"{LengthConverter.convert(user_value, from_unit, to_unit):.3f}", unit_type="length")
        case UnitTypes.weight:
            return render_template("main_page_weight.html", result=f"{WeightConverter.convert(user_value, from_unit, to_unit):.4f}", unit_type="weight")
        case UnitTypes.temperature:
            return render_template("main_page_temperature.html", result=f"{TemperatureConverter.convert(user_value, from_unit, to_unit):.3f}", unit_type="temperature")
          


    # if unit_type == "length":
    #     # Переводим в метры
    #     if from_unit == Length.kilometers:
    #         user_value *= 1000
    #     elif from_unit == Length.foots:
    #         user_value /= 3.281
    #     elif from_unit == Length.miles:
    #         user_value *= 1609
    #     elif from_unit == Length.inches:
    #         user_value /= 39.37

    #     if to_unit == Length.inches:
    #         result = user_value * 39.37
    #     elif to_unit == Length.miles:
    #         result = user_value / 1609
    #     elif to_unit == Length.foots:
    #         result = user_value * 3.281
    #     elif to_unit == Length.kilometers:
    #         result = user_value / 1000

        # return render_template("main_page_length.html", result=f"{result:.3f}")





if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)