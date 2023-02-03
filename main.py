from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = '79a0a6ab193c56a4d78d8a702aac30fd'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')


def criar_conta():
    return  render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
