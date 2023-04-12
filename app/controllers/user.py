#
# API 생성 및 데이터 베이스에 생성(Create), 조회(Read), 수정(Update), 삭제(Delete)를 처리 (CRUD)
#
from datetime import datetime

# mongoDB collection
from app.db_connection import (
    patients_collection
)

"""
print("db 내용은?")

for d in accounts_collection.find():
    print(d)

for d in patients_collection.find():
    print(d)
"""

def read_test():
    return {"Hello": "Sujin"}


def find_all_test():
    print("진입")
    try:
        result = patients_collection.find({})
        print("성공")
    except Exception as e:
        print("에러:", e)


def insert_item_test():
    print("진입")
    try:
        result = patients_collection.insert_one({"test": "test!!", "event_time": datetime.now()})
        print("성공")
        # return result
    except Exception as e:
        print("에러:", e)
