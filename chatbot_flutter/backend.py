from flask import Flask

app = Flask(__name__)

# Создаю API 
@app.route("/")
def index():
     return "Hello, Maksim!"

if __name__ == "__main__":
    app.run()