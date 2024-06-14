from fastapi import APIRouter

from dependency_injector.wiring import inject, Provide

from src.core.di_container import Container

game_router = APIRouter(
    prefix="/game",
)
