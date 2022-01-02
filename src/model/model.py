import sys
sys.path.append('../utils')
sys.path.append('./method_handlers')
import exceptions


class Model(object):

    def create_item(self, name, price, quantity):
        method_handlers.create_item(name, price, quantity)

    def create_items(self, items):
        method_handlers.create_items(items)

    def read_item(self, name):
        return method_handlers.read_item(name)

    def update_item(self, name, price, quantity):
        method_handlers.update_item(name, price, quantity)

    def delete_item(self, name):
        method_handlers.delete_item(name)
