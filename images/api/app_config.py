from pytz import timezone

TITLE = "Illinois Sunshine"
AUTHOR = "Illinois Campaign for Political Reform"
URL = "http://illinoissunshine.org"
DESCRIPTION = "Keep an eye on money in Illinois politics. Search or browse political committees, donations and expenditures going back to 1994."

TIME_ZONE = timezone('America/Chicago')

DB_USER = 'leverage'
DB_PW = 'leverage'
DB_HOST = 'db'
DB_PORT = '3306'
DB_NAME = 'leverage'

DB_CONN='mysql+mysqldb://{0}:{1}@{2}:{3}/{4}?charset=utf8'\
        .format(DB_USER, DB_PW, DB_HOST, DB_PORT, DB_NAME)

DEFAULT_RACE = 'general'
DEFAULT_YEAR = 2017

SECRET_KEY = 'super secret key'

FTP_HOST = 'ftp.elections.il.gov'
FTP_PATH = 'CampDisclDataFiles'
FTP_USER = ''
FTP_PW = ''

AWS_KEY = ''
AWS_SECRET = ''

# See: https://pythonhosted.org/Flask-Cache/#configuring-flask-cache
# for config options
CACHE_CONFIG = {
    'CACHE_TYPE': 'simple',
}

SENTRY_DSN = ''

FLUSH_KEY = 'super secret junk'

# Change this configuration to have PostgreSQL use a custom list of stop words
# for full text search (see README.md for more details)

STOP_WORD_LIST = 'english'
