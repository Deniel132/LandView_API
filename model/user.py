from enums.user_role import UserRole

class User:
    def __init__(self,user_id, email, password, token, role: UserRole):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.token = token
        self.role = role

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password

    def getToken(self):
        return self.token

    def getRole(self):
        return self.role