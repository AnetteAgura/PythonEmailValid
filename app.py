from flask import Flask, render_template, request
import re

app = Flask(__name__)

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/checked/', methods=['POST'])
def checked():
    email = request.form['email']
    if re.fullmatch(regex, email):
        return "<body style=' font-family: Verdana, sans-serif; background:#456990; '></body>" \
               "<p style='margin-top: 10%; text-align: center;color: #90ee90 ;font-size: larger; font-size: 70px;'>😄 " \
               "This " \
               " email is valid 😄</p>" \
               "<a href='../' style='background: white; text-align:center; border-radius: 25px; margin-left:46%; " \
               "font-size: 50px; text-decoration:none; color: black; border: 5px solid black;'>BACK</a> "

    else:
        return "<body style=' font-family: Verdana, sans-serif; background:#456990; '></body>" \
               "<p style='margin-top: 10%; text-align: center;color: #FF7F7F;font-size: larger; font-size: 70px;'>😞 " \
               "This " \
               " email is invalid 😞</p>" \
               "<a href='../' style='background: white; text-align:center; border-radius: 25px; margin-left:46%; " \
               "font-size: 50px; text-decoration:none; color: black; border: 5px solid black;'>BACK</a> "


if __name__ == '__main__':
    app.run()
