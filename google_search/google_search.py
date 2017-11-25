import requests
from bs4 import BeautifulSoup
from random import random
import re

class Google_API:
    def search(query):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cache-Control': 'no-cache'
        }

        subbed_query = re.sub(r"\s+", '+', query)

        r = requests.get('https://www.google.com/search?q='+subbed_query, headers=headers)
        return Google_API.parse_google_response(r)

    def parse_google_response(r):
        if r.status_code != 200:
            return None

        soup = BeautifulSoup(r.content, 'html.parser')
        results = soup.find_all('div', class_='g')
        parsed_results = []

        for result in results:
            try:
                h3 = result.find('h3')
                link = h3.find('a').attrs['href'][len('/url?q='):]
                title = h3.text
                innerHTML = result.find('span', class_='st').decode_contents(formatter="html")
                displayLink = result.find('cite').text

                parsed_results.append({
                    'link': link,
                    'title': title,
                    'htmlSnippet': innerHTML,
                    'displayLink': displayLink
                })
            except:
                print('skipped..')

        return parsed_results
