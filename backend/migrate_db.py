from sqlmodel import create_engine, SQLModel
from models import User  # noqa: F401

# データベース接続情報
DB_URL = "mysql+pymysql://root@mysql/dev"

# エンジンの作成
engine = create_engine(DB_URL, echo=True)

def reset_database():
    SQLModel.metadata.drop_all(bind=engine)
    SQLModel.metadata.create_all(bind=engine)

if __name__ == "__main__":
    reset_database()
