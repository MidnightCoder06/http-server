import './src/controller/gateway'
import './src/controller/map_route'
import './src/controller/route'
import './src/router/registry'
import './src/route'

# this should simply be a wrapper around the Controller (api gateway)
class Server
    def __init__(self):
        self.database = Database()

  def __call__(self):
    req = Route(path)
    request_method = req.method()
    gateway.handle(request_method, path, req)

if __name__ == "__main__":
  app = Server()
