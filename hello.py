"""Flask Web Framework - Flask project from demo"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Display a simple greeting."""
    return '<h1>Hello, World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    """Display a simple greeting based on parameter."""
    return f"Hello {name}"


@app.route('/f/<celsius>')
def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return f"Input value: {celsius} C<br>Result: {fahrenheit:.2f} F"


if __name__ == '__main__':
    app.run()
