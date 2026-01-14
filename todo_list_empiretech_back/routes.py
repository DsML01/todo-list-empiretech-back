from flask import Blueprint, jsonify, request
from pydantic import ValidationError

from .models import Task, db
from .schemas import TaskCreate, TaskRead, TaskUpdate

tasks_bp = Blueprint('tasks', __name__, url_prefix='/api/tasks')


@tasks_bp.route('/', methods=['POST'])
def create_task():
    try:
        task = TaskCreate.model_validate(request.json)
    except ValidationError as e:
        return jsonify(e.errors()), 400

    new_task = Task(
        title=task.title,
        description=task.description,
        is_completed=task.is_completed,
        is_in_progress=task.is_in_progress,
        priority=task.priority,
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify(TaskRead.model_validate(new_task).model_dump()), 201


@tasks_bp.route('/', methods=['GET'])
def get_tasks():
    # Aqui poderia ser adicionado paginação e filtros,
    # porém não o fiz para manter o exemplo simples e didático.
    tasks = Task.query.all()
    tasks_read = [TaskRead.model_validate(task).model_dump() for task in tasks]
    return jsonify(tasks_read), 200


@tasks_bp.route('/<int:task_id>', methods=['PATCH'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)

    try:
        task_update = TaskUpdate.model_validate(request.json)
    except ValidationError as e:
        return jsonify(e.errors()), 400

    update_data = task_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(task, key, value)

    db.session.commit()
    return jsonify(TaskRead.model_validate(task).model_dump()), 200


@tasks_bp.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return '', 204
