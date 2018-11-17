from flask import Flask, Blueprint, request
from flask import request, jsonify
from .dbhandler import BusNoPaperDB
import numpy as np
from random import choice
import string

np.random.seed(2018)

user_bp = Blueprint('user_api', __name__)

db_handler = BusNoPaperDB()

#==========================================================
#   PROCESS FUNCTION
def __generate(length=16, chars=string.ascii_letters + string.digits):
    return ''.join([choice(chars) for i in range(length)])


def __process_code():
    pass

#==========================================================
#   API MOBILE
@user_bp.route("/api/signin", methods=["POST"])
def signin():
    try:
        user_data = request.json

        _query_data = db_handler.query_info(user_data['username'])

        if len(_query_data) ==  0:
            # Not exist
            pass
        else:
            # Exist then check password
            pass
    except Exception as e:
        print(e)



@user_bp.route("/api/signup", methods=["POST"])
def signup():
    _code = __generate()

    _response = {
        "code": _code
    }
    return jsonify(_response)


@user_bp.route("/api/get_user_info", methods=["POST"])
def get_user_info():
    pass

