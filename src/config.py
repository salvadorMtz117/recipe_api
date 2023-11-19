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

class S3Bucket():
    BUCKET_URL = 'https://recipe-images-project.s3.us-east-2.amazonaws.com/'

class apiKey():
    API_KEY = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiMzQ3YTc3YTM4YjA1ZWNhYjhhZmFiYTUyZWI2YTdmNzU3YTFkNTAyZjdkNGFhZjJlZjI5OTkzMTA5NWQyODRhZTk0OTg0OWE5MjAxMzA1NWYiLCJpYXQiOjE3MDAzNzQwOTYuNzI1MTk5LCJuYmYiOjE3MDAzNzQwOTYuNzI1MjA0LCJleHAiOjQ4NTYwNDc2OTYuNzE5NjE3LCJzdWIiOiI3MTkyNDAiLCJzY29wZXMiOltdfQ.DdiYdJTBkOBineldqmTulCU1XLNSB_SzPgoTYLkjQmKgc7-s0WYWGBKqDhG49OCBu1Y9XytT9nucgOXcGSGxIdI70Qj-Ie8Qa_VBhr75bHJt6LpzbZ3XP9aQkjnLyGXy-Vj_ndf4H6e2k1a8LdIzXXYGHjj5zrIWJHOdvQjh9784RXkv183FgVhc_vyY2T4bpLxEi45QSvaK1SKeyYXWytNNmzPRwS3s2I-t16JEogyOYgjhMnCp4V_hNnFEWP-CiaSJpso6NmUy7rmFx_VX2Rqmgw30jCe_Jk1gX805b2BG1qEoht7plLhrRT3K7PQGeU7niH9_QA1ZfJtZ_euaPCOKzxs4E1SfbT1ooMR950jsE9sErrnPKZnKKUSBRU8Bbv2NB7Cgzeqh2ocZfV6SRymNxFeF9MP8v9G21psnk7H7zvifR04_ng8Oq252eT0Bb2rvju87u0tDE-NwtM6uz9zm4DlK-KCfWbObkeAaNiGu15t5G-3VGzfbOl-K8voaEG4a-4Mk3L5e5saU1t9PFPfeix0OxR7phlB7kzBpr9gswU3rA7kUrbDZzM8NYXFWR26NxbxiB7S9XQZI1sbqEr65sBpPk7PRdP0P4u3yPZVQuM84LIB1Nel5Sh2GfmfywsfwSYItLLwpbWKQG0P3AUH8lKvbwjC3ZaJ0kXq0Htg'
    GROUP_ID = '105250393711183196'

config = {
    'development': DevelopmentConfig,
    'local': LocalConfig,
    'gcp': GCPConfig,
}