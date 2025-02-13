#!/usr/bin/python3
"""Script that retrieves an employee's TODO list progress from an API."""

import requests
import sys

if __name__ == '__main__':
    # Retrieve the employee ID from the command line arguments
    employee_id = sys.argv[1]

    # Build the URLs to fetch user information and TODO list data
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

    # Request data from the API endpoints
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    # Parse the JSON responses
    user_info = user_response.json()
    todos_info = todos_response.json()

    # Extract employee name, total tasks and completed tasks
    employee_name = user_info["name"]
    total_tasks = len(todos_info)
    completed_tasks = [task for task in todos_info if task.get("OK") is True]
    number_of_completed_tasks = len(completed_tasks)

    # Print out the progress summary
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_completed_tasks, total_tasks))

    # Print the title of each completed task with a tab and a space
    for task in completed_tasks:
        print("\t " + task["title"])
