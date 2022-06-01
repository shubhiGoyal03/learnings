class BaseConfig():
    TESTING = False
    DEBUG = False


class LocalConfig(BaseConfig):
    ENV = 'local'
    DEBUG = True

    # PREVIEW REFERRER
    PREVIEW_HOST = "console.dev-askalden.com"

    # Embedding
    EMBEDDING_HOST = "http://localhost:8000"

    # Elastic search config
    ES_ANSWER_INDEX_CONFIG = 'config/answer_index.json'
    ES_ANSWER_INDEX_PREFIX = 'answer_'
    ES_QUESTION_INDEX_CONFIG = 'config/question_index.json'
    ES_QUESTION_INDEX_PREFIX = 'question_'
    ES_INTENT_INDEX_CONFIG = 'config/intent_index.json'
    ES_INTENT_INDEX_PREFIX = 'intent_'
    ES_ATTRIBUTE_INDEX_CONFIG = 'config/attribute_index.json'
    ES_ATTRIBUTE_INDEX_PREFIX = 'attribute_'
    ES_HOST = "http://0.0.0.0:9200"
    ES_BATCH_SIZE = 200

    # Application backend config
    APP_ENDPOINT = "https://api.dev-askalden.com/v1"
    APP_ENDPOINT_LIMIT = 500

    # Retrospection DB
    RETROSPECT_DB_USER = "retro"
    RETROSPECT_DB_PASSWORD = "r#tr0"
    RETROSPECT_DB_HOST = "0.0.0.0"
    RETROSPECT_DB_PORT = 3306
    RETROSPECT_DB_NAME = "retrospect"

    RETROSPECT_SERVER_HOST = "http://localhost:8004"

    # Session Management
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    REDIS_DB = 0
    REDIS_SESSION_SORT_LIST = 'session_list'
    REDIS_BOT_SESSION_LIST = '{bot_id}_sessions'

    DEFAULT_SESSION_TTL = 1 * 60  # works if above is "inactive" not "infinite"
    DEFAULT_BOT_DATA_TTL = 180

    SESSION_S3_BUCKET_NAME = "core-session"
    SESSION_S3_BUCKET_LOCATION = "us-east-1"

    # Cookie config
    # COOKIE_MAX_AGE = 3600
    COOKIE_SAME_SITE = 'Lax'
    COOKIE_SECURE = False
    MAX_COOKIE_AGE = 7 * 24 * 60 * 60  # 1 week

    # Logs Dir
    LOGS_DIR = "logs"

    # AWS Credentials - will be filled by ENV
    AWS_ACCESS_KEY = ""
    AWS_SECRET_KEY = ""

    # ML
    EMBEDDING_MODEL = "distilbert-base-nli-stsb-mean-tokens"


class DevConfig(BaseConfig):
    ENV = 'development'
    DEBUG = True

    # PREVIEW REFERRER
    PREVIEW_HOST = "console.dev-askalden.com"

    # Embedding
    EMBEDDING_HOST = "http://localhost:8000"

    # Elastic search config
    ES_ANSWER_INDEX_CONFIG = 'config/answer_index.json'
    ES_ANSWER_INDEX_PREFIX = 'answer_'
    ES_QUESTION_INDEX_CONFIG = 'config/question_index.json'
    ES_QUESTION_INDEX_PREFIX = 'question_'
    ES_INTENT_INDEX_CONFIG = 'config/intent_index.json'
    ES_INTENT_INDEX_PREFIX = 'intent_'
    ES_ATTRIBUTE_INDEX_CONFIG = 'config/attribute_index.json'
    ES_ATTRIBUTE_INDEX_PREFIX = 'attribute_'
    ES_HOST = "http://172.31.26.247:9200"
    ES_BATCH_SIZE = 200

    # Application backend config
    APP_ENDPOINT = "https://api.dev-askalden.com/v1"
    APP_ENDPOINT2 = "https://api2.dev-askalden.com/v1"
    APP_ENDPOINT_LIMIT = 500

    RETROSPECT_SERVER_HOST = "http://localhost:8004"

    # Retrospection DB
    RETROSPECT_DB_USER = "admin"
    RETROSPECT_DB_PASSWORD = "1chatb#talden1"
    RETROSPECT_DB_HOST = "database-analytics.cuh9wmzfpe3e.us-east-1.rds.amazonaws.com"
    RETROSPECT_DB_PORT = 3306
    RETROSPECT_DB_NAME = "retrospect"

    # Session Management
    REDIS_HOST = "chatbot-core.r4hfrh.0001.use1.cache.amazonaws.com"  # Keeping this empty
    REDIS_PORT = 6379
    REDIS_DB = 1
    REDIS_SESSION_SORT_LIST = 'session_list'
    REDIS_BOT_SESSION_LIST = '{bot_id}_sessions'

    DEFAULT_SESSION_TTL = 10 * 60  # works if above is "inactive" not "infinite"
    DEFAULT_BOT_DATA_TTL = 1800

    SESSION_S3_BUCKET_NAME = "core-session"
    SESSION_S3_BUCKET_LOCATION = "us-east-1"

    # Cookie config
    COOKIE_SAME_SITE = 'None'  # because request comes from iframe, we can't use LAX
    COOKIE_SECURE = True  # because samesite is None, browsers enforce this to be SECURE
    MAX_COOKIE_AGE = 7 * 24 * 60 * 60  # 1 week

    # Logs Dir
    LOGS_DIR = "logs/serve"

    # AWS Credentials - will be filled by ENV
    AWS_ACCESS_KEY = ""
    AWS_SECRET_KEY = ""

    # ML
    EMBEDDING_MODEL = "distilbert-base-nli-stsb-mean-tokens"


