import os
class Config:
    SECRET_KEY = '2097b16c8ef76e7ca87118d18db06281'
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "Write here your email id"
    MAIL_PASSWORD = "Write here the password of your email"