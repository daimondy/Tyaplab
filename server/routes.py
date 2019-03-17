from flask import render_template, url_for, flash, redirect, request
from server import app, db, bcrypt
from server.forms import LoginForm, RegistationForm
from server.models import User
import sqlite3
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'message': 'Добро пожаловать на мой сайт. Здесь будет висеть рассписание группы БСТ1803. '
                   'Для того, чтобы увидеть рассписание, войдите в свой профиль.'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='Главная страница')


@app.route('/about')
def about():
    return render_template('about.html', title='О сайте')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Ваш аккаунт создан! Теперь вы можете войти', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Авторизация не прошла успешно. Пожалуйста, проверьте свой логин и пароль', 'danger')
    return render_template('login.html', title='Вход', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Аккаунт')


@app.route('/account/raspisanie', methods=['GET', 'POST'])
@login_required
def raspisanie():
    conn = sqlite3.connect('server/site.db')
    c = conn.cursor()
    c.execute("SELECT * FROM schedule")
    content = c.fetchall()
    return render_template('raspisanie.html', content=content)


@app.route('/account/raspisanie/edit', methods=['POST'])
def resp_edit():
    if request.method == 'POST':
        content = request.json
        user = User.query.filter_by(username=content['username']).first()
        print(content)
        if user and bcrypt.check_password_hash(user.password, content['password']):
            conn = sqlite3.connect('server/site.db')
            c = conn.cursor()
            day = str(content['day'])
            pare1 = str(content['pare1'])
            pare2 = str(content['pare2'])
            pare3 = str(content['pare3'])
            pare4 = str(content['pare4'])
            pare5 = str(content['pare5'])
            c.execute("UPDATE schedule SET pare1 = ?, pare2 = ?, pare3 = ?, pare4 = ?, pare5 = ? WHERE day = ?",
                      (pare1, pare2, pare3, pare4, pare5, day))
            conn.commit()
            return
    return
