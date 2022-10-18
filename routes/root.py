from fastapi import APIRouter, Response
from fastapi.responses import HTMLResponse

from config import settings

routes_root = APIRouter()


@routes_root.get("/", response_class=HTMLResponse)
@routes_root.get("/index", response_class=HTMLResponse)
async def root():
    return Response(content=settings.hello_text, media_type="text/plain")
