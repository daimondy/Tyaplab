import os
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistationForm, LoginForm

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
posts = [
    {
        'message':'Добро пожаловать на мой сайт. Здесь будет висеть рассписание группы БСТ1803'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts, title = 'Главная страница')


@app.route('/about')
def about():
    return render_template('about.html', title = 'О сайте')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistationForm()
    if form.validate_on_submit():
        flash(f'Аккаунт создан с именем {form.username.data}.', 'success')
        return  redirect(url_for('home'))
    return render_template('register.html', title='Регистрация', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Вы вошли в систему!')
            return redirect(url_for('home'))
        else:
            flash('Авторизация не прошла успешно. Пожалуйста, проверьте свой логин и пароль', 'danger')
    return render_template('login.html', title='Вход', form = form)


if __name__ == '__main__':
    app.run(debug=True)  # не нужно перезагружать сервер