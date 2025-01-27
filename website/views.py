# imports necessary modules and functions from flask
from flask import Blueprint, redirect, render_template, url_for, request
# import the todo model
from .models import Todo
#imports the database instance
from . import db

# blueprint for organizing the routes
my_view = Blueprint("my_view", __name__)

# home route
@my_view.route("/")
def home():
    todo_list = Todo.query.all() # todo items from the database
    message = request.args.get('message', None) # message query parameter
    # render index with todo list and message 
    return render_template("index.html", todo_list=todo_list, message=message)

# add route, adding new tasks
@my_view.route("/add", methods=["POST"]) # post requests only
def add():
    try:
        task = request.form.get("task")
        # task empty error
        if not task:
            raise ValueError("Task cannot be empty!")
        new_todo = Todo(task=task) # new todo instance
        # adds new task to teh database and commits it
        db.session.add(new_todo)
        db.session.commit()
        # positive message
        return redirect(url_for("my_view.home", message="Task added successfully!"))
    except: # error
        message = ("There was an error adding your task. Please try again")
        return redirect(url_for("my_view.home", message=message))

# update route, updating existing tasks
@my_view.route("/update/<int:todo_id>", methods=["POST"])
def update(todo_id): # filters todo item by ID
    todo = Todo.query.filter_by(id=todo_id).first()
    if todo: # gets updated task from DB and updates it
        task = request.form.get("task")
        if task:
            todo.task = task
        else: # toggles if no new task
            todo.complete = not todo.complete
        db.session.commit() # commits it and saves to DB
        return redirect(url_for("my_view.home", message="Task updated successfully!")) # success
    return redirect(url_for("my_view.home", message="Task not found!")) # error

# delete route, deleting existing tasks
@my_view.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    if todo: # delets task from DB and saves
        db.session.delete(todo)
        db.session.commit()
        return redirect(url_for("my_view.home", message="Task deleted successfully!"))
    return redirect(url_for("my_view.home", message="Task not found!"))

# edit route, editing existing tasks
@my_view.route("/edit/<int:todo_id>")
def edit(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    if todo:
        return render_template("edit.html", todo=todo)
    return redirect(url_for("my_view.home", message="Task not found!"))
