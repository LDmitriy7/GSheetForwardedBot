from models.documents import Config


def get() -> Config:
    return Config.object() or Config().save()
