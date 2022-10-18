from fastapi import FastAPI

from routes import calculation_get
from routes import calculation_post
from routes import root

app = FastAPI()

app.include_router(root.routes_root)
app.include_router(calculation_get.routes_calculation_to_text)
app.include_router(calculation_post.routes_calculation_to_json)
