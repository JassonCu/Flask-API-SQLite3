from datetime import datetime
from flask import request, jsonify, Blueprint

from database import tasks

task_bp = Blueprint('routes-tasks', __name__)

@task_bp.route('/tasks', methods=['POST'])
def add_task():
    title = request.json['title']
    created_date = datetime.now().strftime("%x") #5/22/2021

    data = (title, created_date)
    task_id = tasks.insert_task(data)

    if task_id:
        task = tasks.select_task_by_id(task_id)
        return jsonify({'Task' : task})
    return jsonify({'message' : 'Internal Error'})

@task_bp.route('/tasks', methods=['GET'])
def get_task():
    data = tasks.select_all_task()

    if data:
        return jsonify({'tasks': data})
    elif data == False:
        return jsonify({'message' : 'Internal Error'})
    else:
        return jsonify({'message' : {}})

@task_bp.route('/tasks', methods=['PUT'])
def update_task():
    title = request.json['title']
    id_args = request.args.get('id')

    if tasks.update_task(id_args, (title,)):
        task = tasks.select_task_by_id(id_args)
        return jsonify(task)
    return jsonify({'message' : 'Internal Error'})

@task_bp.route('/tasks', methods=['DELETE'])
def delete_task():
    id_args = request.args.get('id')

    if tasks.delete_task(id_args):
        return jsonify({'message' : 'Task Deleted'})
    return jsonify({'message' : 'Internal Error'})

@task_bp.route('/tasks/completed', methods=['PUT'])
def complete_task():
    id_args = request.args.get('id')
    completed = request.args.get('completed')

    if tasks.complete_task(id_args, completed):
        return jsonify({'message' : 'Succesfully'})
    return jsonify({'message' : 'Internal Error'})
