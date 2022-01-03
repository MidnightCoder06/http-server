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
        else:
            print(data[0]['generated_object_id'])
    else:
        raise exceptions.PathNotStored('Can\'t read "{}" because it\'s not stored'.format(route['repository_path']))



##### get ^ is the working model ... replicate below 


''' DELETE
'''

def delete(route):
    global storage
    print('delete')


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
def delete_item(name):
    global items
    idxs_items = list(filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
    if idxs_items:
        i, item_to_delete = idxs_items[0][0], idxs_items[0][1] # only deletes at index 0 because there are no duplicates
        del items[i]
    else:
        raise exceptions.PathNotStored(
            'Can\'t delete "{}" because it\'s not stored'.format(name))



















''' PUT
'''

def put(route):
    global storage
    print('put')
    print(storage.data)


# Create
def create_item(name, price, quantity):
    global items
    results = list(filter(lambda x: x['name'] == name, items))
    if results:
        raise exceptions.PathAlreadyStored('"{}" already stored!'.format(name))
    else:
        items.append({'name': name, 'price': price, 'quantity': quantity})

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
def update_item(name, price, quantity):
    global items
    # https://www.programiz.com/python-programming/methods/built-in/enumerate
    idxs_items = list(filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
    if idxs_items:
        i, item_to_update = idxs_items[0][0], idxs_items[0][1]
        items[i] = {'name': name, 'price': price, 'quantity': quantity}
    else:
        raise exceptions.PathNotStored('Can\'t update "{}" because it\'s not stored'.format(name))





# test function -> use an example for your storage test files
def main():

    my_items = [
        {'name': 'bread', 'price': 0.5, 'quantity': 20},
        {'name': 'milk', 'price': 1.0, 'quantity': 10},
        {'name': 'wine', 'price': 10.0, 'quantity': 5},
    ]

    # CREATE
    create_items(my_items) # have this be the initial '/'
    print(items)
    create_item('beer', price=3.0, quantity=15)
    print(items)
    # if we try to re-create an object we get an PathAlreadyStored exception
    # create_item('beer', price=2.0, quantity=10)

    # READ
    # if we try to read an object not stored we get an PathNotStored exception
    # print('READ chocolate')
    # print(read_item('chocolate'))
    print('READ bread')
    print(read_item('bread'))

    # UPDATE
    print('UPDATE bread')
    update_item('bread', price=2.0, quantity=30)
    print(read_item('bread'))
    # if we try to update an object not stored we get an PathNotStored exception
    #print('UPDATE chocolate')
    #update_item('chocolate', price=10.0, quantity=20)

    # DELETE
    print('DELETE beer')
    delete_item('beer')
    # if we try to delete an object not stored we get an PathNotStored exception
    # print('READ beer')
    # print(read_item('beer'))


if __name__ == "__main__":
    # main()
    put('temp fake custom route object')
    get('temp fake custom route object')
    delete('temp fake custom route object')
