import utils
import decorators

log_data = utils.import_log_data()

# get unique values for log datapoint property
@decorators.exec_all(log_data)
def unique_values(arr, property):
    values = [datapoint[property] for datapoint in arr]
    return list(set(values))

# task list is created once to ensure order
tasks = unique_values('taskID')

@decorators.exec_per_task(log_data, tasks)
def count_type(arr, target, type):
    values = [datapoint['type'] for datapoint in arr if datapoint['target'] == target]
    return values.count(type)


# interaction targets are taken once to ensure order
targets = unique_values('target')
targets = [target for target in targets if target != None]

# create dataset for interaction
def create_dataset(interaction_type):
    print('creating dataset for interaction type: ' + interaction_type)
    data = []
    data.append(['target', *tasks])
    for target in targets:
        data.append([target, *count_type(target, interaction_type)])

    # res = utils.transpose_matrix(data)
    # utils.add_headers(res, ['task', *targets])
    utils.export_csv('analysis_interaction_' + interaction_type + '_per_task.csv', data)


create_dataset('scroll')
create_dataset('click')
create_dataset('change')
create_dataset('touchstart')
print('analysis complete')
