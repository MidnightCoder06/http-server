from datetime import datetime
import sys
sys.path.append('./logs_database')
import logs_database

class Logger():
    def __init__(self):
        # access database
        self.logs = logs_database.LogsDatabase().logs

    # dictionary definition
        # key: timestamp: string
        # value: request: string
    def log(self, route):
        # Getting the current date and time
        dt = datetime.now()
        # generating the timestamp
        ts = int(datetime.timestamp(dt))
        print(ts)

        # build log
        log = {}
        #print('route from logger', route.route) # {'generated_object_id': 254308434888230271491368054014250336739, 'method_name': 'PUT ', 'repository_path': '{repository}'}
        #print(type(route.route)) # <class 'dict'>
        log[ts] = { 'method_name': route.route['method_name'], 'path': route.route['repository_path'] }

        # insert into database
        self.logs.append(log)
