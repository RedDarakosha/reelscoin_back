from pydantic import BaseModel


class BaseRequest(BaseModel):
    url: str
    body: dict = {}
    headers: dict = {}
    params: dict = {}


class GETRequest(BaseRequest):
    params: dict = {}


class POSTRequest(BaseRequest):
    body: dict = {}
