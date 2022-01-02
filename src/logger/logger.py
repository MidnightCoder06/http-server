from datetime import datetime
import sys
sys.path.append('./logs_database')
import logs_database


# access database
logs = logs_database.LogsDatabase().logs

# path parameter is the path property of the custom Route object from route.py

# dictionary definition
    # key: timestamp: string
    # value: request: string
def log(path):
    # Getting the current date and time
    dt = datetime.now()
    # generating the timestamp
    ts = int(datetime.timestamp(dt))
    print(ts)

    # build log
    log = {}
    log[ts] = path

    # insert into database
    logs.append(log)

if __name__ == '__main__':
    log('fake path')
    print(logs)
