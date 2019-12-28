class Config(object):
	DEBUG = False
	TESTING = False
	#DATABASE_URI = 'sqlite://'

class ProductionConfig(Config):
	DATABASE_URI = 'mysql://'

class DevelopmentConfig(Config):
	DEBUG = True
	SECRET_KEY = '123456'

class TestingConfig(Config):
	TESTING = True