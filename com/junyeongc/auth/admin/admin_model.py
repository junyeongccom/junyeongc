from dataclasses import dataclass

@dataclass
class AdminModel:
    email : str
    password : str
    adminname : str

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
    def adminname(self) -> object:
        return self._adminname
    @adminname.setter
    def adminname(self,adminname):
        self._adminname = adminname