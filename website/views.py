from flask import Blueprint, redirect, render_template, url_for, request
from .models import Todo
from . import db

my_view = Blueprint("my_view", __name__)

@my_view.route("/")
def home():
    todo_list = Todo.query.all()
    message = request.args.get('message', None)
    return render_template("index.html", todo_list=todo_list, message=message)

@my_view.route("/add", methods=["POST"])
def add():
    try:
        task = request.form.get("task")
        if not task:
            raise ValueError("Task cannot be empty!")
        new_todo = Todo(task=task)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for("my_view.home", message="Task added successfully!"))
    except:
        message = ("There was an error adding your task. Please try again")
        return redirect(url_for("my_view.home", message=message))

@my_view.route("/update/<int:todo_id>", methods=["POST"])
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    if todo:
        task = request.form.get("task")
        if task:
            todo.task = task
        else:
            todo.complete = not todo.complete
        db.session.commit()
        return redirect(url_for("my_view.home", message="Task updated successfully!"))
    return redirect(url_for("my_view.home", message="Task not found!"))

@my_view.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    if todo:
        db.session.delete(todo)
        db.session.commit()
        return redirect(url_for("my_view.home", message="Task deleted successfully!"))
    return redirect(url_for("my_view.home", message="Task not found!"))

@my_view.route("/edit/<int:todo_id>")
def edit(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    if todo:
        return render_template("edit.html", todo=todo)
    return redirect(url_for("my_view.home", message="Task not found!"))
