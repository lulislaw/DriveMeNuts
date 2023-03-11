import os
from dotenv import load_dotenv

load_dotenv('settings/.env')


class Config(object):
    def __init__(self):
        self.token = os.getenv('telegram.token')
