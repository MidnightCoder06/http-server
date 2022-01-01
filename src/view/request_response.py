class View(object):
    # https://stackabuse.com/pythons-classmethod-and-staticmethod-explained/
    # https://www.programiz.com/python-programming/methods/built-in/staticmethod
    # https://www.tutorialsteacher.com/python/staticmethod-decorator

    @staticmethod
    def created(route):
        response = {}
        response['Status'] = '201 Created'
        response['oid'] = route.uuid
        print(response)

    @staticmethod
    def ok():
        response = {}
        response['Status'] = '200 OK'
        response['oid'] = route.uuid
        print(response)

    @staticmethod
    def delete():
        response = {}
        response['Status'] = '200 OK'
        print(response)

    @staticmethod
    def not_found():
        response = {}
        response['Status'] = '404 Not Found'
        print(response)
