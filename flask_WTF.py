from forms import ContactForm
from flask import Flask, render_template
from flask_wtf import Form
from wtforms import TextField
from flask import Flask, redirect, url_for, render_template, request
Flask.redirect(location, statuscode, response)


class ContactForm(Form):
    name = TextField("Name Of Student")


# 为html脚本
# <input id = "csrf_token" name = "csrf_tkoen" type = "hidden" / >
# <label for = "name" > Name Of Student < /label > <br >
# <input id = "name" name = "name" type = "text" value = "" / >

# flask文本中
app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/contact')
def contect():
    form = ContactForm()
    return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run()
