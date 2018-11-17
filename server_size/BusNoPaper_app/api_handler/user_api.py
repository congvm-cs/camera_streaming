from flask import Flask, Blueprint, request
from flask import request, jsonify
from .dbhandler import BusNoPaperDB
import numpy as np
from random import choice
import string

np.random.seed(2018)

user_bp = Blueprint('user_api', __name__)

db_handler = BusNoPaperDB()

# ==========================================================
#   PROCESS FUNCTION


def __generate(length=16, chars=string.ascii_letters + string.digits):
    return ''.join([choice(chars) for i in range(length)])


# ==========================================================
#   API MOBILE
@user_bp.route("/api/signin", methods=["POST"])
def signin():
    try:
        print('signin')
        user_data = request.json

        # print(user_data['username'])

        _query_data = db_handler.query_info(user_data['username'])

        # print(len(_query_data))

        if len(_query_data) == 0:
            # Not exist
            _response = {
                "status": "false",
                "status_message": "not exist",
                "content": {
                }
            }
        else:
            # Exist then check password
            if user_data['password'] == _query_data[0][2]:
                _response = {
                    "status": "true",
                    "status_message": "",
                    "content": {
                        "qrcode": _query_data[0][3],
                        "usertype": _query_data[0][4],
                        "money": _query_data[0][5],
                        "email": _query_data[0][6]
                    }
                }
            else:
                _response = {
                    "status": "false",
                    "status_message": "wrong password",
                    "content": {
                    }
                }
        return jsonify(_response)
    except Exception as e:
        _response = {
            "status": "false",
            "status_message": str(e),
            "content": {
            }
        }
        return jsonify(_response)


@user_bp.route("/api/signup", methods=["POST"])
def signup():
    try:
        _query_data = request.json
        # Generate QRCODE
        _code = __generate()
        db_handler.insert(username=_query_data['username'],
                          password=_query_data['password'],
                          qrcode=_code,
                          usertype=0,
                          money=0,
                          email=_query_data['email'])

        _response = {
            "status": "true",
            "status_message": "register successfully",
            "content": {
            }
        }
        return jsonify(_response)

    except Exception as e:
        _response = {
            "status": "false",
            "status_message": str(e),
            "content": {
            }
        }
        return jsonify(_response)


@user_bp.route("/api/update_usertype", methods=["POST"])
def update_usertype():
    try:
        _query_data = request.json
        print(_query_data)
        db_handler.update_usertype(username=_query_data['username'],
                          usertype=_query_data['usertype'],
                          email=_query_data['email'])
        _response = {
            "status": "true",
            "status_message": "update successfully",
            "content": {
            }
        }
        return jsonify(_response)

    except Exception as e:
        _response = {
            "status": "false",
            "status_message": str(e),
            "content": {
            }
        }
        return jsonify(_response)
