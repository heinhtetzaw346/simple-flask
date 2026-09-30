from flask import Blueprint, render_template, url_for, session
import logging
import secrets

logger = logging.getLogger(__name__)
home_bp = Blueprint('home', __name__)

@home_bp.route("/", methods=["GET"])
def home():
    routes = {
        "Session Cookie": url_for('cookies.cookies'),
        "File Input": url_for('input.input'),
        "Picture Ref": url_for('picture.picture'),
        "Server Status": url_for('status.status'),
        "Health": url_for('health.health')
    }

    if not "session_id" in session:
        session["session_id"] = secrets.token_hex(16)
        logger.info(f'cookie {session["session_id"]} set for client')

    return render_template('home.html', routes=routes)
