from flask import Blueprint, render_template, url_for, flash, request, jsonify
from todo_database import database, todo_table, create_todo, read_todo
import logging
from flask_cors import CORS

todo_logic_bp = Blueprint('todo_logic', __name__)
CORS(todo_logic_bp, supports_credentials=True)

@todo_logic_bp.route('/dashboard', methods=["POST"])
def dashboard():
    start_date = request.form.get('start_date')
    finish_date = request.form.get('finish_date')
    priority = request.form.get('priority')
    category = request.form.get('category')
    notes = request.form.get('notes')
    
    try:
        create_todo(start_date, finish_date, priority, category, notes)
        return jsonify({
            "status": "Success",
            "message": "todo Created Successfully",
            "code": "200"
        }), 200
    except Exception as e:
        return jsonify({
            "message": "An error occured while creating the todo",
            "status": "Internal Server Error",
            "code": 500
        }), 500


@todo_logic_bp.route("/read_todo_list", methods=['GET'])
def read_todo_list():
    data = read_todo()

    return jsonify({
        "status": "success",
        "message": data
    })