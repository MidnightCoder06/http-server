# Singleton
class Registry:
    def __init__(self):
        self.acceptable_method_names = ["GET", "PUT", "DELETE"]
        self.paths = []

    def match():
        if _ in self.acceptable_method_names:
            pass
        else:
            raise `unknow http method ${request_method}`

    def add_new_path():
        route = Route()
        self.paths.append(route)

    # for delete method
    def path_exists(path):
        return path in self.paths
