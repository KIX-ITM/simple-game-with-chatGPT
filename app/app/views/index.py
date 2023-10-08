from flask import Blueprint, render_template

bp = Blueprint('index', __name__, url_prefix='/')


@bp.route('/')
def index():

    return render_template('index.html')

# from flask import abort, redirect, url_for
#
# @app.route('/')
# def index():
# init作業
# 3つの単語をランダムで抽出（正解と回答も）
#     return render_template('hello.html', name=name)
#
# @app.route('/<name>/<nanido>')
# def hello(name=None):
# 難易度取得
# ChatGPTに質問　→　日本語回答がリターン
#     return redirect(url_for('nannido'))
#
# @app.route('/nannido/')
# @app.route('/nannido/<name>')
# def hello(name=None):
#     return redirect(url_for('nannido'))
#     return render_template('hello.html', name=name)
