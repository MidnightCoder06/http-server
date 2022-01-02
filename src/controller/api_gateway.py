import sys
sys.path.append('../router')
import registry
import route
sys.path.append('../logger')
import logger


class APIGateway:
    # responsible for receiving all incoming HTTP requests
    # creates route object
    # checks for mataching route and dispatches the route to the controller
    # calls the logger
    def __init__(self):
        self.registry = Registry()
        self.logger = Logger()
        self.controller = Controller(Model(), View())

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
