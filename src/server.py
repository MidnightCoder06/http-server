import './src/controller/gateway'
import './src/controller/map_route'
import './src/controller/route'
import './src/router/registry'
import './src/route'

class Server
    def __init__(self):
        self.database = Database()
        self.cache = Cache()

  def get(path):
    return ['200 OK', {}, []]

  def __call__(self):
    req = Route(path)
    request_method = req.method()
    gateway.handle(request_method, path, req)

if __name__ == "__main__":
  app = Server()
