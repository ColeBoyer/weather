import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config:
    COORDINATES = [38.5749, -121.4951]
    SECRET_KEY = (
        os.environ.get("SECRET_KEY")
        or "some_really_arbitrary_and_long_string_goes_here"
    )
    USER_AGENT = os.environ.get("USER_AGENT")
