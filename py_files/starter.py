@starter_bp.route('/rgb/')
def rgb():
    return render_template('starter/sonakshirgb.html', images=image_data())

