
from com.junyeongc.auth.login_model import LoginModel

class LoginService:
    def __init__(self):
        pass

    def loginservice(self, login: LoginModel) -> LoginModel: 
        username = login.username
        password = login.password

        if username =='chun' and password == '1234':
            print("😊로그인 성공") 
            result = "index"
        else: 
            print("🤣로그인 실패")
            result = "fail"
            
        login.result = result
        
        return login


        