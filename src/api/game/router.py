from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter

from src.core.di_container import Container

game_router = APIRouter(
    prefix="/game",
)
