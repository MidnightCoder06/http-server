import sys
sys.path.append('../utils')
sys.path.append('./repository')
import exceptions
import repository


storage = repository.Repository().data # global variable where we keep the data

''' GET
'''
def read_item(route):
    global storage
    route_in_list = [route]
    data = list(filter(lambda x: x['repository_path'] in storage, route_in_list))
    if data:
        print('read', storage[route['repository_path']])
        return storage[route['repository_path']]

    else:
        raise exceptions.PathNotStored('Can\'t read "{}" because it\'s not stored'.format(route['repository_path']))


'''
my_list = ['a', 'b', 'c']
print(enumerate(my_list)) # <enumerate object at 0x7ff15f655b80>
print(list(enumerate(my_list))) # [(0, 'a'), (1, 'b'), (2, 'c')]
'''



''' DELETE
'''
def delete(route):
    global storage
    route_in_list = [route]
    data = list(filter(lambda x: x['repository_path'] in storage, route_in_list))
    if data:
        print('delete', route['repository_path'])
        del storage[route['repository_path']]
        print(storage)
    else:
        raise exceptions.PathNotStored('Can\'t delete "{}" because it\'s not stored'.format(route['repository_path']))
'''
items = [
        {'name': 'bread', 'price': 0.5, 'quantity': 20},
        {'name': 'milk', 'price': 1.0, 'quantity': 10},
        {'name': 'wine', 'price': 10.0, 'quantity': 5},
    ]
name = 'bread'
idxs_items = list(filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
print(idxs_items)
# [(0, {'name': 'bread', 'price': 0.5, 'quantity': 20})]

i, item_to_delete = idxs_items[0][0], idxs_items[0][1]
print(i) # 0
print(item_to_delete) # {'name': 'bread', 'price': 0.5, 'quantity': 20}
'''


''' PUT
'''
# remember the controller handles the seperation of creating and updating so its good they are two different methods in this file
def create_item(route):
    global storage
    print('put', storage)
    route_in_list = [route]
    data = list(filter(lambda x: x['repository_path'] in storage, route_in_list))
    if data:
        raise exceptions.PathAlreadyStored('"{}" already stored!'.format(storage['repository_path']))
    else:
        if 'given_object_id' in route:
            storage[route['repository_path']] = route['given_object_id']
            print('created 1', storage)
        else:
            storage[route['repository_path']] = route['generated_object_id']
            print('created 2', storage)

# Update
'''
my_items = [
        {'name': 'bread', 'price': 0.5, 'quantity': 20},
        {'name': 'milk', 'price': 1.0, 'quantity': 10},
        {'name': 'wine', 'price': 10.0, 'quantity': 5},
    ]

blah = list(enumerate(my_items))
#print(blah)
[
(0, {'name': 'bread', 'price': 0.5, 'quantity': 20}),
(1, {'name': 'milk', 'price': 1.0, 'quantity': 10}),
(2, {'name': 'wine', 'price': 10.0, 'quantity': 5})
]
print(blah[1]) # (1, {'name': 'milk', 'price': 1.0, 'quantity': 10})
print(blah[1][1]['name']) # milk
'''
def update_item(route):
    global storage
    route_in_list = [route]
    data = list(filter(lambda x: x['repository_path'] in storage, route_in_list))
    if data:
        print('key: ', storage[route['repository_path']], 'value: ', route['given_object_id'])
        storage[route['repository_path']] = route['given_object_id']
        print('new storage', storage)
    else:
        raise exceptions.PathNotStored('Can\'t update "{}" because it\'s not stored'.format(route['repository_path']))



if __name__ == "__main__":

    mock_get_arg = {'generated_object_id': 132215354869378055163192969691540242915, 'method_name': 'GET ', 'repository_path': '{repository}', 'given_object_id': '{objectID}'}
    mock_delete_arg = {'generated_object_id': 132215431720695693999600435429172068835, 'method_name': 'DELETE ', 'repository_path': '{repository}', 'given_object_id': '{objectID}'}
    mock_put_arg = {'generated_object_id': 132215105300666135230529550028096684515, 'method_name': 'PUT ', 'repository_path': '{repository}'}

    mock_update_arg = {'method_name': 'PUT ', 'repository_path': '{repository}', 'given_object_id': '{new_object_id}'}


    # read_item(mock_get_arg)
    # delete(mock_delete_arg)

    # create_item(mock_put_arg)
    # read_item(mock_get_arg)
    # delete(mock_delete_arg)
    # read_item(mock_get_arg)

    # update_item(mock_update_arg)

    # create_item(mock_put_arg)
    # read_item(mock_get_arg)
    # update_item(mock_update_arg)
    # read_item(mock_get_arg)
