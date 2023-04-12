#
# PUT 요청에 있는 본문(Body)을 받기 위한 모델 만들기
#
from pydantic import BaseModel


class UserSchema(BaseModel):
    name: str
    id: str
    phone: str
