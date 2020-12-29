import utils
import decorators

log_data = utils.import_log_data()

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

print(len(unique_values('windowHeight')))
print(len(unique_values('windowWidth')))

# create dataset
data = []
data.append(users)
data.append(count_type('scroll'))
data.append(count_type('click'))
data.append(count_type('change'))

res = utils.transpose_matrix(data)

utils.add_headers(res, ['user', 'scroll events', 'click events', 'change events'])
utils.export_csv('results.csv', res)

print('analysis complete')
