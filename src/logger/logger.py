# from datetime import datetime
from time import time
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
        # dt = datetime.now()
        # generating the timestamp -> The timestamp method was added in Python 3.3
        # ts = int(datetime.timestamp(dt))
        # print(ts)
        '''
        >>> from datetime import datetime
        >>> datetime.now().timestamp()
        1535495993.949849
        '''

        # python 2 approach
        ts = int(time())

        # build log
        log = {}
        log[ts] = { 'method_name': route['method_name'], 'path': route['repository_path'] }

        # insert into database
        self.logs.append(log)

    def destory_logs(self):
        self.logs = []
