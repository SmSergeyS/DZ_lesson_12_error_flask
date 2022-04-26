from flask import Blueprint, request, render_template
import logging
from functions import load_posts


main_blueprint = Blueprint('main', __name__, static_folder='static_m', template_folder='templates')
logging.basicConfig(encoding='UTF-8', level=logging.INFO)


@main_blueprint.route('/')
def main():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search():
    search_by = request.args['s']
    logging.info(f'Слово для поиска: {search_by}')
    posts = [x for x in load_posts() if search_by.lower() in x['content'].lower()]
    return render_template('post_list.html', search_by=search_by, posts=posts)
