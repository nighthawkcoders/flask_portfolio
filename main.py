# import "packages" from flask

from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)

#zonk was here
#bria was here lol xd
# connects default URL to render index.html
@app.route('/bria/')
def bria():
    return render_template("bria.html")

@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render aboutus.html
@app.route('/aboutus/')
def aboutus():
    return render_template("aboutus.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/Game/')
def Game():
    return render_template("Game.html")


@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route('/minilabs/')
def video():
    return render_template("minilabs.html")

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.form:
        fname = request.form.get("fname")
        if len(fname) != 0:  # input field has content
            return render_template("stub.html", fname=fname)
        else:
            return render_template("stub.html", fname="World")




# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
