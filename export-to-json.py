import json
import redis
import csv

# read keys for valid sessions from csv file
sessions = []
with open('valid_sessions.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        sessions.append(row[0])


# establish connection to local redis-server
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)


print('DB connected, reading...')

# read data from redis server
res = {}
for session in sessions:
    inputarr = r.lrange('log_' + session, 0, -1)
    arr = []

    for item in inputarr:
         arr.append(json.loads(item))

    res[session] = arr

print('reading complete, dumping...')

# dump json into file
with open('log_data.json', 'w') as outfile:
    json.dump(res, outfile)

print('dumping complete')

