import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from supabase import create_client

load_dotenv()

__url = os.getenv("SUPABASE_URL")
__key = os.getenv("SUPABASE_KEY")
__USER = os.getenv("user")
__PASSWORD = os.getenv("password")
__HOST = os.getenv("host")
__PORT = os.getenv("port")
__DBNAME = os.getenv("dbname")

__DATABASE_URL = f"postgresql+psycopg2://{__USER}:{__PASSWORD}@{__HOST}:{__PORT}/{__DBNAME}?sslmode=require"


if not __url or not __key:
    raise RuntimeError("Configure SUPABASE_URL e SUPABASE_KEY no .env")

supabase = create_client(__url, __key)

Engine = create_engine(__DATABASE_URL, pool_pre_ping=True)
Base = declarative_base()