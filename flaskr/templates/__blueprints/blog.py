#!/usr/bin/env python3

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    url_for
)
from werkzeug.exceptions import abort
from flaskr.db import get_db
from flaskr.templates.__blueprints.auth import login_required

bp = Blueprint('blog', __name__)

@bp.get('/')
def index():
    return render_template('blog/index.html')