
from com.junyeongc.auth.login_model import LoginModel
from com.junyeongc.auth.login_service import LoginService


class LoginController:
    def __init__(self):
        pass

    def getresult(self, login: LoginModel) -> LoginModel:
        service = LoginService()
        return service.loginservice(login)