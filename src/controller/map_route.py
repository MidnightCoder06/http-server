class Mapper:
    def __init__(self, method):
        registry = registry()
        registry.send(method_name, *args)

# have all the functions in here that need to be called for any given route
    # -> post() should insert into the cache and database
