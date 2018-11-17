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
        # if "id" in _query:
        db_handler.update_qrcode(_query['id'], _code)

        _response = {
            "status": "true",
            "status_message": "",
            "content":{
                "id": _query['id'],
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

# @qrscan_bp.route("/qrscan_api/get_code", methods=["POST"])
# def get_code():
#     return jsonify({
#         "hi": "Cong"
#     })

#==========================================================
#   API EMBEDDED DEVICE