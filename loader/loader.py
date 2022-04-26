from flask import Blueprint, request, render_template
import logging
from functions import load_posts, uploads_posts

loader_blueprint = Blueprint('loader', __name__, url_prefix='/post', static_folder='static_l', template_folder='templates')


@loader_blueprint.route('/form/')
def form():
    return render_template('post_form.html')


@loader_blueprint.route('/upload/', methods=["POST"])
def upload():
    try:
        file = request.files['picture']
        filename = file.filename
        content = request.values['content']
        posts = load_posts()
        posts.append({
            'pic': f'/uploads/images/{filename}',
            'content': content
        })
        uploads_posts(posts)
        file.save(f'uploads/images/{filename}')
        if filename.split(".")[-1] not in ['png', 'jpeg', 'jpg', 'gif']:
            logging.info("Загружаемый файл не картинка")
    except FileNotFoundError:
        logging.error("Ошибка загрузки файла")
        return "<h1> Файл не найден </h1>"
    else:
        return render_template('post_uploaded.html', pic=f'/uploads/images/{filename}', content=content)

