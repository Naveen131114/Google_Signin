from dotenv import load_dotenv
load_dotenv()
from flask import Flask, redirect, url_for, session, jsonify
from authlib.integrations.flask_client import OAuth
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from config import Config

# Load environment variables from .env

app = Flask(__name__)
app.config.from_object(Config)  # ✅ Load from config.py
app.secret_key = os.urandom(24)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
# Configure OAuth
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=app.config["GOOGLE_OAUTH_CLIENT_ID"],
    client_secret=app.config["GOOGLE_OAUTH_CLIENT_SECRET"],
    server_metadata_url=app.config["SERVER_METADATAT_URL"],
    client_kwargs=app.config["CLIENT_KWARGS"]
)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    google_id = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    profile_pic = db.Column(db.String(200))

@app.route('/')
def index():
    user = session.get('user')
    if user:
        return f"""
        <h1>Welcome {user['name']}</h1>
        <img src="{user['picture']}" alt="Profile Picture" width="100">
        <p>Email: {user['email']}</p>
        <a href="/logout">Logout</a>
        """
    return '<a href="/login">Login with Google</a>'

@app.route('/login')
def login():
    redirect_uri = "http://localhost:5000/callback/google"
    return google.authorize_redirect(redirect_uri)

@app.route('/callback/google')
def authorize():
    token = google.authorize_access_token()
    resp = google.get('https://openidconnect.googleapis.com/v1/userinfo')
    user_info = resp.json()
    print(user_info)
    session['user'] = user_info

    user = User.query.filter_by(google_id=user_info['sub']).first()
    if not user:
        user = User(
            google_id=user_info['sub'],
            name=user_info['name'],
            email=user_info['email'],
            profile_pic=user_info['picture']
        )
        db.session.add(user)
        db.session.commit()

    return redirect(app.config['FRONTEND_URL'])


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Or better: use flask db migrate/upgrade
    app.run(debug=True)