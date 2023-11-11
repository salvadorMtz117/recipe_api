class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'www.db4free.net'
    MYSQL_USER = 'actividadsmatec'
    MYSQL_PASSWORD = '*He@zzzUf6d7Ebj'
    MYSQL_DB = 'actividadsmatec'
    MYSQL_PORT = 3306

class LocalConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Polyglot#2019'
    MYSQL_DB = 'db_recipe'
    MYSQL_PORT = 3307

class GCPConfig():
    DEBUG = True
    MYSQL_HOST = '34.29.43.72'
    MYSQL_USER = 'recetarioadmin'
    MYSQL_PASSWORD = '=+hsiJ3M:gi/iM$['
    MYSQL_DB = 'db_recipe'
    MYSQL_PORT = 3306

config = {
    'development': DevelopmentConfig,
    'local': LocalConfig,
    'gcp': GCPConfig,
}