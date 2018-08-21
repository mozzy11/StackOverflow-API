from app.models.questions import Questions
from app.models.answers import  Answers
from flask import Flask, jsonify, request, Response, json


app = Flask(__name__)

qtn_obj = Questions()
ans_obj = Answers()
    # POST An answer
qtns = qtn_obj.get_all_questions()
ansz = ans_obj.get_all_answers()
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


