from src.config.dev_config import DevConfig
from src.config.production_config import ProductionConfig


class Config:
    def __init__(self) -> None:
        self.dev = DevConfig()
        self.production = ProductionConfig()
