from flask import Flask, session, render_template, request, redirect
import pyrebase


app = Flask(__name__)

config = {
    "apiKey": "AIzaSyBiM7pShglQoWESauwAhsmnDFYzFrBwj3k",
    "authDomain": "testing-with-fastapi.firebaseapp.com",
    "projectId": "testing-with-fastapi",
    "storageBucket": "testing-with-fastapi.appspot.com",
    "messagingSenderId": "117877501282",
    "appId": "1:117877501282:web:b7916553b4c2d24cf8503b",
    "measurementId": "G-JLPNZ0GLGC",
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app.secret_key = 'secret'


@app.route('/', methods=['POST', 'GET'])
def index():
    if 'user' in session:
        return "Hi, {}".format(session['user'])
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = email
            return redirect('/')
        except:
            return 'Failed To Login'
    return render_template('home.html')


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    session.pop("user")
    return redirect('/')


if __name__ == '__main__':
    app.run(port=9999)

