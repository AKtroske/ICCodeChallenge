import re
from flask import Flask, jsonify, request, render_template, Blueprint


from .payloadForm import PayloadForm

bp = Blueprint('api', __name__, url_prefix='/')
"""
    Stored procedures with prepared statements/parameterized queries
    are MUCH more effective in preventing SQL injection attacks. However,
    a regex like one being used below could be used to potentially detect/flag
    users who are consistently using common SQL statements.
"""

# Function will test a form input or any inpt
@bp.route('/v1/sanitized/input', methods=['POST', 'GET'])
def sanitize(input=None):

    form = PayloadForm()
    result = None

    if request.method == 'POST':

        # Through form
        if not input:
            input = form.payload.data
        else: # Through API request
            input = request.json
            input = input["payload"]

        # Pattern matches common SQL phrases, any inline or block comment in sql
        pattern = '/[\t\r\n]|(--[^\r\n]*)|(\/\*[\w\W]*?(?=\*)\*\/)|SELECT|UPDATE|DELETE|INSERT/'
        matches = re.findall(pattern, input)

        if len(matches) == 0:
            result = 'sanitized'
        else:
            result = 'unsanitized' # Store len(matches) for more 'accurate' sanitizations


        if request.json:
            return jsonify({"result":result})

    return render_template('sanitize.html', form=form, result=result)
