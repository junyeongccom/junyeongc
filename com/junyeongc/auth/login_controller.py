
from com.junyeongc.auth.login_model import LoginModel
from com.junyeongc.auth.login_service import LoginService


class LoginController:
    def __init__(self, **kwargs):
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        print("username:", self.username)
        print("password:", self.password)

    def getresult(self) -> LoginModel:
        service = LoginService()
        login = LoginModel()
        login.username = self.username
        login.password = self.password
        return service.loginservice(login)