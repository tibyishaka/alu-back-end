#!/usr/bin/python3
"""Module"""

import requests
import sys

"""Module"""

if __name__ == '__main__':
    """IF SCRIPT IS NOT RUN AS MODULE"""
    employee_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}" \
        .format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos/" \
        .format(employee_id)

    user_info = requests.get(user_url).json()
    todos_info = requests.get(todos_url).json()

    employee_name = user_info["name"]
    task_completed = list(filter(lambda obj:
                                 (obj["completed"] is True), todos_info))
    number_of_done_tasks = len(task_completed)
    total_number_of_tasks = len(todos_info)

    print("Employee {} is done with tasks({}/{}):".
          format(employee_name, number_of_done_tasks, total_number_of_tasks))

    [print("\t " + task["title"]) for task in task_completed]