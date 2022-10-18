from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse

from config import settings

routes_calculation_to_json = APIRouter()


@routes_calculation_to_json.post(
    "/eval",
    status_code=201,
    responses={
        201: {
            "description": "Expression and result of calculation",
            "content": {
                "application/json": {
                    "example": {
                        "data": {"phrase": "2+2/2", "value": "3"}
                    }
                }
            },
        },
        400: {
            "description": "Arithmetic or syntax error",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Error: division by zero"
                    }
                }
            },
        },
    }
)
async def calculation_to_json(
        phrase: str | None = Form(
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
        return JSONResponse(
            content={"detail": f'Error: {a_error.args[0]}'},
            status_code=400
        )
    else:
        return {
            'data': {
                'phrase': phrase, 'value': eval(phrase)
            }
        }
