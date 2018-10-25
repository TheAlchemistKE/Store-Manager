class Config(object):
    DEBUG = False
    TESTING = False
    


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    DATABASE_NAME = "storemanager-tests"


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
