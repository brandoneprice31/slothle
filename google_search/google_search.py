from apiclient.discovery import build
from config.config import Config
import json

class GoogleSearch:

    def __init__(self):
        self.config = Config()
        self.service = build('customsearch', 'v1', developerKey=self.config.getEnvVar('CS_DEV_KEY'))

    def search(self, query):
        query = 'dogs ' + query
        res = self.service.cse().list(q=query, cx=self.config.getEnvVar('CX')).execute()
        return res['items']

google = GoogleSearch()
