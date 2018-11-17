from flask import Flask, Blueprint, request, jsonify
from ..api_handler.dbhandler import BusNoPaperDB

charge_bp = Blueprint('charge_api', __name__)
db_handler = BusNoPaperDB()


NORMAL_TICKET_FEE = 6000
STUDEN_TICKET_FEE = 2000

MOBILEPHONE_CODE = "makerthon2018"
MONEY_RECHARGE = 50000


@charge_bp.route("/api/recharge", methods=["POST"])
def recharge():
    try:
        _request_data = request.json

        _username = _request_data['username']
        
        _query_data = db_handler.query_info(_username)
        
        # Validate Code
        if _request_data['code'] != MOBILEPHONE_CODE:
            _response = {
                "status": "false",
                "status_message": "wrong code",
                "content": {
                }
            }
            return jsonify(_response)
        else:
            _new_money = MONEY_RECHARGE + int(_query_data[0][5])
            db_handler.update_money(_username, _new_money)
            _response = {
                "status": "true",
                "status_message": "Charged",
                "content": {
                    "money": _new_money
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


@charge_bp.route("/api/charge", methods=["POST"])
def charge():
    try:
        _request_data = request.json

        _code = _request_data['code']

        _query_data = db_handler.query_code(_code)

        # Check usertype
        if len(_query_data) == 0:
            _response = {
                "status": "false",
                "status_message": "Invalid QRCode",
                "content": {
                }
            }
            return jsonify(_response)

        # Validate money
        if ((_query_data[0][4] == 0) & (_query_data[0][5] < NORMAL_TICKET_FEE)) | ((_query_data[0][4] == 1) & (_query_data[0][5] < STUDEN_TICKET_FEE)):
            _response = {
                "status": "false",
                "status_message": "Not enough money",
                "content": {
                }
            }

            return jsonify(_response)
        else:
            _new_money = int(_query_data[0][5]) - NORMAL_TICKET_FEE if (int(_query_data[0][4]) == 0) else int(
                _query_data[0][5]) - STUDEN_TICKET_FEE

            # Update money in DB
            db_handler.update_money(_query_data[0][1], _new_money)
            _response = {
                "status": "true",
                "status_message": "Charged",
                "content": {
                    "money": _new_money
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
