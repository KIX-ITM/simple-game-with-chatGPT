from flask import Blueprint, render_template, url_for, redirect, request, abort
from app.controllers import question

bp = Blueprint('index', __name__, url_prefix='/')


@bp.route('/', methods=["GET", "POST"])
def index():
    response = question.get_new_question()
    question_id = response['id'] if response else None
    opthion_a = response['option_a_ja'] if response else None
    opthion_b = response['option_b_ja'] if response else None
    opthion_c = response['option_c_ja'] if response else None
    common_point = 'unacquired'
    if request.method == 'GET':
        difficulty = 'normal'
    elif request.method == 'POST':
        difficulty = request.form['reload-submit']
    else:
        return abort(400)
    return render_template('index.html',
                           question_id=question_id,
                           option_a=opthion_a,
                           option_b=opthion_b,
                           option_c=opthion_c,
                           common_point=common_point,
                           selected_difficulty=difficulty
                           )


@bp.route('/question/<id>', methods=["POST"])
def get_question(id):
    difficulty = request.form['difficulty']
    return redirect(url_for('index.get_common_point', id=id, difficulty=difficulty))


@bp.route('/question/<id>/<difficulty>')
def get_common_point(id, difficulty):
    response = question.get_question_by_id(id, difficulty)
    question_id = response['id'] if response else None
    opthion_a = response['option_a_ja'] if response else None
    opthion_b = response['option_b_ja'] if response else None
    opthion_c = response['option_c_ja'] if response else None
    common_point_name = difficulty + '_common_point_ja'
    common_point = response[common_point_name] if response else None
    return render_template('index.html',
                           question_id=question_id,
                           option_a=opthion_a,
                           option_b=opthion_b,
                           option_c=opthion_c,
                           common_point=common_point,
                           selected_difficulty=difficulty
                           )






