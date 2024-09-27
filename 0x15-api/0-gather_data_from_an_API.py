#!/usr/bin/python3
""" With request ask for header"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    else:
        my_id = sys.argv[1]
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(my_id)
        dict1 = requests.get(url).json()
        name = dict1.get('name')
        url2 = 'https://jsonplaceholder.typicode.com/users/{}/todos'.\
               format(my_id)
        list2 = requests.get(url2).json()
        list_tasks = []
        t_total = 0
        t_done = 0
        for tasks in list2:
            if tasks.get('userId') == int(my_id):
                t_total += 1
                if tasks.get('completed'):
                    list_tasks.append(tasks.get('title'))
                    t_done += 1
        print("Employee {} is done with tasks({}/{}):".format(name,
                                                              t_done, t_total))
        for tasks in list_tasks:
            print("\t", tasks)
