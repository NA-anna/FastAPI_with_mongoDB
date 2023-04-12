#
# URL과 API의 전체적인 동작을 관리
#
from fastapi import APIRouter

from app.controllers.user import (
    read_test,
    find_all_test,
    insert_item_test
)

Router = APIRouter()


@Router.get("/")
def get_root():
    return read_test()


@Router.get("/test")
def get_all_test():
    return find_all_test()


@Router.post("/insert")
def put_test():
    return insert_item_test()


