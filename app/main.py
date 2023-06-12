from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from .register import api_router



app = FastAPI(
    title='SABSEG-FastAPI',
    openapi_url=f"{'/api/v1'}/openapi.json"
)


# @app.on_event("startup")
# async def startup_event():
#     import_bulk_default_data()
#     print('Running default data version scripts')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix='/api/v1')


# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Msg(BaseModel):
#     msg: str


# @app.get("/")
# async def root():
#     return {"message": "Hello World. Welcome to FastAPI!"}


# @app.get("/path")
# async def demo_get():
#     return {"message": "This is /path endpoint, use a post request to transform the text to uppercase"}


# @app.post("/path")
# async def demo_post(inp: Msg):
#     return {"message": inp.msg.upper()}


# @app.get("/path/{path_id}")
# async def demo_get_path_id(path_id: int):
#     return {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}
