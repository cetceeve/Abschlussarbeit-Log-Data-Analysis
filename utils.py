import json
import csv

def import_log_data():
    with open('log_data.json') as json_file:
        return json.load(json_file)

def transpose_matrix(arr):
    return list(map(list, zip(*arr)))

def add_headers(arr, headers_arr):
    arr.insert(0, headers_arr)

def export_csv(filename, res):
    with open('out/' + filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(res)

def stringify_iterable(iterable):
    acc = ''
    for i in iterable:
        acc = acc + str(i) + ', '
    return acc[:-2]

def filter_by_property(arr, prop, value):
    return [dp for dp in arr if dp[prop] == value]

def get_property(arr, prop):
    return [dp[prop] for dp in arr]

def remove_empty_entries(arr):
    return [item for item in arr if item is not None]

def remove_duplicate_entries(arr):
    return remove_empty_entries(list(dict.fromkeys(arr)))
