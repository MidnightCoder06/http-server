import sys
sys.path.append('../model')
import model
sys.path.append('../view')
import request_response
sys.path.append('../utils')
import exceptions

# The Controller accepts user’s inputs and delegates data responses to the View and data processing to the Model.
class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get(self, route):
        # print('get from controller', route) # {'generated_object_id': 132215354869378055163192969691540242915, 'method_name': 'GET ', 'repository_path': '{repository}', 'given_object_id': '{objectID}'}
        try:
            item = self.model.read_item(route)
            self.view.ok()
        except exceptions.PathNotStored:
            self.view.not_found()

    def delete(self, route):
        # print('delete from controller', route) # {'generated_object_id': 132215431720695693999600435429172068835, 'method_name': 'DELETE ', 'repository_path': '{repository}', 'given_object_id': '{objectID}'}
        try:
            self.model.delete_item(route)
            self.view.ok()
        except exceptions.PathNotStored:
            self.view.not_found()

    def put(self, route):
        # print('put from controller', route) # {'generated_object_id': 132215105300666135230529550028096684515, 'method_name': 'PUT ', 'repository_path': '{repository}'}
        try:
            # insert
            self.model.create_item(route)
            self.view.created(route)
        except exceptions.PathAlreadyStored:
            # replace
            older = self.model.read_item(route)
            self.model.update_item(route)
            self.view.ok()

if __name__ == "__main__":
    c = Controller(model.Model(), request_response.View())
