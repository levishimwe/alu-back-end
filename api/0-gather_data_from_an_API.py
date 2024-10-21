#!/usr/bin/python3
import requests
import sys

def get_employee_todo_list(employee_id):
    # Define the base URL
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch user information by ID
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User not found.")
        return
    user = user_response.json()

    # Fetch todos for the employee
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Get employee name
    employee_name = user.get('name')

    # Filter the completed tasks and total tasks
    completed_tasks = [task for task in todos if task.get('completed')]
    total_tasks = len(todos)

    # Display the result
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    
    # Display completed task titles
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_list(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
