import asyncio
from sanic.response import json, html
from sanic import Blueprint

from template_loader.template_loader import template
from google_search.google_search import google

search = Blueprint('search')

@search.route('/', methods=['GET'])
async def index(request):
    return html(template('index.html').render())


@search.route('/search', methods=['GET'])
async def index(request):
    items = google.search(request.args['q'][0])
    return html(template('search_results.html').render(items=items, query=request.args['q'][0]))

@search.route('/images', methods=['GET'])
async def index(request):
    return html(template('images.html').render())