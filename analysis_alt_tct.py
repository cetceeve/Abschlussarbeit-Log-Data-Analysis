import utils
import decorators

print('setting up data analysis')
LOG_DATA = utils.import_log_data()

# user list is created once to ensure order
USERS = list(LOG_DATA.keys())

# get unique values for log datapoint property
@decorators.exec_per_user(LOG_DATA, USERS)
def find_timestamp_for_task(arr, task_id, method=None):
    valid = {min, max, enumerate, sorted, sum}
    if method not in valid:
        raise ValueError("ERROR: Search method not applicable")
    values = utils.filter_by_property(arr, 'taskID', task_id)
    values = utils.get_property(values, 'timeStamp')
    return method(values)


# get unique values for log datapoint property
@decorators.exec_all(LOG_DATA)
def unique_prop_values(arr, prop=None):
    values = utils.get_property(arr, prop)
    values = utils.remove_duplicate_entries(values)
    # reversing order to match mental model of timeline from left to right
    values.reverse()
    return values

# task list is created once to ensure order
TASKS = unique_prop_values('taskID')

def create_dataset(method):
    print('creating dataset')
    data = []
    data.append(USERS)
    for task in TASKS:
        data.append(find_timestamp_for_task(task, method))

    # transposing for nicer display in excel
    res = utils.transpose_matrix(data)

    utils.add_headers(res, ['user', *TASKS])
    return res

def create_dataset_tct():
    return create_dataset(max)

def create_dataset_start_time():
    return create_dataset(min)


utils.export_csv('analysis_alt_tct.csv', create_dataset_tct())
utils.export_csv('analysis_task_start_time.csv', create_dataset_start_time())
