from flask import Flask, session, request, render_template
import random

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route('/', methods=['GET', 'POST'])
def login():
    if 'login_attempts' not in session:
        session['login_attempts'] = 0

    login_attempts = session['login_attempts']

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        random_attempts = random.randint(5, 10)

        if login_attempts == random_attempts:
            session['login_attempts'] = 0
            return "Giriş başarılı! Hoş geldiniz, " + username + "!"
        else:
            session['login_attempts'] += 1
            return "Hatalı kullanıcı adı veya şifre."

    return render_template('login.html')

if __name__ == '__main__':
    app.run()
