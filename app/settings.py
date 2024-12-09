from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    postgres_user: str = Field('test_user', env='POSTGRES_USER')
    postgres_password: str = Field('test_password', env='POSTGRES_PASSWORD')
    postgres_db: str = Field('test_db', env='POSTGRES_DB')
    postgres_host: str = Field('db', env='POSTGRES_HOST')
    postgres_port: str = Field('5432', env='POSTGRES_PORT')

    @property
    def db_url(self) -> str:
        return (
            f"postgresql://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
