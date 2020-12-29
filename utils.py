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
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(res)
