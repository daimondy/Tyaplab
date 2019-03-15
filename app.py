from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'day': 'Понедельник',
        'pare1': 'Физика',
        'pare2': 'Математика'
    },
    {
        'day': 'Вторник',
        'pare1': 'Информатика',
        'pare2': 'Физ-ра'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts, title = 'Главная страница')


@app.route('/about')
def about():
    return render_template('about.html', title = 'О сайте')


if __name__ == '__main__':
    app.run(debug=True)  # не нужно перезагружать сервер
