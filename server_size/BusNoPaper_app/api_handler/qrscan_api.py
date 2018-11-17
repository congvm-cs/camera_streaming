from flask import Flask, Blueprint, request
from flask import request, jsonify
import numpy as np
from random import choice
import string
from .dbhandler import BusNoPaperDB
from random import choice
import string

np.random.seed(2018)

qrscan_bp = Blueprint('qrscan_api', __name__)

db_handler = BusNoPaperDB()

#==========================================================
#   PROCESS FUNCTION
def __generate(length=16, chars=string.ascii_letters + string.digits):
    return ''.join([choice(chars) for i in range(length)])


def __process_code():
    pass

#==========================================================
#   API MOBILE
@qrscan_bp.route("/api/get_code", methods=["POST"])
def generate_qrcode():
    _query = request.json

    _code = __generate()
    try:
        # Update database
        db_handler.update_qrcode(_query['username'], _code)

        _response = {
            "status": "true",
            "status_message": "",
            "content":{
                "username": _query['username'],
                "code": _code
            }
        }

        return jsonify(_response)
    except Exception as e:    
        _response = {
            "status": "false",
            "status_message": str(e),
            "content":{
            }
        }
        return jsonify(_response)



#==========================================================
#   API EMBEDDED DEVICE

@qrscan_bp.route("/api/validate_code", methods=["POST"])
def validate_code():
    _query = request.json

    try:
        # Update database
        _code = _query['code']
        db_handler.update_qrcode(_query['username'], _code)

        _response = {
            "status": "true",
            "status_message": "",
            "content":{
                "username": _query['username'],
                "code": _code
            }
        }

        return jsonify(_response)
    except Exception as e:    
        _response = {
            "status": "false",
            "status_message": str(e),
            "content":{
            }
        }
        return jsonify(_response)