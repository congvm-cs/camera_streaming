from flask import Flask, Blueprint


charge_bp = Blueprint('charge_api', __name__)

@charge_bp.route("/charge", methods=["POST"])
def charge():
    pass

