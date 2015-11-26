from flask import Blueprint, render_template, abort

mysql = Blueprint('simple_page', __name__,
                        template_folder='templates')

@simple_page.route('/app/mysql', defaults={'page': 'index'})
def show(page):
    return 'yo'