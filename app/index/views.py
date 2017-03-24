import os
import sys
from flask import render_template
from . import bp


@bp.route('/')
def index():
    system_info = [{
        'name':'操作系统',
        'val':sys.platform,
        'note':''
    },{
        'name':'系统编码',
        'val':sys.getfilesystemencoding(),
          'note':''
    }]

    data={
        'url_name':'index',
        'system_info':system_info
    }
    print(system_info)
    return render_template('index.html',data=data)

