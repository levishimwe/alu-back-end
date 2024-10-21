#!/usr/bin/python3
"""
Python script that returns TODO list progress for a given employee ID
"""
import requests
from sys import argv


def get_employee_info(employee_id):
    """
    Get employee information by employee ID
    """
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'  # Removed trailing slash
    response = requests.get(url)
    return response.json()


def get_employee_todos(employee_id):
    """
    Get the TODO list of the employee by employee ID
    """
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response = requests.get(url)
    return response.json()


def main(employee_id):
    """
    Main function to fetch and display the TODO list progress of the employee
    """
    employee = get_employee_info(employee_id)
    employee_name = employee.get("name")
    emp_todos = get_employee_todos(employee_id)

    # Changed to work directly with the todo list instead of creating a dictionary
    total_tasks = len(emp_todos)
    completed_tasks = sum(1 for todo in emp_todos if todo.get("completed"))
    
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    
    # Print completed tasks
    for todo in emp_todos:
        if todo.get("completed"):
            print(f"\t {todo.get('title')}")


if __name__ == "__main__":
    if len(argv) > 1:
        main(argv[1])
    else:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
