#!/usr/bin/python3
"""
Script that fetches TODO list progress for a given employee ID using REST API
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a specific employee.
    
    Args:
        employee_id (int): The ID of the employee
    """
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get employee information
    employee_url = f"{base_url}/users/{employee_id}"
    employee_response = requests.get(employee_url)
    
    # Check if employee exists
    if employee_response.status_code != 200:
        print(f"Error: Employee with ID {employee_id} not found")
        sys.exit(1)
    
    employee_data = employee_response.json()
    employee_name = employee_data.get('name')
    
    # Get TODO list for employee
    todos_url = f"{base_url}/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    
    if todos_response.status_code != 200:
        print(f"Error: Could not fetch TODO list for employee {employee_id}")
        sys.exit(1)
    
    todos = todos_response.json()
    
    # Calculate progress
    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo.get('completed'))
    completed_titles = [todo.get('title') for todo in todos if todo.get('completed')]
    
    # Display results in required format
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for title in completed_titles:
        print(f"\t {title}")


if __name__ == "__main__":
    # Check if employee ID is provided
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        if employee_id <= 0:
            raise ValueError
    except ValueError:
        print("Error: Employee ID must be a positive integer")
        sys.exit(1)
    
    get_employee_todo_progress(employee_id)
