from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from .register import api_router
import sys

from app.core.db.default_data.import_bulk_default_data import import_bulk_default_data

# lib
import shutil
import time
import os


# sqlalchemy
from sqlalchemy import engine_from_config
from sqlalchemy import pool

# alembic
from alembic.migration import MigrationContext
from alembic.config import Config
from alembic import command

# Set up the Alembic configuration object
alembic_cfg = Config(file_="alembic.ini")
alembic_cfg.set_main_option('script_location', 'app/alembic')
alembic_cfg.set_main_option('url', f'postgresql://Camilapinz18:swh6GdoLqz8W@ep-white-leaf-37502486.us-east-2.aws.neon.tech/neondb')



app = FastAPI(
    title='SABSEG-FastAPI',
    openapi_url=f"{'/api/v1'}/openapi.json"
)

def generate_upgrade_head():
    print("upgrading")
    command.upgrade(alembic_cfg, revision="head")
    

@app.on_event("startup")
async def startup_event():

    #print(sys.path)
    generate_upgrade_head()
    #import_bulk_default_data()
    print("started")

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
