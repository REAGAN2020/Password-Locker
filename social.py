class Credentials:

    credentials_list = []
    
    def __init__(self,user_name, password, email):
        self.user_name = user_name
        self.password = password
        self.email = email

    def save_credentials(self):
        '''
        method that allows to save credentials into credential list
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
         method to deletes a saved credentials from the credentials_list
        '''

        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_name(cls, name):
        for credentials in cls.credentials_list:
            if credentials.credentials_name == name:
                return credentials

    @classmethod
    def credentials_exist(cls, name):
        '''
        Method that checks if a credentials exists from the credentials list.
        Then returns a boolean depending on whether the credential exists or not
        
        '''
        for credentials in cls.credentials_list:
            if credentials.password == name:
                return credentials

        return False

    @classmethod
    def display_credentials(cls): 
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list
