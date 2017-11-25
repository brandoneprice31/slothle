from sanic import Sanic

from search import search
from etc import etc

app = Sanic()

# static files
app.static('/static', './static')

app.blueprint(etc)
app.blueprint(search)

if __name__ == "__main__":
    print('Starting up Slothle server...')
    app.run(host="0.0.0.0", port=8080)
