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

    def delete_user(self):
        '''
        method that deletes user from user list
        '''
        User.user_list.remove(self)

    @classmethod
    def find_by_name(cls, name):
        for user in cls.user_list:
            if user in cls.user_list == name:
                return user


    @classmethod
    def user_exist(cls, name):
        '''
        method that checks if user exists
        '''