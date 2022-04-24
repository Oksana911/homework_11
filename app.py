import utils

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    candidates = utils.load_candidates_from_json("candidates.json")
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:id>')  # страница кандидата
def candidate_page(id):
    candidate = utils.get_candidate(id)
    return render_template('single.html', candidate=candidate)


@app.route('/search/<candidate_name>')  # страница поиска по имени кандидата
def search_by_name(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates, len_candidates=len(candidates))


@app.route('/skill/<skill_name>')  # страница поиска кандидата по скилам
def search_by_skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template('skill.html', candidates=candidates, len_candidates=len(candidates), skill_name=skill_name)


app.run()
