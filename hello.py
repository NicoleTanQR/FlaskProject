from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World :)</p>"

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"

@app.route('/f/<celsius>')
def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return f"Input value: {celsius} C<br>Result: {fahrenheit:.2f} F"