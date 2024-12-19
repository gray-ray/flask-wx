

class Config: 
  DEBUG = False

  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root123456@localhost/flask-wx'

  SQLALCHEMY_TRACK_MODIFICATIONS = False

  WX_APPID = ''

  WX_APP_SECRET = ''

  JWT_SECRET_KEY = '1122'

class DevelopmentConfig(Config):
  DEBUG = True


class ProductionConfig(Config):
  DEBUG = False