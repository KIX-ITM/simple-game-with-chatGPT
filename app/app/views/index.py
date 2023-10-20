from flask import Blueprint, render_template, url_for, redirect, request, abort
from app.controllers import question

bp = Blueprint('index', __name__, url_prefix='/')


@bp.route('/', methods=["GET", "POST"])
def get_index():
    response = question.get_new_question()
    if not response:
        # fastapiからエラーが返ってきた場合は404
        abort(404)
    obj = question.format_response(response)
    common_point = 'unacquired'
    if request.method == 'GET':
        difficulty = 'normal'
    elif request.method == 'POST':
        difficulty = request.form['reload-submit']
        if not difficulty:
            # パラメーターが空の場合は404
            abort(400)
    else:
        return abort(400)
    return render_template('index.html',
                           question_id=obj['question_id'],
                           option_a=obj['option_a'],
                           option_b=obj['option_b'],
                           option_c=obj['option_c'],
                           common_point=common_point,
                           selected_difficulty=difficulty,
                           correct_word_1=obj['correct_words'][0],
                           correct_word_2=obj['correct_words'][1],
                           incorrect_word=obj['incorrect_word']
                           )


@bp.route('/question/<id>', methods=["POST"])
def get_question(id):
    difficulty = request.form['difficulty']
    if not id or not difficulty:
        # パラメーターが空の場合は404
        abort(400)
    return redirect(url_for('index.get_common_point', id=id, difficulty=difficulty))


@bp.route('/question/<id>/<difficulty>')
def get_common_point(id, difficulty):
    response = question.get_question_by_id(id, difficulty)
    # if not response:
    #     # fastapiからエラーが返ってきた場合は404
    #     abort(404)
    obj = question.format_response(response)
    common_point_name = difficulty + '_common_point_ja'
    common_point = response[common_point_name] if response else None
    return render_template('index.html',
                           question_id=obj['question_id'],
                           option_a=obj['option_a'],
                           option_b=obj['option_b'],
                           option_c=obj['option_c'],
                           common_point=common_point,
                           selected_difficulty=difficulty,
                           correct_word_1=obj['correct_words'][0],
                           correct_word_2=obj['correct_words'][1],
                           incorrect_word=obj['incorrect_word']
                           )






