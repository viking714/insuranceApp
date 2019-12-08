class Config(object):
	DEBUG = False
	TESTING = False
	#DATABASE_URI = 'sqlite://'

class ProductionConfig(Config):
	DATABASE_URI = 'mysql://'

class DevelopmentConfig(Config):
	DEBUG = True

class TestingConfig(Config):
	TESTING = True