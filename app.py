from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("dbname=service_db user=postgres password=postgres")

cursor = conn.cursor()

@app.route("/login/", methods=['GET'])
def index():
    return render_template('login.html')

@app.route("/login/", methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if not (username and password):
        return "You have not entered your username or password"
    cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
    records = list(cursor.fetchall())
    if not records:
        return "You are not registered"
    return render_template('account.html', full_names=records, password=password, login=username)
