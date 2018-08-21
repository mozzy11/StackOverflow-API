class Users (object):
    users = []
    user={}
    user_id = 0
    user_name = ""
    user_pasword = ""
    user_email = ""

    def add_user(self,user_name, user_pasword, user_email):
        self.user_id += 1
        self.user_name = user_name
        self.user_pasword = user_pasword
        self.user_email = user_email
        user = {"user_id" : self.user_id ,
                "user_name" : self.user_name,
                "user_pasword" : self.user_pasword,
                "user_email" : self.user_email
                 }
        Users.users.append(self.user);