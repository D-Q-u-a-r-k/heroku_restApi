USER = "postgres"
PASSWORD = "dquark"
IP = "localhost"
PORT = "5432"
DB_NAME = "test"

SQLALCHEMY_DATBASE_URI = f"postgresql+psycopg2://{USER}:{PASSWORD}@{IP}:{PORT}/{DB_NAME}"