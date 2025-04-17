from flask import Flask, request
import datetime

app = Flask(__name__)

numberPlate = ["P11-09", "J12-32", "J62-59"]

@app.route('/')
def check_plate():
    x = request.args.get('plate')
    if not x:
        return "Gebruik: /?plate=<nummerplaat>", 400

    now = datetime.datetime.now()

    if x in numberPlate:
        if 7 <= now.hour < 12:
            return "Goedemorgen! Welkom bij Fonteyn Vakantieparken"
        elif 12 <= now.hour < 18:
            return "Goedemiddag! Welkom bij Fonteyn Vakantieparken"
        elif 18 <= now.hour < 23:
            return "Goedeavond! Welkom bij Fonteyn Vakantieparken"
        else:
            return "Welkom! (buiten standaarduren)"
    else:
        return "Verkeerde kenteken", 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)