import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base
from supabase import create_client

load_dotenv()

__url = os.getenv("SUPABASE_URL")
__key = os.getenv("SUPABASE_SECRET_KEY")
__USER = os.getenv("user")
__PASSWORD = os.getenv("password")
__HOST = os.getenv("host")
__PORT = os.getenv("port")
__DBNAME = os.getenv("dbname")

__missing = [
    name
    for name, value in {
        "SUPABASE_URL": __url,
        "SUPABASE_SECRET_KEY": __key,
        "user": __USER,
        "password": __PASSWORD,
        "host": __HOST,
        "port": __PORT,
        "dbname": __DBNAME,
    }.items()
    if not value
]
if __missing:
    raise RuntimeError(
        "Configure as variáveis no .env. Ausentes: " + ", ".join(__missing)
    )

try:
    __database_url = URL.create(
        "postgresql+psycopg2",
        username=__USER,
        password=__PASSWORD,
        host=__HOST,
        port=int(__PORT),
        database=__DBNAME,
        query={"sslmode": "require"},
    )
except ValueError as error:
    raise RuntimeError("A variável 'port' deve conter uma porta numérica.") from error

supabase = create_client(__url, __key)
Engine = create_engine(__database_url, pool_pre_ping=True)
Base = declarative_base()