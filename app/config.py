class BaseConfig:
    DEBUG = False
    TESTING = False
    PROJECT_ID = "mt"
    # FIRESTORE
    TEMPLATES_COLLECTION = "templates"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    ENV = "dev"


class TestConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    ENV = "test"


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    ENV = "prod"
