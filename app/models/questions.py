class Questions(object):
    questions = []
    qtn = {}
    qtn_id = 0
    qtn_body = ""
    user_id = 0

    def set_qtn(self, qtn_id,qtn_body,user_id):
        self.qtn_id = qtn_id
        self.qtn_body = qtn_body
        self.user_id = user_id
        self.qtn = {"qtn_id": self.qtn_id, "qtn_body": self.qtn_body, "user_id": self.user_id}
        self.questions.append(self.qtn)


    def add_question(self, qtn_body, user_id):
        if len(Questions.questions) >= 0:
            self.qtn_id = len(Questions.questions) + 1
            self.qtn_body = qtn_body
            self.user_id = user_id

        self.qtn = {"qtn_id": self.qtn_id, "qtn_body": self.qtn_body, "user_id": self.user_id}

        Questions.questions.append(self.qtn)

    def get_all_questions(self):
        return Questions.questions