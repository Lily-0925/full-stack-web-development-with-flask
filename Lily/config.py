import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'"[\xe8\x9cZ\xaaL/\xaaw\xcf\xdf\x893\xb0|'

    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment' }
