from flask import Flask, render_template, request
from models import UploadForm
from werkzeug import secure_filename
import os

application = Flask(__name__)
application.config['SECRET_KEY'] = '1234567890!@#$%^&*()'
application.config['UPLOAD_FOLDER'] = os.path.realpath('.') + \
    '/static/uploads'

#satuan byte
application.config['MAX_CONTENT_PATH'] = 10000000

@application.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm(request.form)
    if request.method == 'POST':
        f = request.files['file']
        filename = application.config['UPLOAD_FOLDER'] + \
            '/' + secure_filename(f.filename)
        try:
            f.save(filename)
            return render_template('upload_sukses.html',
                filename=secure_filename(f.filename))
        except:
            return render_template('upload_gagal.html')
    return render_template('form.html', form=form)

if __name__ == '__main__':
    application.run(debug=True)