class ProductionConfig(BaseConfig):
    ENV = 'production'
    DEBUG = False

    # PREVIEW REFERRER
    PREVIEW_HOST = "console.askalden.io"

    # Embedding
    EMBEDDING_HOST = "http://localhost:8000"

    # Elastic search config
    ES_ANSWER_INDEX_CONFIG = 'config/answer_index.json'
    ES_ANSWER_INDEX_PREFIX = 'answer_'
    ES_QUESTION_INDEX_CONFIG = 'config/question_index.json'
    ES_QUESTION_INDEX_PREFIX = 'question_'
    ES_INTENT_INDEX_CONFIG = 'config/intent_index.json'
    ES_INTENT_INDEX_PREFIX = 'intent_'
    ES_ATTRIBUTE_INDEX_CONFIG = 'config/attribute_index.json'
    ES_ATTRIBUTE_INDEX_PREFIX = 'attribute_'
    ES_HOST = "http://172.31.19.54:9200"
    ES_BATCH_SIZE = 200

    # Application backend config
    APP_ENDPOINT = "https://api.askalden.io/v1"
    APP_ENDPOINT2 = "https://api2.askalden.io/v1"
    APP_ENDPOINT_LIMIT = 500

    RETROSPECT_SERVER_HOST = "http://localhost:8004"

    # Retrospection DB
    RETROSPECT_DB_USER = "admin"
    RETROSPECT_DB_PASSWORD = "1chatb#talden1Prod"
    RETROSPECT_DB_HOST = "database-analytics.ckdlh8xobqfa.us-east-1.rds.amazonaws.com"
    RETROSPECT_DB_PORT = 3306
    RETROSPECT_DB_NAME = "retrospect"

    # Session Management
    REDIS_HOST = "chatbot-core.vw6fb9.0001.use1.cache.amazonaws.com"  # Keeping this empty
    REDIS_PORT = 6379
    REDIS_DB = 1
    REDIS_SESSION_SORT_LIST = 'session_list'
    REDIS_BOT_SESSION_LIST = '{bot_id}_sessions'

    DEFAULT_SESSION_TTL = 10 * 60  # works if above is "inactive" not "infinite"
    DEFAULT_BOT_DATA_TTL = 1800

    SESSION_S3_BUCKET_NAME = "core-session-prod"
    SESSION_S3_BUCKET_LOCATION = "us-east-1"

    # Cookie config
    COOKIE_SAME_SITE = 'None'  # because request comes from iframe, we can't use LAX
    COOKIE_SECURE = True  # because samesite is None, browsers enforce this to be SECURE
    MAX_COOKIE_AGE = 7 * 24 * 60 * 60  # 1 week

    # Logs Dir
    LOGS_DIR = "logs/serve"

    # AWS Credentials - will be filled by ENV
    AWS_ACCESS_KEY = ""
    AWS_SECRET_KEY = ""

    # ML
    EMBEDDING_MODEL = "distilbert-base-nli-stsb-mean-tokens"


class TestConfig(BaseConfig):
    ENV = 'development'
    TESTING = True
    DEBUG = True
