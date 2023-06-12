from pydantic import AnyHttpUrl, BaseSettings, HttpUrl


class Data(BaseSettings):
    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://Camilapinz18:gR6oQeOBftJ9@ep-muddy-snowflake-466588.us-east-2.aws.neon.tech/neondb'
    )

