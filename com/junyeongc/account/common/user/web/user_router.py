from fastapi import APIRouter
from com.junyeongc.account.common.user.web.user_controller import UserController

router = APIRouter()
controller = UserController()

@router.get(path="/")
async def hello_user():
    return controller.hello_user()

    