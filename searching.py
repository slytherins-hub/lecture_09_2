import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path) as f:
        data = json.load(f)
    if field in data.keys():
        return data[field]
    else:
        return None

def main():
    unordered_numbers =read_data('sequential.json', 'unordered_number564')
    print(unordered_numbers)

if __name__ == '__main__':
    main()