from app.models.questions import Questions
from app.models.answers import  Answers
from flask import Flask, jsonify, request, Response, json


app = Flask(__name__)

qtn_obj = Questions()
ans_obj = Answers()
qtns = qtn_obj.get_all_questions()
ansz = ans_obj.get_all_answers()


# POST a queston

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



# GET all questions

@app.route('/api/v1/questions', methods=['GET'])
def get_all_questions():
    questions = qtn_obj.get_all_questions()
    if questions:
        return jsonify({'questions': questions})





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


  #ADD Answers
@app.route('/api/v1/questions/<int:questionId>/answers', methods=['POST'])
def add_ans(questionId):


        request_ans = request.json
        if (valid_ans(request_ans)):
            if any(d['qtn_id'] == questionId for d in qtns):
                ans = {
                    'ans_id': request_ans['ans_id'],
                    'ans_content': request_ans['ans_content'],
                    'qtn_id': questionId
                }

                #ansz.append(ans)
                ans_obj.add_answers(questionId, request_ans['ans_content'] )
                print(ansz)
                return jsonify(ans)

            else:
                bad_object = {
                    "error": "The Question You Posted to doesnt exist",
                    "help_string":
                        " Pleae Post to an existing Question id"}

                response = Response(json.dumps(bad_object), status=400, mimetype="appliation/json")
                return response

        else:
            bad_object = {
                "error": "Invalid Answer",
                "help_string":
                    "Request format should be {'ans_id': 1,'ans_content': ' Andela is good','qtn_id': 101 }"

            }
            response = Response(json.dumps(bad_object), status=400, mimetype="appliation/json")
            return response

def valid_ans(ansObj):
        if "ans_id" in ansObj and "ans_content" in ansObj and "qtn_id" in ansObj:
            return True
        else:
            return False
