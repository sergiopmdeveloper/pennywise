import os

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///db.sqlite")
CONNECT_ARGS = {"check_same_thread": False}
