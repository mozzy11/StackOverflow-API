class Answers (object):
    answers = []
    ans = {}
    ans_id = 0
    qtn_id = 0
    ans_content =""

    def add_answers(self, qtn_id, ans_content):
        if len(Answers.answers) >= 0:
            self.ans_id = len(Answers.answers) + 1
            self.ans_content = ans_content
            self.qtn_id = qtn_id


        self.ans = {"ans_id ": self.ans_id , "qtn_id": self.qtn_id, " ans_content": self. ans_content}

        Answers.answers.append(self.ans)

    def get_all_answers(self):
        return Answers.answers