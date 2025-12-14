from os import PathLike

from dynaconf import Dynaconf
from pydantic import BaseModel


class Settings(BaseModel):
    SIMILARITY_THRESHOLD: float
    USE_PREPROCESSING: bool
    RESULT_FILE_NAME: PathLike = "duplicates.json"

env_settings = Dynaconf(settings_file=["settings.yml"])


settings = Settings(
    SIMILARITY_THRESHOLD=env_settings["SIMILARITY_THRESHOLD"],
    USE_PREPROCESSING=env_settings["USE_PREPROCESSING"],
    RESULT_FILE_NAME = env_settings["RESULT_FILE_NAME"],
)