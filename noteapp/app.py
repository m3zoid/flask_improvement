from flask import Flask
from noteapp.views.index import bp as index_bp
from noteapp.views.createnote import bp as createnote_bp


app = Flask(__name__)

app.register_blueprint(index_bp)
app.register_blueprint(createnote_bp)