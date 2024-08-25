from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Создаю объект 
app = Flask(__name__) 
# обращаюсь к словарю, прописываю базу, с которой работаю
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///python_flask.db'
#Работаю с БД
db = SQLAlchemy(app)

# Создаю класс, которые будет отображать таблицу БД
class Article (db.Model):
    id = db.Column(db.Integer, primary_key = True) # primary_key = True - уникальное поле
    title = db.Column(db.String(100) , nullable = False)
    intro = db.Column(db.String(300) , nullable = False)
    text = db.Column(db.Text , nullable = False)
    date = db.Column(db.DateTime, default = datetime.utcnow())

with app.app_context():
    db.create_all()

# С помощью декоратора обращаюсь к путям (корням) 
@app.route('/')
@app.route('/home') 
def index(): 
    return render_template("index.html")

@app.route('/about') 
def about():  # Изменил имя функции, чтобы избежать конфликта
    return render_template("about.html")

@app.route('/create_article') 
def create_article():  # Изменил имя функции, чтобы избежать конфликта
    return render_template("create-article.html") 


@app.route('/user/<string>: name/<int>:id') 
def user(name, id):  # Изменил имя функции, чтобы избежать конфликта
    return "User name: " + name + "User id: " + str(id)

# Если файл главный, то есть тот, который запускает сервер 
if __name__ == "__main__": 
    # Запускаю сервер (если debug=True - вывожу все ошибки на страницу) 
    app.run(debug=True)
