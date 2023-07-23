from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'secretly'
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
 
def create_db():
    with app.app_context():
        db.create_all()
    print('Created Database!')
 
if __name__ == '__main__':
    app.run(debug=True)