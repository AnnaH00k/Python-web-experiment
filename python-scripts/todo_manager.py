# python-scripts/todo_manager.py

import sys

def add_task(task, filename='todo.txt'):
    with open(filename, 'a') as f:
        f.write(task + '\n')

def list_tasks(filename='todo.txt'):
    with open(filename, 'r') as f:
        tasks = f.readlines()
    return tasks

if __name__ == "__main__":
    command = sys.argv[1]
    if command == 'add':
        task = ' '.join(sys.argv[2:])
        add_task(task)
    elif command == 'list':
        tasks = list_tasks()
        for task in tasks:
            print(task.strip())
