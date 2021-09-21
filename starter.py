@starter_bp.route('/rgb/')
def rgb():
    return render_template('starter/rgb.html', images=image_data())