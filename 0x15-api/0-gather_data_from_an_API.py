#!/usr/bin/python3
'''
Gather employee data from API and display TODO list progress.
'''

import requests
from sys import argv

if __name__ == "__main__":
    employee_id = argv[1]
    api = 'https://jsonplaceholder.typicode.com/'

    # Fetch employee data
    endpoint = 'users/{}'.format(employee_id)
    employee = requests.get(api + endpoint).json()
    
    # Fetch tasks for the employee
    endpoint = 'todos?userId={}'.format(employee_id)
    tasks = requests.get(api + endpoint).json()

    # Extract employee name and task details
    employee_name = employee.get("name")
    task_count = len(tasks)
    completed_tasks = [task for task in tasks if task.get("completed")]

    # Print the results in the expected format
    print("Employee Name: {}".format(employee_name))
    print("To Do Count: {}".format(task_count))
    print("Completed Tasks:")
    for i, task in enumerate(completed_tasks, start=1):
        print("Task {}: {}".format(i, task.get("title")))
