from app.models.questions import Questions
from flask import Flask, jsonify, request, Response, json

app = Flask(__name__)

# GET all questions
qtn_obj = Questions()


@app.route('/api/v1/questions')
def get_all_questions():
    questions = qtn_obj.get_all_questions()
    if questions:
        return jsonify({'questions': questions})
