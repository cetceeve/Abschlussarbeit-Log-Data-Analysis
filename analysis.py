import json
import csv

with open('log_data.json') as json_file:
    log_data = json.load(json_file)

# users are taken once to ensure loop execution order
users = list(log_data.keys())

# decorators to simplify data traversal
# exec on all data
def exec_all(func):
    def wrapper(*args, **kwargs):
        if (wrapper.flat_list == None):
            print('converting')
            all_arr = log_data.values()
            wrapper.flat_list = [item for sublist in all_arr for item in sublist]

        return func(wrapper.flat_list, *args, **kwargs)
    wrapper.flat_list = None
    return wrapper

# exec function for every user
def exec_per_user(func):
    def wrapper(*args, **kwargs):
        return [func(log_data[user], *args, **kwargs) for user in users]
    return wrapper


# datpoint properties ['taskID', 'time', 'timeStamp', 'windowHeight', 'windowWidth', 'type', 'target', 'posX', 'posY', 'tag', 'content', 'data', 'info']

# count a type of interaction for each session
@exec_per_user
def count_type(arr, type):
    events = [datapoint['type'] for datapoint in arr]
    return events.count(type)


# get unique values for log datapoint property
@exec_all
def unique_values(data, property):
    values = [datapoint[property] for datapoint in data]
    return set(values)


print(unique_values('type'))

#print(count_type('scroll'))
#print(count_type('click'))

data = []
data.append(users)
data.append(count_type('scroll'))
data.append(count_type('click'))
data.append(count_type('change'))
data.append(count_type('touchstart'))

# transpose the matrix
res = list(map(list, zip(*data)))
res.insert(0, ['user', 'scroll events', 'click events', 'change events', 'touchstart events'])

with open('results.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(res)

print('analysis complete')
