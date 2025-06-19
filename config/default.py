import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-very-secret-key-please-change-this'
    DATABASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../instance/site.db')