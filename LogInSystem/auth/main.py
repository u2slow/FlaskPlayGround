from flask import Flask,request,jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class profile():
    loggetIn = False

user = profile()

class ProfileModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        		return f"id: {self.id} email: {self.email} pass: {self.password}"

@app.route('/login', methods=['POST'])
def login():
    postemail = request.form.get('email')
    postpassword = request.form.get('password')
    dbemail = ProfileModel.query.filter_by(email=postemail).first()
    if dbemail != None:
        if dbemail.password == postpassword:
            user.loggetIn = True
            return jsonify({"message": True})

    return jsonify({"message": False})
    

@app.route('/profile', methods=['GET'])
def profile():
    if user.loggetIn:
        return jsonify({"message": "userdate"})
    else:
        return jsonify({"message": "first log in"})

@app.route('/register', methods=['POST'])
def register():
    selfemail = request.form.get('email')
    selfpassword = request.form.get('password')

    new_Profile = ProfileModel(email = selfemail, password = selfpassword)

    db.session.add(new_Profile)
    db.session.commit()
    return jsonify({"message": "super"})


if __name__ == "__main__":
    app.run(debug=True)
