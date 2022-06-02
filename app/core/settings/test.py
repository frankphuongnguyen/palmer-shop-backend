import logging

from pydantic import PostgresDsn, SecretStr

from app.core.settings.app import AppSettings


class TestAppSettings(AppSettings):
    debug: bool = True

    title: str = "Test Palmer books store app"

    secret_key : SecretStr = SecretStr("test_secret")

    database_url: PostgresDsn
    max_connection_count = 5
    min_connection_count = 5

    logging_level = logging.DEBUG
