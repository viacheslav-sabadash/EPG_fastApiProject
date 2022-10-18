from fastapi import APIRouter, Form

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
    return {
        'data': {
            'phrase': phrase, 'value': eval(phrase)
        }
    }
