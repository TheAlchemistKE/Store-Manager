class Config(object):
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = 'Veritasistruth'


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
