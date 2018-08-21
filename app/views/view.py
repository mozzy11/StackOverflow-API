from app.models.questions import Questions
from app.models.answers import  Answers
from flask import Flask, jsonify, request, Response, json


app = Flask(__name__)

qtn_obj = Questions()

    # POST An a queston
qtns = qtn_obj.get_all_questions()


@app.route('/api/v1/questions', methods=['POST'])
def add_qtn():

        request_qtn = request.json
        if (valid_qtn(request_qtn)):
            qtn = {
                'qtn_id': request_qtn['qtn_id'],
                'qtn_body': request_qtn['qtn_body'],
                'User_id': request_qtn['User_id']
            }
            qtn_obj.add_question(request_qtn['qtn_body'],request_qtn['User_id'])
            print(qtns)
            return jsonify(qtns)

        else:
            bad_object = {
                "error": "Invalid Qtn",
                "help_string":
                    "Request format should be {'qtn_id': 1,'qtn_body': 'Where is Andela','User_id': 3 }"

            }
            response = Response(json.dumps(bad_object), status=400, mimetype="appliation/json")
            return response

def valid_qtn(qtnObj):
        if "qtn_id" in qtnObj and "qtn_body" in qtnObj and "User_id" in qtnObj:
            return True
        else:
            return False
