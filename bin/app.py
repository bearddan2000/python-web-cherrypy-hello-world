import json
import cherrypy

config = {
    'global' : {
        'server.socket_host' : '0.0.0.0',
        'server.socket_port' : 8080
    }
}


class App:

    @cherrypy.expose
    def index(self):
        return json.dumps({"message": "Hello World"})


if __name__ == '__main__':
    cherrypy.quickstart(App(), '/', config)
