import os
import sys
from flask import render_template
from . import bp


@bp.route('/')
def kits():
    data={
        'url_name':'kits'
    }
    return render_template('kits.html',data=data)

