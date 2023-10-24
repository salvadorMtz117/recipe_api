class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Polyglot#2019'
    MYSQL_DB = 'db_recipe'
    MYSQL_PORT = 3307

config = {
    'development': DevelopmentConfig
}