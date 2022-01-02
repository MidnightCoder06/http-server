import './src/controller/gateway'
import './src/controller/map_route'
import './src/controller/route'
import './src/router/registry'
import './src/route'

# wrapper around the api gateway
class Server
    def __init__(self):
        self.gateway = APIGateway()

if __name__ == "__main__":
  server = Server()
  # you would pass requests in here -> server.handle_request('PUT /data/{repository}')
