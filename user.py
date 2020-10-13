class User:
    """
    Class that generates users new instances .
    """
    user_list = [] #empty user list

    def __init__(self,user_name,password,email):
        self.user_name = user_name
        self.password = password
        self.email = email

    def save_user(self):
        '''
        method that saves user into user_list
        '''

        User.user_list.append(self)