import sys
sys.path.append('../utils')
import exceptions

class Registry:
    def __init__(self):
        self.acceptable_method_names = ["GET", "PUT", "DELETE"]

    def match(self, route):
        method_name = route.split(' ')[0]
        if method_name in self.acceptable_method_names:
            return True
        else:
            raise exceptions.UnknownHTTPMethod('unknown http method: {}'.format(route.method_name))
