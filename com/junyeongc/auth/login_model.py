from dataclasses import dataclass

@dataclass
class LoginModel:

    username: str
    password: str
    result: str


    @property
    def username(self) -> object:
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self) -> object:
        return self._password

    @password.setter
    def password(self, password):
        self._password = password
    
    @property
    def result(self) -> object:
        return self._result

    @result.setter
    def result(self, result):
        self._result = result
