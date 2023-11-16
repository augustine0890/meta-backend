import databases
import sqlalchemy

from storeapi.config import settings

metadata = sqlalchemy.MetaData()

post_table = sqlalchemy.Table(
    "posts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("body", sqlalchemy.String),
)

comment_table = sqlalchemy.Table(
    "comments",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("body", sqlalchemy.String),
    sqlalchemy.Column("post_id", sqlalchemy.ForeignKey("posts.id"), nullable=False),
)

engine = sqlalchemy.create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False},
)

metadata.create_all(engine)
database = databases.Database(
    settings.DATABASE_URL, force_rollback=settings.DB_FORCE_ROLL_BACK
)
