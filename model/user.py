import enums.user_role as UserRole

class User:
    def __init__(self,id, email, password, token, role: UserRole):
        self.id = id
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