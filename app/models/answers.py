class Answers (object):
    anwers = []
    ans = {}
    ans_id = 0
    qtn_id = 0
    ans_content =""

    def add_question(self, qtn_id, ans_content):
        if len(Answers.answers) > 0:
            self.ans_id = Answers.answers[-1].get('ans_id') + 1
            self.ans_content = ans_content
            self.qtn_id = qtn_id
        else:
            ans = 1
            self.ans_content = ans_content
            self.qtn_id  = qtn_id

        self.qtn = {"ans_id ": self.ans_id , "qtn_id": self.qtn_id, " ans_content": self. ans_content}

        Answers.answers(self.ans)

    def get_all_answers(self):
        return Answers.answers
