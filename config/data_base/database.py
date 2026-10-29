import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from supabase import create_client

load_dotenv()

__url = os.getenv("SUPABASE_URL")
__key = os.getenv("SUPABASE_SECRET_KEY")
__USER = os.getenv("USER")
__PASSWORD = os.getenv("PASSWORD")
__HOST = os.getenv("HOST")
__PORT = os.getenv("PORT")
__DBNAME = os.getenv("DBNAME")

__DATABASE_URL = f"postgresql+psycopg2://{__USER}:{__PASSWORD}@{__HOST}:{__PORT}/{__DBNAME}?sslmode=require"


if not __url or not __key:
    raise RuntimeError("Configure SUPABASE_URL e SUPABASE_SECRET_KEY no .env")

supabase = create_client(__url, __key)

Engine = create_engine(__DATABASE_URL, pool_pre_ping=True)
Base = declarative_base()