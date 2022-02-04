from flask import Blueprint, render_template, request
from .fibonacci import Fibonacci

app_algorithm = Blueprint('algorithm', __name__,
                          url_prefix='/algorithm',
                          template_folder='templates/algorithm',
                          static_folder='static',
                          static_url_path='assets')


@app_algorithm.route('/fibonacci/', methods=["GET", "POST"])
def fibonacci():
    if request.form:
        return render_template("api/Used/fibonacci.html", fibonacci=Fibonacci(int(request.form.get("series"))))
    return render_template("api/Used/fibonacci.html", fibonacci=Fibonacci(2))