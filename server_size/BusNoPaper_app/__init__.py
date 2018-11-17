from flask import Flask, Blueprint, request
from flask import request, jsonify

from .api_handler.qrscan_api import qrscan_bp
from .api_handler.charge_api import charge_bp
from .api_handler.user_api import user_bp

from .api_handler.dbhandler import BusNoPaperDB



app = Flask(__name__)

app.register_blueprint(qrscan_bp)
app.register_blueprint(charge_bp)
app.register_blueprint(user_bp)


