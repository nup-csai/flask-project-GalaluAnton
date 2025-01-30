from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from markupsafe import Markup

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=True)
    parent = db.relationship('Task', remote_side=[id], backref='subtasks')

def render_task_tree(task):
    html = f'<li><strong>{task.description}</strong>'

    if task.subtasks:
        html += '<ul>'
        for subtask in task.subtasks:
            html += f'{render_task_tree(subtask)}'
        html += '</ul>'

    html += '</li>'
    return Markup(html)

app.jinja_env.globals['render_task_tree'] = render_task_tree

@app.route('/')
def home():
    return redirect(url_for('tasks_view'))

@app.route('/tasks')
def tasks_view():
    tasks = Task.query.order_by(Task.deadline).all()
    return render_template('tasks.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    description = request.form['description']
    deadline = datetime.strptime(request.form['deadline'], '%Y-%m-%dT%H:%M')
    parent_id = request.form.get('parent_id')

    new_task = Task(description=description, deadline=deadline, parent_id=parent_id if parent_id else None)
    db.session.add(new_task)
    db.session.commit()

    return redirect(url_for('tasks_view'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task:
        def delete_subtasks(task):
            for subtask in task.subtasks:
                delete_subtasks(subtask)
                db.session.delete(subtask)
        delete_subtasks(task)
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('tasks_view'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if not task:
        return redirect(url_for('tasks_view'))

    if request.method == 'POST':
        task.description = request.form['description']
        task.deadline = datetime.strptime(request.form['deadline'], '%Y-%m-%dT%H:%M')
        db.session.commit()
        return redirect(url_for('tasks_view'))

    return render_template('edit_task.html', task=task)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
