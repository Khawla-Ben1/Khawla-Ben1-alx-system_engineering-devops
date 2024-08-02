#!/usr/bin/python3
'''
Gather employee data from API and display TODO list progress.
'''

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 <script_name> <employee_id>")
        exit(1)
    
    employee_id = argv[1]
    api = 'https://jsonplaceholder.typicode.com/'

    endpoint = f'users/{employee_id}'
    employee = requests.get(api + endpoint).json()

    endpoint = f'todos?userId={employee_id}'
    tasks = requests.get(api + endpoint).json()

    employee_name = employee.get("name")
    total_tasks = len(tasks)
    completed_tasks = [task for task in tasks if task.get("completed")]
    completed_count = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks({completed_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
