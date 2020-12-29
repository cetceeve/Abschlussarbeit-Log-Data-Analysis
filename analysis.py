import json
import csv
import decorators

with open('log_data.json') as json_file:
    log_data = json.load(json_file)

# users are taken once to ensure loop execution order
users = list(log_data.keys())

# count a type of interaction for each session
@decorators.exec_per_user(log_data, users)
def count_type(arr, type):
    events = [datapoint['type'] for datapoint in arr]
    return events.count(type)


# get unique values for log datapoint property
@decorators.exec_per_user(log_data, users)
def unique_values(arr, property):
    values = [datapoint[property] for datapoint in arr]
    return set(values)

print(unique_values('windowHeight'))
print(unique_values('windowWidth'))

# create dataset
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
