from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = "dac284beb4dc92d774a9585dfa585b153bed68f7"
app.config["MONGO_URI"] = (
    "mongodb+srv://python_user:Lpz26ghewaAnkU6W@cluster0.tqaeshh.mongodb.net/flask_db"
)

# setup mongodb
mongodb_client = PyMongo(app)
db = mongodb_client.db

# Check database connection
try:
    db.command("ping")  # This command checks the connection
    print("Database connection successful.")
except Exception as e:
    print("Database connection failed:", e)

from application import routes
