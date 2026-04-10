from flask import Flask, jsonify, request

app = Flask(__name__)

cars_data = [
    {"marka": "BMW", "model": "X5", "qiymet": 45000, "sekil": "/static/bmw.jpg"},
    {"marka": "Mercedes", "model": "C200", "qiymet": 40000, "sekil": "/static/mercedes.jpg"},
    {"marka": "Toyota", "model": "Corolla", "qiymet": 25000, "sekil": "/static/toyota.jpg"}
]

@app.route("/cars")
def cars():
    marka = request.args.get("marka")
    max_price = request.args.get("price")

    result = cars_data

    if marka:
        result = [c for c in result if marka.lower() in c["marka"].lower()]

    if max_price:
        result = [c for c in result if c["qiymet"] <= int(max_price)]

    return jsonify(result)

@app.route("/")
def home():
    html = """
    <html>
    <head>
        <title>Car Showcase</title>
        <style>
            body {
                font-family: Arial;
                background: linear-gradient(to right, #141e30, #243b55);
                color: white;
                text-align: center;
            }
            .card {
                background: white;
                color: black;
                margin: 15px;
                padding: 15px;
                border-radius: 15px;
                width: 250px;
                display: inline-block;
            }
            img {
                width: 100%;
                border-radius: 10px;
            }
        </style>
    </head>
    <body>
        <h1>🚗 Cars</h1>
    """

    for car in cars_data:
        html += f"""
        <div class="card">
            <img src="{car['sekil']}">
            <h2>{car['marka']} {car['model']}</h2>
            <p>Qiymət: ${car['qiymet']}</p>
        </div>
        """

    html += "</body></html>"
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)