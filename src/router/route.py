import uuid

class Route:
    def __init__(self, req):
        self.route = self.initialize_route(req)

    def initialize_route(self, req):
        route = {}
        generated_object_id = int(uuid.uuid1())
        route_properties = req.split('/')
        route['generated_object_id'] = generated_object_id
        route['method_name'] = route_properties[0]
        route['repository_path'] = route_properties[2]
        if len(route_properties) > 3:
            route['given_object_id'] = route_properties[3]
        return route

if __name__ == '__main__':
    r = Route('PUT /data/{repository}')
    print(r.route) # {'generated_object_id': 210591014432009452074551886180100096483, 'method_name': 'PUT ', 'repository_path': '{repository}'}
