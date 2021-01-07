import utils
import decorators

print('setting up data analysis')
LOG_DATA = utils.import_log_data()
# users are taken once to ensure loop execution order
USERS = list(LOG_DATA.keys())

# count a type of interaction for each session
@decorators.exec_per_user(LOG_DATA, USERS)
def count_interaction_per_user(arr, interaction=None):
    values = utils.exclude_by_property(arr, 'taskID',  'exploration') 
    values = utils.get_property(values, 'type')
    return values.count(interaction)


# get unique values for log datapoint property
@decorators.exec_per_user(LOG_DATA, USERS)
def unique_prop_values_per_user(arr, prop=None):
    values = utils.get_property(arr, prop)
    res = utils.remove_duplicate_entries(values)
    # reversing order to match mental model of timeline from left to right
    res.reverse()
    return utils.stringify_iterable(res)


print('creating dataset')
DATA = []
DATA.append(USERS)
DATA.append(count_interaction_per_user('scroll'))
DATA.append(count_interaction_per_user('click'))
DATA.append(count_interaction_per_user('change'))
DATA.append(count_interaction_per_user('touchstart'))
DATA.append(unique_prop_values_per_user('windowHeight'))
DATA.append(unique_prop_values_per_user('windowWidth'))
DATA.append(unique_prop_values_per_user('taskID'))

# transposing for nicer display in excel
RESULT = utils.transpose_matrix(DATA)

print('exporting results')
utils.add_headers(RESULT, ['user', 'scroll events', 'click events', 'change events', 'touch events', 'window height', 'window width', 'task order'])
utils.export_csv('analysis_per_user.csv', RESULT)
