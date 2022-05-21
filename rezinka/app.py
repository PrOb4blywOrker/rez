from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

post = [{
        'name': 'Графічний дизайн',
        'price': '1200грн',
        'contact': 'Контакти адміна'
},
    {
        'name': 'QA-automation',
        'price': '1500грн',
        'contact': 'Контакти адміна'
},
    {
        'name': 'PHP Web-development',
        'price': '1700грн',
        'contact': 'Контакти адміна'
},
    {
        'name': 'Node.js',
        'price': '1200грн',
        'contact': 'Контакти адміна'
},
    {
        'name': 'Kotlin',
        'price': '1500грн',
        'contact': 'Контакти адміна'
},
    {
        'name': 'React.js',
        'price': '1700грн',
        'contact': 'Контакти адміна'
},
    {
        'name': 'iT Project Management',
        'price': '1700грн',
        'contact': 'Контакти адміна'
},
    {
        'name': 'Тестування ПЗ (QA)',
        'price': '1500грн',
        'contact': 'Контакти адміна'
},
    {
        'name': 'Основи програмування',
        'price': '1700грн',
        'contact': 'Контакти адміна'
},
    {
        'name': 'Java',
        'price': '1700грн',
        'contact': 'Контакти адміна'
     }
]


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
