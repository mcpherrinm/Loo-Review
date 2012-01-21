#!/usr/bin/env python
from flup.server.cgi import WSGIServer
from loo import app

if __name__ == '__main__':
    WSGIServer(app).run()
