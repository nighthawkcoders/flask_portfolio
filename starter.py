@starter_bp.route('/rgb/')
def rgb():
    return render_template('starter/rgb.html', images=image_data())
© 2021 GitHub, Inc.
