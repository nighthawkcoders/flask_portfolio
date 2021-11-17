# import "packages" from flask
from flask import Flask, render_template
from algorithms.connor import c_image
from pathlib import Path

# create a Flask instance
app = Flask(__name__)


@app.route('/connor/')
def connor():
    path = Path(app.root_path) / "static" / "assets"
    return render_template('connor.html', images=c_image(path))


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
