from fastapi import APIRouter, Query, Response
from fastapi.responses import HTMLResponse

from config import settings

routes_calculation_to_text = APIRouter()


@routes_calculation_to_text.get(
    "/eval",
    response_class=HTMLResponse,
    responses={
        200: {
            "description": "Expression and result of calculation",
            "content": {
                "text/html": {
                    "example": "2+2/2 = 3"
                }
            },
        },
        400: {
            "description": "Arithmetic or syntax error",
            "content": {
                "text/html": {
                    "example": "Error: division by zero"
                }
            },
        },
    }
)
async def calculation_to_text(
        phrase: str = Query(
            title='Expression for calculation',
            description='Example of expression: "2+2/2" or "2*(3+7)/5"',
            example='2+2/2',
            default='0',
            regex=settings.val_regex
        )
):
    try:
        value: int = eval(phrase)
    except (ArithmeticError, SyntaxError) as a_error:
        return Response(content=f'Error: {a_error.args[0]}', media_type="text/html", status_code=400)
    else:
        return Response(content=f'{phrase} = {value}', media_type="text/html")
