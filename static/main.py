from flask import Flask, render_template, request, url_for, redirect
from image import image_data
from pathlib import Path

app = Flask(__name__)

app = Flask(__name__)

app = Flask(__name__)

@app.route('/rgb/')
def rgb():
    path = Path(app.root_path) / "static" / "img"
    return render_template('rgb.html', images=image_data(path))
    #return render_template('rgb.html', images=image_data(Path(app.root_path)))







@app.route('/game/easy', methods=['GET', 'POST'])
def easy():
    names = get_names(SONGS)
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    form = NameForm()
    message = ""
    if form.validate_on_submit():
        name = form.name.data
        if name.lower() in names:
            # empty the form field
            form.name.data = ""
            id = get_id(SONGS, name)
            # redirect the browser to another route and template
            return redirect( url_for('hard', id=id) )
        else:
            message = "That song is not in our database."
    return render_template('game/easy.html', names=names, form=form, message=message)

@app.route('/bria/')
def bria():
    return render_template("bria.html")

@app.route('/game/medium')
def medium():
    return render_template("game/medium.html")

@app.route('/game/hard')
def hard():
    return render_template("game/hard.html")

@app.route('/riya/')
def riya():
    return render_template("riya.html")

@app.route('/sreeja/')
def sreeja():
    return render_template("sreeja.html")

@app.route('/valerie/')
def valerie():
    return render_template("valerie.html")

@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render aboutus.html
@app.route('/aboutus/')
def aboutus():
    return render_template("aboutus.html")


@app.route('/game/')
def game():
    return render_template("Favorites.html")


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

@app.route('/binary/', methods=['GET', 'POST'])
def binary():
    # submit button has been pushed
    if request.form:
        bits = request.form.get("bits")
        pic = request.form.get("pic")
        if pic == True:
            print("hi")
        if len(bits) != 0 and pic == True:  # input field has content
            return render_template("binary.html", BITS=int(bits), imgBulbOn="/static/assets/harryalbum.jpg", imgBulbOff="static/assets/paris.jpg")
        elif len(bits) != 0 and pic == False:
            return render_template("binary.html", BITS=int(bits), imgBulbOn="/static/assets/goodgoose.jpeg", imgBulbOff="/static/assets/goose.jpeg")
        elif pic == True:
            return render_template("binary.html", BITS=8, imgBulbOn="/static/assets/harryalbum.jpg", imgBulbOff="static/assets/paris.jpg")
    return render_template("binary.html", BITS=8, imgBulbOn="/static/assets/goodgoose.jpeg", imgBulbOff="/static/assets/goose.jpeg")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
