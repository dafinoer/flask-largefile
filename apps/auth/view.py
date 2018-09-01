from flask import Blueprint, render_template


mod_auth = Blueprint('auth', __name__, url_prefix='/auth')


@mod_auth.route('/signin/', methods=['GET', 'POST'])
def hello_world():

    context = {
        'title': 'hallo world'
    }
    return render_template('auth/register.html', context=context)