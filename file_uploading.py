# enctype 属性设置为multipart/form-data,将文件发布到URL

# url处理程序从request.file[]对象中提取文件，然后保存到所需位置

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

import os


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload/'


@app.route('/upload')
def upload_file():
    return remder_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uplloader():
    if request.method == 'POST':
        f = request.files['file']
        print(request.files)
        f.save(os.path.join(
            app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return 'file uploaded successfully'
    else:
        return render_template('upload.html')


if __name__ == '__main__'
app.run()
