from os import PathLike

from dynaconf import Dynaconf
from pydantic import BaseModel

class FileSettings(BaseModel):
    result_file_path: PathLike = "duplicates.json"
    new_items_file_path: PathLike = "new_items.txt"
    catalog_file_path: PathLike = "catalog.txt"


class Settings(BaseModel):
    SIMILARITY_THRESHOLD: float
    USE_PREPROCESSING: bool
    files: FileSettings

env_settings = Dynaconf(settings_file=["settings.yml"])


settings = Settings(
    SIMILARITY_THRESHOLD=env_settings["SIMILARITY_THRESHOLD"],
    USE_PREPROCESSING=env_settings["USE_PREPROCESSING"],
    files=env_settings["result_file_path"],
)
