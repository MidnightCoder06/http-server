from datetime import datetime
import sys
sys.path.append('./logs_database')
import logs_database

class Logger():
    def __init__(self):
        # access database
        logs = logs_database.LogsDatabase().logs

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
        log[ts] = { 'method_name': route.method_name, 'path': route.path }

        # insert into database
        logs.append(log)
