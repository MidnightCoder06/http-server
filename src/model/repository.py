# This class stores all the paths
# dictionary definition
    # key: repoisitory path: string
    # value: object id: string

class Repository:
    def __init__(self):
        self.data = {}
        self.data['/'] = 'index.html'

    def delete_repository(self):
        self.data.clear()
