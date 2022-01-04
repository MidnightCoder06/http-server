import sys
sys.path.append('../utils')
sys.path.append('./repository')
import exceptions
import repository


storage = repository.Repository() # global variable where we keep the data

''' GET
'''
def read_item(route):
    global storage
    route_in_list = [route]
    data = list(filter(lambda x: x['repository_path'] in storage, route_in_list))
    if data:
        if data[0]['given_object_id']: # 0th index is always ok because no duplicates
            print(data[0]['given_object_id'])
            return data[0]['given_object_id']
        else:
            print(data[0]['generated_object_id'])
            return data[0]['generated_object_id']
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
    idx_data = list(filter(lambda i_x: i_x[1]['repository_path'] in storage, enumerate(route_in_list)))
    if idx_data:
        i, item_to_delete = idx_data[0][0], idx_data[0][1] # only deletes at index 0 because there are no duplicates
        del storage[i]
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
    print('put')
    route_in_list = [route]
    data = list(filter(lambda x: x['repository_path'] in storage, route_in_list))
    if data:
        raise exceptions.PathAlreadyStored('"{}" already stored!'.format(storage['repository_path']))
    else:
        if data[0]['given_object_id']: # 0th index is always ok because no duplicates
            storage['repository_path'] = route['given_object_id']
        else:
            storage['repository_path'] = route['generated_object_id']

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
    # https://www.programiz.com/python-programming/methods/built-in/enumerate
    idx_data = list(filter(lambda i_x: i_x[1]['repository_path'] in storage, enumerate(route_in_list)))
    if idx_data:
        # idx, item_to_update = idx_data[0][0], idx_data[0][1]
        if data[0]['given_object_id']: # 0th index is always ok because no duplicates
            storage['repository_path'] = route['given_object_id']
        else:
            storage['repository_path'] = route['generated_object_id']
    else:
        raise exceptions.PathNotStored('Can\'t update "{}" because it\'s not stored'.format(route['repository_path']))



if __name__ == "__main__":
    read_item()
    delete()
    create_item()
    read_item()
    delete()
    read_item()
    create_item()
    read_item()
    update_item()
    read_item()
