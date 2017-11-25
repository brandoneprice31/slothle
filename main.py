from sanic import Sanic

from search import search
from etc import etc
from validator.validator import is_http

app = Sanic()

# middlewares
@app.middleware('request')
async def redirect_host_urls(request):
    if 'localhost' in request.url:
        return None
    if is_http(request):
        return redirect('https://' + request.url[len('http://'):])

# static files
app.static('/static', './static')

# endpoints
app.blueprint(etc)
app.blueprint(search)

if __name__ == "__main__":
    print('Starting up Slothle server...')
    app.run(host="0.0.0.0", port=8080)
