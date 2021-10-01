# import "packages" from flask
from pathlib import Path

from flask import Flask, render_template, request
from algorithms.image import rotatehack, sonakshi_image_data, kashish_image_data


# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def home():
    return render_template("home.html")


# connects /kangaroos path to render home.html
@app.route('/asia/')
def asia():
    return render_template("asia.html")

@app.route('/africa/')
def africa():
    return render_template("africa.html")

@app.route('/northamerica/')
def northamerica():
    return render_template("northamerica.html")

@app.route('/southamerica/')
def southamerica():
    return render_template("southamerica.html")

@app.route('/antarctica/')
def antarctica():
    return render_template("antarctica.html")

@app.route('/europe/')
def europe():
    return render_template("europe.html")

@app.route('/australia/')
def australia():
    return render_template("australia.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route("/binary", methods=['GET','POST'])
def binary():
    if request.form:
        bits = request.form.get("bits")
        if len(bits) != 0:  # input field has content
            return render_template("binary.html", bits=int(bits))
        # starting and empty input default
    return render_template("binary.html", bits=8)

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

@app.route('/sonakshirgb/', methods=['GET', 'POST'])
def sonakshirgb():
    trash = sonakshi_image_data()
    rotate = rotatehack
    colorList = []
    grayList = [] # pass in the lists from the image_data() function
    for img in trash:
        colorList.append(img['base64'])
        grayList.append(img['base64_GRAY'])
    try:
        if request.form:
            option = request.form["option"]
        if option == 'yes':
            return render_template("sonakshirgb.html", images=rotate)
        elif option == 'no':
            return render_template("sonakshirgb.html", images=trash, colored=colorList, grayed=grayList)
        else:
            return render_template("sonakshirgb.html", images=trash, colored=colorList, grayed=grayList)
    except:
        return render_template("sonakshirgb.html", images=trash, colored=colorList, grayed=grayList)


@app.route('/kashishrgb/', methods=['GET', 'POST'])
def kashishrgb():
    trash = kashish_image_data()
    colorList = []
    grayList = [] # pass in the lists from the image_data() function
    for img in trash:
        colorList.append(img['base64'])
        grayList.append(img['base64_GRAY'])
    return render_template("kashishrgb.html", images=trash, colored=colorList, grayed=grayList )



@app.route('/insights/')
def insights():
    return render_template("insights.html")

@app.route('/greet/')
def greet():
    return render_template("greet.html")




# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
