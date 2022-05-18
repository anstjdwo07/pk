from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'h\xcb\xdf\xaa\x11\xcb\xca\xa6\x9f*\xa9\xbd\x93\x14\xc5\x8a'