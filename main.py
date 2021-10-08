# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
from algorithms.image import image_data

app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")

@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")

@app.route('/binary', methods=['GET', 'POST'])
def binary():
    if request.form:
        bits = request.form.get("bits")
        if len(bits) != 0:  # input field has content
            return render_template("binary.html", bits=int(bits))
        # starting and empty input default
    return render_template("binary.html", bits=12)


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")


@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greet.html", name=name)
    # starting and empty input default
    return render_template("greet.html", name="World")

@app.route('/grid')
def grid():
    return render_template("grid.html")

@app.route('/wireframes')
def wireframes():
    return render_template("wireframes.html")

@app.route('/aboutme')
def aboutme():
    return render_template("aboutme.html")

@app.route('/week3')
def week3():
    return render_template("week3.html")

@app.route('/rgb', methods=["GET", "POST"])
def rgb():
    return render_template("rgb.html", images=image_data())

@app.route('/list')
def list():
    return render_template("list.html")

@app.route('/colorcodes')
def colorcodes():
    return render_template("colorcodes.html")


@app.route('/logicgates')
def logicgates():
    return render_template("logicgates.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)