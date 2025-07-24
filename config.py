import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    GOOGLE_OAUTH_CLIENT_ID=os.getenv("GOOGLE_OAUTH_CLIENT_ID")
    GOOGLE_OAUTH_CLIENT_SECRET=os.getenv("GOOGLE_OAUTH_CLIENT_SECRET")
    SERVER_METADATAT_URL='https://accounts.google.com/.well-known/openid-configuration'
    CLIENT_KWARGS={
        'scope': 'openid email profile',
    }
    FRONTEND_URL=os.getenv("FRONTEND_URL")