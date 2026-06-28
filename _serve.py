import functools
from http.server import SimpleHTTPRequestHandler, HTTPServer
Handler = functools.partial(SimpleHTTPRequestHandler, directory='/tmp/adlive')
HTTPServer(('127.0.0.1', 8765), Handler).serve_forever()
