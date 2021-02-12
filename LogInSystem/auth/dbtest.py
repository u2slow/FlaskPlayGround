from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ProfileModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
    		return f"id: {self.id} email: {self.email} pass: {self.password}"

def write():
    email = input("email?")
    passwd = input("pass?")
    new_profile = ProfileModel(email=email, password=passwd)
    db.session.add(new_profile)
    db.session.commit()

def read():
    print(ProfileModel.query.all())

if __name__ == "__main__":
    write()
    read()