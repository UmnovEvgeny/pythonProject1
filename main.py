from flask import Flask

import functions

app = Flask(__name__)


@app.route("/")
def all_candidates():
    candidates = functions.get_all()
    result = '\n'
    for candidate in candidates:
        result += candidate['name'] + '\n'
        result += candidate['position'] + '\n'
        result += candidate['skills'] + '\n'
        result += '\n'
    return f'<pre> {result} </pre>'


@app.route("/candidates/<int:pk>")
def candidates_pk(pk):
    candidate = functions.get_by_pk(pk)
    link = candidate['picture']
    result = '\n'
    result += candidate['name'] + '\n'
    result += candidate['position'] + '\n'
    result += candidate['skills'] + '\n'
    result += '\n'

    return f'<pre> <img src="{link}"> {result} </pre>'


@app.route("/skills/<skill_name>")
def candidates_skills(skill_name):
    candidates = functions.get_by_skill(skill_name)
    result = '\n'
    for candidate in candidates:
        result += candidate['name'] + '\n'
        result += candidate['position'] + '\n'
        result += candidate['skills'] + '\n'
        result += '\n'
    return f'<pre> {result} </pre>'


app.run()

