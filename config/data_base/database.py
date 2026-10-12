import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from supabase import create_client

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
db = os.getenv("DB_URL")

if not url or not key:
    raise RuntimeError("Configure SUPABASE_URL e SUPABASE_KEY no .env")

if not db:
    raise RuntimeError("Configure DB_URL no .env")

supabase = create_client(url, key)

Engine = create_engine(db, pool_pre_ping=True)
Base = declarative_base()
