import controller # you don't need to import if in the same folder
import sys
sys.path.append('../router') # you append the folder, not the file
import registry # import the file
import route
sys.path.append('../logger')
import logger
sys.path.append('../model')
import model
sys.path.append('../view')
import request_response


class APIGateway:
    # responsible for receiving all incoming HTTP requests
    # creates route object
    # checks for mataching route and dispatches the route to the controller
    # calls the logger
    def __init__(self):
        self.registry = registry.Registry()
        self.logger = logger.Logger()
        self.controller = controller.Controller(model.Model(), request_response.View())

    def handle_request(self, req):
        match = self.registry.match(req)
        # print('match from api gateway', match)
        if match:
            parsed_route = route.Route(req)
            self.logger.log(parsed_route)
            self.dispatch(parsed_route.route)

    def dispatch(self, route):
        # print('route from dispatch', route)
        if route['method_name'] == 'PUT ':
            self.controller.put(route)
        if route['method_name'] == 'GET ':
            self.controller.get(route)
        if route['method_name'] == 'DELETE ':
            self.controller.delete(route)

if __name__ == '__main__':
    blah = APIGateway()
    blah.handle_request('PUT /data/{repository}')
    blah.handle_request('GET /data/{repository}/{objectID}')
    blah.handle_request('DELETE /data/{repository}/{objectID}')
