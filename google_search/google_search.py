from apiclient.discovery import build
import json

class GoogleSearch:

    def __init__(self):
        self.service = build('customsearch', 'v1', developerKey="AIzaSyBQmZTDhHbUae5SO0RCUPG1G3aqemzbIDA")

    def search(self, query):
        query = 'dogs ' + query
        res = self.service.cse().list(q=query, cx='017199820021536338197:le0mbdsa7ty').execute()
        return res['items']

google = GoogleSearch()
