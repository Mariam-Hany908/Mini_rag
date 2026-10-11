# from pydantic_settings import BaseSettings, SettingsConfigDict

# class Settings(BaseSettings):

#     APP_NAME: str     
#     APP_VERSION: str 
#     OPENAI_API_KEY: str
#     FILE_ALLOWED_TYPES: list[str]
#     FILE_MAX_SIZE_MB: int

#     class config:
#         env_file = ".env"



# def get_settings() :
#     return Settings()

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str
    FILE_ALLOWED_TYPES: list[str]
    FILE_MAX_SIZE_MB: int
    FILE_DEFAULT_CHUNK_SIZE: int

    model_config = SettingsConfigDict(env_file=".env")

def get_settings():
    return Settings()


    