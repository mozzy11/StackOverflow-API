from app.models.questions import Questions
from flask import Flask, jsonify, request, Response, json

app = Flask(__name__)


qtn_obj = Questions()


qtn_obj = Questions()
#GET A QUESTION

qtns = qtn_obj.get_all_questions()
@app.route('/api/v1/questions/<int:questionId>', methods=['GET'])
def get_qtn(questionId):
        qtn = {}
        for item in qtns:
            if item['qtn_id'] == questionId:
                qtn = {
                    'qtn_id': questionId,
                    'qtn_body': item['qtn_body'],
                    'User_id': item['User_id']
                }
                return jsonify(qtn)
            else:
                bad_object = {
                    "error": "The QTN u requested  doesnt exist",
                    "help_string":
                        " Pleae Request usng an Existing Question id"}

                response = Response(json.dumps(bad_object), status=400, mimetype="appliation/json")
                return response