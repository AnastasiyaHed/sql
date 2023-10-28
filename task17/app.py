from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@localhost/admindb'
db = SQLAlchemy(app)

#модель для таблицы регистрации
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)

with app.app_context():
    db.create_all()

#маршруты
@app.route('/')
def index():
    registrations = Registration.query.all()
    return render_template('index.html', registrations=registrations)

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']

    registration = Registration(name=name, email=email)
    db.session.add(registration)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)