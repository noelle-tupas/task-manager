# MMS 146 Project - Task Manager

### Members
This is the list of the the members of Group 3

- Sangalang, Cathlyn 
- Boholano, Marcial Rode
- Revilla, Isaiah Caleb
- Balita, Ziane Ysabel
- Capon, Angela Joyce
- Bernarte, Nhel Ceejay
- De Guzman, Amos Benjamin
- Flores, Glenn Paul Jr
- Tupas, Pamela Noelle

### How to run the project
0. Configure your git locally. Run the following commands:
```
git config --global user.name "<Your Name>"
git config --global user.email "<Your Github Email>"
```
1. Clone the repository.
```
git clone https://github.com/noelle-tupas/task-manager.git
```
2. Navigate to the project repository
```
cd task-manager
```

3. Run the project
```
python task_manager.py
```

### To-do:

1. Functionalities
- [x] Users can create tasks with details like task name, description, deadline, and priority level.
- [x] Implement functionalities to add, edit, delete, and view tasks.
- [x] Allow users to set and update the priority level of each task (e.g., high, medium, low).
- [x] Provide sorting options to organize tasks based on priority.
- [x] Display the reminders for upcoming task deadlines.
- [x] Notify users of tasks that are overdue.
- [x] Users can mark tasks as completed and track their progress.
- [x] Archive completed tasks for reference.

2. Methods (does not include additional methods)
- [x] add_task
- [x] edit_task
- [x] delete_task
- [x] view_task
- [x] sort_tasks_by_priority
- [x] get_overdue_tasks
- [x] set_description
- [x] set_priority
- [x] set_completion_status
- [x] generate_reminder
- [x] display_notification

3. Additional notes:
- [x] Utilize inheritance and polymorphism to structure classes efficiently
- [x] Use encapsulation for date protection and modularity
- [x] Implement a loop for user interaction
- [x] Implement error handling for edge cases like invalid inputs or missing data
