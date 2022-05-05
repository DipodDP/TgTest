from dataclasses import dataclass

from environs import Env


@dataclass
class Config:
    api_id: int
    api_hash: str
    channel_id: int
    proxy: str


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        api_id=env.int("API_ID"),
        api_hash=env.str("API_HASH"),
        channel_id=env.int('CHANNEL_ID'),
        proxy=env.list('PROXY_URL')
    )


