
class APIGateway:
    # responsible for receiving all incoming HTTP requests
    # checks for mataching route and dispatches the appropriate controller action

    def handle_request(self, method_name, path, req):
        match = registry.match(method_name, path)
        if not match:
            return [404, {}, ["{path} not found]""]
        else:
            route = match.route
            params = match.params
            dispatch(route, params, req)

    def dispatch(self, route, params, req):
        pass

# store all the 'routes' in here + the 404 logic
