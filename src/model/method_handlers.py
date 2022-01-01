# returns all the status codes here by calling the view
    # 200, 400 and blah blah

import sys
sys.path.append('../utils')
import exceptions

# https://www.programiz.com/python-programming/methods/built-in/list
items = list()  # global variable where we keep the data -> the repoisitory should store all the paths


# root path
def create_items(app_items): # have this be the initial '/'
    global items
    items = app_items

''' PUT
'''

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
        raise exceptions.PathNotStored(
            'Can\'t update "{}" because it\'s not stored'.format(name))


''' GET
'''


'''
sample_list = ["hello", "world"]
sample_word = "hello"
new_items = filter(lambda x: x[:] == "hello", sample_list)
# x represents each index in the list
    # you could do x : x[0] == "h" and the result would be the same
print(new_items) # <filter object at 0x7f9c1675ad90>
print(list(new_items)) # ['hello']
'''
def read_item(name):
    global items
    myitems = list(filter(lambda x: x['name'] == name, items))
    if myitems:
        return myitems[0] # 0th index is always ok because no duplicates
    else:
        raise exceptions.PathNotStored(
            'Can\'t read "{}" because it\'s not stored'.format(name))



# Delete
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
    main()
