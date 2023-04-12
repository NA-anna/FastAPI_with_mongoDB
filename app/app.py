#
# FAST API 웹 서버 app 생성
#
from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI

from app.routes.user import Router as UserRouter

app = FastAPI(
    title="DTx API",
)


def create_app():
    # 라우터 연결
    app.include_router(UserRouter) #, tags=["User"], prefix=api_prefix + "user")

    return app


_app = VersionedFastAPI(create_app(), version_format='{major}', prefix_format='/v{major}')

