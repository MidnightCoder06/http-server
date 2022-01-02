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
        if match:
            route = Route(req)
            logger.log(route)
            dispatch(route)

    def dispatch(self, route):
        if route.method_name == 'put':
            pass # call the proper controller method
        if route.method_name == 'get':
            pass # call the proper controller method
        if route.method_name == 'delete':
            pass # call the proper controller method

if __name__ == '__main__':
    blah = APIGateway()
