# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def home():
    return render_template("home.html")


# connects /kangaroos path to render home.html


@app.route('/about/')
def about():
    return render_template("about.html")


@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route('/sonakshi', methods=['GET', 'POST'])
def sonakshi():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("sonakshi.html", name=name)
    # starting and empty input default
    return render_template("sonakshi.html", name="World")

@app.route('/saumya', methods=['GET', 'POST'])
def saumya():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("saumya.html", name=name)
    # starting and empty input default
    return render_template("saumya.html", name="World")

@app.route('/kashish', methods=['GET', 'POST'])
def kashish():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("kashish.html", name=name)
    # starting and empty input default
    return render_template("kashish.html", name="World")

@app.route('/concepts/')
def concepts():
    return render_template("concepts.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
