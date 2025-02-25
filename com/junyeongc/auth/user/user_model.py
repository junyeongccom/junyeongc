from dataclasses import dataclass

@dataclass
class UserModel:
    email : str
    password : str
    username : str

    @property
    def email(self) -> object:
        return self._email
    @email.setter
    def email(self,email):
        self._email = email
    @property
    def password(self) -> object:
        return self._password
    @password.setter
    def password(self,password):
        self._password = password
    @property
    def username(self) -> object:
        return self._username
    @username.setter
    def username(self,username):
        self._username = username