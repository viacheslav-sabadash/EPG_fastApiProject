## EPG_FastApi_Calc

### Installation

#### Creating Docker container
    docker build --tag epg_fastapi_calc .

#### Run Docker container
    docker run -d -p 8000:8000 epg_fastapi_calc

### Configuration example
Filename: **.env**

    HELLO_TEXT = "Hello world"
    VAL_REGEX = r'^[0-9\s\.\/\*\+\-\(\)]*$'

**Warning**!!! Do not change VAL_REGEX param unless absolutely necessary! This can lead to serious security problems!


### Project Swagger
http://127.0.0.1:8000/docs

http://127.0.0.1:8000/redoc

### Request examples (How to use)

GET http://127.0.0.1:8000/

GET http://127.0.0.1:8000/index

GET http://127.0.0.1:8000/eval?phrase=(1+2)*2

POST http://127.0.0.1:8000/eval
Accept: application/json
Content-Type: application/x-www-form-urlencoded

phrase=3%2B3*2
