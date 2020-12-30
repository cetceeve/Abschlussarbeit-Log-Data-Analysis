import utils
import decorators

print('setting up data analysis')
LOG_DATA = utils.import_log_data()

# get unique values for log datapoint property
@decorators.exec_all(LOG_DATA)
def unique_porp_values(arr, prop=None):
    values = [datapoint[prop] for datapoint in arr]
    return list(set(values))

# task list is created once to ensure order
TASKS = unique_porp_values('taskID')
@decorators.exec_per_task(LOG_DATA, TASKS)
def count_interaction_per_task(arr, target, interaction=None):
    values = utils.filter_by_property(arr, 'target', target)
    values = utils.get_property(values, 'type')
    return values.count(interaction)

USERS = list(LOG_DATA.keys())
@decorators.exec_per_user(LOG_DATA, USERS)
def count_interaction_per_user(arr, target, interaction=None):
    values = utils.filter_by_property(arr, 'target', target)
    values = utils.get_property(values, 'type')
    return values.count(interaction)


# interaction targets are taken once to ensure order
TARGETS = unique_porp_values('target')
TARGETS = [target for target in TARGETS if target is not None]

def create_dataset_per_task(interaction):
    print('creating dataset for ' + interaction + ' interaction per task')
    data = []
    data.append(['target', *TASKS])
    for target in TARGETS:
        data.append([target, *count_interaction_per_task(target, interaction)])
    return data

def create_dataset_per_user(interaction):
    print('creating dataset for ' + interaction + ' interaction per user')
    data = []
    data.append(['target', *USERS])
    for target in TARGETS:
        data.append([target, *count_interaction_per_user(target, interaction)])
    return data


print('crunching data')
utils.export_csv('analysis_scroll_targets_per_task.csv', create_dataset_per_task('scroll'))
utils.export_csv('analysis_click_targets_per_task.csv', create_dataset_per_task('click'))
utils.export_csv('analysis_change_targets_per_task.csv', create_dataset_per_task('change'))

utils.export_csv('analysis_scroll_targets_per_user.csv', create_dataset_per_user('scroll'))
utils.export_csv('analysis_click_targets_per_user.csv', create_dataset_per_user('click'))
utils.export_csv('analysis_change_targets_per_user.csv', create_dataset_per_user('change'))
print('analysis complete')
