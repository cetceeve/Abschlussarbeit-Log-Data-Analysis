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
    # remove duplicates while preserving order
    res = list(dict.fromkeys(values))
    # reversing order to match mental model of timeline from left to right
    res.reverse()
    return utils.stringify_iterable(res)


# create dataset
data = []
data.append(users)
data.append(count_type('scroll'))
data.append(count_type('click'))
data.append(count_type('change'))
data.append(count_type('touchstart'))
data.append(unique_values('windowHeight'))
data.append(unique_values('windowWidth'))
data.append(unique_values('taskID'))

res = utils.transpose_matrix(data)

utils.add_headers(res, ['user', 'scroll events', 'click events', 'change events', 'touch events', 'window height', 'window width', 'task order'])
utils.export_csv('analysis_per_user.csv', res)

print('analysis complete')
