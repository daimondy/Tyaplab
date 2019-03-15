import os
from flask import Flask, render_template, url_for
from forms import RegistationForm, LoginForm

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
posts = [
    {
        'day': 'Понедельник',
        'pare1': 'Физика',
        'pare2': 'Математика',
        'time':'9:30-11:05',
        'time2':'11:15-12:50'
    },
    {
        'day': 'Вторник',
        'pare1': 'Информатика',
        'pare2': 'Физ-ра',
        'time':'9:30-11:05',
        'time2':'11:15-12:50'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts, title = 'Главная страница')


@app.route('/about')
def about():
    return render_template('about.html', title = 'О сайте')

@app.route('/register')
def register():
    form = RegistationForm()
    return render_template('register.html', title='Регистрация', form = form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Вход', form = form)


if __name__ == '__main__':
    app.run(debug=True)  # не нужно перезагружать сервер