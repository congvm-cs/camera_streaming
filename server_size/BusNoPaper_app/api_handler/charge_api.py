from flask import Flask, Blueprint


charge_bp = Blueprint('charge_api', __name__)

@charge_bp.route("/api/recharge", methods=["POST"])
def recharge():
    pass

    
@charge_bp.route("/api/charge", methods=["POST"])
def charge():
    pass

