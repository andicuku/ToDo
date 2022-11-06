# Welcome to my ToDo App

This is a simple application to show you my development skill using a framework on python called Django.

## How to run

All you need is to have python installed in your machine and to create a virtual environment to isolate the dependencies
of this project.

### Create a virtual environment

```bash
python3 -m venv <name_of_your_virtual_environment>
```

### Activate the virtual environment

Linux:

```bash
source <name_of_your_virtual_environment>/bin/activate
```

Windows:

```bash
<name_of_your_virtual_environment>\Scripts\activate
```

### Install the dependencies

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python manage.py runserver
```

## How to use

You can create a new task by clicking on the button "New Task" and then you can edit the task by clicking on the
button "Edit" and delete the task by clicking on the button "Delete".

You can finalize a task by clicking finish as well.

ToDos:

- [x] To separate finished tasks from unfinished tasks