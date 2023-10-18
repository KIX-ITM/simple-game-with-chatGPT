from flask import Blueprint, render_template, url_for, redirect, request, abort
from app.controllers import question

bp = Blueprint('info', __name__, url_prefix='/info')


@bp.route('/', methods=["POST"])
def get_info():
    difficulty = request.form['selected_difficulty']
    id = request.form['question_id']
    if not difficulty or not id:
        # パラメーターが空の場合は404
        abort(400)
    return render_template('info.html',
                           question_id=id,
                           selected_difficulty=difficulty
                           )

