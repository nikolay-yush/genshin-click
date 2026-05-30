from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    GENSHIN_DAILY_TASK_URL: str
    ICON_CHECK_SELECTOR: str
    CHROME_EXECUTABLE_PATH: str
    FIRST_RUN: bool

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
