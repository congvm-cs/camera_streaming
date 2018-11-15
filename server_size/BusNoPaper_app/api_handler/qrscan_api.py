from flask import Flask, Blueprint
from flask import request, jsonify
import numpy as np

np.random.seed(2018)

qrscan_bp = Blueprint('qrscan_api', __name__)

#==========================================================
#   PROCESS FUNCTION
def __generate():
    ''' Generate a random code for QRCODE
    '''
    code = ""
    return code

def __process_code():
    pass

#==========================================================
#   API
@qrscan_bp.route("/qrscan_api/get_code", methods=["POST"])
def get_code():
    # Receive Code from Embedding Device
    pass


@qrscan_bp.route("/qrscan_api/send_code", methods=["POST"])
def generate_code():
    # Send code to MobileApp
    code = __generate()
    return jsonify(code)

