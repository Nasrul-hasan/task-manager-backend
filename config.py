# config.py

#DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/task_db'
import os

DATABASE_URI = os.environ.get("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/task_db")


