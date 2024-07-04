import urllib.parse as urlparse
from urllib.parse import urlencode

from aiohttp import ClientSession
from pydantic import BaseModel

from .base_request import BaseRequest, GETRequest, POSTRequest
from .base_response import BaseResponse


class ClientSettings(BaseModel):
    base_url: str
    auth_token: str = ""
    max_req_per_sec: int = 100
    headers: dict = []


class BaseClient:
    def __init__(self, client_settings: ClientSettings):
        self.base_url = client_settings.base_url
        self.auth_token = client_settings.auth_token
        self.max_req_per_sec = client_settings.max_req_per_sec
        self.headers = client_settings.headers

    async def validate_reponse(self, response) -> BaseResponse:
        body = await response.json()

        exceptions = {}
        if response.body.get("exceptions"):
            exceptions = {"exceptions": response.body.get("exceptions")}

        return BaseResponse(
            status_code=response.status,
            body=body,
            headers=response.body,
            exceptions=exceptions,
            content_type=response.content_type,
        )

    async def session(self) -> ClientSession:
        async with ClientSession() as session:
            yield session

    async def get(self, request: GETRequest) -> BaseResponse:
        params = request.params

        try:
            response = await self.validate_reponse(
                await self.session.get(request.url, params=request.params)
            )
            return response
        except Exception as e:
            print(request.url)
            print(e)

    async def post(self, request: POSTRequest) -> BaseResponse:
        pass
