import method_handlers # you don't need to import if in the same folder
import sys
sys.path.append('../utils')
import exceptions


class Model(object):

    def read_item(self, route):
        return method_handlers.read_item(route)

    def delete_item(self, route):
        method_handlers.delete_item(route)

    def create_item(self, route):
        method_handlers.create_item(route)

    def update_item(self, route):
        method_handlers.update_item(route)
