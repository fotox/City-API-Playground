import os

SQLALCHEMY_DATABASE_URI = (f"postgresql://{os.getenv('PGUSER')}:{os.getenv('PGPASSWORD')}@"
                           f"{os.getenv('PGHOST')}:{os.getenv('PGPORT')}/dev_{os.getenv('PGDATABASE')}")
SQLALCHEMY_TRACK_MODIFICATIONS = False
