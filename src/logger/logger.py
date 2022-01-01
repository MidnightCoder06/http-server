# should generate a timestamp
    # store the timestamp, the request and the path in the logs_database
# import this and call it for every call

def log(method_name, path):
    generate_timestamp()
    logs_database.insert_log(.....)
