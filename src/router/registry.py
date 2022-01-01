import sys
sys.path.append('../utils')
import exceptions

class Registry:
    def __init__(self):
        self.acceptable_method_names = ["GET", "PUT", "DELETE"]

    # input: custom route object
    def match(route):
        if route.method_name in self.acceptable_method_names:
            pass
        else:
            raise exceptions.UnknownHTTPMethod('unknown http method: {}'.format(route.method_name))
