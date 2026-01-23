import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    COORDINATES = [38.5749, -121.4951]
    USER_AGENT = os.environ.get('USER_AGENT')