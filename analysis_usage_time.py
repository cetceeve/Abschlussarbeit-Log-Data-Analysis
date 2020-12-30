import utils
import decorators

print('setting up data analysis')
LOG_DATA = utils.import_log_data()

# user list is created once to ensure order
USERS = list(LOG_DATA.keys())

# get unique values for log datapoint property
@decorators.exec_per_user(LOG_DATA, USERS)
def find_time(arr, condition='start'):
    valid = {'start', 'end'}
    if condition not in valid:
        raise ValueError("ERROR: Condition not applicable")
    values = utils.get_property(arr, 'time')
    if condition == 'end':
        return values[0]
    return values[-1]

print('creating dataset')
DATA = []
DATA.append(USERS)
DATA.append(find_time('start'))
DATA.append(find_time('end'))

# transposing for nicer display in excel
RESULT = utils.transpose_matrix(DATA)
utils.add_headers(RESULT, ['user', 'start time', 'end time'])

utils.export_csv('analysis_usage_time.csv', RESULT)
