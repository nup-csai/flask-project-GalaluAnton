import pytest
from app import app, db, Task
from datetime import datetime

@pytest.fixture
def client():
    """Создаёт тестовый клиент Flask"""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_home_redirect(client):
    """Тест: главная страница перенаправляет на /tasks"""
    response = client.get('/')
    assert response.status_code == 302
    assert response.location.endswith('/tasks')

def test_add_task(client):
    """Тест: добавление новой задачи"""
    response = client.post('/add', data={
        'description': 'Тестовая задача',
        'deadline': '2025-01-30T12:00'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert 'Тестовая задача' in response.data.decode('utf-8')

def test_delete_task(client):
    """Тест: удаление задачи"""
    with app.app_context():
        task = Task(description='Удаляемая задача', deadline=datetime(2025, 1, 30))
        db.session.add(task)
        db.session.commit()
        task_id = task.id

    response = client.post(f'/delete/{task_id}', follow_redirects=True)
    assert response.status_code == 200

    with app.app_context():
        assert Task.query.get(task_id) is None
